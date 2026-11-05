# Posterior comparison: testYuleUncalibrated

**Verdict: matched**

- beast2: `beast2/log/testYuleUncalibrated/rep1`, `beast2/log/testYuleUncalibrated/rep2`
- beast3: `beast3/log/testYuleUncalibrated/rep1`, `beast3/log/testYuleUncalibrated/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 557; max z: 1.601; max clade |Δp|: 0.001

## Findings

- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** column map used: `reports/maps/testYuleUncalibrated.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testYuleUncalibrated/rep1/ape.yule.1.log` | 10001 (9001) | 1000 | 2.7.9 Prerelease | yes | 1m01s |  |
| beast2 | rep2 | `beast2/log/testYuleUncalibrated/rep2/ape.yule.2.log` | 10001 (9001) | 1000 | 2.7.9 Prerelease | yes | 1m01s |  |
| beast3 | rep1 | `beast3/log/testYuleUncalibrated/rep1/ape.yule.1.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 57s |  |
| beast3 | rep2 | `beast3/log/testYuleUncalibrated/rep2/ape.yule.2.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 57s |  |

## Parameters: `ape.yule.N.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1845.45 | [-1850.53, -1841.06] | 3205 (1424) | -1845.38 | [-1850.31, -1841.05] | 4909 (2184) | 1.14 | 100% | ok |
| `likelihood` | -1816.89 | [-1821.41, -1813.17] | 2918 (1328) | -1816.86 | [-1821.19, -1813.05] | 4024 (1748) | 0.65 | 98% | ok |
| `prior` | -28.56 | [-32.29, -25.49] | 6122 (2917) | -28.52 | [-32.03, -25.42] | 10592 (4967) | 1.09 | 99% | ok |
| `treeLikelihood.lignment` | -1816.89 | [-1821.41, -1813.17] | 2918 (1328) | -1816.86 | [-1821.19, -1813.05] | 4024 (1748) | 0.65 | 98% | ok |
| `TreeHeight → Tree.height` | 14.62 | [6.796, 23.78] | 16817 (8196) | 14.57 | [6.665, 23.56] | 18002 (9001) | 1.00 | 99% | ok |
| `kappa` | 24.1 | [13.1, 37.92] | 1808 (762) | 23.89 | [13.35, 37.51] | 5269 (2537) | 1.09 | 100% | ok |
| `logP(mrca(chimpgroup))` | -1.887 | [-3.622, -1.262] | 18002 (9001) | -1.894 | [-3.657, -1.262] | 17945 (8944) | 0.79 | 100% | ok |
| `mrca.ge(chimpgroup)` | 4.982 | [2.673, 7.483] | 16959 (8184) | 4.96 | [2.727, 7.492] | 17161 (8160) | 1.60 | 100% | ok |
| `clockRate` | 0.004625 | [0.002279, 0.007481] | 16720 (8173) | 0.004646 | [0.002297, 0.007506] | 18002 (9001) | 1.40 | 100% | ok |
| `YuleModel` | -17.43 | [-20.54, -14.26] | 17372 (8640) | -17.41 | [-20.62, -14.37] | 18002 (9001) | 0.90 | 99% | ok |
| `birthRate` | 0.1156 | [0.02709, 0.2373] | 16254 (7838) | 0.116 | [0.02287, 0.2325] | 16965 (7964) | 0.59 | 98% | ok |
| `freqParameter.1` | 0.3263 | [0.2966, 0.3586] | 1286 (585) | 0.3254 | [0.2937, 0.3559] | 1522 (700) | 1.53 | 96% | ok |
| `freqParameter.2` | 0.2569 | [0.2273, 0.2833] | 1221 (557) | 0.2574 | [0.2297, 0.2833] | 1936 (913) | 0.97 | 100% | ok |
| `freqParameter.3` | 0.1552 | [0.1327, 0.1782] | 1760 (747) | 0.155 | [0.1328, 0.1771] | 2305 (1128) | 0.57 | 100% | ok |
| `freqParameter.4` | 0.2616 | [0.2323, 0.2868] | 1299 (623) | 0.2622 | [0.2339, 0.2893] | 1740 (783) | 1.20 | 97% | ok |

### Replicate agreement (baseline noise): `ape.yule.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -1845.42, -1845.48 | 0.74 | -1845.41, -1845.36 | 0.72 |
| `likelihood` | -1816.87, -1816.92 | 0.65 | -1816.91, -1816.81 | 1.41 |
| `prior` | -28.55, -28.56 | 0.30 | -28.5, -28.55 | 1.41 |
| `treeLikelihood.lignment` | -1816.87, -1816.92 | 0.65 | -1816.91, -1816.81 | 1.41 |
| `TreeHeight → Tree.height` | 14.62, 14.62 | 0.07 | 14.59, 14.56 | 0.40 |
| `kappa` | 24.07, 24.13 | 0.17 | 23.7, 24.08 | 2.09 |
| `logP(mrca(chimpgroup))` | -1.889, -1.884 | 0.34 | -1.897, -1.89 | 0.55 |
| `mrca.ge(chimpgroup)` | 4.981, 4.984 | 0.19 | 4.962, 4.959 | 0.12 |
| `clockRate` | 0.004628, 0.004623 | 0.25 | 0.004651, 0.004642 | 0.42 |
| `YuleModel` | -17.42, -17.44 | 0.61 | -17.41, -17.42 | 0.28 |
| `birthRate` | 0.116, 0.1153 | 0.71 | 0.116, 0.116 | 0.08 |
| `freqParameter.1` | 0.3266, 0.326 | 0.65 | 0.3257, 0.3251 | 0.64 |
| `freqParameter.2` | 0.257, 0.2567 | 0.33 | 0.2575, 0.2572 | 0.42 |
| `freqParameter.3` | 0.1553, 0.1552 | 0.18 | 0.1548, 0.1552 | 0.90 |
| `freqParameter.4` | 0.2611, 0.2621 | 1.20 | 0.262, 0.2624 | 0.53 |

## Trees: `ape.yule.N.trees`

18002 trees (beast2) and 18002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.009, beast3 0.012.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.150 | 0.149 | 0.001 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.811 | 0.811 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, human} | 3 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2m02s | 3205 | 94889 | 36154 (`freqParameter.2`) |
| beast3 | 1m55s | 4909 | 154202 | 47802 (`freqParameter.1`) |

Run-time ratio beast3 / beast2: 0.94

