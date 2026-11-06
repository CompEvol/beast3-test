# Posterior comparison: testCoalescent

**Verdict: matched**

- beast2: `beast2/log/testCoalescent/rep1`, `beast2/log/testCoalescent/rep2`
- beast3: `beast3/log/testCoalescent/rep1`, `beast3/log/testCoalescent/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1977; max z: 1.88; max clade |Δp|: 0.007

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testCoalescent/rep1/test.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast2 | rep2 | `beast2/log/testCoalescent/rep2/test.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast3 | rep1 | `beast3/log/testCoalescent/rep1/test.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 3s |  |
| beast3 | rep2 | `beast3/log/testCoalescent/rep2/test.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 3s |  |

## Parameters: `test.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `coalescent` | 7.273 | [5.51, 8.68] | 4967 (2410) | 7.27 | [5.466, 8.701] | 8610 (4266) | 0.25 | 100% | ok |
| `treeLikelihood` | -1815.62 | [-1818.96, -1812.73] | 8413 (3978) | -1815.57 | [-1818.95, -1812.87] | 8724 (4223) | 1.88 | 100% | ok |
| `popSize` | 0.09779 | [0.02981, 0.2056] | 4209 (1977) | 0.09808 | [0.02767, 0.2051] | 8702 (4201) | 0.27 | 100% | ok |
| `hky.kappa` | 26.36 | [13.81, 41.14] | 5396 (2429) | 26.53 | [13.99, 42.15] | 8276 (4013) | 1.32 | 99% | ok |
| `posterior` | -1814.95 | [-1819.06, -1811.61] | 6305 (3009) | -1814.91 | [-1818.96, -1811.51] | 8718 (4266) | 0.95 | 99% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `coalescent` | 7.285, 7.262 | 0.91 | 7.279, 7.261 | 0.96 |
| `treeLikelihood` | -1815.62, -1815.62 | 0.01 | -1815.59, -1815.55 | 0.99 |
| `popSize` | 0.09777, 0.09781 | 0.03 | 0.09752, 0.09865 | 0.89 |
| `hky.kappa` | 26.3, 26.42 | 0.59 | 26.56, 26.51 | 0.31 |
| `posterior` | -1814.93, -1814.96 | 0.58 | -1814.92, -1814.90 | 0.39 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.008, beast3 0.004.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.839 | 0.846 | 0.007 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.130 | 0.124 | 0.006 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 1.000 | 0.001 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 8s | 6305 | 2836691 | 1893968 (`popSize`) |
| beast3 | 6s | 8718 | 5700151 | 5411437 (`hky.kappa`) |

Run-time ratio beast3 / beast2: 0.69

