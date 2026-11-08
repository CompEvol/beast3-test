# Posterior comparison: testPlates

**Verdict: matched**

- beast2: `beast2/log/testPlates/rep1`, `beast2/log/testPlates/rep2`
- beast3: `beast3/log/testPlates/rep1`, `beast3/log/testPlates/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 224; max z: 0.9307; max clade |Δp|: 0.009

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testPlates/rep1/test.1.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 42s |  |
| beast2 | rep2 | `beast2/log/testPlates/rep2/test.2.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 42s |  |
| beast3 | rep1 | `beast3/log/testPlates/rep1/test.1.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 32s |  |
| beast3 | rep2 | `beast3/log/testPlates/rep2/test.2.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 32s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `likelihood` | -1827.12 | [-1841.96, -1811.38] | 483 (224) | -1827.18 | [-1842.38, -1811.75] | 9002 (4501) | 0.13 | 99% | ok |
| `hky.kappa.p1` | 1.583e+14 | [29.04, 1.131e+15] | 1553 (708) | 1.636e+14 | [17.33, 1.099e+15] | 8512 (4011) | 0.32 | 100% | ok |
| `hky.kappa.p2` | 19.93 | [4.825, 41.4] | 8443 (3942) | 19.97 | [5.074, 41.49] | 8487 (3986) | 0.24 | 100% | ok |
| `hky.kappa.p3` | 43.29 | [11.23, 88.92] | 9002 (4501) | 43.65 | [11.29, 91.12] | 8309 (4072) | 0.93 | 100% | ok |
| `tree.height` | 0.0645 | [0.05202, 0.07624] | 7916 (3746) | 0.06445 | [0.05287, 0.0768] | 8641 (4297) | 0.57 | 98% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `likelihood` | -1826.65, -1827.59 | 1.16 | -1827.07, -1827.29 | 1.15 |
| `hky.kappa.p1` | 1.335e+14, 1.831e+14 | 1.64 | 1.494e+14, 1.778e+14 | 2.17 |
| `hky.kappa.p2` | 19.88, 19.97 | 0.34 | 19.72, 20.22 | 1.92 |
| `hky.kappa.p3` | 43, 43.59 | 1.09 | 43.43, 43.88 | 0.81 |
| `tree.height` | 0.06455, 0.06446 | 0.64 | 0.06451, 0.06439 | 0.86 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.007, beast3 0.009.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.838 | 0.829 | 0.009 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.127 | 0.134 | 0.007 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `likelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 1m25s | 483 | 20535 | 20535 (`likelihood`) |
| beast3 | 1m04s | 9002 | 506854 | 467811 (`hky.kappa.p3`) |

Run-time ratio beast3 / beast2: 0.75

