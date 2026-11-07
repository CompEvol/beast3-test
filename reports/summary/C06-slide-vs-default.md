# Posterior comparison: C06-slide-vs-default

**Verdict: borderline (ESS < 200)**

- default: `beast3/log/C06/rep1`, `beast3/log/C06/rep2`
- slide: `beast3/log/C06-slide/rep1`, `beast3/log/C06-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 179; max z: 3.163; max clade |Δp|: –

## Findings

- **FLAG** `freqParameter.2ndpos.3`: z = 3.16 (default mean 0.1025, slide mean 0.1001)
- **WARN** ESS < 200 in at least one replicate for 2 column(s): `freqParameter.1stpos.1` (default), `freqParameter.3rdpos.1` (slide). README: rerun longer before comparing
- **NOTE** Trace log file names differ: default `CN-bN.log` paired with slide `CN-bN-slide.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C06/rep1/C06-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 4m15s |  |
| default | rep2 | `beast3/log/C06/rep2/C06-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 4m14s |  |
| slide | rep1 | `beast3/log/C06-slide/rep1/C06-b3-slide.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 14m08s |  |
| slide | rep2 | `beast3/log/C06-slide/rep2/C06-b3-slide.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 14m09s |  |

## Parameters: `CN-bN.log / CN-bN-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5585.67 | [-5593.93, -5577.75] | 1769 (622) | -5585.50 | [-5593.87, -5577.55] | 1816 (866) | 1.24 | 100% | ok |
| `likelihood` | -5556.96 | [-5565.08, -5548.93] | 1606 (664) | -5556.70 | [-5565.30, -5549.33] | 1426 (620) | 1.72 | 99% | ok |
| `prior` | -28.71 | [-34.15, -23.44] | 1207 (506) | -28.8 | [-34.46, -23.83] | 1104 (418) | 0.76 | 97% | ok |
| `treeLikelihood.1stpos` | -1405.98 | [-1413.18, -1398.71] | 2743 (1366) | -1405.88 | [-1412.77, -1398.61] | 2976 (1350) | 0.94 | 99% | ok |
| `treeLikelihood.2ndpos` | -1005.89 | [-1012.31, -1000.02] | 1613 (764) | -1005.71 | [-1012.07, -999.84] | 1772 (834) | 1.65 | 99% | ok |
| `treeLikelihood.3rdpos` | -2173.71 | [-2189.64, -2158.77] | 1694 (789) | -2173.65 | [-2189.31, -2158.65] | 1859 (855) | 0.23 | 100% | ok |
| `treeLikelihood.noncoding` | -971.38 | [-976.56, -966.54] | 1550 (674) | -971.45 | [-976.66, -966.50] | 1884 (909) | 0.77 | 100% | ok |
| `Tree.height` | 1.387 | [1.027, 1.783] | 1151 (565) | 1.388 | [1.026, 1.769] | 1212 (543) | 0.14 | 100% | ok |
| `Tree.treeLength` | 6.781 | [5.261, 8.489] | 1067 (527) | 6.784 | [5.241, 8.398] | 1138 (511) | 0.08 | 99% | ok |
| `YuleModel` | -6.092 | [-9.085, -3.259] | 1449 (670) | -6.113 | [-9.096, -3.222] | 1423 (604) | 0.37 | 100% | ok |
| `birthRate` | 1.648 | [0.719, 2.706] | 5735 (2856) | 1.643 | [0.6577, 2.69] | 6581 (3076) | 0.59 | 99% | ok |
| `gammaShape.1stpos` | 0.3112 | [0.2434, 0.3846] | 1788 (849) | 0.3109 | [0.2437, 0.3872] | 2064 (1018) | 0.25 | 100% | ok |
| `gammaShape.2ndpos` | 0.1445 | [0.1129, 0.1855] | 1524 (731) | 0.1446 | [0.112, 0.1827] | 1576 (758) | 0.26 | 99% | ok |
| `gammaShape.3rdpos` | 4.02 | [1.903, 6.718] | 2547 (1249) | 4.03 | [2.008, 6.69] | 2391 (1070) | 0.27 | 100% | ok |
| `gammaShape.noncoding` | 0.1392 | [0.1079, 0.1818] | 1703 (836) | 0.1408 | [0.1073, 0.1828] | 1798 (712) | 2.30 | 100% | ok |
| `kappa.1stpos` | 13.48 | [8.498, 18.8] | 1629 (716) | 13.41 | [8.434, 18.63] | 1715 (799) | 0.66 | 99% | ok |
| `kappa.2ndpos` | 23.06 | [10.52, 37.11] | 2206 (1049) | 23.25 | [10.81, 36.96] | 1832 (899) | 0.83 | 100% | ok |
| `kappa.3rdpos` | 16.81 | [12.28, 21.88] | 830 (373) | 16.88 | [12.04, 21.77] | 892 (397) | 0.55 | 99% | ok |
| `kappa.noncoding` | 36.54 | [18.86, 55.38] | 1353 (578) | 36.3 | [19.16, 55.08] | 1338 (662) | 0.63 | 100% | ok |
| `freqParameter.1stpos.1` | 0.4434 | [0.3894, 0.4937] | 471 (199) ⚠ | 0.4444 | [0.3987, 0.4957] | 666 (320) | 0.66 | 98% | low ESS |
| `freqParameter.1stpos.2` | 0.2576 | [0.2189, 0.2984] | 583 (258) | 0.2575 | [0.2187, 0.2984] | 780 (389) | 0.10 | 100% | ok |
| `freqParameter.1stpos.3` | 0.1024 | [0.08057, 0.1262] | 854 (419) | 0.1034 | [0.08062, 0.1268] | 990 (476) | 1.78 | 100% | ok |
| `freqParameter.1stpos.4` | 0.1966 | [0.1615, 0.2293] | 622 (287) | 0.1947 | [0.1617, 0.2276] | 868 (425) | 2.10 | 100% | ok |
| `freqParameter.2ndpos.1` | 0.191 | [0.149, 0.2355] | 721 (345) | 0.1913 | [0.146, 0.2337] | 749 (338) | 0.24 | 98% | ok |
| `freqParameter.2ndpos.2` | 0.3169 | [0.2671, 0.3623] | 628 (293) | 0.3188 | [0.2759, 0.3676] | 747 (351) | 1.46 | 94% | ok |
| `freqParameter.2ndpos.3` | 0.1025 | [0.06958, 0.1335] | 777 (362) | 0.1001 | [0.0713, 0.1297] | 1010 (356) | 3.16 | 100% | **z** |
| `freqParameter.2ndpos.4` | 0.3896 | [0.3392, 0.4401] | 542 (218) | 0.3898 | [0.3437, 0.4393] | 829 (398) | 0.14 | 100% | ok |
| `freqParameter.3rdpos.1` | 0.4177 | [0.3772, 0.4577] | 560 (231) | 0.4185 | [0.3729, 0.4563] | 415 (179) ⚠ | 0.58 | 98% | low ESS |
| `freqParameter.3rdpos.2` | 0.3668 | [0.3329, 0.3974] | 619 (237) | 0.3664 | [0.3298, 0.399] | 540 (267) | 0.42 | 100% | ok |
| `freqParameter.3rdpos.3` | 0.04889 | [0.03917, 0.05919] | 915 (438) | 0.04865 | [0.03859, 0.05841] | 1082 (472) | 1.05 | 97% | ok |
| `freqParameter.3rdpos.4` | 0.1666 | [0.1469, 0.1877] | 872 (393) | 0.1665 | [0.1476, 0.1861] | 814 (321) | 0.23 | 100% | ok |
| `freqParameter.noncoding.1` | 0.3875 | [0.3349, 0.4465] | 667 (271) | 0.3869 | [0.3304, 0.4442] | 599 (296) | 0.37 | 98% | ok |
| `freqParameter.noncoding.2` | 0.2276 | [0.1845, 0.2665] | 925 (437) | 0.228 | [0.1872, 0.2708] | 662 (287) | 0.37 | 97% | ok |
| `freqParameter.noncoding.3` | 0.1211 | [0.09102, 0.1535] | 903 (430) | 0.1205 | [0.08967, 0.152] | 904 (430) | 0.89 | 98% | ok |
| `freqParameter.noncoding.4` | 0.2638 | [0.2179, 0.3126] | 722 (301) | 0.2647 | [0.2217, 0.3118] | 586 (278) | 0.68 | 100% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -5585.62, -5585.73 | 0.52 | -5585.52, -5585.48 | 0.23 |
| `likelihood` | -5556.85, -5557.07 | 1.03 | -5556.79, -5556.61 | 0.82 |
| `prior` | -28.77, -28.66 | 0.67 | -28.73, -28.87 | 0.81 |
| `treeLikelihood.1stpos` | -1405.90, -1406.05 | 1.09 | -1405.83, -1405.94 | 0.85 |
| `treeLikelihood.2ndpos` | -1005.80, -1005.99 | 1.19 | -1005.70, -1005.73 | 0.19 |
| `treeLikelihood.3rdpos` | -2173.86, -2173.56 | 0.77 | -2173.86, -2173.45 | 1.11 |
| `treeLikelihood.noncoding` | -971.29, -971.47 | 1.31 | -971.41, -971.49 | 0.70 |
| `Tree.height` | 1.382, 1.392 | 0.84 | 1.383, 1.393 | 0.90 |
| `Tree.treeLength` | 6.758, 6.804 | 0.89 | 6.762, 6.806 | 0.90 |
| `YuleModel` | -6.057, -6.127 | 0.88 | -6.072, -6.154 | 1.02 |
| `birthRate` | 1.654, 1.643 | 0.80 | 1.65, 1.635 | 1.14 |
| `gammaShape.1stpos` | 0.3115, 0.3108 | 0.37 | 0.3121, 0.3097 | 1.47 |
| `gammaShape.2ndpos` | 0.1449, 0.1441 | 0.81 | 0.1449, 0.1443 | 0.62 |
| `gammaShape.3rdpos` | 4.079, 3.962 | 2.20 | 4.022, 4.039 | 0.33 |
| `gammaShape.noncoding` | 0.1392, 0.1393 | 0.14 | 0.1405, 0.141 | 0.52 |
| `kappa.1stpos` | 13.48, 13.47 | 0.13 | 13.32, 13.51 | 1.51 |
| `kappa.2ndpos` | 23.1, 23.03 | 0.25 | 23.34, 23.16 | 0.56 |
| `kappa.3rdpos` | 16.7, 16.92 | 1.28 | 16.77, 16.99 | 1.30 |
| `kappa.noncoding` | 36.51, 36.56 | 0.10 | 36.25, 36.35 | 0.17 |
| `freqParameter.1stpos.1` | 0.443, 0.4438 | 0.29 | 0.4443, 0.4445 | 0.10 |
| `freqParameter.1stpos.2` | 0.258, 0.2573 | 0.43 | 0.257, 0.258 | 0.71 |
| `freqParameter.1stpos.3` | 0.1012, 0.1035 | 2.81 | 0.1032, 0.1035 | 0.38 |
| `freqParameter.1stpos.4` | 0.1977, 0.1955 | 1.60 | 0.1955, 0.1939 | 1.32 |
| `freqParameter.2ndpos.1` | 0.1901, 0.1918 | 1.02 | 0.1906, 0.1919 | 0.80 |
| `freqParameter.2ndpos.2` | 0.3175, 0.3164 | 0.55 | 0.3184, 0.3193 | 0.52 |
| `freqParameter.2ndpos.3` | 0.1021, 0.1029 | 0.74 | 0.09982, 0.1004 | 0.57 |
| `freqParameter.2ndpos.4` | 0.3904, 0.3889 | 0.64 | 0.3912, 0.3884 | 1.62 |
| `freqParameter.3rdpos.1` | 0.4179, 0.4175 | 0.19 | 0.4178, 0.4191 | 0.60 |
| `freqParameter.3rdpos.2` | 0.3667, 0.3669 | 0.13 | 0.3665, 0.3662 | 0.15 |
| `freqParameter.3rdpos.3` | 0.04896, 0.04883 | 0.38 | 0.04882, 0.04848 | 1.07 |
| `freqParameter.3rdpos.4` | 0.1665, 0.1668 | 0.42 | 0.1669, 0.1662 | 0.92 |
| `freqParameter.noncoding.1` | 0.3879, 0.387 | 0.38 | 0.3868, 0.3869 | 0.03 |
| `freqParameter.noncoding.2` | 0.2268, 0.2283 | 1.07 | 0.2275, 0.2284 | 0.56 |
| `freqParameter.noncoding.3` | 0.1208, 0.1215 | 0.63 | 0.1212, 0.1197 | 1.37 |
| `freqParameter.noncoding.4` | 0.2644, 0.2632 | 0.69 | 0.2645, 0.265 | 0.25 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 8m28s | 1769 | 12535 | 3337 (`freqParameter.1stpos.1`) |
| slide | 28m17s | 1816 | 3853 | 881 (`freqParameter.3rdpos.1`) |

Run-time ratio slide / default: 3.34

