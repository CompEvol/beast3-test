#!/bin/bash
# Run the example XMLs with BEAST 2 or BEAST 3 in replicates and write a Markdown run report.
#
# Usage (from anywhere):
#   scripts/run_examples.sh beast2|beast3 [options] [example ...]
#
#   beast2  runs beast2/xml/<example> with LAUNCHER_BEAST2 into beast2/log/, report
#           reports/beast2-run-report.md
#   beast3  runs beast3/xml/<example> with LAUNCHER_BEAST3 into beast3/log/, report
#           reports/beast3-run-report.md
#
# Copy the XMLs first with scripts/copy_examples.sh. Each replicate runs in its own directory,
# <beast2|beast3>/log/<example>/rep<N>/, with a copy of the XML/JSON. BEAST is started with
# -working -beagle_SSE, so the *.log / *.trees files land in that rep directory; the screen log
# goes to beast.out and warnings/errors (stderr) to beast.err. After the runs, the home directory
# is replaced by ~ in every text file of the rep directories, so no absolute path is saved.
#
# Versions: before each replicate, rep<N>/run_info.txt records the BEAST.base and Java versions
# (from "$LAUNCHER -version"), the run date, and the beast3 branch and commit the XML was copied
# from (from <side>/xml/source_info.tsv, written by scripts/copy_examples.sh). After the runs,
# <side>/log/run_examples.tsv is rebuilt from those files (example, source, beast3_branch,
# beast3_commit, beast_base, java, run_date), so it describes what the runs actually used, also
# after -r or a partial re-run.
#
# Seeds: rep<N> reuses the seed of the other version's rep<N> (from its beast.out) when there is
# one, so BEAST 2 and BEAST 3 replicates share seeds; otherwise a random seed is drawn.
#
# Options:
#   -n N      replicates per example (default 4)
#   -j N      replicates run in parallel (default 1; >1 means run times are not comparable)
#   -b PCT    burn-in percentage for the ESS in the report (default 10)
#   -B DIR    beast3 repo, only to record its commit in the report (default ../beast3)
#   -o FILE   report file, relative to this repo
#   -f        re-run replicates that already have output (passes -overwrite to BEAST)
#   -r        report only: do not run anything, just rebuild the report from the log folder
#   -h        help
#
# Without example names, the default list below is run. Names may be given with or without
# the .xml/.json extension.

set -u

DEFAULT_EXAMPLES="testRandomLocalClock testRelaxedClock testUCLNclock.json testTipDates
testTipDates2 testSRD06 testMultipleAlignments_randomTaxaOrder testDirectSimulator
testDirectSimulator2 testDirectSimulatorHierarchical testSeqGen testSimulatedAlignment"

LAUNCHER_BEAST2="/Applications/BEAST 2.7.7/bin/beast"   # BEAST.base 2.7.9, BEAST.app 2.7.8
LAUNCHER_BEAST3="/Applications/BEAST 2.8.0/bin/beast"   # BEAST v2.8.0 rc2
BEAST_OPTS="-working -beagle_SSE"

usage() { sed -n '2,32p' "$0" | sed 's/^# \{0,1\}//'; exit "${1:-0}"; }

SIDE="${1:-}"
case "$SIDE" in
    beast2) LAUNCHER="$LAUNCHER_BEAST2"; OTHER=beast3 ;;
    beast3) LAUNCHER="$LAUNCHER_BEAST3"; OTHER=beast2 ;;
    -h|"") usage 0 ;;
    *) echo "first argument must be beast2 or beast3" >&2; usage 1 ;;
esac
shift

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 1           # all paths below are relative to this repo
NREP=4
JOBS=1
BURNIN=10
BEAST3_REPO="../beast3"
REPORT="reports/$SIDE-run-report.md"
FORCE=0
REPORT_ONLY=0

while getopts "n:j:b:B:o:frh" opt; do
    case "$opt" in
        n) NREP="$OPTARG" ;;
        j) JOBS="$OPTARG" ;;
        b) BURNIN="$OPTARG" ;;
        B) BEAST3_REPO="$OPTARG" ;;
        o) REPORT="$OPTARG" ;;
        f) FORCE=1 ;;
        r) REPORT_ONLY=1 ;;
        h) usage 0 ;;
        *) usage 1 ;;
    esac
done
shift $((OPTIND - 1))

EXAMPLES="${*:-$DEFAULT_EXAMPLES}"
XML_DIR="$SIDE/xml"
LOGROOT="$SIDE/log"
STATUS_FILE="$LOGROOT/run_examples.tsv"   # example, source, versions; read by the report
[ -x "$LAUNCHER" ] || { echo "BEAST launcher not found: $LAUNCHER" >&2; exit 1; }

BEAST_BASE="" JAVA_VER=""
if [ "$REPORT_ONLY" = 0 ]; then
    VERSION_TXT="$("$LAUNCHER" -version 2>&1 < /dev/null)"
    BEAST_BASE="$(printf '%s\n' "$VERSION_TXT" | sed -n 's/^BEAST\.base v\([^ ]*\).*/\1/p' | tail -1)"
    JAVA_VER="$(printf '%s\n' "$VERSION_TXT" | sed -n 's/^Java version *//p' | tail -1)"
    echo "BEAST.base ${BEAST_BASE:-unknown}, Java ${JAVA_VER:-unknown}"
fi

