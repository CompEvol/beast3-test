# Posterior comparison: testCalibration

**Verdict: matched**

- beast2: `beast2/log/testCalibration/rep1`, `beast2/log/testCalibration/rep2`
- beast3: `beast3/log/testCalibration/rep1`, `beast3/log/testCalibration/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 571; max z: 1.328; max clade |Δp|: 0.000

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testCalibration/rep1/test.1.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 23s |  |
| beast2 | rep2 | `beast2/log/testCalibration/rep2/test.2.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 25s |  |
| beast3 | rep1 | `beast3/log/testCalibration/rep1/test.1.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 22s |  |
| beast3 | rep2 | `beast3/log/testCalibration/rep2/test.2.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 23s |  |

## Parameters: `test.N.log`

Constant columns (skipped): `monophyletic(human,chimp)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1971.15 | [-1976.01, -1967.13] | 2835 (1238) | -1971.12 | [-1975.73, -1966.87] | 3870 (1895) | 0.54 | 97% | ok |
| `prior` | -142.67 | [-145.24, -140.48] | 5244 (2510) | -142.65 | [-145.16, -140.47] | 7717 (3840) | 0.83 | 100% | ok |
| `tree.height` | 0.06422 | [0.05212, 0.07647] | 8192 (4074) | 0.06415 | [0.05254, 0.07616] | 8646 (4145) | 0.74 | 100% | ok |
| `mrca.age(human,chimp)` | 0.01702 | [0.0116, 0.02239] | 7984 (3812) | 0.01705 | [0.01196, 0.0227] | 8682 (4284) | 0.65 | 97% | ok |
| `popSize` | 0.1072 | [0.02929, 0.2202] | 8846 (4353) | 0.1067 | [0.03208, 0.2212] | 9002 (4501) | 0.62 | 99% | ok |
| `hky.kappa` | 27.11 | [13.95, 42.07] | 2554 (1245) | 26.86 | [13.71, 42.03] | 5470 (2659) | 1.33 | 100% | ok |
| `hky.frequencies.1` | 0.3268 | [0.2943, 0.3554] | 1201 (571) | 0.3262 | [0.2952, 0.3549] | 1984 (965) | 1.11 | 100% | ok |
| `hky.frequencies.2` | 0.2577 | [0.2307, 0.2845] | 1617 (787) | 0.2581 | [0.2307, 0.2861] | 1951 (865) | 0.97 | 100% | ok |
| `hky.frequencies.3` | 0.1549 | [0.1335, 0.1781] | 1522 (716) | 0.1548 | [0.1329, 0.1761] | 2529 (1243) | 0.24 | 99% | ok |
| `hky.frequencies.4` | 0.2606 | [0.2305, 0.2852] | 1583 (763) | 0.2609 | [0.2339, 0.2895] | 2020 (1010) | 0.56 | 94% | ok |
| `likelihood` | -1828.48 | [-1832.93, -1824.97] | 2727 (1232) | -1828.47 | [-1832.74, -1824.73] | 3563 (1765) | 0.24 | 98% | ok |
| `coalescent` | 6.861 | [5.156, 8.344] | 8276 (4074) | 6.855 | [5.115, 8.232] | 8940 (4467) | 0.52 | 99% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -1971.10, -1971.21 | 1.17 | -1971.12, -1971.12 | 0.07 |
| `prior` | -142.65, -142.69 | 1.34 | -142.64, -142.66 | 0.96 |
| `tree.height` | 0.06422, 0.06422 | 0.02 | 0.06411, 0.06419 | 0.65 |
| `mrca.age(human,chimp)` | 0.017, 0.01704 | 0.76 | 0.01703, 0.01706 | 0.53 |
| `popSize` | 0.1064, 0.1081 | 1.28 | 0.106, 0.1073 | 1.02 |
| `hky.kappa` | 26.96, 27.26 | 0.97 | 26.9, 26.83 | 0.35 |
| `hky.frequencies.1` | 0.3271, 0.3265 | 0.66 | 0.3259, 0.3264 | 0.66 |
| `hky.frequencies.2` | 0.2576, 0.2577 | 0.13 | 0.2585, 0.2578 | 1.18 |
| `hky.frequencies.3` | 0.1544, 0.1554 | 1.72 | 0.1548, 0.1548 | 0.09 |
| `hky.frequencies.4` | 0.2608, 0.2603 | 0.72 | 0.2607, 0.261 | 0.43 |
| `likelihood` | -1828.45, -1828.51 | 0.73 | -1828.48, -1828.46 | 0.30 |
| `coalescent` | 6.87, 6.852 | 0.96 | 6.874, 6.835 | 2.13 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.000, beast3 0.000.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {chimp, human} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, human} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 48s | 2835 | 210448 | 89144 (`hky.frequencies.1`) |
| beast3 | 45s | 3870 | 312599 | 157596 (`hky.frequencies.2`) |

Run-time ratio beast3 / beast2: 0.92

