#!/bin/bash
# Installer check: does a BEAST 3 installer, as shipped, run BEAST, find and run package apps,
# and install packages from Maven? Uses only the installer's own bin/ scripts, headless, with
# a package folder of its own, so nothing in your BEAST folder is read or changed.
#
#   packages/check_installer.sh -d BEAST.v2.8.0-rc4.dmg      (macOS: mounted read-only)
#   packages/check_installer.sh -i "/Applications/BEAST 2.8.0"
#
# See packages/README.md ("Installer check"). Writes reports/installer-check.md.
set -u

HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$HERE/.." && pwd)
DMG=""
INSTALL=""
WORK="$HERE/work/installer"
REPORT="$REPO/reports/installer-check.md"
TIMEOUT=300
# a package on Maven Central that ships apps (packageapp elements in its version.xml)
MAVEN_COORD="io.github.compevol:ccd:1.2.2"
MAVEN_PKG_DIR="CCD"          # its folder when it is bundled (unpacked from a zip)
APP="EntropyCalculator"      # one of its apps
APP_CLASS="ccd.tools.EntropyCalculator"
# a Maven package that needs a JDK module the launchers' boot layer does not have: BEASTLabs
# brings Nashorn, which needs jdk.dynalink
MAVEN_JDK_COORD="io.github.beast2-dev:beast-labs:2.1.0-beta2"
MAVEN_JDK_PKG="BEASTLabs"

# Checks that fail because of an open issue: <check id> <issue> [<text in work/<check id>.out>].
# A failure listed here is reported as a known problem and does not make the script fail; with a
# text, only when its log has that text, so a failure for another reason still fails.
KNOWN="
maven-install https://github.com/CompEvol/beast3/issues/297
maven-list https://github.com/CompEvol/beast3/issues/82
maven-run https://github.com/CompEvol/beast3/issues/297
maven-first https://github.com/CompEvol/beast3/issues/297 Maven resolver not available
maven-load https://github.com/CompEvol/beast3/issues/297 Maven resolver not available
"

usage() { sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
while getopts "d:i:w:o:t:h" opt; do
    case $opt in
        d) DMG=$OPTARG ;;
        i) INSTALL=$OPTARG ;;
        w) WORK=$OPTARG ;;
        o) REPORT="$REPO/$OPTARG" ;;
        t) TIMEOUT=$OPTARG ;;
        *) usage ;;
    esac
done
[ -n "$DMG$INSTALL" ] || usage

mkdir -p "$WORK"
WORK=$(cd "$WORK" && pwd)
MOUNT=""
cleanup() {
    [ -n "$MOUNT" ] && hdiutil detach -quiet "$MOUNT" 2>/dev/null
}
trap cleanup EXIT

if [ -n "$DMG" ]; then
    MOUNT="$WORK/mnt"
    mkdir -p "$MOUNT"
    hdiutil detach -quiet "$MOUNT" 2>/dev/null
    hdiutil attach -nobrowse -readonly -mountpoint "$MOUNT" "$DMG" >/dev/null || { echo "could not mount $DMG"; exit 2; }
    INSTALL=$(find "$MOUNT" -maxdepth 1 -type d -name "BEAST*" | head -1)
fi
BIN="$INSTALL/bin"
[ -x "$BIN/beast" ] || { echo "no bin/beast in $INSTALL"; exit 2; }
VERSION=$(ls "$INSTALL"/BEAST.app/Contents/app/beast-pkgmgmt-*.jar 2>/dev/null | sed 's/.*beast-pkgmgmt-//; s/\.jar$//')

# run <log> <package folder> <command...>: an installer script, headless, with its own package
# folder, stopped after $TIMEOUT seconds. The bin scripts start java as a child, so on a timeout
# the java processes started from this installer are stopped too.
run() {
    local log=$1 pkgdir=$2; shift 2
    JDK_JAVA_OPTIONS="-Djava.awt.headless=true -Dbeast.user.package.dir=$pkgdir" "$@" > "$log" 2>&1 &
    local pid=$! waited=0
    while kill -0 $pid 2>/dev/null; do
        if [ $waited -ge "$TIMEOUT" ]; then
            kill $pid 2>/dev/null
            pkill -f "$INSTALL/BEAST.app" 2>/dev/null
            echo "[check_installer] stopped after $TIMEOUT s" >> "$log"
            return 124
        fi
        sleep 1; waited=$((waited + 1))
    done
    wait $pid
}

RESULTS=()
# result <check id> <PASS|FAIL> <what> <detail>
result() {
    local id=$1 status=$2 what=$3 detail=$4 issue text
    issue=$(echo "$KNOWN" | awk -v id="$id" '$1 == id {print $2}')
    text=$(echo "$KNOWN" | awk -v id="$id" '$1 == id {$1 = ""; $2 = ""; sub(/^ +/, ""); print}')
    if [ -n "$text" ] && ! grep -qF "$text" "$WORK/$id.out" 2>/dev/null; then
        issue=""
    fi
    if [ "$status" = FAIL ] && [ -n "$issue" ]; then
        status="KNOWN"
        detail="$detail ([${issue##*/}]($issue))"
    fi
    RESULTS+=("$id|$status|$what|$detail")
    printf '%-14s %-5s %s\n' "$id" "$status" "$what"
}

