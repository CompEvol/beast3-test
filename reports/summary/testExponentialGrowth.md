# Posterior comparison: testExponentialGrowth

**Verdict: matched**

- beast2: `beast2/log/testExponentialGrowth/rep1`, `beast2/log/testExponentialGrowth/rep2`
- beast3: `beast3/log/testExponentialGrowth/rep1`, `beast3/log/testExponentialGrowth/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1898; max z: 1.058; max clade |Δp|: 0.010

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testExponentialGrowth/rep1/test.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast2 | rep2 | `beast2/log/testExponentialGrowth/rep2/test.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 5s |  |
| beast3 | rep1 | `beast3/log/testExponentialGrowth/rep1/test.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 3s |  |
| beast3 | rep2 | `beast3/log/testExponentialGrowth/rep2/test.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 3s |  |

## Parameters: `test.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `coalescent` | 7.34 | [5.506, 8.757] | 5209 (2495) | 7.34 | [5.615, 8.818] | 8688 (4187) | 0.02 | 98% | ok |
| `treeLikelihood` | -1815.65 | [-1819.22, -1812.85] | 7688 (3578) | -1815.62 | [-1819.06, -1812.90] | 8575 (4074) | 1.06 | 100% | ok |
| `popSize` | 0.1008 | [0.02737, 0.2112] | 4000 (1898) | 0.1008 | [0.02715, 0.2065] | 8675 (4207) | 0.05 | 100% | ok |
| `hky.kappa` | 26.4 | [13.32, 41.65] | 6629 (3240) | 26.35 | [13.5, 41.27] | 8846 (4345) | 0.44 | 100% | ok |
| `posterior` | -1814.93 | [-1819.20, -1811.57] | 5923 (2860) | -1814.90 | [-1819.09, -1811.55] | 7986 (3664) | 0.83 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `coalescent` | 7.362, 7.319 | 1.76 | 7.334, 7.346 | 0.68 |
| `treeLikelihood` | -1815.65, -1815.64 | 0.29 | -1815.62, -1815.62 | 0.04 |
| `popSize` | 0.0991, 0.1025 | 1.80 | 0.1012, 0.1004 | 0.62 |
| `hky.kappa` | 26.34, 26.46 | 0.62 | 26.26, 26.43 | 1.05 |
| `posterior` | -1814.90, -1814.96 | 1.07 | -1814.90, -1814.90 | 0.13 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.006, beast3 0.001.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.131 | 0.120 | 0.010 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.842 | 0.847 | 0.005 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 9s | 5923 | 2391502 | 1615150 (`popSize`) |
| beast3 | 6s | 7986 | 4763970 | 4763970 (`posterior`) |

Run-time ratio beast3 / beast2: 0.68

