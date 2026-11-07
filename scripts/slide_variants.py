#!/usr/bin/env python3
"""Subtree-slide variants of the BEAST 3 BEAUti analyses (beast3#200, #201, #214).

BEAUti 3 v2.8.0-rc2 starts BactrianSubtreeSlide at size 1.0, which is about 100x too large for a
substitution-scale tree, and auto-tuning cannot shrink it back within a run. This script makes two
copies of each BEAST 3 analysis, and reports how the operator tuned in the original and the copies:

  -slide  BactrianSubtreeSlide started at --size (default 0.01), what BEAUti 3 writes from #201.
  -scale  BactrianSubtreeScale (beast3#214) in place of BactrianSubtreeSlide, at its default size
          (any size attribute is removed). Needs a BEAST 3 build that has the class (#214);
          v2.8.0-rc2 does not. Record the commit used.

BEAST 2 is the fixed reference, so it gets no variants.

  python3 scripts/slide_variants.py make [--size 0.01]
      For every beast3/xml/*.xml with a BactrianSubtreeSlide operator, write
      beast3/xml-slide/<name>-slide.xml and beast3/xml-scale/<name>-scale.xml. Nothing else in
      the file changes, operator ids included. Existing variants are overwritten.
      Run them like the originals, into beast3/log/<ID>-slide/rep<N>/ and
      beast3/log/<ID>-scale/rep<N>/ with the same seeds, where <ID> is the original's log folder.

  python3 scripts/slide_variants.py report [-b 10]
      For every <ID> with variant runs, read the stdout and tree files of the original and the
      variant runs and write reports/summary/slide-size.md: the operator's final size and
      acceptance in each run, mean root height H and taxon count n, and, for -slide, the final
      size divided by H/sqrt(2n-1).

Compare posteriors with compare.py as usual, e.g.
  python3 scripts/compare.py --name C01-scale-vs-default \\
      --a beast3/log/C01 --label-a default --b beast3/log/C01-scale --label-b scale
The variants must sample the same posterior as the originals; only mixing may differ.
"""
import argparse
import glob
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = 'beast3'
VARIANTS = ('-slide', '-scale')
SCALE_CLASS = 'BactrianSubtreeScale'

OPERATOR_TAG = re.compile(r'<operator\b[^>]*>', re.S)
SLIDE_SPEC = re.compile(r'''\bspec\s*=\s*(["'])(?:[\w.]*\.)?BactrianSubtreeSlide\1''')
LEGACY_SPEC = re.compile(r'''\bspec\s*=\s*(["'])(?:beast\.base\.evolution\.operator\.)?SubtreeSlide\1''')
SIZE_ATTR = re.compile(r'''(\bsize\s*=\s*)(["'])[^"']*\2''')
ROW_CLASS = re.compile(r'Bactrian(?:SubtreeSlide|SubtreeScale)\((.*)\)$')


# ---------------------------------------------------------------- make

def _edit_slides(xml, edit):
    """Apply edit(tag) to every BactrianSubtreeSlide operator tag; return (new xml, count)."""
    count = 0

    def fix(m):
        nonlocal count
        tag = m.group(0)
        if not SLIDE_SPEC.search(tag):
            return tag
        count += 1
        return edit(tag)

    return OPERATOR_TAG.sub(fix, xml), count


def set_slide_size(xml, size):
    def edit(tag):
        if SIZE_ATTR.search(tag):
            return SIZE_ATTR.sub(lambda a: f'{a.group(1)}{a.group(2)}{size}{a.group(2)}', tag, count=1)
        return re.sub(r'^<operator\b', f'<operator size="{size}"', tag, count=1)
    return _edit_slides(xml, edit)


def use_scale_class(xml):
    def edit(tag):
        tag = SLIDE_SPEC.sub(lambda m: m.group(0).replace('BactrianSubtreeSlide', SCALE_CLASS), tag)
        return re.sub(r'\s+size\s*=\s*(["\'])[^"\']*\1', '', tag)
    return _edit_slides(xml, edit)


