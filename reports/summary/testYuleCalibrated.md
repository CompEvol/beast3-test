# Posterior comparison: testYuleCalibrated

**Verdict: matched**

- beast2: `beast2/log/testYuleCalibrated/rep1`, `beast2/log/testYuleCalibrated/rep2`
- beast3: `beast3/log/testYuleCalibrated/rep1`, `beast3/log/testYuleCalibrated/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 566; max z: 1.317; max clade |Δp|: 0.006

## Findings

- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** column map used: `reports/maps/testYuleCalibrated.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testYuleCalibrated/rep1/ape.calyule.1.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m08s |  |
| beast2 | rep2 | `beast2/log/testYuleCalibrated/rep2/ape.calyule.2.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m08s |  |
| beast3 | rep1 | `beast3/log/testYuleCalibrated/rep1/ape.calyule.1.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 1m05s |  |
| beast3 | rep2 | `beast3/log/testYuleCalibrated/rep2/ape.calyule.2.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 1m05s |  |

## Parameters: `ape.calyule.N.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1845.64 | [-1850.45, -1841.19] | 3370 (1509) | -1845.60 | [-1850.50, -1841.19] | 4701 (2189) | 0.71 | 100% | ok |
| `likelihood` | -1816.85 | [-1821.13, -1813.11] | 2987 (1451) | -1816.81 | [-1821.19, -1813.13] | 3973 (1832) | 0.79 | 100% | ok |
| `prior` | -28.79 | [-32.16, -25.87] | 4743 (2319) | -28.79 | [-32.03, -25.79] | 6605 (3112) | 0.06 | 99% | ok |
| `treeLikelihood.lignment` | -1816.85 | [-1821.13, -1813.11] | 2987 (1451) | -1816.81 | [-1821.19, -1813.13] | 3973 (1832) | 0.79 | 100% | ok |
| `TreeHeight → Tree.height` | 16.9 | [7.621, 27.19] | 8805 (4304) | 16.91 | [8.145, 27.68] | 8795 (4294) | 0.12 | 97% | ok |
| `kappa` | 24.09 | [13.11, 37.38] | 1914 (934) | 24.04 | [12.9, 37.99] | 5030 (2345) | 0.24 | 100% | ok |
| `CalibratedYuleModel` | -13.2 | [-15.89, -10.53] | 9002 (4501) | -13.22 | [-15.82, -10.5] | 8629 (4128) | 0.87 | 99% | ok |
| `birthRateY` | 0.09711 | [0.01524, 0.2157] | 8461 (4189) | 0.098 | [0.01358, 0.2216] | 8401 (3900) | 0.94 | 100% | ok |
| `logP(mrca(chimpgroup))` | -1.758 | [-3.163, -1.262] | 8764 (4263) | -1.749 | [-3.126, -1.262] | 8925 (4424) | 0.93 | 100% | ok |
| `mrca.ge(chimpgroup)` | 5.6 | [3.14, 8.404] | 9002 (4501) | 5.592 | [3.264, 8.557] | 8307 (3891) | 0.40 | 98% | ok |
| `clockRate` | 0.003999 | [0.001916, 0.006426] | 9002 (4501) | 0.003995 | [0.00196, 0.006447] | 8633 (4132) | 0.24 | 100% | ok |
| `freqParameter.1` | 0.3255 | [0.2957, 0.3575] | 1290 (566) | 0.326 | [0.2966, 0.3576] | 1746 (830) | 0.90 | 100% | ok |
| `freqParameter.2` | 0.2572 | [0.2275, 0.2826] | 1336 (595) | 0.2569 | [0.2289, 0.2832] | 1710 (775) | 0.47 | 99% | ok |
| `freqParameter.3` | 0.1551 | [0.1336, 0.1788] | 1510 (664) | 0.1545 | [0.1325, 0.1768] | 2301 (1065) | 1.32 | 97% | ok |
| `freqParameter.4` | 0.2623 | [0.2351, 0.2916] | 1227 (606) | 0.2625 | [0.2343, 0.2888] | 1782 (825) | 0.44 | 99% | ok |

### Replicate agreement (baseline noise): `ape.calyule.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -1845.67, -1845.61 | 0.78 | -1845.60, -1845.60 | 0.07 |
| `likelihood` | -1816.93, -1816.78 | 1.84 | -1816.82, -1816.80 | 0.17 |
| `prior` | -28.75, -28.83 | 1.67 | -28.79, -28.79 | 0.17 |
| `treeLikelihood.lignment` | -1816.93, -1816.78 | 1.84 | -1816.82, -1816.80 | 0.17 |
| `TreeHeight → Tree.height` | 16.87, 16.94 | 0.57 | 16.98, 16.85 | 1.16 |
| `kappa` | 23.95, 24.22 | 0.88 | 23.97, 24.12 | 0.82 |
| `CalibratedYuleModel` | -13.19, -13.21 | 0.52 | -13.22, -13.21 | 0.38 |
| `birthRateY` | 0.0977, 0.09652 | 0.89 | 0.09683, 0.09916 | 1.75 |
| `logP(mrca(chimpgroup))` | -1.744, -1.773 | 1.92 | -1.753, -1.745 | 0.56 |
| `mrca.ge(chimpgroup)` | 5.572, 5.629 | 1.91 | 5.602, 5.581 | 0.66 |
| `clockRate` | 0.004002, 0.003996 | 0.20 | 0.003984, 0.004005 | 0.81 |
| `freqParameter.1` | 0.3256, 0.3253 | 0.35 | 0.3269, 0.3251 | 2.38 |
| `freqParameter.2` | 0.2577, 0.2567 | 1.24 | 0.2569, 0.257 | 0.17 |
| `freqParameter.3` | 0.1549, 0.1552 | 0.45 | 0.1542, 0.1549 | 1.53 |
| `freqParameter.4` | 0.2618, 0.2628 | 1.22 | 0.262, 0.263 | 1.42 |

## Trees: `ape.calyule.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.002, beast3 0.005.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.146 | 0.141 | 0.006 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.816 | 0.821 | 0.005 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, human} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2m15s | 3370 | 89713 | 32650 (`freqParameter.4`) |
| beast3 | 2m09s | 4701 | 130715 | 47555 (`freqParameter.2`) |

Run-time ratio beast3 / beast2: 0.96