# Distinct values of a run_info.txt key over the reps of an example, comma-separated.
rep_info() {
    cat "$LOGROOT/$1"/rep*/run_info.txt 2>/dev/null |
        awk -F'\t' -v k="$2" '$1 == k && !seen[$2]++ { printf "%s%s", (n++ ? "," : ""), $2 }'
}

# Find the XML/JSON for an example name in the xml folder; prints its path or nothing.
find_source() {
    local name="$1" f
    case "$name" in
        *.xml|*.json) [ -f "$XML_DIR/$name" ] && echo "$XML_DIR/$name" ;;
        *) for f in "$XML_DIR/$name.xml" "$XML_DIR/$name.json"; do
               [ -f "$f" ] && { echo "$f"; return; }
           done ;;
    esac
}

# Seed used by the other version for the same example and rep, or nothing.
other_seed() {
    sed -n 's/^Random number seed: *\([0-9][0-9]*\).*/\1/p' "$OTHER/log/$1/rep$2/beast.out" 2>/dev/null | head -1
}

# Run one replicate: run_rep <rep dir> <file name> <seed>
run_rep() {
    local dir="$1" file="$2" seed="$3" ow=""
    [ "$FORCE" = 1 ] && ow="-overwrite"
    # run from inside the rep dir too: some outputs (e.g. SimulatedAlignment's outputFileName in
    # BEAST 2) are written relative to the current directory, not the -working one
    (cd "$dir" && "$LAUNCHER" $BEAST_OPTS -seed "$seed" $ow "$file" > beast.out 2> beast.err < /dev/null)
    echo "  done  $dir  seed=$seed  exit=$?"
}

wait_for_slot() {
    while [ "$(jobs -rp | wc -l)" -ge "$JOBS" ]; do sleep 2; done
}

mkdir -p "$LOGROOT" "$(dirname "$REPORT")"
EXLIST=""   # example <tab> source, one per line; written to $STATUS_FILE after the runs
RAN_DIRS=""

for ex in $EXAMPLES; do
    src="$(find_source "$ex")"
    name="$(basename "$ex")"; name="${name%.xml}"; name="${name%.json}"
    if [ -z "$src" ]; then
        echo "MISSING $ex: not in $XML_DIR (run scripts/copy_examples.sh first)" >&2
        EXLIST="$EXLIST$name	MISSING
"
        continue
    fi
    EXLIST="$EXLIST$name	$src
"
    [ "$REPORT_ONLY" = 1 ] && continue

    file="$(basename "$src")"
    seeds=""
    for i in $(seq 1 "$NREP"); do
        s="$(other_seed "$name" "$i")"
        while [ -z "$s" ] || case " $seeds " in *" $s "*) true ;; *) false ;; esac; do
            s=$(( RANDOM * 32768 + RANDOM + 1 ))
        done
        seeds="$seeds $s"
    done

    i=0
    for seed in $seeds; do
        i=$((i + 1))
        dir="$LOGROOT/$name/rep$i"
        if [ "$FORCE" = 0 ] && [ -f "$dir/beast.out" ]; then
            echo "  skip  $dir (already run; use -f to re-run)"
            continue
        fi
        mkdir -p "$dir"
        cp "$src" "$dir/$file"
        b3="$(awk -F'\t' -v f="$file" '$1 == f { b = $2; c = $3 } END { print b "\t" c }' \
              "$XML_DIR/source_info.tsv" 2>/dev/null)"
        printf 'beast3_branch\t%s\nbeast3_commit\t%s\nbeast_base\t%s\njava\t%s\nrun_date\t%s\n' \
            "$(printf '%s' "$b3" | cut -f1 | sed 's/^$/unknown/')" \
            "$(printf '%s' "$b3" | cut -f2 | sed 's/^$/unknown/')" \
            "${BEAST_BASE:-unknown}" "${JAVA_VER:-unknown}" "$(date +%Y-%m-%d)" > "$dir/run_info.txt"
        RAN_DIRS="$RAN_DIRS $dir"
        wait_for_slot
        echo "  start $dir  seed=$seed"
        run_rep "$dir" "$file" "$seed" &
    done
done
wait

# Never keep absolute paths: replace the home directory by ~ in all text files of the runs.
for dir in $RAN_DIRS; do
    grep -l -I -F "$HOME" "$dir"/* 2>/dev/null | while read -r f; do
        sed -i '' "s|$HOME|~|g" "$f" && echo "  ~     $f"
    done
done

COLS="beast3_branch beast3_commit beast_base java run_date"
printf 'example\tsource\t%s\n' "$(echo $COLS | tr ' ' '\t')" > "$STATUS_FILE"
printf '%s' "$EXLIST" | while IFS=$'\t' read -r name src; do
    if [ "$src" = MISSING ]; then
        printf '%s\tMISSING\t\t\t\t\t\n' "$name"
    else
        printf '%s\t%s' "$name" "$src"
        for c in $COLS; do printf '\t%s' "$(rep_info "$name" "$c")"; done
        printf '\n'
    fi
done >> "$STATUS_FILE"

PYTHONDONTWRITEBYTECODE=1 python3 scripts/run_report.py --side "$SIDE" --logroot "$LOGROOT" \
    --status "$STATUS_FILE" --beast3 "$BEAST3_REPO" --launcher "$LAUNCHER" --opts "$BEAST_OPTS" \
    --burnin "$BURNIN" --nrep "$NREP" --out "$REPORT"