def make(args):
    made = 0
    src_dir = os.path.join(ROOT, VERSION, 'xml')
    variants = (('-slide', lambda x: set_slide_size(x, args.size), f'size set to {args.size}'),
                ('-scale', use_scale_class, f'replaced by {SCALE_CLASS}, default size'))
    for path in sorted(glob.glob(os.path.join(src_dir, '*.xml'))):
        name = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding='utf-8') as f:
            xml = f.read()
        legacy = len([t for t in OPERATOR_TAG.findall(xml) if LEGACY_SPEC.search(t)])
        note = f'  (also {legacy} legacy SubtreeSlide, not changed)' if legacy else ''
        for suffix, fn, what in variants:
            new, n = fn(xml)
            if n == 0:
                print(f'{VERSION}/xml/{name}.xml: no BactrianSubtreeSlide, skipped{note}')
                break
            out_dir = os.path.join(ROOT, VERSION, 'xml' + suffix)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, f'{name}{suffix}.xml'), 'w', encoding='utf-8') as f:
                f.write(new)
            made += 1
            print(f'{VERSION}/xml{suffix}/{name}{suffix}.xml: {n} operator(s) {what}{note}')
    print(f'{made} variant(s) written')


# ---------------------------------------------------------------- report

def stdout_file(rep_dir):
    """beast.out, or else the only *.out file in rep_dir (preferring the one named after the XML)."""
    p = os.path.join(rep_dir, 'beast.out')
    if os.path.exists(p):
        return p
    outs = glob.glob(os.path.join(rep_dir, '*.out'))
    if len(outs) > 1:
        outs = [o for o in outs if os.path.exists(o[:-4] + '.xml')]
    return outs[0] if len(outs) == 1 else p


def slide_rows(beast_out):
    """[(operator id, final size, acceptance)] from the operator table in beast.out."""
    rows = []
    try:
        with open(beast_out, encoding='utf-8', errors='replace') as f:
            for line in f:
                p = line.split()
                m = ROW_CLASS.search(p[0]) if p else None
                if not m:
                    continue
                try:
                    rows.append((m.group(1), float(p[1]), float(p[5])))
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
    lines = ['# Subtree slide: default vs -slide and -scale variants (BEAST 3)', '',
             'Generated by `scripts/slide_variants.py report`. One row per operator, variant and replicate.',
             '`-slide` starts BactrianSubtreeSlide at a small size; `-scale` uses BactrianSubtreeScale',
             '(beast3#214), whose size is on a log scale, so `ratio` is given for `-slide` only.',
             '`ratio` = final size / (H/√(2n−1)), with H the mean root height after '
             f'{args.burnin}% burn-in and n the number of taxa, from the variant run\'s tree file.',
             'Acceptance well below 0.3 with a default size far above the variant\'s means tuning never',
             'converged (beast3#200).', '',
             '| name | variant | rep | operator | default size | default acc | variant size | variant acc | n | H | ratio |',
             '|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
    found = 0
    log_root = os.path.join(ROOT, VERSION, 'log')
    vdirs = sorted((d, suf) for suf in VARIANTS for d in glob.glob(os.path.join(log_root, f'*{suf}')))
    for vdir, suffix in vdirs:
        name = os.path.basename(vdir)[:-len(suffix)]
        for rep_dir in sorted(glob.glob(os.path.join(vdir, 'rep*'))):
            rep = os.path.basename(rep_dir)
            variant = slide_rows(stdout_file(rep_dir))
            default = dict((r[0], r) for r in slide_rows(stdout_file(os.path.join(log_root, name, rep))))
            trees_files = sorted(glob.glob(os.path.join(rep_dir, '*.trees')))
            for op_id, size, acc in variant:
                found += 1
                d = default.get(op_id)
                tf = trees_for(op_id, trees_files)
                stats = tree_stats(tf, args.burnin) if tf else None
                h, n = stats if stats else (None, None)
                ratio = size / (h / math.sqrt(2 * n - 1)) if h and n and suffix == '-slide' else None
                lines.append(f'| {name} | {suffix} | {rep} | `{op_id}` | {fmt(d[1] if d else None)} | '
                             f'{fmt(d[2] if d else None, 2)} | {fmt(size)} | {fmt(acc, 2)} | '
                             f'{n or "–"} | {fmt(h)} | {fmt(ratio, 2)} |')
    if not found:
        print('no -slide or -scale runs with a subtree-slide row in their stdout found under beast3/log/')
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
    m = sub.add_parser('make', help='write the -slide and -scale XML variants')
    m.add_argument('--size', default='0.01', help='start size for BactrianSubtreeSlide (default 0.01)')
    r = sub.add_parser('report', help='tabulate slide tuning for default, -slide and -scale runs')
    r.add_argument('-b', '--burnin', type=int, default=10, help='burn-in percentage for root heights (default 10)')
    args = p.parse_args()
    {'make': make, 'report': report}[args.cmd](args)


if __name__ == '__main__':
    sys.exit(main())