# --- packages: a fresh folder, seeded with the bundled packages on first launch ------------
PKG="$WORK/packages"
rm -rf "$PKG" && mkdir -p "$PKG"

# beast: a short run of an example shipped with the installer, which also writes trees for
# the apps below
mkdir -p "$WORK/beast"
sed -E 's/chainLength="[0-9]+"/chainLength="200000"/; s/logEvery="[0-9]+"/logEvery="500"/g' \
    "$INSTALL/examples/testHKY.xml" > "$WORK/beast/hky.xml"
run "$WORK/beast/beast.out" "$PKG" "$BIN/beast" -overwrite -seed 1 -working "$WORK/beast/hky.xml"
TREES=$(ls "$WORK"/beast/*.trees 2>/dev/null | head -1)
if grep -q "End likelihood" "$WORK/beast/beast.out" && [ -n "$TREES" ]; then
    result beast PASS "bin/beast runs examples/testHKY.xml (200,000 steps)" "trees: $(grep -c '^tree' "$TREES")"
else
    result beast FAIL "bin/beast runs examples/testHKY.xml (200,000 steps)" "see work/installer/beast/beast.out"
fi

# bundled-list: applauncher -list shows the apps of the bundled packages
run "$WORK/bundled-list.out" "$PKG" "$BIN/applauncher" -list
BUNDLED=$(ls "$PKG" | grep -v '^\.' | grep -v -e beauti.properties | tr '\n' ' ')
NAPPS=$(grep -E '^[^ ]+ +\|[A-Za-z]' "$WORK/bundled-list.out" | grep -vc '^Package ')
if grep -qE "^$MAVEN_PKG_DIR +\|$APP " "$WORK/bundled-list.out"; then
    result bundled-list PASS "applauncher -list shows the apps of bundled packages" "$NAPPS apps; packages seeded: $BUNDLED"
else
    result bundled-list FAIL "applauncher -list shows the apps of bundled packages" "$APP not listed; see work/installer/bundled-list.out"
fi

# bundled-run: applauncher runs a bundled package's app, with arguments
run_app() {
    local id=$1 what=$2 pkgdir=$3 out="$WORK/$1.txt"
    rm -f "$out"
    if [ -z "$TREES" ]; then
        result "$id" FAIL "$what" "no trees file (the beast check failed)"
        return
    fi
    run "$WORK/$id.out" "$pkgdir" "$BIN/applauncher" "$APP" -trees "$TREES" -burnin 10 -ccdType CCD1 -output "$out"
    if grep -q "Done invoking $APP_CLASS" "$WORK/$id.out" && [ -s "$out" ] && grep -q "entropy" "$out"; then
        result "$id" PASS "$what" "entropy $(tail -1 "$out" | cut -f3)"
    else
        result "$id" FAIL "$what" "see work/installer/$id.out"
    fi
}
run_app bundled-run "applauncher $APP (bundled $MAVEN_PKG_DIR) with arguments" "$PKG"

# --- the same package installed from Maven instead -------------------------------------------
# A fresh folder is seeded with the bundled packages too: remove the bundled copy first, so the
# package is loaded once, from Maven.
MPKG="$WORK/packages-maven"
rm -rf "$MPKG" && mkdir -p "$MPKG"
run "$WORK/maven-seed.out" "$MPKG" "$BIN/applauncher" -list
rm -rf "${MPKG:?}/$MAVEN_PKG_DIR"

run "$WORK/maven-install.out" "$MPKG" "$BIN/packagemanager" -maven "$MAVEN_COORD"
if grep -q "artifactId=\"$(echo "$MAVEN_COORD" | cut -d: -f2)\"" "$MPKG/maven-packages.xml" 2>/dev/null; then
    result maven-install PASS "packagemanager -maven $MAVEN_COORD" "listed in maven-packages.xml"
else
    # the first exception, e.g. "UnsupportedOperationException: Maven resolver not available ..."
    ERR=$(grep -m1 -E "(Exception|Error): " "$WORK/maven-install.out" | sed -E 's/^.*\.([A-Za-z]+(Exception|Error): )/\1/' | cut -c1-160)
    result maven-install FAIL "packagemanager -maven $MAVEN_COORD" "${ERR:-see work/installer/maven-install.out}"
fi

run "$WORK/maven-list.out" "$MPKG" "$BIN/applauncher" -list
if grep -qE "^$MAVEN_PKG_DIR +\|$APP |^[^ ]+ +\|$APP " "$WORK/maven-list.out"; then
    result maven-list PASS "applauncher -list shows the apps of a Maven-installed package" ""
else
    result maven-list FAIL "applauncher -list shows the apps of a Maven-installed package" "$APP not listed"
fi

run_app maven-run "applauncher $APP (Maven-installed) with arguments" "$MPKG"

# maven-load: BEAST loads a Maven package that needs a JDK module the launchers' boot layer does
# not have (BEASTLabs' Nashorn needs jdk.dynalink). If the JVM rejects the plan, BEAST still runs,
# without any of its packages. In the folder above, which is seeded, so this does not depend on
# maven-first.
run "$WORK/maven-load-install.out" "$MPKG" "$BIN/packagemanager" -maven "$MAVEN_JDK_COORD"
mkdir -p "$WORK/beast-labs"
sed -E 's/chainLength="[0-9]+"/chainLength="20000"/; s/logEvery="[0-9]+"/logEvery="1000"/g' \
    "$INSTALL/examples/testHKY.xml" > "$WORK/beast-labs/hky.xml"
run "$WORK/maven-load.out" "$MPKG" "$BIN/beast" -overwrite -seed 1 -working "$WORK/beast-labs/hky.xml"
cat "$WORK/maven-load-install.out" >> "$WORK/maven-load.out"
if grep -q "End likelihood" "$WORK/maven-load.out" && grep -q "^Loading package $MAVEN_JDK_PKG " "$WORK/maven-load.out" \
        && ! grep -q "rejected the load plan" "$WORK/maven-load.out"; then
    result maven-load PASS "bin/beast loads $MAVEN_JDK_PKG installed from Maven (needs jdk.dynalink)" ""
else
    ERR=$(grep -m1 -E "rejected the load plan|Not installing|(Exception|Error): " "$WORK/maven-load.out" \
        | sed -E 's/^Warning: //; s/^.*\.([A-Za-z]+(Exception|Error): )/\1/' | cut -c1-160)
    result maven-load FAIL "bin/beast loads $MAVEN_JDK_PKG installed from Maven (needs jdk.dynalink)" "${ERR:-see work/installer/maven-load.out}"
fi

# --- packagemanager first, straight after installing --------------------------------------------
# packagemanager may be the first program run after installing BEAST. It must seed the bundled
# core itself: without BEAST.base in the folder, a Maven package is refused as needing it.
FPKG="$WORK/packages-first"
rm -rf "$FPKG" && mkdir -p "$FPKG"
run "$WORK/maven-first.out" "$FPKG" "$BIN/packagemanager" -maven "$MAVEN_COORD"
if grep -q "artifactId=\"$(echo "$MAVEN_COORD" | cut -d: -f2)\"" "$FPKG/maven-packages.xml" 2>/dev/null; then
    result maven-first PASS "packagemanager -maven $MAVEN_COORD, before any other program" "listed in maven-packages.xml"
else
    ERR=$(grep -m1 -E "(Exception|Error): " "$WORK/maven-first.out" | sed -E 's/^.*\.([A-Za-z]+(Exception|Error): )/\1/' | cut -c1-160)
    result maven-first FAIL "packagemanager -maven $MAVEN_COORD, before any other program" "${ERR:-see work/installer/maven-first.out}"
fi

# --- every run loaded what it planned ----------------------------------------------------------
# When the JVM rejects a load plan, BEAST goes on without its packages, and a run that needs only
# the core still succeeds. So look for the warning in the logs of all the checks above.
REJECTED=$(grep -rlE "rejected the load plan|Loading BEAST without its packages" "$WORK" --include='*.out' 2>/dev/null \
    | sed "s|^$WORK/||" | tr '\n' ' ')
if [ -z "$REJECTED" ]; then
    result load-plan PASS "no run fell back to loading BEAST without its packages" ""
else
    result load-plan FAIL "no run fell back to loading BEAST without its packages" "in: $REJECTED"
fi

# --- report ------------------------------------------------------------------------------------
FAILED=0
{
    echo "# Installer check"
    echo
    echo "Installer: \`$( [ -n "$DMG" ] && basename "$DMG" || echo "$INSTALL")\` (beast-pkgmgmt $VERSION), run $(date '+%Y-%m-%d %H:%M') on $(uname -s) $(uname -m)."
    echo "Made by [packages/check_installer.sh](../packages/check_installer.sh); see [packages/README.md](../packages/README.md#installer-check)."
    echo
    echo "| Check | Result | What | Detail |"
    echo "|---|---|---|---|"
    for r in "${RESULTS[@]}"; do
        IFS='|' read -r id status what detail <<< "$r"
        [ "$status" = FAIL ] && FAILED=1
        echo "| $id | $status | $what | $detail |"
    done
    echo
    echo "KNOWN: fails because of the open issue linked. Logs are in \`packages/work/installer/\` (not in git)."
} > "$REPORT"
echo "report: ${REPORT#$REPO/}"
exit $FAILED
