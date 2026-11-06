# Posterior comparison: testYuleUncalibrated

**Verdict: matched**

- beast2: `beast2/log/testYuleUncalibrated/rep1`, `beast2/log/testYuleUncalibrated/rep2`, `beast2/log/testYuleUncalibrated/rep3`, `beast2/log/testYuleUncalibrated/rep4`
- beast3: `beast3/log/testYuleUncalibrated/rep1`, `beast3/log/testYuleUncalibrated/rep2`, `beast3/log/testYuleUncalibrated/rep3`, `beast3/log/testYuleUncalibrated/rep4`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 590; max z: 2.103; max clade |Δp|: 0.002

## Findings

- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** column map used: `reports/maps/testYuleUncalibrated.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testYuleUncalibrated/rep1/ape.yule.1.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m18s |  |
| beast2 | rep2 | `beast2/log/testYuleUncalibrated/rep2/ape.yule.2.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m19s |  |
| beast2 | rep3 | `beast2/log/testYuleUncalibrated/rep3/ape.yule.3.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m00s |  |
| beast2 | rep4 | `beast2/log/testYuleUncalibrated/rep4/ape.yule.4.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m00s |  |
| beast3 | rep1 | `beast3/log/testYuleUncalibrated/rep1/ape.yule.1.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 1m12s |  |
| beast3 | rep2 | `beast3/log/testYuleUncalibrated/rep2/ape.yule.2.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 1m14s |  |
| beast3 | rep3 | `beast3/log/testYuleUncalibrated/rep3/ape.yule.3.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 56s |  |
| beast3 | rep4 | `beast3/log/testYuleUncalibrated/rep4/ape.yule.4.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 56s |  |

## Parameters: `ape.yule.N.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1844.13 | [-1849.13, -1839.83] | 6614 (1589) | -1844.11 | [-1849.09, -1839.65] | 8836 (2143) | 0.63 | 100% | ok |
| `likelihood` | -1816.84 | [-1821.22, -1813.17] | 5960 (1346) | -1816.84 | [-1821.22, -1813.19] | 7572 (1804) | 0.04 | 100% | ok |
| `prior` | -27.29 | [-30.62, -24.29] | 10170 (2276) | -27.27 | [-30.59, -24.39] | 13929 (3291) | 1.13 | 100% | ok |
| `treeLikelihood.lignment` | -1816.84 | [-1821.22, -1813.17] | 5960 (1346) | -1816.84 | [-1821.22, -1813.19] | 7572 (1804) | 0.04 | 100% | ok |
| `TreeHeight → Tree.height` | 17.21 | [8.184, 28.25] | 17596 (4142) | 17.16 | [7.946, 28.17] | 17825 (4368) | 0.79 | 100% | ok |
| `kappa` | 24.01 | [12.74, 37.4] | 4876 (1074) | 24.04 | [12.43, 37] | 10219 (2417) | 0.30 | 99% | ok |
| `logP(mrca(chimpgroup))` | -1.762 | [-3.184, -1.262] | 17440 (4227) | -1.76 | [-3.174, -1.262] | 17504 (4231) | 0.23 | 100% | ok |
| `mrca.ge(chimpgroup)` | 5.59 | [3.055, 8.429] | 16920 (3950) | 5.569 | [3.016, 8.359] | 17872 (4396) | 1.39 | 99% | ok |
| `clockRate` | 0.003947 | [0.001808, 0.006275] | 17726 (4223) | 0.003959 | [0.001905, 0.006372] | 17707 (4371) | 0.92 | 98% | ok |
| `YuleModel` | -18.21 | [-21.38, -15.1] | 17720 (4217) | -18.17 | [-21.29, -15.01] | 17502 (4218) | 2.10 | 99% | ok |
| `birthRate` | 0.08354 | [0.01379, 0.1748] | 17801 (4391) | 0.08359 | [0.01384, 0.1713] | 16860 (3823) | 0.11 | 100% | ok |
| `freqParameter.1` | 0.326 | [0.2946, 0.3544] | 2605 (621) | 0.3262 | [0.2957, 0.3567] | 3103 (646) | 0.53 | 98% | ok |
| `freqParameter.2` | 0.2573 | [0.2308, 0.2856] | 3052 (721) | 0.2574 | [0.2297, 0.2849] | 3520 (701) | 0.19 | 99% | ok |
| `freqParameter.3` | 0.155 | [0.1311, 0.1765] | 3103 (672) | 0.1546 | [0.1314, 0.177] | 4451 (1019) | 1.30 | 99% | ok |
| `freqParameter.4` | 0.2617 | [0.235, 0.2911] | 2749 (590) | 0.2618 | [0.2327, 0.2895] | 3507 (781) | 0.17 | 97% | ok |

