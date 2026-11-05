# Posterior comparison: testYuleCalibrated

**Verdict: matched**

- beast2: `beast2/log/testYuleCalibrated/rep1`, `beast2/log/testYuleCalibrated/rep2`
- beast3: `beast3/log/testYuleCalibrated/rep1`, `beast3/log/testYuleCalibrated/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 473; max z: 1.998; max clade |Δp|: 0.004

## Findings

- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** column map used: `reports/maps/testYuleCalibrated.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testYuleCalibrated/rep1/ape.calyule.1.log` | 10001 (9001) | 1000 | 2.7.9 Prerelease | yes | 1m00s |  |
| beast2 | rep2 | `beast2/log/testYuleCalibrated/rep2/ape.calyule.2.log` | 10001 (9001) | 1000 | 2.7.9 Prerelease | yes | 1m01s |  |
| beast3 | rep1 | `beast3/log/testYuleCalibrated/rep1/ape.calyule.1.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 58s |  |
| beast3 | rep2 | `beast3/log/testYuleCalibrated/rep2/ape.calyule.2.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 58s |  |

## Parameters: `ape.calyule.N.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1847.73 | [-1852.76, -1843.34] | 3710 (1763) | -1847.68 | [-1852.62, -1843.22] | 5331 (2319) | 0.94 | 99% | ok |
| `likelihood` | -1816.86 | [-1821.15, -1813.08] | 2949 (1429) | -1816.85 | [-1821.33, -1813.23] | 3964 (1845) | 0.10 | 98% | ok |
| `prior` | -30.88 | [-34.38, -27.86] | 5455 (2501) | -30.83 | [-34.38, -27.9] | 11156 (5396) | 1.62 | 100% | ok |
| `treeLikelihood.lignment` | -1816.86 | [-1821.15, -1813.08] | 2949 (1429) | -1816.85 | [-1821.33, -1813.23] | 3964 (1845) | 0.10 | 98% | ok |
| `TreeHeight → Tree.height` | 15.63 | [7.245, 25.52] | 17168 (8433) | 15.68 | [7.171, 25.7] | 16919 (7987) | 1.01 | 100% | ok |
| `kappa` | 24.16 | [12.91, 38.35] | 2004 (831) | 23.81 | [13.02, 37.11] | 5616 (2639) | 2.00 | 100% | ok |
| `CalibratedYuleModel` | -12.91 | [-15.67, -10.26] | 17941 (8940) | -12.92 | [-15.68, -10.26] | 16778 (8220) | 0.47 | 100% | ok |
| `birthRateY` | 0.1066 | [0.01143, 0.2376] | 16042 (7804) | 0.1057 | [0.01133, 0.2342] | 18002 (9001) | 1.32 | 100% | ok |
| `logP(mrca(chimpgroup))` | -1.804 | [-3.315, -1.262] | 17477 (8476) | -1.793 | [-3.283, -1.262] | 17841 (8840) | 1.32 | 100% | ok |
| `mrca.ge(chimpgroup)` | 5.29 | [2.915, 8.041] | 17652 (8769) | 5.304 | [2.969, 8.055] | 17168 (8493) | 0.91 | 100% | ok |
| `clockRate` | 0.004338 | [0.001991, 0.006906] | 17112 (8473) | 0.004324 | [0.001996, 0.006924] | 15828 (7466) | 0.95 | 100% | ok |
| `freqParameter.1` | 0.3259 | [0.2959, 0.3558] | 1112 (473) | 0.326 | [0.2972, 0.3568] | 1830 (886) | 0.27 | 98% | ok |
| `freqParameter.2` | 0.2573 | [0.23, 0.2854] | 1333 (635) | 0.2572 | [0.2292, 0.2842] | 1968 (896) | 0.15 | 99% | ok |
| `freqParameter.3` | 0.1548 | [0.1323, 0.176] | 1519 (698) | 0.1546 | [0.1325, 0.1767] | 2338 (1141) | 0.66 | 100% | ok |
| `freqParameter.4` | 0.262 | [0.2333, 0.2888] | 1352 (658) | 0.2621 | [0.234, 0.2888] | 1760 (742) | 0.32 | 100% | ok |

### Replicate agreement (baseline noise): `ape.calyule.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -1847.68, -1847.79 | 1.33 | -1847.67, -1847.69 | 0.29 |
| `likelihood` | -1816.82, -1816.89 | 0.79 | -1816.86, -1816.84 | 0.25 |
| `prior` | -30.85, -30.9 | 1.00 | -30.81, -30.85 | 1.17 |
| `treeLikelihood.lignment` | -1816.82, -1816.89 | 0.79 | -1816.86, -1816.84 | 0.25 |
| `TreeHeight → Tree.height` | 15.57, 15.69 | 1.57 | 15.75, 15.62 | 1.72 |
| `kappa` | 24.06, 24.26 | 0.62 | 23.57, 24.05 | 2.77 |
| `CalibratedYuleModel` | -12.91, -12.92 | 0.25 | -12.93, -12.91 | 0.83 |
| `birthRateY` | 0.1072, 0.106 | 1.13 | 0.1053, 0.1061 | 0.80 |
| `logP(mrca(chimpgroup))` | -1.792, -1.815 | 2.04 | -1.8, -1.786 | 1.29 |
| `mrca.ge(chimpgroup)` | 5.288, 5.293 | 0.24 | 5.315, 5.292 | 1.13 |
| `clockRate` | 0.004341, 0.004335 | 0.30 | 0.004312, 0.004336 | 1.15 |
| `freqParameter.1` | 0.3259, 0.3259 | 0.03 | 0.3266, 0.3255 | 1.44 |
| `freqParameter.2` | 0.2573, 0.2573 | 0.11 | 0.2569, 0.2576 | 1.03 |
| `freqParameter.3` | 0.1547, 0.1549 | 0.38 | 0.1543, 0.1548 | 1.02 |
| `freqParameter.4` | 0.262, 0.2619 | 0.14 | 0.2622, 0.2621 | 0.15 |

## Trees: `ape.calyule.N.trees`

18002 trees (beast2) and 18002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.003, beast3 0.005.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.146 | 0.150 | 0.004 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.814 | 0.813 | 0.001 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, human} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2m01s | 3710 | 110273 | 33068 (`freqParameter.1`) |
| beast3 | 1m55s | 5331 | 166241 | 54879 (`freqParameter.4`) |

Run-time ratio beast3 / beast2: 0.95

