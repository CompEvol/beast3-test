#!/usr/bin/env python3
"""Exact checks for the two examples whose calibrated node ages have a known distribution.

testConditionalRootCalibrationPrior and testCalYule_5t_2c have no sequence data and use the
calibrated Yule prior with type="full". That correction makes the marginal distribution of each
calibrated node's age equal to its calibration density, so the sampled ages can be tested
against an exact answer instead of against the other BEAST version:

- testConditionalRootCalibrationPrior: the root age (log column `cal`) ~ LogNormal(M=2, S=0.2);
- testCalYule_5t_2c: the age of MRCA(a, b), read from the tree files, ~ Uniform(4, 7).

  python3 scripts/check_calibrated_marginals.py [-b 10]

reads beast2/log/<name>-analytic/rep*/ and beast3/log/<name>-analytic/rep*/ and prints, per
version: the mean (with z = (mean - exact) / (sd_exact / sqrt(ESS)), ESS summed over
replicates), quantiles against their exact values, and the Kolmogorov-Smirnov distance
against the exact CDF with its 5% critical value at that ESS (1.358 / sqrt(ESS)).
Standard library only.
"""
import argparse
import glob
import math
import os
import re
from statistics import NormalDist

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUANTILES = (0.05, 0.25, 0.5, 0.75, 0.95)


def ess(x):
    """Effective sample size, summing autocorrelations until they drop below 0.05."""
    n = len(x)
    m = sum(x) / n
    v = sum((a - m) ** 2 for a in x) / n
    if v == 0:
        return float(n)
    s = 0.0
    for lag in range(1, n // 2):
        c = sum((x[i] - m) * (x[i + lag] - m) for i in range(n - lag)) / (n * v)
        if c < 0.05:
            break
        s += c
    return n / (1 + 2 * s)


def log_column(path, column, burnin):
    rows = [l.rstrip('\n').split('\t') for l in open(path) if not l.startswith('#')]
    i = rows[0].index(column)
    values = [float(r[i]) for r in rows[1:] if len(r) > i]
    return values[len(values) * burnin // 100:]


def mrca_ages(path, taxa, burnin):
    """Age of the MRCA of `taxa` in every tree of a NEXUS tree file."""
    text = open(path).read()
    translate = {}
    m = re.search(r'Translate(.*?);', text, re.S | re.I)
    if m:
        for entry in m.group(1).split(','):
            parts = entry.split()
            if len(parts) >= 2:
                translate[parts[0]] = parts[1]
    ages = []
    for line in text.splitlines():
        if not line.strip().lower().startswith('tree '):
            continue
        s = re.sub(r'\[[^\]]*\]', '', line.split('=', 1)[1]).strip().rstrip(';')
        pos = 0

        def node():
            # returns (branch length, height, taxa below, age of the wanted MRCA or None)
            nonlocal pos
            kids = []
            if s[pos] == '(':
                pos += 1
                kids.append(node())
                while s[pos] == ',':
                    pos += 1
                    kids.append(node())
                pos += 1
            start = pos
            while pos < len(s) and s[pos] not in ':,);':
                pos += 1
            label = s[start:pos]
            length = 0.0
            if pos < len(s) and s[pos] == ':':
                pos += 1
                start = pos
                while pos < len(s) and s[pos] not in ',);':
                    pos += 1
                length = float(s[start:pos])
            if not kids:
                return length, 0.0, {translate.get(label, label)}, None
            height = max(k[0] + k[1] for k in kids)
            below = set().union(*(k[2] for k in kids))
            found = [k[3] for k in kids if k[3] is not None]
            return length, height, below, found[0] if found else (height if taxa <= below else None)

        ages.append(node()[3])
    return ages[len(ages) * burnin // 100:]


def check(title, version, reps, cdf, mean, sd, quantile):
    pooled = [x for r in reps for x in r]
    total_ess = sum(ess(r) for r in reps)
    n = len(pooled)
    xs = sorted(pooled)
    m = sum(pooled) / n
    ks = max(max(abs((i + 1) / n - cdf(v)), abs(i / n - cdf(v))) for i, v in enumerate(xs))
    z = (m - mean) / (sd / math.sqrt(total_ess))
    crit = 1.358 / math.sqrt(total_ess)
    print(f'{title} [{version}] {len(reps)} replicates, {n} samples, ESS {total_ess:.0f}')
    print(f'  mean {m:.4f} (exact {mean:.4f}, z {z:+.2f})')
    print('  quantiles (sampled/exact): ' + '  '.join(
        f'{int(p * 100)}%: {xs[int(p * n)]:.3f}/{quantile(p):.3f}' for p in QUANTILES))
    print(f'  KS {ks:.4f} (5% critical {crit:.4f}): {"pass" if ks < crit and abs(z) < 3 else "FAIL"}')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('-b', '--burnin', type=int, default=10, help='burn-in percentage per replicate (default 10)')
    b = p.parse_args().burnin
    ln = NormalDist(2.0, 0.2)
    for version in ('beast2', 'beast3'):
        d = os.path.join(ROOT, version, 'log', 'testConditionalRootCalibrationPrior-analytic')
        reps = [log_column(f, 'cal', b) for f in sorted(glob.glob(d + '/rep*/*.log'))]
        if reps:
            check('testConditionalRootCalibrationPrior: root age ~ LogNormal(2, 0.2)', version, reps,
                  lambda v: ln.cdf(math.log(v)), math.exp(2.02), math.exp(2.02) * math.sqrt(math.exp(0.04) - 1),
                  lambda q: math.exp(ln.inv_cdf(q)))
        d = os.path.join(ROOT, version, 'log', 'testCalYule_5t_2c-analytic')
        reps = [mrca_ages(f, {'a', 'b'}, b) for f in sorted(glob.glob(d + '/rep*/*.trees'))]
        if reps:
            check('testCalYule_5t_2c: MRCA(a, b) age ~ Uniform(4, 7)', version, reps,
                  lambda v: min(1.0, max(0.0, (v - 4) / 3)), 5.5, math.sqrt(0.75), lambda q: 4 + 3 * q)


if __name__ == '__main__':
    main()
