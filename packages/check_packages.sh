#!/bin/bash
# Check that the main BEAST packages still work with a BEAST 3 build, and that they give the
# same answers as with an earlier BEAST 3 release.
#
# Usage (from anywhere):
#   packages/check_packages.sh [options]
#
# What it does, for the packages in packages/packages.tsv:
#   install   builds the beast3 checkout and installs it in the local Maven repository
#   build     clones each package (default branch), builds it against that BEAST 3 and runs
#             its unit tests; unpacks the package zips into one folder, as if installed
#   examples  runs the example XMLs in packages/examples.tsv with the new BEAST 3 and with
#             the baseline release, in replicates, and compares the posteriors with
#             scripts/compare.py
#   beauti    runs the BEAUti scenarios in packages/scenarios.sh with both versions (real
#             BEAUti, off-screen, all packages installed), saves each XML and runs it briefly
#   report    writes the Markdown report
#
# "New" is the beast3 checkout given with -B. "Baseline" is a released BEAST 3 version on Maven
# Central (-a). A failure that the baseline also shows is reported as a known problem; a failure
# that only the new version shows is a regression, and the script exits with status 1.
#
# Options:
#   -B DIR      beast3 checkout to test (default ../beast3, next to this repository)
#   -a VERSION  baseline BEAST 3 version on Maven Central (default 2.8.0-rc1)
#   -w DIR      work folder for clones, builds and logs (default packages/work, not in git)
#   -n N        replicates per example and version (default 4; seeds 1..N)
#   -j N        BEAST runs in parallel (default 4; run times are only comparable with -j 1)
#   -e NAMES    comma-separated examples to run (default: all in packages/examples.tsv)
#   -f          run every example replicate again, also those that already finished
#   -s STEPS    comma-separated steps to run (default install,build,examples,beauti,report)
#   -o FILE     report file, relative to this repository (default reports/packages-check.md)
#   -h          help
#
# Needs: JDK 25 or later, Maven, git, Python 3, network access. JAVA_HOME is used when set,
# otherwise the JDK that Maven runs on. Nothing in the user's BEAST folder is read or changed:
# the runs use their own package folder and their own settings folder.

set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
BEAST3="$ROOT/../beast3"
BASELINE="2.8.0-rc1"
WORK="$HERE/work"
REPS=4
JOBS=4
ONLY=""
FORCE=no
STEPS="install,build,examples,beauti,report"
REPORT="reports/packages-check.md"

while getopts "B:a:w:n:j:s:o:e:fh" opt; do
    case $opt in
        B) BEAST3="$OPTARG" ;;
        a) BASELINE="$OPTARG" ;;
        w) WORK="$OPTARG" ;;
        n) REPS="$OPTARG" ;;
        j) JOBS="$OPTARG" ;;
        s) STEPS="$OPTARG" ;;
        o) REPORT="$OPTARG" ;;
        e) ONLY="$OPTARG" ;;
        f) FORCE=yes ;;
        h) sed -n '2,40p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) exit 2 ;;
    esac
done

has_step() { case ",$STEPS," in *",$1,"*) return 0 ;; *) return 1 ;; esac; }
say() { echo "[check_packages] $*"; }
die() { echo "[check_packages] ERROR: $*" >&2; exit 2; }

BEAST3="$(cd "$BEAST3" 2>/dev/null && pwd)" || die "beast3 checkout not found (use -B DIR)"
[ -f "$BEAST3/pom.xml" ] || die "$BEAST3 is not a beast3 checkout"
mkdir -p "$WORK" && WORK="$(cd "$WORK" && pwd)"
PKG="$WORK/src"            # package clones
INSTALLED="$WORK/installed" # unpacked package zips, one folder per package
USERDIR="$WORK/userdir"     # BEAST settings folder for these runs
NEXUS="$BEAST3/beast-base/examples/nexus"
mkdir -p "$PKG" "$INSTALLED" "$USERDIR"
# no "new packages are available" dialog when BEAUti starts
echo "package.update.status=DO_NOT_CHECK" > "$USERDIR/beauti.properties"

# --- Java -----------------------------------------------------------------------------------
if [ -n "${JAVA_HOME:-}" ] && [ -x "$JAVA_HOME/bin/java" ]; then
    JH="$JAVA_HOME"
else
    JH="$(mvn -v 2>/dev/null | sed -n 's/.*runtime: //p')"
fi
[ -x "$JH/bin/java" ] || die "no JDK found: set JAVA_HOME"
JAVA="$JH/bin/java"; JAVAC="$JH/bin/javac"

