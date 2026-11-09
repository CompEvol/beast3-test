#!/bin/bash
# Copy example XMLs from the beast3 repo into this repo before running them:
#   BEAST 3 version  beast-base/src/test/resources/beast.base/examples/<name>
#                    or beast-fx/src/test/resources/beast.fx/examples/<name>         -> beast3/xml/
#   BEAST 2 version  the legacy/ sub-folder of the same examples folder             -> beast2/xml/
#
# Usage: scripts/copy_examples.sh [-B beast3-repo] [-f] [example ...]
#   -B DIR  beast3 repo (default ../beast3, relative to this repo)
#   -f      overwrite a destination file that differs from the source
# Names may be given with or without .xml/.json. Without names, the default list is copied.
#
# Each destination folder gets source_info.tsv (file, beast3_branch, beast3_commit, copied): where
# each XML came from. A row is written when its file is copied (an unchanged file keeps its row);
# scripts/run_examples.sh copies it into every replicate's run_info.txt and run_examples.tsv.

set -u

DEFAULT_EXAMPLES="testRandomLocalClock testRelaxedClock testUCLNclock.json testTipDates
testTipDates2 testSRD06 testMultipleAlignments_randomTaxaOrder testDirectSimulator
testDirectSimulator2 testDirectSimulatorHierarchical testSeqGen testSimulatedAlignment"

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 1
BEAST3_REPO="../beast3"
FORCE=0
while getopts "B:fh" opt; do
    case "$opt" in
        B) BEAST3_REPO="$OPTARG" ;;
        f) FORCE=1 ;;
        *) sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    esac
done
shift $((OPTIND - 1))
EXAMPLES="${*:-$DEFAULT_EXAMPLES}"

EX_DIRS="beast-base/src/test/resources/beast.base/examples beast-fx/src/test/resources/beast.fx/examples"

# find <sub folder ("" or "/legacy")> <name>: prints the path relative to this repo, or nothing
find_file() {
    local sub="$1" name="$2" d f
    for d in $EX_DIRS; do
        case "$name" in
            *.xml|*.json) f="$BEAST3_REPO/$d$sub/$name"; [ -f "$f" ] && { echo "$f"; return; } ;;
            *) for f in "$BEAST3_REPO/$d$sub/$name.xml" "$BEAST3_REPO/$d$sub/$name.json"; do
                   [ -f "$f" ] && { echo "$f"; return; }
               done ;;
        esac
    done
}

# record_source <dest dir> <file name>: (re)write its row in <dest dir>/source_info.tsv
record_source() {
    local info="$1/source_info.tsv" tmp="$1/.source_info.tsv.tmp"
    { printf 'file\tbeast3_branch\tbeast3_commit\tcopied\n'
      [ -f "$info" ] && tail -n +2 "$info" | awk -F'\t' -v f="$2" '$1 != f'
      printf '%s\t%s\t%s\t%s\n' "$2" "$B3_BRANCH" "$B3_COMMIT" "$(date +%Y-%m-%d)"
    } > "$tmp" && mv "$tmp" "$info"
}

# copy_one <source> <dest dir>
copy_one() {
    local src="$1" dst="$2/$(basename "$1")" f="$(basename "$1")"
    if [ -f "$dst" ] && cmp -s "$src" "$dst"; then
        # unchanged: keep its record (the branch it was first copied from); add one if missing
        tail -n +2 "$2/source_info.tsv" 2>/dev/null | cut -f1 | grep -qxF "$f" || record_source "$2" "$f"
        echo "  same  $dst"; return
    fi
    if [ -f "$dst" ]; then
        if [ "$FORCE" = 0 ]; then
            echo "  KEEP  $dst differs from $src (use -f to overwrite)"; errors=$((errors + 1)); return
        fi
    fi
    cp "$src" "$dst" && echo "  copy  $src -> $dst" && record_source "$2" "$(basename "$1")"
}

B3_BRANCH="$(git -C "$BEAST3_REPO" rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)"
B3_COMMIT="$(git -C "$BEAST3_REPO" log -1 --format=%h 2>/dev/null || echo unknown)"
[ -n "$(git -C "$BEAST3_REPO" status --porcelain --untracked-files=no 2>/dev/null)" ] &&
    B3_COMMIT="$B3_COMMIT+uncommitted"

mkdir -p beast3/xml beast2/xml
errors=0
for ex in $EXAMPLES; do
    b3="$(find_file "" "$ex")"
    b2="$(find_file "/legacy" "$ex")"
    if [ -n "$b3" ]; then copy_one "$b3" beast3/xml; else echo "  MISSING beast3 version of $ex"; errors=$((errors + 1)); fi
    if [ -n "$b2" ]; then copy_one "$b2" beast2/xml; else echo "  MISSING legacy (beast2) version of $ex"; errors=$((errors + 1)); fi
done
echo "beast3 repo $BEAST3_REPO, branch $B3_BRANCH, commit $B3_COMMIT ($(git -C "$BEAST3_REPO" log -1 --format=%ad --date=short))"
[ "$errors" = 0 ] || { echo "$errors problem(s)"; exit 1; }
