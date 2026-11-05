#!/usr/bin/env python3
"""Subtree-slide start-size variants of the BEAUti analyses (beast3#200, beast3#201).

BEAUti in BEAST 2.7.9 and BEAST 3 v2.8.0-rc2 starts BactrianSubtreeSlide at size 1.0, which is
about 100x too large for a substitution-scale tree, and auto-tuning cannot shrink it back within a
run. This script makes a copy of each analysis that starts the slide at a smaller size, and
reports how the slide tuned in the original and in the copy.

  python3 scripts/slide_variants.py make [--size 0.01]
      For every beast2/xml/*.xml and beast3/xml/*.xml with a BactrianSubtreeSlide operator,
      write beast2/xml-slide/<name>-slide.xml (beast3 likewise) with that operator's size set
      to --size. Nothing else in the file changes. Existing variants are overwritten.
      Run the variants like the originals, into beast2/log/<name>-slide/rep<N>/ and
      beast3/log/<name>-slide/rep<N>/, with the same seeds.

  python3 scripts/slide_variants.py report [-b 10]
      For every <name> with -slide runs, read beast.out and the tree files of the original and
      the variant runs and write reports/summary/slide-size.md: the slide's final size and
      acceptance in each run, mean root height H and taxon count n, and the final size divided
      by H/sqrt(2n-1).

Compare posteriors with compare.py as usual, e.g.
  python3 scripts/compare.py --name beauti-C07-slide-vs-default \\
      --a beast3/log/beauti-C07 --label-a default --b beast3/log/beauti-C07-slide --label-b slide
The variants must sample the same posterior as the originals; only mixing may differ.
"""
import argparse
import glob
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSIONS = ('beast2', 'beast3')
SUFFIX = '-slide'

OPERATOR_TAG = re.compile(r'<operator\b[^>]*>', re.S)
SLIDE_SPEC = re.compile(r'''\bspec\s*=\s*(["'])(?:[\w.]*\.)?BactrianSubtreeSlide\1''')
LEGACY_SPEC = re.compile(r'''\bspec\s*=\s*(["'])(?:beast\.base\.evolution\.operator\.)?SubtreeSlide\1''')
SIZE_ATTR = re.compile(r'''(\bsize\s*=\s*)(["'])[^"']*\2''')


# ---------------------------------------------------------------- make

def set_slide_size(xml, size):
    """Return (new xml, number of BactrianSubtreeSlide operators changed)."""
    count = 0

    def fix(m):
        nonlocal count
        tag = m.group(0)
        if not SLIDE_SPEC.search(tag):
            return tag
        count += 1
        if SIZE_ATTR.search(tag):
            return SIZE_ATTR.sub(lambda a: f'{a.group(1)}{a.group(2)}{size}{a.group(2)}', tag, count=1)
        # no size attribute: add one after the element name
        return re.sub(r'^<operator\b', f'<operator size="{size}"', tag, count=1)

    return OPERATOR_TAG.sub(fix, xml), count


def make(args):
    made = 0
    for version in VERSIONS:
        src_dir = os.path.join(ROOT, version, 'xml')
        out_dir = os.path.join(ROOT, version, 'xml-slide')
        for path in sorted(glob.glob(os.path.join(src_dir, '*.xml'))):
            name = os.path.splitext(os.path.basename(path))[0]
            with open(path, encoding='utf-8') as f:
                xml = f.read()
            new, n = set_slide_size(xml, args.size)
            legacy = len([t for t in OPERATOR_TAG.findall(xml) if LEGACY_SPEC.search(t)])
            note = f'  (also {legacy} legacy SubtreeSlide, not changed)' if legacy else ''
            if n == 0:
                print(f'{version}/xml/{name}.xml: no BactrianSubtreeSlide, skipped{note}')
                continue
            os.makedirs(out_dir, exist_ok=True)
            out = os.path.join(out_dir, f'{name}{SUFFIX}.xml')
            with open(out, 'w', encoding='utf-8') as f:
                f.write(new)
            made += 1
            print(f'{version}/xml-slide/{name}{SUFFIX}.xml: {n} operator(s) set to size {args.size}{note}')
    print(f'{made} variant(s) written')


# ---------------------------------------------------------------- report

def slide_rows(beast_out):
    """[(operator id, final size, acceptance)] from the operator table in beast.out."""
    rows = []
    try:
        with open(beast_out, encoding='utf-8', errors='replace') as f:
            for line in f:
                if 'BactrianSubtreeSlide(' not in line:
                    continue
                p = line.split()
                m = re.search(r'BactrianSubtreeSlide\((.*)\)$', p[0])
                try:
                    rows.append((m.group(1) if m else p[0], float(p[1]), float(p[5])))
                except (IndexError, ValueError):
                    pass
    except OSError:
        pass
    return rows