# --- Versions -------------------------------------------------------------------------------
NEW="$(cd "$BEAST3" && mvn -q help:evaluate -Dexpression=project.version -DforceStdout 2>/dev/null)"
[ -n "$NEW" ] || die "cannot read the version from $BEAST3/pom.xml"
{
    printf 'date\t%s\n' "$(date +%Y-%m-%d)"
    printf 'new\t%s\n' "$NEW"
    printf 'beast3_branch\t%s\n' "$(cd "$BEAST3" && git rev-parse --abbrev-ref HEAD)"
    printf 'beast3_commit\t%s\n' "$(cd "$BEAST3" && git rev-parse --short HEAD)"
    printf 'baseline\t%s\n' "$BASELINE"
    printf 'java\t%s\n' "$("$JAVA" -version 2>&1 | head -1)"
    printf 'os\t%s\n' "$(uname -sm)"
    printf 'replicates\t%s\n' "$REPS"
    printf 'jobs\t%s\n' "$JOBS"
} > "$WORK/versions.tsv"
say "new: $NEW ($(cd "$BEAST3" && git rev-parse --short HEAD))   baseline: $BASELINE"

# read a TSV without its comment lines
rows() { grep -v '^#' "$1" | grep -v '^[[:space:]]*$'; }

# run at most $JOBS background jobs at a time
NJOBS=0
throttle() { NJOBS=$((NJOBS + 1)); if [ "$NJOBS" -ge "$JOBS" ]; then wait; NJOBS=0; fi; }

# ============================================================================================
if has_step install; then
    say "install: building $BEAST3"
    (cd "$BEAST3" && mvn -q -B install -DskipTests) > "$WORK/install.log" 2>&1 \
        || die "beast3 does not build, see $WORK/install.log"
fi

# ============================================================================================
if has_step build; then
    : > "$WORK/build.tsv"
    rows "$HERE/packages.tsv" | while IFS=$'\t' read -r name repo branch; do
        say "build: $name"
        if [ -d "$PKG/$name/.git" ]; then
            (cd "$PKG/$name" && git fetch -q --depth 1 origin ${branch:+"$branch"} && git reset -q --hard FETCH_HEAD)
        else
            git clone -q --depth 1 ${branch:+-b "$branch"} "https://github.com/$repo.git" "$PKG/$name"
        fi
        commit="$(cd "$PKG/$name" && git rev-parse --short HEAD 2>/dev/null)"
        log="$WORK/build-$name.log"
        (cd "$PKG/$name" && mvn -B install -Dbeast.version="$NEW" -Dgpg.skip -Dmaven.javadoc.skip=true) > "$log" 2>&1
        built=no; grep -q "BUILD SUCCESS" "$log" && built=yes
        tests="$(grep -E '^\[(INFO|WARNING|ERROR)\] Tests run:' "$log" | grep -v 'Time elapsed' | tail -1 | sed 's/^\[[A-Z]*\] //')"
        [ -n "$tests" ] || tests="no unit tests"
        zip="$(ls "$PKG/$name"/target/*.zip 2>/dev/null | head -1)"
        pkgname=""
        if [ "$built" = yes ] && [ -n "$zip" ]; then
            tmp="$INSTALLED/.tmp"; rm -rf "$tmp"; mkdir -p "$tmp"; unzip -q "$zip" -d "$tmp"
            pkgname="$(sed -n "s/.*<package[^>]*name=['\"]\([^'\"]*\)['\"].*/\1/p" "$tmp/version.xml" | head -1)"
            pkgversion="$(sed -n "s/.*<package[^>]*version=['\"]\([^'\"]*\)['\"].*/\1/p" "$tmp/version.xml" | head -1)"
            rm -rf "$INSTALLED/$pkgname"; mv "$tmp" "$INSTALLED/$pkgname"
        fi
        printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$repo" "$commit" "$built" "$tests" "${pkgname:-–}" "${pkgversion:-–}" >> "$WORK/build.tsv"
    done
fi