### Replicate agreement (baseline noise): `ape.yule.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -1844.14, -1844.11, -1844.16, -1844.12 | 0.54 | -1844.07, -1844.08, -1844.16, -1844.11 | 1.15 |
| `likelihood` | -1816.86, -1816.79, -1816.86, -1816.86 | 0.88 | -1816.82, -1816.83, -1816.88, -1816.83 | 0.84 |
| `prior` | -27.28, -27.32, -27.31, -27.26 | 1.23 | -27.25, -27.26, -27.28, -27.28 | 0.79 |
| `treeLikelihood.lignment` | -1816.86, -1816.79, -1816.86, -1816.86 | 0.88 | -1816.82, -1816.83, -1816.88, -1816.83 | 0.84 |
| `TreeHeight → Tree.height` | 17.15, 17.36, 17.19, 17.13 | 1.96 | 17.08, 17.12, 17.23, 17.23 | 1.32 |
| `kappa` | 23.85, 23.94, 24.13, 24.12 | 1.03 | 23.95, 24.16, 24.01, 24.06 | 1.14 |
| `logP(mrca(chimpgroup))` | -1.763, -1.772, -1.76, -1.753 | 1.24 | -1.761, -1.744, -1.768, -1.767 | 1.61 |
| `mrca.ge(chimpgroup)` | 5.583, 5.608, 5.584, 5.584 | 0.83 | 5.545, 5.558, 5.589, 5.583 | 1.48 |
| `clockRate` | 0.00396, 0.003914, 0.003955, 0.003959 | 1.86 | 0.003969, 0.003969, 0.003951, 0.003946 | 0.91 |
| `YuleModel` | -18.21, -18.25, -18.21, -18.17 | 2.41 | -18.16, -18.15, -18.19, -18.19 | 1.41 |
| `birthRate` | 0.08395, 0.08295, 0.08336, 0.08387 | 1.01 | 0.0846, 0.08417, 0.08272, 0.08287 | 1.91 |
| `freqParameter.1` | 0.326, 0.326, 0.3266, 0.3253 | 1.51 | 0.3262, 0.3259, 0.3265, 0.3262 | 0.81 |
| `freqParameter.2` | 0.2577, 0.2577, 0.2564, 0.2575 | 1.81 | 0.2573, 0.2574, 0.2578, 0.257 | 1.25 |
| `freqParameter.3` | 0.155, 0.155, 0.155, 0.1549 | 0.22 | 0.1544, 0.1548, 0.1539, 0.1554 | 2.99 |
| `freqParameter.4` | 0.2613, 0.2613, 0.262, 0.2624 | 1.45 | 0.2621, 0.2619, 0.2618, 0.2614 | 0.92 |

## Trees: `ape.yule.N.trees`

18004 trees (beast2) and 18004 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.014, beast3 0.018.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.824 | 0.822 | 0.002 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.141 | 0.141 | 0.001 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, human} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 4m36s | 6614 | 86152 | 33929 (`freqParameter.1`) |
| beast3 | 4m17s | 8836 | 124010 | 43543 (`freqParameter.1`) |

Run-time ratio beast3 / beast2: 0.93