def parse_newick(nwk):
    """(root height, number of tips) of a newick string with branch lengths."""
    s = re.sub(r'\[[^\]]*\]', '', nwk).strip().rstrip(';')
    i = 0

    def node():
        nonlocal i
        kids = []
        if s[i] == '(':
            i += 1
            kids.append(node())
            while s[i] == ',':
                i += 1
                kids.append(node())
            i += 1
        while i < len(s) and s[i] not in ':,);':
            i += 1
        length = 0.0
        if i < len(s) and s[i] == ':':
            i += 1
            j = i
            while i < len(s) and s[i] not in ',);':
                i += 1
            length = float(s[j:i])
        if not kids:
            return length, 0.0, 1
        return length, max(k[0] + k[1] for k in kids), sum(k[2] for k in kids)

    _, height, tips = node()
    return height, tips


def tree_stats(trees_file, burnin):
    """(mean root height after burn-in, number of tips), or None."""
    try:
        with open(trees_file, encoding='utf-8', errors='replace') as f:
            trees = [l.split('=', 1)[1] for l in f if l.strip().lower().startswith('tree ')]
    except OSError:
        return None
    trees = trees[len(trees) * burnin // 100:]
    if not trees:
        return None
    heights, tips = [], 0
    for t in trees:
        try:
            h, tips = parse_newick(t)
        except (IndexError, ValueError):
            return None
        heights.append(h)
    return sum(heights) / len(heights), tips


def trees_for(op_id, trees_files):
    """The tree file for a slide operator, matched on the tree name after '.t:'."""
    if len(trees_files) == 1:
        return trees_files[0]
    tree = op_id.split('.t:', 1)[1] if '.t:' in op_id else None
    hits = [t for t in trees_files if tree and tree in os.path.basename(t)]
    return hits[0] if len(hits) == 1 else None


def fmt(x, digits=3):
    return '–' if x is None else f'{x:.{digits}g}'


def report(args):
    lines = ['# Subtree-slide start size: default vs -slide variants', '',
             'Generated by `scripts/slide_variants.py report`. One row per slide operator and replicate.',
             '`ratio` = final size / (H/√(2n−1)), with H the mean root height after '
             f'{args.burnin}% burn-in and n the number of taxa, from the run\'s tree file.',
             'Acceptance well below 0.3 with a size far above the variant\'s means tuning never',
             'converged (beast3#200).', '',
             '| name | version | rep | operator | default size | default acc | slide size | slide acc | n | H | ratio |',
             '|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
    found = 0
    for version in VERSIONS:
        log_root = os.path.join(ROOT, version, 'log')
        for vdir in sorted(glob.glob(os.path.join(log_root, f'*{SUFFIX}'))):
            name = os.path.basename(vdir)[:-len(SUFFIX)]
            for rep_dir in sorted(glob.glob(os.path.join(vdir, 'rep*'))):
                rep = os.path.basename(rep_dir)
                slide = slide_rows(os.path.join(rep_dir, 'beast.out'))
                default = dict((r[0], r) for r in slide_rows(os.path.join(log_root, name, rep, 'beast.out')))
                trees_files = sorted(glob.glob(os.path.join(rep_dir, '*.trees')))
                for op_id, size, acc in slide:
                    found += 1
                    d = default.get(op_id)
                    tf = trees_for(op_id, trees_files)
                    stats = tree_stats(tf, args.burnin) if tf else None
                    h, n = stats if stats else (None, None)
                    ratio = size / (h / math.sqrt(2 * n - 1)) if h and n else None
                    lines.append(f'| {name} | {version} | {rep} | `{op_id}` | {fmt(d[1] if d else None)} | '
                                 f'{fmt(d[2] if d else None, 2)} | {fmt(size)} | {fmt(acc, 2)} | '
                                 f'{n or "–"} | {fmt(h)} | {fmt(ratio, 2)} |')
    if not found:
        print('no -slide runs with a BactrianSubtreeSlide row in beast.out found under beast*/log/')
        return
    out = os.path.join(ROOT, 'reports', 'summary', 'slide-size.md')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    print(f'\nwritten to {os.path.relpath(out, ROOT)}')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make', help='write the -slide XML variants')
    m.add_argument('--size', default='0.01', help='start size for BactrianSubtreeSlide (default 0.01)')
    r = sub.add_parser('report', help='tabulate slide tuning for default and -slide runs')
    r.add_argument('-b', '--burnin', type=int, default=10, help='burn-in percentage for root heights (default 10)')
    args = p.parse_args()
    {'make': make, 'report': report}[args.cmd](args)


if __name__ == '__main__':
    sys.exit(main())