# --- Launchers ------------------------------------------------------------------------------
# The jars of one BEAST version: everything on the module path, except headless JavaFX
# (Monocle), which goes on the class path.
module_path() { # <side> <version>
    local all="$WORK/classpath.$1.txt"
    if [ ! -s "$all" ] || has_step install || has_step build; then
        mvn -q -B -f "$HERE/launcher-pom.xml" dependency:build-classpath -Dbeast.version="$2" \
            -Dmdep.outputFile="$all" > "$WORK/classpath.$1.log" 2>&1 || die "cannot resolve BEAST $2, see $WORK/classpath.$1.log"
    fi
    tr ':' '\n' < "$all" | grep -v openjfx-monocle | paste -sd: - > "$WORK/modulepath.$1.txt"
    tr ':' '\n' < "$all" | grep openjfx-monocle | paste -sd: - > "$WORK/monocle.$1.txt"
}
package_path() { ls -d "$INSTALLED"/*/ 2>/dev/null | sed 's#/$##' | paste -sd: -; }

beast() { # <side> args...
    local side="$1"; shift
    "$JAVA" --module-path "$(cat "$WORK/modulepath.$side.txt")" \
        -DBEAST_PACKAGE_PATH="$(package_path)" -Dbeast.user.package.dir="$USERDIR" \
        -m beast.base/beast.base.minimal.BeastMain "$@"
}
beauti_driver() { # <side> steps...
    local side="$1"; shift
    "$JAVA" --module-path "$(cat "$WORK/modulepath.$side.txt")" --add-modules ALL-MODULE-PATH \
        -cp "$(cat "$WORK/monocle.$side.txt"):$WORK/driver" \
        --add-exports javafx.graphics/com.sun.glass.ui=ALL-UNNAMED \
        --add-exports javafx.graphics/com.sun.javafx.application=ALL-UNNAMED \
        --add-exports javafx.graphics/com.sun.javafx.util=ALL-UNNAMED \
        --add-exports javafx.base/com.sun.javafx.logging=ALL-UNNAMED \
        --add-opens javafx.graphics/com.sun.glass.ui=ALL-UNNAMED \
        -Dglass.platform=Monocle -Dmonocle.platform=Headless -Dprism.order=sw -Djava.awt.headless=true \
        -DBEAST_PACKAGE_PATH="$(package_path)" -Dbeast.user.package.dir="$USERDIR" \
        Driver "$@"
}
# BEAST exits with status 0 after an exception in the run (beast3#265), so success is
# "the output has an End likelihood line", not the exit status. BEAST writes that line to
# stderr, so stdout and stderr both go to beast.out.
finished() { grep -q "End likelihood" "$1" 2>/dev/null && echo yes || echo no; }
set_chain() { sed -E "s/chainLength=(['\"])[0-9]+['\"]/chainLength=\\1$2\\1/" "$1"; }

if has_step examples || has_step beauti; then
    module_path new "$NEW"
    module_path base "$BASELINE"
fi

# ============================================================================================
if has_step examples; then
    run_example() { # <side> <name> <xml> <chain> <rep>
        local dir="$WORK/examples/$1/$2/rep$5" xml
        xml="$(basename "$3")"
        # keep a replicate that already finished with the same XML and chain length
        if [ "$FORCE" != yes ] && [ "$(finished "$dir/beast.out")" = yes ] \
            && set_chain "$3" "$4" | cmp -s - "$dir/$xml"; then
            say "examples: $2 $1 rep$5 kept"
            return
        fi
        rm -rf "$dir"; mkdir -p "$dir"
        set_chain "$3" "$4" > "$dir/$xml"
        (cd "$dir" && beast "$1" -overwrite -seed "$5" "$(basename "$3")" > beast.out 2>&1)
        say "examples: $2 $1 rep$5 finished=$(finished "$dir/beast.out")"
    }
    while IFS=$'\t' read -r name pkg path chain; do
        xml="$PKG/$pkg/$path"
        [ -f "$xml" ] || { say "examples: $name: $path not found in $pkg, skipped"; continue; }
        case ",${ONLY:-$name}," in *",$name,"*) ;; *) continue ;; esac
        for rep in $(seq 1 "$REPS"); do
            for side in base new; do
                run_example "$side" "$name" "$xml" "$chain" "$rep" &
                throttle
            done
        done
    done < <(rows "$HERE/examples.tsv")
    wait

    : > "$WORK/examples.tsv"; : > "$WORK/compare.tsv"
    mkdir -p "$WORK/summary"
    while IFS=$'\t' read -r name pkg path chain; do
        for side in base new; do
            for rep in $(seq 1 "$REPS"); do
                out="$WORK/examples/$side/$name/rep$rep/beast.out"
                # with -e, the other examples have only the replicates of their own run
                [ -d "$(dirname "$out")" ] || continue
                secs="$(sed -n 's/.*Total calculation time: \([0-9.]*\) seconds.*/\1/p' "$out" 2>/dev/null | tail -1)"
                printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$pkg" "$chain" "$side" "$rep" "$(finished "$out")" "${secs:-–}" >> "$WORK/examples.tsv"
            done
        done
        for side in base new; do
            for d in "$WORK/examples/$side/$name"/rep*; do
                [ -d "$d" ] && [ "${d##*/rep}" -gt "$REPS" ] && rm -rf "$d"
            done
        done
        verdict="not compared"
        if [ -d "$WORK/examples/base/$name" ] && [ -d "$WORK/examples/new/$name" ]; then
            python3 "$ROOT/scripts/compare.py" --name "$name" \
                --a "$WORK/examples/base/$name" --label-a "$BASELINE" \
                --b "$WORK/examples/new/$name" --label-b "$NEW" \
                --no-trees --out "$WORK/summary" -q > "$WORK/summary/$name.out" 2>&1
            v="$(sed -n 's/^\*\*Verdict: \(.*\)\*\*$/\1/p' "$WORK/summary/$name.md" 2>/dev/null | head -1)"
            stats="$(grep -m1 '^- min ESS' "$WORK/summary/$name.md" 2>/dev/null | sed 's/^- //')"
            [ -n "$v" ] && verdict="$v"
        fi
        printf '%s\t%s\t%s\n' "$name" "$verdict" "${stats:-}" >> "$WORK/compare.tsv"
    done < <(rows "$HERE/examples.tsv")
fi

# ============================================================================================
if has_step beauti; then
    mkdir -p "$WORK/driver"
    "$JAVAC" --module-path "$(cat "$WORK/modulepath.new.txt")" --add-modules beast.fx,beast.base,javafx.controls \
        -d "$WORK/driver" "$HERE/Driver.java" > "$WORK/driver/javac.log" 2>&1 \
        || die "Driver.java does not compile against BEAST $NEW (BEAUti internals changed?), see $WORK/driver/javac.log"
    : > "$WORK/beauti.tsv"

    sc() { # <name> steps...
        local name="$1"; shift
        local dir="$WORK/beauti/$SIDE/$name"
        rm -rf "$dir"; mkdir -p "$dir"
        # BEAUti, with a time limit in case a dialog is left open
        ( cd "$dir" && beauti_driver "$SIDE" -out "$dir/$name.xml" "$@" > beauti.out 2>&1 ) &
        local pid=$! waited=0
        while kill -0 $pid 2>/dev/null && [ $waited -lt 180 ]; do sleep 2; waited=$((waited + 2)); done
        if kill -0 $pid 2>/dev/null; then kill $pid 2>/dev/null; pkill -P $pid 2>/dev/null; echo "DRIVER KILLED after ${waited}s" >> "$dir/beauti.out"; fi
        wait $pid 2>/dev/null
        local gui=no saved=no ran="not run" why=""
        grep -q "DRIVER DONE errors=0" "$dir/beauti.out" && gui=yes
        [ -s "$dir/$name.xml" ] && saved=yes
        if [ "$gui" != yes ]; then
            why="$(grep -m1 -E 'DRIVER (EXCEPTION|UNCAUGHT|TIMEOUT|KILLED|COULD NOT|NO )' -A1 "$dir/beauti.out" | tr '\n' ' ' | cut -c1-140)"
        fi
        if [ "$saved" = yes ]; then
            set_chain "$dir/$name.xml" 200000 > "$dir/run.xml"
            (cd "$dir" && beast "$SIDE" -overwrite -seed 1 run.xml > beast.out 2>&1)
            ran="$(finished "$dir/beast.out")"
            if [ "$ran" != yes ] && [ -z "$why" ]; then
                why="$(grep -m1 -hE 'Exception|Error [0-9]+ parsing|validate and intiali[sz]e error' "$dir/beast.out" | cut -c1-140)"
            fi
        fi
        why="$(printf '%s' "$why" | sed "s#$WORK#work#g; s#$HOME#~#g" | tr '\t' ' ')"
        printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$SIDE" "$gui" "$saved" "$ran" "$why" >> "$WORK/beauti.tsv"
        say "beauti: $name $SIDE gui=$gui saved=$saved runs=$ran"
    }
    for SIDE in new base; do
        . "$HERE/scenarios.sh"
    done
fi

# ============================================================================================
if has_step report; then
    python3 "$HERE/report.py" --work "$WORK" --out "$ROOT/$REPORT"
    status=$?
    say "report: $REPORT"
    exit $status
fi
