# Posterior comparison: C06-scale-vs-default

**Verdict: matched (ESS < 200)**

- default: `beast3/log/C06/rep1`, `beast3/log/C06/rep2`
- scale: `beast3/log/C06-scale/rep1`, `beast3/log/C06-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 199; max z: 2.546; max clade |Δp|: –

## Findings

- **WARN** ESS < 200 in at least one replicate for 1 column(s): `freqParameter.1stpos.1` (default). README: rerun longer before comparing
- **NOTE** Trace log file names differ: default `CN-bN.log` paired with scale `CN-bN-scale.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C06/rep1/C06-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 4m15s |  |
| default | rep2 | `beast3/log/C06/rep2/C06-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 4m14s |  |
| scale | rep1 | `beast3/log/C06-scale/rep1/C06-b3-scale.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 14m17s |  |
| scale | rep2 | `beast3/log/C06-scale/rep2/C06-b3-scale.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 14m17s |  |

## Parameters: `CN-bN.log / CN-bN-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5585.67 | [-5593.93, -5577.75] | 1769 (622) | -5585.43 | [-5593.73, -5577.78] | 1687 (699) | 1.72 | 100% | ok |
| `likelihood` | -5556.96 | [-5565.08, -5548.93] | 1606 (664) | -5556.79 | [-5565.06, -5549.04] | 1754 (703) | 1.21 | 100% | ok |
| `prior` | -28.71 | [-34.15, -23.44] | 1207 (506) | -28.64 | [-33.85, -23.29] | 1371 (678) | 0.65 | 99% | ok |
| `treeLikelihood.1stpos` | -1405.98 | [-1413.18, -1398.71] | 2743 (1366) | -1405.84 | [-1413.25, -1398.92] | 2791 (1330) | 1.41 | 99% | ok |
| `treeLikelihood.2ndpos` | -1005.89 | [-1012.31, -1000.02] | 1613 (764) | -1005.76 | [-1011.87, -999.67] | 1711 (798) | 1.19 | 97% | ok |
| `treeLikelihood.3rdpos` | -2173.71 | [-2189.64, -2158.77] | 1694 (789) | -2173.85 | [-2190.00, -2159.09] | 1964 (968) | 0.53 | 99% | ok |
| `treeLikelihood.noncoding` | -971.38 | [-976.56, -966.54] | 1550 (674) | -971.33 | [-976.42, -966.40] | 1905 (946) | 0.53 | 99% | ok |
| `Tree.height` | 1.387 | [1.027, 1.783] | 1151 (565) | 1.384 | [1.025, 1.768] | 1389 (693) | 0.37 | 100% | ok |
| `Tree.treeLength` | 6.781 | [5.261, 8.489] | 1067 (527) | 6.764 | [5.225, 8.363] | 1273 (636) | 0.51 | 99% | ok |
| `YuleModel` | -6.092 | [-9.085, -3.259] | 1449 (670) | -6.081 | [-9.169, -3.293] | 1618 (805) | 0.20 | 99% | ok |
| `birthRate` | 1.648 | [0.719, 2.706] | 5735 (2856) | 1.647 | [0.6833, 2.734] | 6755 (3240) | 0.17 | 100% | ok |
| `gammaShape.1stpos` | 0.3112 | [0.2434, 0.3846] | 1788 (849) | 0.3126 | [0.2423, 0.3831] | 2034 (991) | 1.20 | 99% | ok |
| `gammaShape.2ndpos` | 0.1445 | [0.1129, 0.1855] | 1524 (731) | 0.1452 | [0.1115, 0.185] | 1599 (721) | 1.01 | 99% | ok |
| `gammaShape.3rdpos` | 4.02 | [1.903, 6.718] | 2547 (1249) | 3.986 | [1.953, 6.55] | 2791 (1335) | 0.94 | 100% | ok |
| `gammaShape.noncoding` | 0.1392 | [0.1079, 0.1818] | 1703 (836) | 0.1404 | [0.1058, 0.1804] | 1757 (864) | 1.71 | 98% | ok |
| `kappa.1stpos` | 13.48 | [8.498, 18.8] | 1629 (716) | 13.32 | [8.628, 18.4] | 1633 (770) | 1.67 | 100% | ok |
| `kappa.2ndpos` | 23.06 | [10.52, 37.11] | 2206 (1049) | 22.96 | [10.57, 36.85] | 2138 (1064) | 0.49 | 100% | ok |
| `kappa.3rdpos` | 16.81 | [12.28, 21.88] | 830 (373) | 16.9 | [12.54, 22.24] | 930 (445) | 0.72 | 97% | ok |
| `kappa.noncoding` | 36.54 | [18.86, 55.38] | 1353 (578) | 36.37 | [20.41, 55.17] | 1485 (719) | 0.46 | 100% | ok |
| `freqParameter.1stpos.1` | 0.4434 | [0.3894, 0.4937] | 471 (199) ⚠ | 0.4423 | [0.3894, 0.4916] | 522 (232) | 0.66 | 100% | low ESS |
| `freqParameter.1stpos.2` | 0.2576 | [0.2189, 0.2984] | 583 (258) | 0.2571 | [0.2179, 0.2984] | 516 (226) | 0.47 | 100% | ok |
| `freqParameter.1stpos.3` | 0.1024 | [0.08057, 0.1262] | 854 (419) | 0.1038 | [0.08038, 0.1255] | 917 (409) | 2.55 | 100% | ok |
| `freqParameter.1stpos.4` | 0.1966 | [0.1615, 0.2293] | 622 (287) | 0.1968 | [0.1653, 0.23] | 806 (317) | 0.25 | 99% | ok |
| `freqParameter.2ndpos.1` | 0.191 | [0.149, 0.2355] | 721 (345) | 0.191 | [0.1467, 0.2324] | 705 (300) | 0.02 | 97% | ok |
| `freqParameter.2ndpos.2` | 0.3169 | [0.2671, 0.3623] | 628 (293) | 0.3161 | [0.2671, 0.3638] | 714 (292) | 0.59 | 100% | ok |
| `freqParameter.2ndpos.3` | 0.1025 | [0.06958, 0.1335] | 777 (362) | 0.101 | [0.06983, 0.1303] | 932 (401) | 2.00 | 100% | ok |
| `freqParameter.2ndpos.4` | 0.3896 | [0.3392, 0.4401] | 542 (218) | 0.3919 | [0.3409, 0.4425] | 627 (284) | 1.49 | 98% | ok |
| `freqParameter.3rdpos.1` | 0.4177 | [0.3772, 0.4577] | 560 (231) | 0.419 | [0.382, 0.4607] | 598 (277) | 1.11 | 96% | ok |
| `freqParameter.3rdpos.2` | 0.3668 | [0.3329, 0.3974] | 619 (237) | 0.3659 | [0.334, 0.3951] | 697 (333) | 1.00 | 100% | ok |
| `freqParameter.3rdpos.3` | 0.04889 | [0.03917, 0.05919] | 915 (438) | 0.04894 | [0.03837, 0.05858] | 1007 (386) | 0.18 | 97% | ok |
| `freqParameter.3rdpos.4` | 0.1666 | [0.1469, 0.1877] | 872 (393) | 0.1661 | [0.1447, 0.1869] | 819 (406) | 0.97 | 98% | ok |
| `freqParameter.noncoding.1` | 0.3875 | [0.3349, 0.4465] | 667 (271) | 0.3884 | [0.3328, 0.4431] | 645 (308) | 0.57 | 98% | ok |
| `freqParameter.noncoding.2` | 0.2276 | [0.1845, 0.2665] | 925 (437) | 0.2267 | [0.1852, 0.2681] | 698 (281) | 0.84 | 99% | ok |
| `freqParameter.noncoding.3` | 0.1211 | [0.09102, 0.1535] | 903 (430) | 0.1213 | [0.0907, 0.1525] | 815 (364) | 0.23 | 99% | ok |
| `freqParameter.noncoding.4` | 0.2638 | [0.2179, 0.3126] | 722 (301) | 0.2636 | [0.2162, 0.3081] | 661 (328) | 0.15 | 98% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -5585.62, -5585.73 | 0.52 | -5585.27, -5585.59 | 1.54 |
| `likelihood` | -5556.85, -5557.07 | 1.03 | -5556.62, -5556.95 | 1.65 |
| `prior` | -28.77, -28.66 | 0.67 | -28.65, -28.63 | 0.12 |
| `treeLikelihood.1stpos` | -1405.90, -1406.05 | 1.09 | -1405.87, -1405.81 | 0.42 |
| `treeLikelihood.2ndpos` | -1005.80, -1005.99 | 1.19 | -1005.71, -1005.82 | 0.77 |
| `treeLikelihood.3rdpos` | -2173.86, -2173.56 | 0.77 | -2173.69, -2174.01 | 0.88 |
| `treeLikelihood.noncoding` | -971.29, -971.47 | 1.31 | -971.35, -971.31 | 0.33 |
| `Tree.height` | 1.382, 1.392 | 0.84 | 1.386, 1.381 | 0.47 |
| `Tree.treeLength` | 6.758, 6.804 | 0.89 | 6.773, 6.754 | 0.41 |
| `YuleModel` | -6.057, -6.127 | 0.88 | -6.097, -6.066 | 0.41 |
| `birthRate` | 1.654, 1.643 | 0.80 | 1.644, 1.649 | 0.41 |
| `gammaShape.1stpos` | 0.3115, 0.3108 | 0.37 | 0.312, 0.3132 | 0.69 |
| `gammaShape.2ndpos` | 0.1449, 0.1441 | 0.81 | 0.1444, 0.1459 | 1.50 |
| `gammaShape.3rdpos` | 4.079, 3.962 | 2.20 | 3.978, 3.995 | 0.36 |
| `gammaShape.noncoding` | 0.1392, 0.1393 | 0.14 | 0.1402, 0.1406 | 0.38 |
| `kappa.1stpos` | 13.48, 13.47 | 0.13 | 13.24, 13.4 | 1.18 |
| `kappa.2ndpos` | 23.1, 23.03 | 0.25 | 23.01, 22.91 | 0.31 |
| `kappa.3rdpos` | 16.7, 16.92 | 1.28 | 16.95, 16.84 | 0.68 |
| `kappa.noncoding` | 36.51, 36.56 | 0.10 | 36.56, 36.18 | 0.77 |
| `freqParameter.1stpos.1` | 0.443, 0.4438 | 0.29 | 0.4405, 0.4441 | 1.63 |
| `freqParameter.1stpos.2` | 0.258, 0.2573 | 0.43 | 0.2577, 0.2564 | 0.74 |
| `freqParameter.1stpos.3` | 0.1012, 0.1035 | 2.81 | 0.104, 0.1036 | 0.42 |
| `freqParameter.1stpos.4` | 0.1977, 0.1955 | 1.60 | 0.1978, 0.1959 | 1.56 |
| `freqParameter.2ndpos.1` | 0.1901, 0.1918 | 1.02 | 0.1909, 0.1911 | 0.08 |
| `freqParameter.2ndpos.2` | 0.3175, 0.3164 | 0.55 | 0.3169, 0.3153 | 0.86 |
| `freqParameter.2ndpos.3` | 0.1021, 0.1029 | 0.74 | 0.1008, 0.1011 | 0.35 |
| `freqParameter.2ndpos.4` | 0.3904, 0.3889 | 0.64 | 0.3914, 0.3925 | 0.52 |
| `freqParameter.3rdpos.1` | 0.4179, 0.4175 | 0.19 | 0.4196, 0.4184 | 0.74 |
| `freqParameter.3rdpos.2` | 0.3667, 0.3669 | 0.13 | 0.3657, 0.366 | 0.24 |
| `freqParameter.3rdpos.3` | 0.04896, 0.04883 | 0.38 | 0.04887, 0.04901 | 0.41 |
| `freqParameter.3rdpos.4` | 0.1665, 0.1668 | 0.42 | 0.1657, 0.1665 | 1.11 |
| `freqParameter.noncoding.1` | 0.3879, 0.387 | 0.38 | 0.388, 0.3888 | 0.34 |
| `freqParameter.noncoding.2` | 0.2268, 0.2283 | 1.07 | 0.2265, 0.2269 | 0.24 |
| `freqParameter.noncoding.3` | 0.1208, 0.1215 | 0.63 | 0.1215, 0.1211 | 0.29 |
| `freqParameter.noncoding.4` | 0.2644, 0.2632 | 0.69 | 0.264, 0.2632 | 0.45 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 8m28s | 1769 | 12535 | 3337 (`freqParameter.1stpos.1`) |
| scale | 28m34s | 1687 | 3543 | 1084 (`freqParameter.1stpos.2`) |

Run-time ratio scale / default: 3.37

