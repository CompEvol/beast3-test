# Posterior comparison: testExponentialGrowth-v278

**Verdict: matched**

- beast2: `beast2/log/testExponentialGrowth-v278/rep1`, `beast2/log/testExponentialGrowth-v278/rep2`
- beast3: `beast3/log/testExponentialGrowth-v278/rep1`, `beast3/log/testExponentialGrowth-v278/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1540; max z: 2.386; max clade |Δp|: 0.010

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testExponentialGrowth-v278/rep1/test.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast2 | rep2 | `beast2/log/testExponentialGrowth-v278/rep2/test.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast3 | rep1 | `beast3/log/testExponentialGrowth-v278/rep1/test.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 2s |  |
| beast3 | rep2 | `beast3/log/testExponentialGrowth-v278/rep2/test.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 2s |  |

## Parameters: `test.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `coalescent` | 7.065 | [4.714, 8.69] | 4068 (1782) | 7.06 | [4.662, 8.731] | 3959 (1692) | 0.21 | 100% | ok |
| `treeLikelihood` | -1815.69 | [-1819.18, -1812.86] | 7458 (3634) | -1815.76 | [-1819.33, -1812.81] | 8694 (4273) | 2.39 | 100% | ok |
| `popSize` | 0.1321 | [0.03354, 0.2942] | 3438 (1540) | 0.1332 | [0.02874, 0.298] | 3698 (1558) | 0.50 | 100% | ok |
| `hky.kappa` | 32.91 | [16.67, 54.49] | 6246 (3067) | 33.2 | [14.4, 54.34] | 6235 (2957) | 1.51 | 100% | ok |
| `posterior` | -1808.63 | [-1812.69, -1805.19] | 5856 (2547) | -1808.70 | [-1812.81, -1805.08] | 7231 (3477) | 1.97 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `coalescent` | 7.047, 7.083 | 1.01 | 7.08, 7.039 | 1.11 |
| `treeLikelihood` | -1815.70, -1815.69 | 0.39 | -1815.74, -1815.79 | 1.20 |
| `popSize` | 0.1325, 0.1317 | 0.26 | 0.1312, 0.1352 | 1.31 |
| `hky.kappa` | 32.87, 32.95 | 0.31 | 33.08, 33.33 | 0.91 |
| `posterior` | -1808.66, -1808.60 | 0.92 | -1808.66, -1808.75 | 1.73 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.011, beast3 0.003.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.834 | 0.844 | 0.010 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.135 | 0.126 | 0.009 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 8s | 5856 | 2689035 | 1578601 (`popSize`) |
| beast3 | 5s | 7231 | 5613547 | 2871208 (`popSize`) |

Run-time ratio beast3 / beast2: 0.59

