# Posterior comparison: C13-scale-vs-default

**Verdict: not matched**

- default: `beast3/log/C13/rep1`, `beast3/log/C13/rep2`
- scale: `beast3/log/C13-scale/rep1`, `beast3/log/C13-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 243; max z: 35.24; max clade |Δp|: –

## Findings

- **FLAG** `posterior`: z = 35.14 (default mean -6631.30, scale mean -6697.24)
- **FLAG** `prior`: z = 35.24 (default mean -1111.45, scale mean -1177.71)
- **FLAG** `indicators.alltrees.2`: z = 3.13 (default mean 0.002481, scale mean 0.00487)
- **FLAG** `indicators.alltrees.5`: z = 3.15 (default mean 0.003, scale mean 0.005907)
- **FLAG** `indicators.alltrees.14`: z = 3.82 (default mean 0.001704, scale mean 0.004352)
- **FLAG** `indicators.alltrees.93`: z = 3.11 (default mean 0.002204, scale mean 0.0045)
- **FLAG** `indicators.alltrees.118`: z = 3.78 (default mean 0.007777, scale mean 0.01213)
- **FLAG** `indicators.alltrees.125`: z = 3.13 (default mean 0.0277, scale mean 0.03487)
- **FLAG** `indicators.alltrees.128`: z = 5.70 (default mean 0.0445, scale mean 0.03261)
- **FLAG** `popSizes.alltrees.1`: z = 5.25 (default mean 38.2, scale mean 37.27)
- **FLAG** `popSizes.alltrees.2`: z = 21.01 (default mean 19.59, scale mean 42.26)
- **FLAG** `popSizes.alltrees.3`: z = 18.89 (default mean 21.04, scale mean 42.72)
- **FLAG** `popSizes.alltrees.4`: z = 13.50 (default mean 23.7, scale mean 42.33)
- **FLAG** `popSizes.alltrees.5`: z = 17.00 (default mean 21.3, scale mean 42.64)
- **FLAG** `popSizes.alltrees.6`: z = 20.47 (default mean 18.93, scale mean 42.75)
- **FLAG** `popSizes.alltrees.7`: z = 14.72 (default mean 22.74, scale mean 42.37)
- **FLAG** `popSizes.alltrees.8`: z = 16.28 (default mean 21.15, scale mean 42.45)
- **FLAG** `popSizes.alltrees.9`: z = 19.41 (default mean 20.29, scale mean 42.91)
- **FLAG** `popSizes.alltrees.10`: z = 16.74 (default mean 21.68, scale mean 42.67)
- **FLAG** `popSizes.alltrees.11`: z = 20.20 (default mean 19.97, scale mean 43.06)
- **FLAG** `popSizes.alltrees.12`: z = 17.56 (default mean 21.48, scale mean 41.92)
- **FLAG** `popSizes.alltrees.13`: z = 19.46 (default mean 20.73, scale mean 42.39)
- **FLAG** `popSizes.alltrees.14`: z = 16.43 (default mean 22.09, scale mean 42.57)
- **FLAG** `popSizes.alltrees.15`: z = 18.31 (default mean 20.04, scale mean 42.86)
- **FLAG** `popSizes.alltrees.16`: z = 15.42 (default mean 22.27, scale mean 42.59)
- **FLAG** `popSizes.alltrees.17`: z = 18.86 (default mean 20.13, scale mean 42.11)
- **FLAG** `popSizes.alltrees.18`: z = 18.60 (default mean 20.74, scale mean 42.12)
- **FLAG** `popSizes.alltrees.19`: z = 15.72 (default mean 21.08, scale mean 42.19)
- **FLAG** `popSizes.alltrees.20`: z = 18.74 (default mean 20.71, scale mean 42.75)
- **FLAG** `popSizes.alltrees.21`: z = 18.84 (default mean 20.42, scale mean 42.81)
- **FLAG** `popSizes.alltrees.22`: z = 14.98 (default mean 21.81, scale mean 42.23)
- **FLAG** `popSizes.alltrees.23`: z = 19.41 (default mean 20.32, scale mean 43)
- **FLAG** `popSizes.alltrees.24`: z = 18.34 (default mean 21.01, scale mean 42.76)
- **FLAG** `popSizes.alltrees.25`: z = 20.43 (default mean 19.34, scale mean 42.08)
- **FLAG** `popSizes.alltrees.26`: z = 14.53 (default mean 21.13, scale mean 42.56)
- **FLAG** `popSizes.alltrees.27`: z = 16.49 (default mean 21.6, scale mean 42.8)
- **FLAG** `popSizes.alltrees.28`: z = 16.55 (default mean 21.69, scale mean 43.36)
- **FLAG** `popSizes.alltrees.29`: z = 13.05 (default mean 23.2, scale mean 42.46)
- **FLAG** `popSizes.alltrees.30`: z = 19.01 (default mean 20.6, scale mean 43.09)
- **FLAG** `popSizes.alltrees.31`: z = 16.94 (default mean 20.46, scale mean 42.79)
- **FLAG** `popSizes.alltrees.32`: z = 15.17 (default mean 21.9, scale mean 42.69)
- **FLAG** `popSizes.alltrees.33`: z = 14.60 (default mean 20.87, scale mean 42.48)
- **FLAG** `popSizes.alltrees.34`: z = 17.13 (default mean 21.98, scale mean 42.42)
- **FLAG** `popSizes.alltrees.35`: z = 15.14 (default mean 21.31, scale mean 42.06)
- **FLAG** `popSizes.alltrees.36`: z = 17.33 (default mean 21.13, scale mean 42.61)
- **FLAG** `popSizes.alltrees.37`: z = 16.65 (default mean 21.08, scale mean 42.25)
- **FLAG** `popSizes.alltrees.38`: z = 14.91 (default mean 21.78, scale mean 42.48)
- **FLAG** `popSizes.alltrees.39`: z = 18.87 (default mean 19.77, scale mean 42.59)
- **FLAG** `popSizes.alltrees.40`: z = 16.73 (default mean 20.62, scale mean 42.47)
- **FLAG** `popSizes.alltrees.41`: z = 18.88 (default mean 21.25, scale mean 42.73)
- **FLAG** `popSizes.alltrees.42`: z = 15.45 (default mean 22.3, scale mean 42.84)
- **FLAG** `popSizes.alltrees.43`: z = 17.30 (default mean 22.05, scale mean 42.24)
- **FLAG** `popSizes.alltrees.44`: z = 14.08 (default mean 22.55, scale mean 42.53)
- **FLAG** `popSizes.alltrees.45`: z = 18.49 (default mean 20.95, scale mean 43.27)
- **FLAG** `popSizes.alltrees.46`: z = 20.79 (default mean 19.3, scale mean 42.91)
- **FLAG** `popSizes.alltrees.47`: z = 21.73 (default mean 18.37, scale mean 42.89)
- **FLAG** `popSizes.alltrees.48`: z = 16.95 (default mean 22.46, scale mean 42.55)
- **FLAG** `popSizes.alltrees.49`: z = 16.77 (default mean 20.93, scale mean 42.4)
- **FLAG** `popSizes.alltrees.50`: z = 15.27 (default mean 21.26, scale mean 42.38)
- **FLAG** `popSizes.alltrees.51`: z = 18.08 (default mean 20.29, scale mean 42.86)
- **FLAG** `popSizes.alltrees.52`: z = 22.08 (default mean 19.9, scale mean 41.37)
- **FLAG** `popSizes.alltrees.53`: z = 19.72 (default mean 20.39, scale mean 42.57)
- **FLAG** `popSizes.alltrees.54`: z = 15.15 (default mean 21.34, scale mean 42.05)
- **FLAG** `popSizes.alltrees.55`: z = 16.95 (default mean 20.09, scale mean 42.91)
- **FLAG** `popSizes.alltrees.56`: z = 18.00 (default mean 20.8, scale mean 42.8)
- **FLAG** `popSizes.alltrees.57`: z = 17.68 (default mean 20.71, scale mean 43.13)
- **FLAG** `popSizes.alltrees.58`: z = 17.80 (default mean 20.39, scale mean 42.14)
- **FLAG** `popSizes.alltrees.59`: z = 15.16 (default mean 21.12, scale mean 42.46)
- **FLAG** `popSizes.alltrees.60`: z = 17.89 (default mean 20.84, scale mean 42.82)
- **FLAG** `popSizes.alltrees.61`: z = 18.87 (default mean 20.68, scale mean 43.36)
- **FLAG** `popSizes.alltrees.62`: z = 15.33 (default mean 21.67, scale mean 42.58)
- **FLAG** `popSizes.alltrees.63`: z = 17.34 (default mean 21.26, scale mean 42.37)
- **FLAG** `popSizes.alltrees.64`: z = 15.01 (default mean 22.16, scale mean 41.89)
- **FLAG** `popSizes.alltrees.65`: z = 15.87 (default mean 20.32, scale mean 43.73)
- **FLAG** `popSizes.alltrees.66`: z = 15.85 (default mean 21.31, scale mean 42.44)
- **FLAG** `popSizes.alltrees.67`: z = 17.38 (default mean 21.06, scale mean 42.66)
- **FLAG** `popSizes.alltrees.68`: z = 18.84 (default mean 20.41, scale mean 42.9)
- **FLAG** `popSizes.alltrees.69`: z = 19.20 (default mean 21.05, scale mean 42.62)
- **FLAG** `popSizes.alltrees.70`: z = 17.88 (default mean 20.87, scale mean 42.16)
- **FLAG** `popSizes.alltrees.71`: z = 18.36 (default mean 21.4, scale mean 42.03)
- **FLAG** `popSizes.alltrees.72`: z = 17.32 (default mean 20.16, scale mean 42.06)
- **FLAG** `popSizes.alltrees.73`: z = 16.33 (default mean 21.37, scale mean 42.91)
- **FLAG** `popSizes.alltrees.74`: z = 19.13 (default mean 20.1, scale mean 42.8)
- **FLAG** `popSizes.alltrees.75`: z = 20.25 (default mean 19.95, scale mean 43.79)
- **FLAG** `popSizes.alltrees.76`: z = 16.85 (default mean 20.61, scale mean 42.15)
- **FLAG** `popSizes.alltrees.77`: z = 17.86 (default mean 20.29, scale mean 42.39)
- **FLAG** `popSizes.alltrees.78`: z = 15.04 (default mean 21.91, scale mean 42.63)
- **FLAG** `popSizes.alltrees.79`: z = 17.91 (default mean 20.38, scale mean 42.15)
- **FLAG** `popSizes.alltrees.80`: z = 17.62 (default mean 21.3, scale mean 42.02)
- **FLAG** `popSizes.alltrees.81`: z = 16.35 (default mean 21.72, scale mean 42.04)
- **FLAG** `popSizes.alltrees.82`: z = 23.68 (default mean 18.19, scale mean 42.65)
- **FLAG** `popSizes.alltrees.83`: z = 20.00 (default mean 19.98, scale mean 42.45)
- **FLAG** `popSizes.alltrees.84`: z = 17.03 (default mean 21.3, scale mean 42.18)
- **FLAG** `popSizes.alltrees.85`: z = 16.90 (default mean 21.41, scale mean 42.77)
- **FLAG** `popSizes.alltrees.86`: z = 18.68 (default mean 20.73, scale mean 43.23)
- **FLAG** `popSizes.alltrees.87`: z = 14.90 (default mean 21.91, scale mean 43.12)
- **FLAG** `popSizes.alltrees.88`: z = 17.18 (default mean 20.74, scale mean 42.51)
- **FLAG** `popSizes.alltrees.89`: z = 16.05 (default mean 20.99, scale mean 42.2)
- **FLAG** `popSizes.alltrees.90`: z = 21.95 (default mean 19.14, scale mean 41.97)
- **FLAG** `popSizes.alltrees.91`: z = 13.11 (default mean 23.31, scale mean 42.47)
- **FLAG** `popSizes.alltrees.92`: z = 19.19 (default mean 19.84, scale mean 42.46)
- **FLAG** `popSizes.alltrees.93`: z = 21.11 (default mean 19.53, scale mean 42.42)
- **FLAG** `popSizes.alltrees.94`: z = 20.90 (default mean 19.89, scale mean 42.36)
- **FLAG** `popSizes.alltrees.95`: z = 21.37 (default mean 19.02, scale mean 42.31)
- **FLAG** `popSizes.alltrees.96`: z = 18.74 (default mean 20.1, scale mean 42.4)
- **FLAG** `popSizes.alltrees.97`: z = 15.55 (default mean 22.13, scale mean 42.39)
- **FLAG** `popSizes.alltrees.98`: z = 18.56 (default mean 19.96, scale mean 42.39)
- **FLAG** `popSizes.alltrees.99`: z = 17.80 (default mean 20.39, scale mean 42.85)
- **FLAG** `popSizes.alltrees.100`: z = 15.59 (default mean 23.1, scale mean 42.75)
- **FLAG** `popSizes.alltrees.101`: z = 14.32 (default mean 22.1, scale mean 42.25)
- **FLAG** `popSizes.alltrees.102`: z = 18.22 (default mean 21.14, scale mean 42.47)
- **FLAG** `popSizes.alltrees.103`: z = 16.11 (default mean 21.65, scale mean 42.2)
- **FLAG** `popSizes.alltrees.104`: z = 14.89 (default mean 22.3, scale mean 42.64)
- **FLAG** `popSizes.alltrees.105`: z = 16.91 (default mean 22.22, scale mean 42.11)
- **FLAG** `popSizes.alltrees.106`: z = 16.18 (default mean 21.53, scale mean 42.93)
- **FLAG** `popSizes.alltrees.107`: z = 19.33 (default mean 18.82, scale mean 43.19)
- **FLAG** `popSizes.alltrees.108`: z = 19.52 (default mean 19.69, scale mean 42.22)
- **FLAG** `popSizes.alltrees.109`: z = 15.69 (default mean 20.63, scale mean 42.26)
- **FLAG** `popSizes.alltrees.110`: z = 17.17 (default mean 21.48, scale mean 42.65)
- **FLAG** `popSizes.alltrees.111`: z = 17.09 (default mean 21.98, scale mean 42.17)
- **FLAG** `popSizes.alltrees.112`: z = 17.52 (default mean 20.55, scale mean 42.94)
- **FLAG** `popSizes.alltrees.113`: z = 17.49 (default mean 20.96, scale mean 42.15)
- **FLAG** `popSizes.alltrees.114`: z = 16.26 (default mean 22.08, scale mean 42.39)
- **FLAG** `popSizes.alltrees.115`: z = 18.46 (default mean 19.24, scale mean 42.74)
- **FLAG** `popSizes.alltrees.116`: z = 16.24 (default mean 21.64, scale mean 42.55)
- **FLAG** `popSizes.alltrees.117`: z = 18.21 (default mean 21.32, scale mean 41.88)
- **FLAG** `popSizes.alltrees.118`: z = 13.85 (default mean 23.38, scale mean 42.54)
- **FLAG** `popSizes.alltrees.119`: z = 15.70 (default mean 21.47, scale mean 42.79)
- **FLAG** `popSizes.alltrees.120`: z = 14.74 (default mean 22.76, scale mean 41.53)
- **FLAG** `popSizes.alltrees.121`: z = 17.60 (default mean 21.58, scale mean 41.85)
- **FLAG** `popSizes.alltrees.122`: z = 14.26 (default mean 23.5, scale mean 42.3)
- **FLAG** `popSizes.alltrees.123`: z = 17.63 (default mean 21.72, scale mean 41.14)
- **FLAG** `popSizes.alltrees.124`: z = 13.18 (default mean 23.36, scale mean 41.4)
- **FLAG** `popSizes.alltrees.125`: z = 14.41 (default mean 23.14, scale mean 42.3)
- **FLAG** `popSizes.alltrees.126`: z = 14.82 (default mean 22.44, scale mean 40.81)
- **FLAG** `popSizes.alltrees.127`: z = 13.79 (default mean 23.06, scale mean 41.9)
- **FLAG** `popSizes.alltrees.128`: z = 15.97 (default mean 23.93, scale mean 42.21)
- **FLAG** `popSizes.alltrees.129`: z = 12.80 (default mean 24.29, scale mean 41.52)
- **FLAG** `sum(indicators.alltrees)`: z = 10.31 (default mean 0.567, scale mean 0.7178)
- **NOTE** Trace log file names differ: default `CN-bN.log` paired with scale `CN-bN-scale.log`
- **NOTE** non-numeric column `popsSize0` in EBSP.log ignored
- **NOTE** non-numeric column `popsSize0` in EBSP.log ignored
- **NOTE** non-numeric column `popsSize0` in EBSP.log ignored
- **NOTE** non-numeric column `popsSize0` in EBSP.log ignored
- **NOTE** tree files present in only one version; clades not compared
- **NOTE** `posterior` is shifted by -65.93 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -66.26 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C13/rep1/EBSP.log` | 6001 (5401) | 5000 | 2.8.0 rc2 | yes | 10m34s |  |
| default | rep2 | `beast3/log/C13/rep2/EBSP.log` | 6001 (5401) | 5000 | 2.8.0 rc2 | yes | 10m41s |  |
| scale | rep1 | `beast3/log/C13-scale/rep1/EBSP.log` | 6001 (5401) | 5000 | 2.8.0 rc2 | yes | 26m55s |  |
| scale | rep2 | `beast3/log/C13-scale/rep2/EBSP.log` | 6001 (5401) | 5000 | 2.8.0 rc2 | yes | 26m45s |  |
| default | rep1 | `beast3/log/C13/rep1/C13-b3.log` | 30001 (27001) | 1000 | 2.8.0 rc2 | yes | 10m34s |  |
| default | rep2 | `beast3/log/C13/rep2/C13-b3.log` | 30001 (27001) | 1000 | 2.8.0 rc2 | yes | 10m41s |  |
| scale | rep1 | `beast3/log/C13-scale/rep1/C13-b3-scale.log` | 30001 (27001) | 1000 | 2.8.0 rc2 | yes | 26m55s |  |
| scale | rep2 | `beast3/log/C13-scale/rep2/C13-b3-scale.log` | 30001 (27001) | 1000 | 2.8.0 rc2 | yes | 26m45s |  |

## Parameters: `EBSP.log`

No non-constant columns in common.

## Parameters: `CN-bN.log / CN-bN-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -6631.30 | [-6812.59, -6454.06] | 4630 (2279) | -6697.24 | [-6884.86, -6519.93] | 5142 (2498) | 35.14 | 82% | **z** |
| `likelihood` | -5519.86 | [-5537.48, -5502.23] | 9651 (4628) | -5519.53 | [-5537.62, -5502.81] | 9526 (4627) | 2.54 | 100% | ok |
| `prior` | -1111.45 | [-1294.50, -935.71] | 4630 (2287) | -1177.71 | [-1368.23, -1003.16] | 5123 (2495) | 35.24 | 81% | **z** |
| `treeLikelihood.RSV2` | -5519.86 | [-5537.48, -5502.23] | 9651 (4628) | -5519.53 | [-5537.62, -5502.81] | 9526 (4627) | 2.54 | 100% | ok |
| `Tree.height` | 55.5 | [51.34, 60.12] | 12947 (6454) | 55.45 | [51.15, 59.89] | 13375 (6589) | 1.79 | 98% | ok |
| `Tree.treeLength` | 552.56 | [501.62, 605.98] | 10284 (4598) | 552.18 | [501.08, 605.41] | 10220 (4739) | 1.02 | 99% | ok |
| `clockRate` | 0.00229 | [0.002014, 0.002573] | 13021 (6352) | 0.002291 | [0.00202, 0.002575] | 13624 (6355) | 0.69 | 100% | ok |
| `kappa` | 10.8 | [8.934, 12.83] | 10391 (5186) | 10.82 | [8.899, 12.84] | 11013 (5308) | 1.74 | 100% | ok |
| `freqParameter.1` | 0.3642 | [0.337, 0.392] | 12100 (6002) | 0.3643 | [0.3363, 0.3912] | 12815 (6344) | 0.54 | 99% | ok |
| `freqParameter.2` | 0.3518 | [0.3261, 0.3793] | 12252 (6054) | 0.3518 | [0.3261, 0.3782] | 13183 (6026) | 0.37 | 100% | ok |
| `freqParameter.3` | 0.08845 | [0.07586, 0.101] | 9224 (4350) | 0.08855 | [0.07601, 0.1014] | 9782 (4875) | 1.11 | 99% | ok |
| `freqParameter.4` | 0.1955 | [0.1763, 0.2148] | 11803 (5527) | 0.1953 | [0.1759, 0.2145] | 12113 (5877) | 1.09 | 99% | ok |
| `ExtendedBayesianSkyline` | -588.45 | [-609.96, -567.52] | 9461 (3930) | -588.30 | [-609.46, -566.64] | 9492 (4451) | 0.95 | 99% | ok |
| `indicators.alltrees.1` | 0.002833 | [0, 0] | 11156 (4940) | 0.004315 | [0, 0] | 9374 (3584) | 1.76 | 100% | ok |
| `indicators.alltrees.2` | 0.002481 | [0, 0] | 15323 (6908) | 0.00487 | [0, 0] | 11548 (3566) | 3.13 | 100% | **z** |
| `indicators.alltrees.3` | 0.00387 | [0, 0] | 9710 (3421) | 0.004018 | [0, 0] | 10003 (3583) | 0.17 | 100% | ok |
| `indicators.alltrees.4` | 0.003148 | [0, 0] | 11502 (4412) | 0.004796 | [0, 0] | 9447 (3917) | 1.87 | 100% | ok |
| `indicators.alltrees.5` | 0.003 | [0, 0] | 12112 (3148) | 0.005907 | [0, 0] | 9729 (3978) | 3.15 | 100% | **z** |
| `indicators.alltrees.6` | 0.003167 | [0, 0] | 10323 (4525) | 0.004555 | [0, 0] | 13191 (6567) | 1.72 | 100% | ok |
| `indicators.alltrees.7` | 0.002611 | [0, 0] | 16898 (7834) | 0.003981 | [0, 0] | 11130 (3677) | 1.92 | 100% | ok |
| `indicators.alltrees.8` | 0.003518 | [0, 0] | 10902 (5400) | 0.005166 | [0, 0] | 7327 (3161) | 1.63 | 100% | ok |
| `indicators.alltrees.9` | 0.003907 | [0, 0] | 11894 (5417) | 0.004018 | [0, 0] | 13586 (5573) | 0.14 | 100% | ok |
| `indicators.alltrees.10` | 0.0025 | [0, 0] | 14980 (6413) | 0.004148 | [0, 0] | 13551 (6723) | 2.40 | 100% | ok |
| `indicators.alltrees.11` | 0.003 | [0, 0] | 9933 (4258) | 0.003074 | [0, 0] | 18622 (8359) | 0.11 | 100% | ok |
| `indicators.alltrees.12` | 0.002685 | [0, 0] | 8852 (4222) | 0.003315 | [0, 0] | 14447 (5363) | 0.86 | 100% | ok |
| `indicators.alltrees.13` | 0.00313 | [0, 0] | 12676 (5222) | 0.003315 | [0, 0] | 12507 (6194) | 0.26 | 100% | ok |
| `indicators.alltrees.14` | 0.001704 | [0, 0] | 15719 (7124) | 0.004352 | [0, 0] | 11646 (5663) | 3.82 | 100% | **z** |
| `indicators.alltrees.15` | 0.001722 | [0, 0] | 18002 (8813) | 0.003222 | [0, 0] | 15304 (7189) | 2.71 | 100% | ok |
| `indicators.alltrees.16` | 0.002463 | [0, 0] | 13203 (3686) | 0.003315 | [0, 0] | 14192 (6316) | 1.32 | 100% | ok |
| `indicators.alltrees.17` | 0.002759 | [0, 0] | 12562 (6253) | 0.003296 | [0, 0] | 16404 (6007) | 0.83 | 100% | ok |
| `indicators.alltrees.18` | 0.002778 | [0, 0] | 12997 (4907) | 0.003278 | [0, 0] | 13307 (5472) | 0.74 | 100% | ok |
| `indicators.alltrees.19` | 0.002296 | [0, 0] | 14165 (6761) | 0.002722 | [0, 0] | 11598 (5515) | 0.68 | 100% | ok |
| `indicators.alltrees.20` | 0.002185 | [0, 0] | 13740 (5510) | 0.002759 | [0, 0] | 16570 (8079) | 1.01 | 100% | ok |
| `indicators.alltrees.21` | 0.001963 | [0, 0] | 14002 (6155) | 0.002722 | [0, 0] | 16079 (7933) | 1.37 | 100% | ok |
| `indicators.alltrees.22` | 0.002111 | [0, 0] | 16156 (8064) | 0.002222 | [0, 0] | 20567 (9167) | 0.23 | 100% | ok |
| `indicators.alltrees.23` | 0.001944 | [0, 0] | 19930 (8824) | 0.002722 | [0, 0] | 11587 (4563) | 1.35 | 100% | ok |
| `indicators.alltrees.24` | 0.001815 | [0, 0] | 17085 (7356) | 0.00337 | [0, 0] | 15481 (7608) | 2.74 | 100% | ok |
| `indicators.alltrees.25` | 0.002407 | [0, 0] | 13796 (6029) | 0.002741 | [0, 0] | 16495 (5906) | 0.57 | 100% | ok |
| `indicators.alltrees.26` | 0.001685 | [0, 0] | 23179 (10561) | 0.002481 | [0, 0] | 19766 (6831) | 1.79 | 100% | ok |
| `indicators.alltrees.27` | 0.001611 | [0, 0] | 18569 (8529) | 0.002759 | [0, 0] | 18288 (7947) | 2.36 | 100% | ok |
| `indicators.alltrees.28` | 0.002241 | [0, 0] | 17427 (5187) | 0.002889 | [0, 0] | 18072 (6946) | 1.21 | 100% | ok |
| `indicators.alltrees.29` | 0.001648 | [0, 0] | 22776 (9637) | 0.002093 | [0, 0] | 25156 (11911) | 1.13 | 100% | ok |
| `indicators.alltrees.30` | 0.001426 | [0, 0] | 25183 (10628) | 0.002315 | [0, 0] | 25453 (10368) | 2.32 | 100% | ok |
| `indicators.alltrees.31` | 0.001944 | [0, 0] | 12617 (4465) | 0.002611 | [0, 0] | 17251 (7058) | 1.21 | 100% | ok |
| `indicators.alltrees.32` | 0.001759 | [0, 0] | 21756 (8834) | 0.002518 | [0, 0] | 20312 (7301) | 1.68 | 100% | ok |
| `indicators.alltrees.33` | 0.002074 | [0, 0] | 16013 (5485) | 0.002518 | [0, 0] | 22980 (7822) | 0.91 | 100% | ok |
| `indicators.alltrees.34` | 0.001833 | [0, 0] | 23070 (9474) | 0.002296 | [0, 0] | 21379 (9995) | 1.07 | 100% | ok |
| `indicators.alltrees.35` | 0.001593 | [0, 0] | 22939 (10671) | 0.002944 | [0, 0] | 15590 (6006) | 2.66 | 100% | ok |
| `indicators.alltrees.36` | 0.002037 | [0, 0] | 14724 (5785) | 0.002444 | [0, 0] | 26462 (11903) | 0.85 | 100% | ok |
| `indicators.alltrees.37` | 0.002981 | [0, 0] | 8492 (2404) | 0.00313 | [0, 0] | 19822 (8259) | 0.21 | 100% | ok |
| `indicators.alltrees.38` | 0.001537 | [0, 0] | 16784 (7227) | 0.002944 | [0, 0] | 19380 (8179) | 2.86 | 100% | ok |
| `indicators.alltrees.39` | 0.001889 | [0, 0] | 15687 (6591) | 0.002944 | [0, 0] | 18733 (7631) | 2.01 | 100% | ok |
| `indicators.alltrees.40` | 0.002352 | [0, 0] | 12662 (2952) | 0.003 | [0, 0] | 19916 (9681) | 1.12 | 100% | ok |
| `indicators.alltrees.41` | 0.002407 | [0, 0] | 11764 (5269) | 0.003444 | [0, 0] | 16725 (6051) | 1.62 | 100% | ok |
| `indicators.alltrees.42` | 0.001944 | [0, 0] | 14352 (5943) | 0.003315 | [0, 0] | 17752 (7568) | 2.42 | 100% | ok |
| `indicators.alltrees.43` | 0.001981 | [0, 0] | 14603 (6675) | 0.003018 | [0, 0] | 20810 (9958) | 1.96 | 100% | ok |
| `indicators.alltrees.44` | 0.002481 | [0, 0] | 18610 (5019) | 0.003167 | [0, 0] | 18530 (6984) | 1.24 | 100% | ok |
| `indicators.alltrees.45` | 0.002074 | [0, 0] | 13494 (5018) | 0.003389 | [0, 0] | 13614 (4010) | 2.08 | 100% | ok |
| `indicators.alltrees.46` | 0.002741 | [0, 0] | 9179 (4409) | 0.002444 | [0, 0] | 19767 (6817) | 0.46 | 100% | ok |
| `indicators.alltrees.47` | 0.002518 | [0, 0] | 14669 (4204) | 0.003926 | [0, 0] | 12740 (3486) | 2.04 | 100% | ok |
| `indicators.alltrees.48` | 0.00213 | [0, 0] | 12657 (2962) | 0.003685 | [0, 0] | 12748 (5245) | 2.30 | 100% | ok |
| `indicators.alltrees.49` | 0.001963 | [0, 0] | 12793 (2501) | 0.002889 | [0, 0] | 11943 (5112) | 1.47 | 100% | ok |
| `indicators.alltrees.50` | 0.002407 | [0, 0] | 10849 (4525) | 0.004 | [0, 0] | 9909 (4011) | 2.02 | 100% | ok |
| `indicators.alltrees.51` | 0.001667 | [0, 0] | 17583 (6504) | 0.003759 | [0, 0] | 9518 (4726) | 3.00 | 100% | ok |
| `indicators.alltrees.52` | 0.002055 | [0, 0] | 13748 (4849) | 0.003944 | [0, 0] | 11133 (3837) | 2.67 | 100% | ok |
| `indicators.alltrees.53` | 0.002296 | [0, 0] | 11803 (5341) | 0.003926 | [0, 0] | 9213 (4206) | 2.07 | 100% | ok |
| `indicators.alltrees.54` | 0.002018 | [0, 0] | 12479 (5908) | 0.003944 | [0, 0] | 11579 (4703) | 2.72 | 100% | ok |
| `indicators.alltrees.55` | 0.002296 | [0, 0] | 13979 (2984) | 0.004333 | [0, 0] | 9255 (3560) | 2.57 | 100% | ok |
| `indicators.alltrees.56` | 0.002722 | [0, 0] | 8434 (3673) | 0.003778 | [0, 0] | 10076 (4684) | 1.27 | 100% | ok |
| `indicators.alltrees.57` | 0.002704 | [0, 0] | 8999 (4413) | 0.004592 | [0, 0] | 11234 (4162) | 2.25 | 100% | ok |
| `indicators.alltrees.58` | 0.001981 | [0, 0] | 14162 (5110) | 0.003444 | [0, 0] | 12297 (4550) | 2.26 | 100% | ok |
| `indicators.alltrees.59` | 0.00263 | [0, 0] | 13860 (3437) | 0.004704 | [0, 0] | 8998 (4137) | 2.46 | 100% | ok |
| `indicators.alltrees.60` | 0.002093 | [0, 0] | 12937 (5992) | 0.003741 | [0, 0] | 10843 (5413) | 2.32 | 100% | ok |
| `indicators.alltrees.61` | 0.002037 | [0, 0] | 15218 (2643) | 0.003907 | [0, 0] | 12574 (6088) | 2.81 | 100% | ok |
| `indicators.alltrees.62` | 0.004389 | [0, 0] | 4677 (2198) | 0.004204 | [0, 0] | 10653 (4576) | 0.16 | 100% | ok |
| `indicators.alltrees.63` | 0.002407 | [0, 0] | 8340 (3964) | 0.004092 | [0, 0] | 9392 (4455) | 1.98 | 100% | ok |
| `indicators.alltrees.64` | 0.002 | [0, 0] | 12811 (2928) | 0.003611 | [0, 0] | 13780 (6108) | 2.50 | 100% | ok |
| `indicators.alltrees.65` | 0.002963 | [0, 0] | 8850 (4178) | 0.003685 | [0, 0] | 7603 (2704) | 0.80 | 100% | ok |
| `indicators.alltrees.66` | 0.002278 | [0, 0] | 10436 (3944) | 0.003592 | [0, 0] | 12396 (4664) | 1.85 | 100% | ok |
| `indicators.alltrees.67` | 0.002463 | [0, 0] | 9973 (2991) | 0.003981 | [0, 0] | 8610 (3831) | 1.81 | 100% | ok |
| `indicators.alltrees.68` | 0.001537 | [0, 0] | 15276 (4812) | 0.002852 | [0, 0] | 14416 (4788) | 2.41 | 100% | ok |
| `indicators.alltrees.69` | 0.002574 | [0, 0] | 7971 (3232) | 0.003518 | [0, 0] | 15253 (4821) | 1.27 | 100% | ok |
| `indicators.alltrees.70` | 0.002241 | [0, 0] | 8165 (1928) | 0.002833 | [0, 0] | 16616 (7417) | 0.89 | 100% | ok |
| `indicators.alltrees.71` | 0.00187 | [0, 0] | 10262 (4894) | 0.002907 | [0, 0] | 12476 (5261) | 1.61 | 100% | ok |
| `indicators.alltrees.72` | 0.002241 | [0, 0] | 11175 (5391) | 0.003759 | [0, 0] | 11489 (5430) | 2.09 | 100% | ok |
| `indicators.alltrees.73` | 0.002352 | [0, 0] | 14196 (4448) | 0.003111 | [0, 0] | 13920 (5215) | 1.22 | 100% | ok |
| `indicators.alltrees.74` | 0.001963 | [0, 0] | 15675 (7439) | 0.003704 | [0, 0] | 13363 (5616) | 2.75 | 100% | ok |
| `indicators.alltrees.75` | 0.002407 | [0, 0] | 10837 (5239) | 0.004648 | [0, 0] | 7270 (3164) | 2.42 | 100% | ok |
| `indicators.alltrees.76` | 0.001722 | [0, 0] | 13056 (5588) | 0.00313 | [0, 0] | 12434 (5520) | 2.28 | 100% | ok |
| `indicators.alltrees.77` | 0.002278 | [0, 0] | 11946 (5567) | 0.00313 | [0, 0] | 14067 (4756) | 1.33 | 100% | ok |
| `indicators.alltrees.78` | 0.00263 | [0, 0] | 10374 (4450) | 0.003926 | [0, 0] | 10960 (5149) | 1.66 | 100% | ok |
| `indicators.alltrees.79` | 0.002037 | [0, 0] | 11482 (4669) | 0.00387 | [0, 0] | 11310 (4408) | 2.55 | 100% | ok |
| `indicators.alltrees.80` | 0.002148 | [0, 0] | 14963 (3162) | 0.003407 | [0, 0] | 13333 (5376) | 2.00 | 100% | ok |
| `indicators.alltrees.81` | 0.001815 | [0, 0] | 12265 (6039) | 0.003426 | [0, 0] | 13644 (6481) | 2.55 | 100% | ok |
| `indicators.alltrees.82` | 0.001981 | [0, 0] | 12058 (4939) | 0.003574 | [0, 0] | 13563 (6450) | 2.44 | 100% | ok |
| `indicators.alltrees.83` | 0.002722 | [0, 0] | 12426 (5801) | 0.003889 | [0, 0] | 9980 (4114) | 1.50 | 100% | ok |
| `indicators.alltrees.84` | 0.002481 | [0, 0] | 15241 (7372) | 0.002852 | [0, 0] | 10333 (3769) | 0.56 | 100% | ok |
| `indicators.alltrees.85` | 0.003018 | [0, 0] | 11116 (5324) | 0.003407 | [0, 0] | 13243 (5846) | 0.54 | 100% | ok |
| `indicators.alltrees.86` | 0.002648 | [0, 0] | 11944 (5223) | 0.003037 | [0, 0] | 12140 (6034) | 0.57 | 100% | ok |
| `indicators.alltrees.87` | 0.003204 | [0, 0] | 9479 (4582) | 0.004037 | [0, 0] | 9873 (4166) | 0.97 | 100% | ok |
| `indicators.alltrees.88` | 0.002704 | [0, 0] | 12448 (4828) | 0.003815 | [0, 0] | 13856 (6431) | 1.59 | 100% | ok |
| `indicators.alltrees.89` | 0.002815 | [0, 0] | 9416 (4618) | 0.003704 | [0, 0] | 14103 (6554) | 1.19 | 100% | ok |
| `indicators.alltrees.90` | 0.002722 | [0, 0] | 11957 (5442) | 0.003 | [0, 0] | 10051 (3829) | 0.38 | 100% | ok |
| `indicators.alltrees.91` | 0.002352 | [0, 0] | 12473 (3171) | 0.002648 | [0, 0] | 20211 (9423) | 0.52 | 100% | ok |
| `indicators.alltrees.92` | 0.002481 | [0, 0] | 16464 (8121) | 0.003111 | [0, 0] | 16490 (7717) | 1.08 | 100% | ok |
| `indicators.alltrees.93` | 0.002204 | [0, 0] | 15193 (3964) | 0.0045 | [0, 0] | 11177 (4827) | 3.11 | 100% | **z** |
| `indicators.alltrees.94` | 0.002204 | [0, 0] | 12225 (5261) | 0.003537 | [0, 0] | 13283 (5622) | 2.00 | 100% | ok |
| `indicators.alltrees.95` | 0.002555 | [0, 0] | 12324 (5851) | 0.003889 | [0, 0] | 9730 (2571) | 1.71 | 100% | ok |
| `indicators.alltrees.96` | 0.002055 | [0, 0] | 13283 (5960) | 0.003296 | [0, 0] | 12068 (4982) | 1.90 | 100% | ok |
| `indicators.alltrees.97` | 0.001852 | [0, 0] | 17537 (6092) | 0.003315 | [0, 0] | 14454 (6066) | 2.53 | 100% | ok |
| `indicators.alltrees.98` | 0.002333 | [0, 0] | 11746 (5331) | 0.004185 | [0, 0] | 13032 (2709) | 2.57 | 100% | ok |
| `indicators.alltrees.99` | 0.002352 | [0, 0] | 15802 (4784) | 0.003852 | [0, 0] | 10804 (4980) | 2.11 | 100% | ok |
| `indicators.alltrees.100` | 0.002481 | [0, 0] | 15766 (6199) | 0.004315 | [0, 0] | 12774 (5058) | 2.61 | 100% | ok |
| `indicators.alltrees.101` | 0.003037 | [0, 0] | 16370 (6593) | 0.00437 | [0, 0] | 9325 (2569) | 1.65 | 100% | ok |
| `indicators.alltrees.102` | 0.003315 | [0, 0] | 11501 (4800) | 0.003648 | [0, 0] | 13411 (6490) | 0.45 | 100% | ok |
| `indicators.alltrees.103` | 0.004111 | [0, 0] | 7475 (3520) | 0.004574 | [0, 0] | 11010 (5285) | 0.47 | 100% | ok |
| `indicators.alltrees.104` | 0.003629 | [0, 0] | 9298 (2664) | 0.006444 | [0, 0] | 7924 (3040) | 2.57 | 100% | ok |
| `indicators.alltrees.105` | 0.004148 | [0, 0] | 10369 (5167) | 0.004666 | [0, 0] | 14995 (4972) | 0.62 | 100% | ok |
| `indicators.alltrees.106` | 0.002759 | [0, 0] | 15363 (5453) | 0.003963 | [0, 0] | 15652 (7627) | 1.83 | 100% | ok |
| `indicators.alltrees.107` | 0.002907 | [0, 0] | 16819 (6624) | 0.0045 | [0, 0] | 15769 (7331) | 2.36 | 100% | ok |
| `indicators.alltrees.108` | 0.003092 | [0, 0] | 17648 (6190) | 0.004704 | [0, 0] | 18668 (7175) | 2.47 | 100% | ok |
| `indicators.alltrees.109` | 0.005555 | [0, 0] | 9010 (3682) | 0.003963 | [0, 0] | 20816 (10156) | 1.78 | 100% | ok |
| `indicators.alltrees.110` | 0.004574 | [0, 0] | 15661 (6615) | 0.005555 | [0, 0] | 17451 (7013) | 1.26 | 100% | ok |
| `indicators.alltrees.111` | 0.004352 | [0, 0] | 15421 (7442) | 0.006426 | [0, 0] | 14097 (6745) | 2.42 | 100% | ok |
| `indicators.alltrees.112` | 0.004222 | [0, 0] | 15252 (7587) | 0.005241 | [0, 0] | 16259 (7685) | 1.32 | 100% | ok |
| `indicators.alltrees.113` | 0.004981 | [0, 0] | 15094 (7104) | 0.005129 | [0, 0] | 17674 (8077) | 0.19 | 100% | ok |
| `indicators.alltrees.114` | 0.004852 | [0, 0] | 13841 (5786) | 0.005778 | [0, 0] | 19007 (8817) | 1.15 | 100% | ok |
| `indicators.alltrees.115` | 0.005796 | [0, 0] | 17652 (7702) | 0.008074 | [0, 0] | 13879 (5228) | 2.40 | 100% | ok |
| `indicators.alltrees.116` | 0.006648 | [0, 0] | 15809 (7539) | 0.007944 | [0, 0] | 19927 (9456) | 1.44 | 100% | ok |
| `indicators.alltrees.117` | 0.00724 | [0, 0] | 19519 (8992) | 0.009055 | [0, 0] | 17144 (6805) | 1.92 | 100% | ok |
| `indicators.alltrees.118` | 0.007777 | [0, 0] | 14160 (5692) | 0.01213 | [0, 0] | 15310 (6709) | 3.78 | 100% | **z** |
| `indicators.alltrees.119` | 0.01004 | [0, 0] | 15642 (6876) | 0.01317 | [0, 0] | 17076 (7721) | 2.65 | 100% | ok |
| `indicators.alltrees.120` | 0.01393 | [0, 0] | 15444 (7020) | 0.01704 | [0, 0] | 14606 (6804) | 2.18 | 100% | ok |
| `indicators.alltrees.121` | 0.01683 | [0, 0] | 13379 (6344) | 0.0215 | [0, 0] | 14503 (7235) | 2.85 | 100% | ok |
| `indicators.alltrees.122` | 0.02409 | [0, 0] | 11340 (5138) | 0.02824 | [0, 0] | 11764 (5536) | 1.98 | 100% | ok |
| `indicators.alltrees.123` | 0.03192 | [0, 0] | 10710 (4691) | 0.03389 | [0, 0] | 12344 (6140) | 0.83 | 100% | ok |
| `indicators.alltrees.124` | 0.03007 | [0, 0] | 12136 (5999) | 0.03641 | [0, 0] | 10994 (5180) | 2.68 | 100% | ok |
| `indicators.alltrees.125` | 0.0277 | [0, 0] | 11021 (5089) | 0.03487 | [0, 0] | 11957 (5584) | 3.13 | 100% | **z** |
| `indicators.alltrees.126` | 0.02193 | [0, 0] | 18146 (8570) | 0.02057 | [0, 0] | 21314 (10067) | 0.93 | 100% | ok |
| `indicators.alltrees.127` | 0.02776 | [0, 0] | 22198 (10205) | 0.02454 | [0, 0] | 25722 (12063) | 2.20 | 100% | ok |
| `indicators.alltrees.128` | 0.0445 | [0, 0] | 14800 (7262) | 0.03261 | [0, 0] | 21398 (10389) | 5.70 | 100% | **z** |
| `populationMean.alltrees` | 41.02 | [4.748, 106.50] | 4970 (2426) | 42.54 | [4.809, 112.46] | 5385 (2574) | 2.13 | 100% | ok |
| `popSizes.alltrees.1` | 38.2 | [14.73, 63.54] | 14708 (7301) | 37.27 | [9.124, 62.56] | 16881 (7542) | 5.25 | 98% | **z** |
| `popSizes.alltrees.2` | 19.59 | [0.0118, 68.69] | 1155 (534) | 42.26 | [0.001318, 150.49] | 12264 (6012) | 21.01 | 100% | **z** |
| `popSizes.alltrees.3` | 21.04 | [0.03375, 73.5] | 1123 (527) | 42.72 | [1.172e-04, 152.10] | 11802 (5579) | 18.89 | 100% | **z** |
| `popSizes.alltrees.4` | 23.7 | [0.004922, 84.4] | 874 (417) | 42.33 | [0.001135, 149.28] | 11956 (5975) | 13.50 | 100% | **z** |
| `popSizes.alltrees.5` | 21.3 | [0.009475, 76.97] | 942 (404) | 42.64 | [5.044e-04, 154.94] | 11250 (5468) | 17.00 | 100% | **z** |
| `popSizes.alltrees.6` | 18.93 | [0.003428, 68.87] | 963 (397) | 42.75 | [3.878e-04, 151.88] | 11755 (5739) | 20.47 | 100% | **z** |
| `popSizes.alltrees.7` | 22.74 | [6.870e-04, 84.48] | 1079 (529) | 42.37 | [0.001144, 152.73] | 11196 (5160) | 14.72 | 100% | **z** |
| `popSizes.alltrees.8` | 21.15 | [7.332e-04, 76.51] | 789 (354) | 42.45 | [4.605e-04, 150.88] | 11729 (5801) | 16.28 | 100% | **z** |
| `popSizes.alltrees.9` | 20.29 | [0.01071, 72.35] | 1095 (498) | 42.91 | [0.001366, 153.54] | 11442 (5539) | 19.41 | 100% | **z** |
| `popSizes.alltrees.10` | 21.68 | [0.001646, 76.78] | 1080 (515) | 42.67 | [0.001313, 153.56] | 11395 (5202) | 16.74 | 100% | **z** |
| `popSizes.alltrees.11` | 19.97 | [0.001339, 71.2] | 1052 (457) | 43.06 | [4.621e-04, 154.54] | 10562 (4642) | 20.20 | 100% | **z** |
| `popSizes.alltrees.12` | 21.48 | [2.308e-04, 76.12] | 1143 (524) | 41.92 | [1.912e-04, 148.63] | 12305 (5894) | 17.56 | 100% | **z** |
| `popSizes.alltrees.13` | 20.73 | [2.067e-04, 74.81] | 1245 (579) | 42.39 | [1.547e-04, 150.35] | 11057 (5433) | 19.46 | 100% | **z** |
| `popSizes.alltrees.14` | 22.09 | [0.007396, 77.17] | 1001 (369) | 42.57 | [8.208e-04, 152.50] | 11908 (5549) | 16.43 | 100% | **z** |
| `popSizes.alltrees.15` | 20.04 | [0.005077, 71.6] | 886 (397) | 42.86 | [0.00315, 153.20] | 10814 (5340) | 18.31 | 100% | **z** |
| `popSizes.alltrees.16` | 22.27 | [0.00187, 80.9] | 844 (404) | 42.59 | [0.001717, 152.42] | 12534 (5972) | 15.42 | 100% | **z** |
| `popSizes.alltrees.17` | 20.13 | [0.00787, 73.33] | 992 (481) | 42.11 | [7.870e-04, 148.99] | 11763 (5739) | 18.86 | 100% | **z** |
| `popSizes.alltrees.18` | 20.74 | [0.001891, 73.33] | 1171 (473) | 42.12 | [0.001074, 150.79] | 10149 (4916) | 18.60 | 100% | **z** |
| `popSizes.alltrees.19` | 21.08 | [1.022e-04, 76.06] | 818 (388) | 42.19 | [4.031e-04, 149.20] | 11805 (5718) | 15.72 | 100% | **z** |
| `popSizes.alltrees.20` | 20.71 | [0.01042, 73.58] | 1098 (400) | 42.75 | [2.064e-04, 152.60] | 11522 (5548) | 18.74 | 100% | **z** |
| `popSizes.alltrees.21` | 20.42 | [0.001793, 74.62] | 1007 (450) | 42.81 | [1.040e-04, 151.37] | 11419 (5688) | 18.84 | 100% | **z** |
| `popSizes.alltrees.22` | 21.81 | [0.002706, 80.44] | 953 (316) | 42.23 | [3.119e-04, 149.94] | 11727 (5563) | 14.98 | 100% | **z** |
| `popSizes.alltrees.23` | 20.32 | [0.002027, 70.26] | 1020 (476) | 43 | [1.702e-05, 152.71] | 10742 (5315) | 19.41 | 100% | **z** |
| `popSizes.alltrees.24` | 21.01 | [0.001627, 74.22] | 1081 (473) | 42.76 | [4.626e-04, 151.08] | 12169 (6071) | 18.34 | 100% | **z** |
| `popSizes.alltrees.25` | 19.34 | [0.003145, 69.03] | 1180 (573) | 42.08 | [2.656e-04, 148.35] | 11709 (5423) | 20.43 | 100% | **z** |
| `popSizes.alltrees.26` | 21.13 | [8.541e-05, 77] | 697 (330) | 42.56 | [0.003534, 150.99] | 11199 (4951) | 14.53 | 100% | **z** |
| `popSizes.alltrees.27` | 21.6 | [0.002142, 74.96] | 897 (448) | 42.8 | [4.814e-04, 152.19] | 10618 (4965) | 16.49 | 100% | **z** |
| `popSizes.alltrees.28` | 21.69 | [6.031e-04, 78.12] | 936 (443) | 43.36 | [0.001368, 157.26] | 11612 (5741) | 16.55 | 100% | **z** |
| `popSizes.alltrees.29` | 23.2 | [0.00268, 83.88] | 742 (339) | 42.46 | [4.296e-05, 151.92] | 11529 (5665) | 13.05 | 100% | **z** |
| `popSizes.alltrees.30` | 20.6 | [7.817e-04, 74.04] | 1178 (509) | 43.09 | [6.885e-04, 151.76] | 11921 (5522) | 19.01 | 100% | **z** |
| `popSizes.alltrees.31` | 20.46 | [5.341e-05, 71.28] | 846 (336) | 42.79 | [3.930e-04, 151.83] | 12340 (5939) | 16.94 | 100% | **z** |
| `popSizes.alltrees.32` | 21.9 | [0.004443, 77.23] | 812 (385) | 42.69 | [3.452e-04, 153.41] | 12161 (5735) | 15.17 | 100% | **z** |
| `popSizes.alltrees.33` | 20.87 | [2.572e-04, 74.95] | 755 (286) | 42.48 | [0.001052, 150.96] | 11376 (5586) | 14.60 | 100% | **z** |
| `popSizes.alltrees.34` | 21.98 | [0.008331, 74.57] | 967 (450) | 42.42 | [0.002752, 149.98] | 12204 (5855) | 17.13 | 100% | **z** |
| `popSizes.alltrees.35` | 21.31 | [0.002628, 75.3] | 882 (390) | 42.06 | [1.297e-04, 151.26] | 11532 (5745) | 15.14 | 100% | **z** |
| `popSizes.alltrees.36` | 21.13 | [0.004868, 78.2] | 1080 (480) | 42.61 | [2.450e-04, 152.29] | 11235 (5432) | 17.33 | 100% | **z** |
| `popSizes.alltrees.37` | 21.08 | [0.002057, 75.06] | 950 (386) | 42.25 | [0.00143, 151.57] | 11924 (5829) | 16.65 | 100% | **z** |
| `popSizes.alltrees.38` | 21.78 | [0.004306, 79.84] | 880 (400) | 42.48 | [3.026e-04, 148.91] | 11450 (5490) | 14.91 | 100% | **z** |
| `popSizes.alltrees.39` | 19.77 | [0.002027, 69.89] | 1094 (442) | 42.59 | [2.051e-04, 153.76] | 11872 (5839) | 18.87 | 100% | **z** |
| `popSizes.alltrees.40` | 20.62 | [1.756e-04, 74.68] | 734 (360) | 42.47 | [0.001048, 150.88] | 12287 (5885) | 16.73 | 100% | **z** |
| `popSizes.alltrees.41` | 21.25 | [0.001125, 74.79] | 1083 (517) | 42.73 | [6.651e-04, 151.84] | 12060 (5767) | 18.88 | 100% | **z** |
| `popSizes.alltrees.42` | 22.3 | [0.002623, 80.04] | 902 (445) | 42.84 | [0.001452, 153.93] | 11825 (5636) | 15.45 | 100% | **z** |
| `popSizes.alltrees.43` | 22.05 | [0.004359, 77.69] | 1196 (569) | 42.24 | [3.864e-04, 149.34] | 11535 (5307) | 17.30 | 100% | **z** |
| `popSizes.alltrees.44` | 22.55 | [0.001417, 80.99] | 891 (314) | 42.53 | [0.001162, 152.20] | 11383 (5648) | 14.08 | 100% | **z** |
| `popSizes.alltrees.45` | 20.95 | [0.006116, 74.49] | 964 (397) | 43.27 | [6.806e-04, 155.33] | 11037 (4818) | 18.49 | 100% | **z** |
| `popSizes.alltrees.46` | 19.3 | [0.02476, 67.81] | 1037 (431) | 42.91 | [8.560e-05, 153.68] | 11520 (5565) | 20.79 | 100% | **z** |
| `popSizes.alltrees.47` | 18.37 | [0.001292, 66.55] | 989 (446) | 42.89 | [7.864e-04, 156.92] | 11445 (5490) | 21.73 | 100% | **z** |
| `popSizes.alltrees.48` | 22.46 | [0.001453, 80.55] | 1075 (477) | 42.55 | [4.864e-04, 152.15] | 11541 (5547) | 16.95 | 100% | **z** |
| `popSizes.alltrees.49` | 20.93 | [0.008578, 78.12] | 920 (421) | 42.4 | [7.082e-04, 149.56] | 12216 (6106) | 16.77 | 100% | **z** |
| `popSizes.alltrees.50` | 21.26 | [3.139e-04, 74.78] | 963 (419) | 42.38 | [1.340e-04, 152.90] | 11304 (5196) | 15.27 | 100% | **z** |
| `popSizes.alltrees.51` | 20.29 | [0.002841, 71.95] | 920 (377) | 42.86 | [4.472e-06, 154.64] | 10996 (5109) | 18.08 | 100% | **z** |
| `popSizes.alltrees.52` | 19.9 | [0.001586, 68.4] | 1414 (576) | 41.37 | [1.090e-04, 145.49] | 13608 (6779) | 22.08 | 100% | **z** |
| `popSizes.alltrees.53` | 20.39 | [1.358e-04, 71.73] | 1030 (480) | 42.57 | [2.454e-04, 151.80] | 11481 (5311) | 19.72 | 100% | **z** |
| `popSizes.alltrees.54` | 21.34 | [0.003033, 78.13] | 771 (384) | 42.05 | [3.340e-05, 147.16] | 11448 (5419) | 15.15 | 100% | **z** |
| `popSizes.alltrees.55` | 20.09 | [0.001216, 71.12] | 791 (279) | 42.91 | [6.424e-04, 151.80] | 11963 (5823) | 16.95 | 100% | **z** |
| `popSizes.alltrees.56` | 20.8 | [0.004768, 73.39] | 1002 (448) | 42.8 | [0.001371, 150.57] | 11107 (5488) | 18.00 | 100% | **z** |
| `popSizes.alltrees.57` | 20.71 | [0.003382, 71.87] | 964 (459) | 43.13 | [1.560e-04, 152.56] | 11101 (5431) | 17.68 | 100% | **z** |
| `popSizes.alltrees.58` | 20.39 | [0.004069, 72.57] | 978 (459) | 42.14 | [3.059e-04, 151.50] | 11158 (5337) | 17.80 | 100% | **z** |
| `popSizes.alltrees.59` | 21.12 | [0.009308, 75.46] | 684 (256) | 42.46 | [4.264e-04, 153.66] | 11684 (5696) | 15.16 | 100% | **z** |
| `popSizes.alltrees.60` | 20.84 | [2.337e-04, 74.35] | 919 (393) | 42.82 | [1.043e-04, 152.32] | 11437 (5661) | 17.89 | 100% | **z** |
| `popSizes.alltrees.61` | 20.68 | [7.250e-04, 71.18] | 1118 (480) | 43.36 | [0.002106, 155.55] | 11773 (5577) | 18.87 | 100% | **z** |
| `popSizes.alltrees.62` | 21.67 | [0.004328, 79.14] | 910 (335) | 42.58 | [0.001463, 150.28] | 11162 (5481) | 15.33 | 100% | **z** |
| `popSizes.alltrees.63` | 21.26 | [1.637e-05, 75.81] | 993 (306) | 42.37 | [3.616e-05, 151.07] | 11490 (5534) | 17.34 | 100% | **z** |
| `popSizes.alltrees.64` | 22.16 | [8.559e-04, 81.9] | 970 (406) | 41.89 | [2.924e-04, 148.18] | 11073 (5335) | 15.01 | 100% | **z** |
| `popSizes.alltrees.65` | 20.32 | [6.813e-04, 72.52] | 745 (369) | 43.73 | [7.909e-04, 155.97] | 11099 (5334) | 15.87 | 100% | **z** |
| `popSizes.alltrees.66` | 21.31 | [0.002554, 75.08] | 796 (302) | 42.44 | [2.664e-04, 151.14] | 11581 (5515) | 15.85 | 100% | **z** |
| `popSizes.alltrees.67` | 21.06 | [1.118e-04, 74.75] | 1176 (496) | 42.66 | [1.861e-04, 152.67] | 11547 (5552) | 17.38 | 100% | **z** |
| `popSizes.alltrees.68` | 20.41 | [0.001041, 72.71] | 954 (383) | 42.9 | [2.029e-04, 153.06] | 11452 (5675) | 18.84 | 100% | **z** |
| `popSizes.alltrees.69` | 21.05 | [0.002836, 73.82] | 1206 (509) | 42.62 | [3.388e-04, 152.75] | 11350 (5264) | 19.20 | 100% | **z** |
| `popSizes.alltrees.70` | 20.87 | [0.005583, 75.54] | 958 (377) | 42.16 | [0.00292, 148.45] | 12254 (5815) | 17.88 | 100% | **z** |
| `popSizes.alltrees.71` | 21.4 | [0.00215, 76.31] | 1232 (500) | 42.03 | [5.904e-04, 150.96] | 12297 (5794) | 18.36 | 100% | **z** |
| `popSizes.alltrees.72` | 20.16 | [0.003856, 72.95] | 917 (350) | 42.06 | [0.001745, 150.19] | 11321 (5224) | 17.32 | 100% | **z** |
| `popSizes.alltrees.73` | 21.37 | [0.01504, 76.07] | 931 (334) | 42.91 | [0.001224, 151.71] | 12039 (5867) | 16.33 | 100% | **z** |
| `popSizes.alltrees.74` | 20.1 | [0.004521, 70.36] | 1090 (534) | 42.8 | [1.740e-04, 153.06] | 10422 (4914) | 19.13 | 100% | **z** |
| `popSizes.alltrees.75` | 19.95 | [0.004731, 69.7] | 1308 (649) | 43.79 | [0.001157, 156.04] | 10700 (5258) | 20.25 | 100% | **z** |
| `popSizes.alltrees.76` | 20.61 | [0.002557, 73.55] | 992 (448) | 42.15 | [3.345e-04, 151.73] | 11165 (5407) | 16.85 | 100% | **z** |
| `popSizes.alltrees.77` | 20.29 | [0.005861, 73.7] | 986 (446) | 42.39 | [0.001386, 151.88] | 10986 (5089) | 17.86 | 100% | **z** |
| `popSizes.alltrees.78` | 21.91 | [0.01213, 76.85] | 828 (298) | 42.63 | [5.614e-04, 150.63] | 10991 (5494) | 15.04 | 100% | **z** |
| `popSizes.alltrees.79` | 20.38 | [0.01157, 72.59] | 887 (417) | 42.15 | [6.168e-04, 147.70] | 12110 (5813) | 17.91 | 100% | **z** |
| `popSizes.alltrees.80` | 21.3 | [0.003973, 74.75] | 1055 (482) | 42.02 | [0.001143, 148.85] | 11831 (5786) | 17.62 | 100% | **z** |
| `popSizes.alltrees.81` | 21.72 | [0.003547, 76.74] | 1156 (560) | 42.04 | [1.350e-04, 152.21] | 11926 (5835) | 16.35 | 100% | **z** |
| `popSizes.alltrees.82` | 18.19 | [0.01848, 64.64] | 979 (452) | 42.65 | [2.015e-04, 152.80] | 11441 (5368) | 23.68 | 100% | **z** |
| `popSizes.alltrees.83` | 19.98 | [0.007082, 73.54] | 1125 (556) | 42.45 | [7.400e-04, 151.64] | 12110 (5888) | 20.00 | 100% | **z** |
| `popSizes.alltrees.84` | 21.3 | [5.433e-04, 73.54] | 962 (434) | 42.18 | [6.870e-04, 151.52] | 11584 (5376) | 17.03 | 100% | **z** |
| `popSizes.alltrees.85` | 21.41 | [0.00637, 75.16] | 910 (411) | 42.77 | [4.982e-04, 152.64] | 11360 (5238) | 16.90 | 100% | **z** |
| `popSizes.alltrees.86` | 20.73 | [0.001838, 74.35] | 1038 (445) | 43.23 | [4.383e-04, 153.64] | 11563 (5618) | 18.68 | 100% | **z** |
| `popSizes.alltrees.87` | 21.91 | [0.009697, 79.7] | 933 (437) | 43.12 | [0.001107, 153.42] | 11144 (5302) | 14.90 | 100% | **z** |
| `popSizes.alltrees.88` | 20.74 | [0.004784, 73.58] | 1044 (487) | 42.51 | [0.003826, 150.32] | 11399 (5588) | 17.18 | 100% | **z** |
| `popSizes.alltrees.89` | 20.99 | [0.001046, 73.8] | 950 (472) | 42.2 | [2.571e-04, 150.33] | 11707 (5484) | 16.05 | 100% | **z** |
| `popSizes.alltrees.90` | 19.14 | [0.003603, 66.88] | 1079 (526) | 41.97 | [0.001689, 148.63] | 11861 (5696) | 21.95 | 100% | **z** |
| `popSizes.alltrees.91` | 23.31 | [0.002295, 86.23] | 829 (321) | 42.47 | [0.001521, 151.82] | 10718 (5207) | 13.11 | 100% | **z** |
| `popSizes.alltrees.92` | 19.84 | [2.760e-04, 71.34] | 971 (434) | 42.46 | [5.875e-04, 149.63] | 11483 (5289) | 19.19 | 100% | **z** |
| `popSizes.alltrees.93` | 19.53 | [0.008291, 67.46] | 1096 (527) | 42.42 | [6.011e-05, 150.10] | 11717 (5485) | 21.11 | 100% | **z** |
| `popSizes.alltrees.94` | 19.89 | [0.007081, 69.82] | 1110 (465) | 42.36 | [3.163e-05, 150.19] | 11734 (5494) | 20.90 | 100% | **z** |
| `popSizes.alltrees.95` | 19.02 | [0.0057, 69.12] | 1181 (486) | 42.31 | [4.657e-04, 153.05] | 11459 (5415) | 21.37 | 100% | **z** |
| `popSizes.alltrees.96` | 20.1 | [0.01288, 72.98] | 923 (414) | 42.4 | [4.160e-04, 149.92] | 10712 (5249) | 18.74 | 100% | **z** |
| `popSizes.alltrees.97` | 22.13 | [4.450e-04, 82.22] | 956 (375) | 42.39 | [6.704e-04, 153.31] | 11049 (5281) | 15.55 | 100% | **z** |
| `popSizes.alltrees.98` | 19.96 | [0.00266, 70.58] | 956 (405) | 42.39 | [0.001004, 151.16] | 11748 (5756) | 18.56 | 100% | **z** |
| `popSizes.alltrees.99` | 20.39 | [0.007236, 72.81] | 905 (420) | 42.85 | [9.923e-05, 151.43] | 11300 (5524) | 17.80 | 100% | **z** |
| `popSizes.alltrees.100` | 23.1 | [0.002377, 83.65] | 1089 (463) | 42.75 | [0.0025, 153.32] | 12407 (6006) | 15.59 | 100% | **z** |
| `popSizes.alltrees.101` | 22.1 | [0.002119, 81.56] | 816 (258) | 42.25 | [0.002569, 152.27] | 11883 (5848) | 14.32 | 100% | **z** |
| `popSizes.alltrees.102` | 21.14 | [5.215e-04, 74.55] | 1096 (545) | 42.47 | [1.600e-04, 150.67] | 11461 (5554) | 18.22 | 100% | **z** |
| `popSizes.alltrees.103` | 21.65 | [0.01108, 74.51] | 972 (479) | 42.2 | [2.005e-04, 148.83] | 11254 (5607) | 16.11 | 100% | **z** |
| `popSizes.alltrees.104` | 22.3 | [5.338e-04, 80.85] | 978 (474) | 42.64 | [0.001037, 153.16] | 11523 (5677) | 14.89 | 100% | **z** |
| `popSizes.alltrees.105` | 22.22 | [0.02149, 79.44] | 1149 (546) | 42.11 | [5.565e-05, 151.01] | 11831 (5377) | 16.91 | 100% | **z** |
| `popSizes.alltrees.106` | 21.53 | [0.003564, 76.7] | 923 (423) | 42.93 | [0.001403, 151.13] | 11391 (5594) | 16.18 | 100% | **z** |
| `popSizes.alltrees.107` | 18.82 | [0.001123, 66.41] | 761 (243) | 43.19 | [0.001147, 153.27] | 10706 (5215) | 19.33 | 100% | **z** |
| `popSizes.alltrees.108` | 19.69 | [0.01311, 68.76] | 916 (437) | 42.22 | [0.001687, 150.27] | 11217 (5073) | 19.52 | 100% | **z** |
| `popSizes.alltrees.109` | 20.63 | [0.001331, 73.62] | 695 (281) | 42.26 | [1.944e-04, 150.28] | 12339 (6040) | 15.69 | 100% | **z** |
| `popSizes.alltrees.110` | 21.48 | [0.002551, 75.48] | 1080 (454) | 42.65 | [6.174e-04, 150.98] | 11660 (5550) | 17.17 | 100% | **z** |
| `popSizes.alltrees.111` | 21.98 | [0.008404, 74.85] | 1114 (536) | 42.17 | [4.861e-04, 148.76] | 10926 (4947) | 17.09 | 100% | **z** |
| `popSizes.alltrees.112` | 20.55 | [0.001772, 74.44] | 906 (300) | 42.94 | [2.389e-04, 153.42] | 11938 (5742) | 17.52 | 100% | **z** |
| `popSizes.alltrees.113` | 20.96 | [0.002621, 77.34] | 970 (376) | 42.15 | [4.516e-04, 151.20] | 10975 (5153) | 17.49 | 100% | **z** |
| `popSizes.alltrees.114` | 22.08 | [0.001554, 78.44] | 993 (419) | 42.39 | [7.084e-04, 153.29] | 10692 (4942) | 16.26 | 100% | **z** |
| `popSizes.alltrees.115` | 19.24 | [0.003099, 70.5] | 762 (285) | 42.74 | [4.125e-04, 152.33] | 11912 (5909) | 18.46 | 100% | **z** |
| `popSizes.alltrees.116` | 21.64 | [0.002904, 79.16] | 975 (464) | 42.55 | [2.438e-04, 151.14] | 11836 (5790) | 16.24 | 100% | **z** |
| `popSizes.alltrees.117` | 21.32 | [0.006525, 75.27] | 1191 (455) | 41.88 | [2.589e-04, 148.30] | 11733 (5677) | 18.21 | 100% | **z** |
| `popSizes.alltrees.118` | 23.38 | [0.004886, 84.43] | 977 (463) | 42.54 | [4.957e-04, 153.54] | 11839 (5673) | 13.85 | 100% | **z** |
| `popSizes.alltrees.119` | 21.47 | [0.00787, 77.69] | 868 (334) | 42.79 | [0.001619, 152.17] | 12079 (6037) | 15.70 | 100% | **z** |
| `popSizes.alltrees.120` | 22.76 | [0.01391, 84.26] | 1018 (484) | 41.53 | [5.274e-04, 147.74] | 12540 (6257) | 14.74 | 100% | **z** |
| `popSizes.alltrees.121` | 21.58 | [0.01918, 75.98] | 1129 (476) | 41.85 | [6.722e-04, 149.99] | 10941 (5063) | 17.60 | 100% | **z** |
| `popSizes.alltrees.122` | 23.5 | [0.01013, 83.06] | 1002 (462) | 42.3 | [0.001087, 150.93] | 11744 (5660) | 14.26 | 100% | **z** |
| `popSizes.alltrees.123` | 21.72 | [0.009321, 76.54] | 1327 (590) | 41.14 | [3.642e-04, 148.80] | 12371 (6169) | 17.63 | 100% | **z** |
| `popSizes.alltrees.124` | 23.36 | [0.001559, 83.04] | 955 (413) | 41.4 | [0.002609, 149.37] | 11261 (5440) | 13.18 | 100% | **z** |
| `popSizes.alltrees.125` | 23.14 | [2.207e-05, 82.87] | 971 (442) | 42.3 | [2.508e-05, 150.91] | 11654 (5135) | 14.41 | 100% | **z** |
| `popSizes.alltrees.126` | 22.44 | [0.004246, 79.14] | 972 (475) | 40.81 | [0.00135, 146.79] | 11276 (5523) | 14.82 | 100% | **z** |
| `popSizes.alltrees.127` | 23.06 | [0.006583, 83.69] | 1024 (475) | 41.9 | [9.848e-04, 150.41] | 11038 (5517) | 13.79 | 100% | **z** |
| `popSizes.alltrees.128` | 23.93 | [0.005033, 83.35] | 1357 (577) | 42.21 | [1.247e-04, 151.03] | 11354 (5472) | 15.97 | 100% | **z** |
| `popSizes.alltrees.129` | 24.29 | [2.845e-05, 85.94] | 1151 (401) | 41.52 | [8.781e-04, 149.60] | 10806 (5358) | 12.80 | 100% | **z** |
| `sum(indicators.alltrees)` | 0.567 | [0, 2] | 7294 (3512) | 0.7178 | [0, 2] | 7409 (3656) | 10.31 | 100% | **z** |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -6629.70, -6632.91 | 1.18 | -6697.31, -6697.16 | 0.06 |
| `likelihood` | -5519.86, -5519.85 | 0.04 | -5519.48, -5519.58 | 0.53 |
| `prior` | -1109.84, -1113.06 | 1.18 | -1177.83, -1177.58 | 0.10 |
| `treeLikelihood.RSV2` | -5519.86, -5519.85 | 0.04 | -5519.48, -5519.58 | 0.53 |
| `Tree.height` | 55.53, 55.48 | 1.08 | 55.48, 55.43 | 1.09 |
| `Tree.treeLength` | 552.82, 552.30 | 0.98 | 552.54, 551.82 | 1.37 |
| `clockRate` | 0.002289, 0.002291 | 0.95 | 0.00229, 0.002292 | 0.68 |
| `kappa` | 10.79, 10.8 | 0.74 | 10.82, 10.82 | 0.03 |
| `freqParameter.1` | 0.3642, 0.3642 | 0.01 | 0.3643, 0.3644 | 0.47 |
| `freqParameter.2` | 0.3519, 0.3518 | 0.21 | 0.3518, 0.3518 | 0.05 |
| `freqParameter.3` | 0.08846, 0.08844 | 0.15 | 0.08853, 0.08858 | 0.40 |
| `freqParameter.4` | 0.1954, 0.1955 | 0.39 | 0.1954, 0.1952 | 1.00 |
| `ExtendedBayesianSkyline` | -588.54, -588.37 | 0.73 | -588.40, -588.20 | 0.91 |
| `indicators.alltrees.1` | 0.002926, 0.002741 | 0.18 | 0.003741, 0.004889 | 0.84 |
| `indicators.alltrees.2` | 0.002518, 0.002444 | 0.09 | 0.003555, 0.006185 | 1.79 |
| `indicators.alltrees.3` | 0.004815, 0.002926 | 1.38 | 0.003667, 0.00437 | 0.53 |
| `indicators.alltrees.4` | 0.004148, 0.002148 | 1.80 | 0.004889, 0.004704 | 0.13 |
| `indicators.alltrees.5` | 0.002185, 0.003815 | 1.35 | 0.006592, 0.005222 | 0.86 |
| `indicators.alltrees.6` | 0.003444, 0.002889 | 0.50 | 0.004666, 0.004444 | 0.19 |
| `indicators.alltrees.7` | 0.002111, 0.003111 | 1.26 | 0.004037, 0.003926 | 0.09 |
| `indicators.alltrees.8` | 0.003704, 0.003333 | 0.33 | 0.005037, 0.005296 | 0.15 |
| `indicators.alltrees.9` | 0.004259, 0.003555 | 0.61 | 0.003741, 0.004296 | 0.50 |
| `indicators.alltrees.10` | 0.002852, 0.002148 | 0.84 | 0.004259, 0.004037 | 0.20 |
| `indicators.alltrees.11` | 0.003741, 0.002259 | 1.31 | 0.002518, 0.003629 | 1.35 |
| `indicators.alltrees.12` | 0.002555, 0.002815 | 0.24 | 0.003852, 0.002778 | 1.06 |
| `indicators.alltrees.13` | 0.002926, 0.003333 | 0.41 | 0.00337, 0.003259 | 0.11 |
| `indicators.alltrees.14` | 0.001481, 0.001926 | 0.67 | 0.005666, 0.003037 | 2.16 |
| `indicators.alltrees.15` | 0.001815, 0.00163 | 0.30 | 0.003333, 0.003111 | 0.24 |
| `indicators.alltrees.16` | 0.001963, 0.002963 | 1.00 | 0.003481, 0.003148 | 0.34 |
| `indicators.alltrees.17` | 0.002592, 0.002926 | 0.36 | 0.003704, 0.002889 | 0.86 |
| `indicators.alltrees.18` | 0.00263, 0.002926 | 0.31 | 0.003259, 0.003296 | 0.04 |
| `indicators.alltrees.19` | 0.002296, 0.002296 | 0.00 | 0.00337, 0.002074 | 1.35 |
| `indicators.alltrees.20` | 0.001889, 0.002481 | 0.72 | 0.002852, 0.002667 | 0.23 |
| `indicators.alltrees.21` | 0.001778, 0.002148 | 0.49 | 0.003111, 0.002333 | 0.95 |
| `indicators.alltrees.22` | 0.002222, 0.002 | 0.31 | 0.00263, 0.001815 | 1.22 |
| `indicators.alltrees.23` | 0.001889, 0.002 | 0.18 | 0.003074, 0.00237 | 0.70 |
| `indicators.alltrees.24` | 0.001407, 0.002222 | 1.22 | 0.003222, 0.003518 | 0.32 |
| `indicators.alltrees.25` | 0.002518, 0.002296 | 0.26 | 0.002074, 0.003407 | 1.52 |
| `indicators.alltrees.26` | 0.001481, 0.001889 | 0.75 | 0.002481, 0.002481 | 0.00 |
| `indicators.alltrees.27` | 0.001222, 0.002 | 1.30 | 0.002889, 0.00263 | 0.33 |
| `indicators.alltrees.28` | 0.001704, 0.002778 | 1.31 | 0.003111, 0.002667 | 0.54 |
| `indicators.alltrees.29` | 0.001667, 0.00163 | 0.07 | 0.001704, 0.002481 | 1.34 |
| `indicators.alltrees.30` | 0.00137, 0.001481 | 0.23 | 0.002333, 0.002296 | 0.06 |
| `indicators.alltrees.31` | 0.002222, 0.001667 | 0.69 | 0.002259, 0.002963 | 0.88 |
| `indicators.alltrees.32` | 0.001815, 0.001704 | 0.19 | 0.001704, 0.003333 | 2.13 |
| `indicators.alltrees.33` | 0.002222, 0.001926 | 0.39 | 0.002444, 0.002592 | 0.21 |
| `indicators.alltrees.34` | 0.001667, 0.002 | 0.59 | 0.002667, 0.001926 | 1.12 |
| `indicators.alltrees.35` | 0.001407, 0.001778 | 0.70 | 0.00337, 0.002518 | 0.94 |
| `indicators.alltrees.36` | 0.001889, 0.002185 | 0.39 | 0.002296, 0.002592 | 0.48 |
| `indicators.alltrees.37` | 0.002704, 0.003259 | 0.41 | 0.002555, 0.003704 | 1.41 |
| `indicators.alltrees.38` | 0.001333, 0.001741 | 0.66 | 0.003111, 0.002778 | 0.42 |
| `indicators.alltrees.39` | 0.001518, 0.002259 | 1.07 | 0.002778, 0.003111 | 0.42 |
| `indicators.alltrees.40` | 0.001778, 0.002926 | 1.06 | 0.002852, 0.003148 | 0.38 |
| `indicators.alltrees.41` | 0.00237, 0.002444 | 0.08 | 0.003222, 0.003667 | 0.47 |
| `indicators.alltrees.42` | 0.001593, 0.002296 | 0.93 | 0.003852, 0.002778 | 1.22 |
| `indicators.alltrees.43` | 0.001889, 0.002074 | 0.25 | 0.002852, 0.003185 | 0.44 |
| `indicators.alltrees.44` | 0.001926, 0.003037 | 1.29 | 0.003518, 0.002815 | 0.82 |
| `indicators.alltrees.45` | 0.001444, 0.002704 | 1.50 | 0.004148, 0.00263 | 1.33 |
| `indicators.alltrees.46` | 0.002148, 0.003333 | 1.09 | 0.003, 0.001889 | 1.45 |
| `indicators.alltrees.47` | 0.001815, 0.003222 | 1.45 | 0.005185, 0.002667 | 1.89 |
| `indicators.alltrees.48` | 0.001481, 0.002778 | 1.24 | 0.002963, 0.004407 | 1.30 |
| `indicators.alltrees.49` | 0.001889, 0.002037 | 0.15 | 0.003296, 0.002481 | 0.81 |
| `indicators.alltrees.50` | 0.003037, 0.001778 | 1.29 | 0.003444, 0.004555 | 0.85 |
| `indicators.alltrees.51` | 0.001074, 0.002259 | 1.78 | 0.004666, 0.002852 | 1.45 |
| `indicators.alltrees.52` | 0.001518, 0.002592 | 1.28 | 0.004889, 0.003 | 1.46 |
| `indicators.alltrees.53` | 0.002926, 0.001667 | 1.40 | 0.003222, 0.004629 | 1.08 |
| `indicators.alltrees.54` | 0.002407, 0.00163 | 0.96 | 0.003592, 0.004296 | 0.60 |
| `indicators.alltrees.55` | 0.002926, 0.001667 | 1.19 | 0.003778, 0.004889 | 0.78 |
| `indicators.alltrees.56` | 0.002185, 0.003259 | 0.95 | 0.004037, 0.003518 | 0.42 |
| `indicators.alltrees.57` | 0.003296, 0.002111 | 1.08 | 0.003778, 0.005407 | 1.21 |
| `indicators.alltrees.58` | 0.002259, 0.001704 | 0.70 | 0.002518, 0.00437 | 1.64 |
| `indicators.alltrees.59` | 0.001481, 0.003778 | 2.06 | 0.005, 0.004407 | 0.41 |
| `indicators.alltrees.60` | 0.001963, 0.002222 | 0.32 | 0.004037, 0.003444 | 0.51 |
| `indicators.alltrees.61` | 0.003111, 9.629e-04 | 1.92 | 0.004259, 0.003555 | 0.63 |
| `indicators.alltrees.62` | 0.004148, 0.004629 | 0.25 | 0.003444, 0.004963 | 1.18 |
| `indicators.alltrees.63` | 0.001963, 0.002852 | 0.82 | 0.003667, 0.004518 | 0.64 |
| `indicators.alltrees.64` | 0.001778, 0.002222 | 0.46 | 0.003333, 0.003889 | 0.54 |
| `indicators.alltrees.65` | 0.003222, 0.002704 | 0.45 | 0.004259, 0.003111 | 0.77 |
| `indicators.alltrees.66` | 0.00237, 0.002185 | 0.19 | 0.004259, 0.002926 | 1.18 |
| `indicators.alltrees.67` | 0.003, 0.001926 | 0.95 | 0.002704, 0.005259 | 1.84 |
| `indicators.alltrees.68` | 0.001259, 0.001815 | 0.79 | 0.00263, 0.003074 | 0.47 |
| `indicators.alltrees.69` | 0.001741, 0.003407 | 1.40 | 0.004333, 0.002704 | 1.52 |
| `indicators.alltrees.70` | 0.002481, 0.002 | 0.38 | 0.002481, 0.003185 | 0.84 |
| `indicators.alltrees.71` | 0.002, 0.001741 | 0.30 | 0.002222, 0.003592 | 1.43 |
| `indicators.alltrees.72` | 0.002555, 0.001926 | 0.71 | 0.004185, 0.003333 | 0.74 |
| `indicators.alltrees.73` | 0.003333, 0.00137 | 2.08 | 0.00237, 0.003852 | 1.48 |
| `indicators.alltrees.74` | 0.002222, 0.001704 | 0.73 | 0.003963, 0.003444 | 0.48 |
| `indicators.alltrees.75` | 0.002815, 0.002 | 0.87 | 0.005, 0.004296 | 0.44 |
| `indicators.alltrees.76` | 0.001481, 0.001963 | 0.66 | 0.002778, 0.003481 | 0.70 |
| `indicators.alltrees.77` | 0.001704, 0.002852 | 1.30 | 0.00337, 0.002889 | 0.49 |
| `indicators.alltrees.78` | 0.002667, 0.002592 | 0.07 | 0.004111, 0.003741 | 0.31 |
| `indicators.alltrees.79` | 0.002333, 0.001741 | 0.70 | 0.003629, 0.004111 | 0.40 |
| `indicators.alltrees.80` | 0.002926, 0.00137 | 1.53 | 0.003148, 0.003667 | 0.50 |
| `indicators.alltrees.81` | 0.001852, 0.001778 | 0.10 | 0.003518, 0.003333 | 0.18 |
| `indicators.alltrees.82` | 0.002148, 0.001815 | 0.40 | 0.002741, 0.004407 | 1.62 |
| `indicators.alltrees.83` | 0.002148, 0.003296 | 1.22 | 0.003741, 0.004037 | 0.23 |
| `indicators.alltrees.84` | 0.002444, 0.002518 | 0.09 | 0.00337, 0.002333 | 0.93 |
| `indicators.alltrees.85` | 0.003259, 0.002778 | 0.46 | 0.003407, 0.003407 | 0.00 |
| `indicators.alltrees.86` | 0.003185, 0.002111 | 1.12 | 0.003407, 0.002667 | 0.74 |
| `indicators.alltrees.87` | 0.003481, 0.002926 | 0.48 | 0.003407, 0.004666 | 0.99 |
| `indicators.alltrees.88` | 0.002963, 0.002444 | 0.54 | 0.00337, 0.004259 | 0.84 |
| `indicators.alltrees.89` | 0.003518, 0.002111 | 1.29 | 0.003889, 0.003518 | 0.36 |
| `indicators.alltrees.90` | 0.002926, 0.002518 | 0.42 | 0.002963, 0.003037 | 0.07 |
| `indicators.alltrees.91` | 0.002815, 0.001889 | 0.89 | 0.002518, 0.002778 | 0.36 |
| `indicators.alltrees.92` | 0.002222, 0.002741 | 0.67 | 0.003148, 0.003074 | 0.09 |
| `indicators.alltrees.93` | 0.001518, 0.002889 | 1.48 | 0.003296, 0.005703 | 1.92 |
| `indicators.alltrees.94` | 0.001778, 0.00263 | 1.01 | 0.004, 0.003074 | 0.88 |
| `indicators.alltrees.95` | 0.002444, 0.002667 | 0.24 | 0.004074, 0.003704 | 0.26 |
| `indicators.alltrees.96` | 0.002037, 0.002074 | 0.05 | 0.003667, 0.002926 | 0.69 |
| `indicators.alltrees.97` | 0.002296, 0.001407 | 1.26 | 0.003111, 0.003518 | 0.42 |
| `indicators.alltrees.98` | 0.001852, 0.002815 | 1.07 | 0.004741, 0.003629 | 0.77 |
| `indicators.alltrees.99` | 0.00263, 0.002074 | 0.65 | 0.003555, 0.004148 | 0.49 |
| `indicators.alltrees.100` | 0.001778, 0.003185 | 1.68 | 0.003778, 0.004852 | 0.92 |
| `indicators.alltrees.101` | 0.003037, 0.003037 | 0.00 | 0.004444, 0.004296 | 0.10 |
| `indicators.alltrees.102` | 0.003222, 0.003407 | 0.17 | 0.00337, 0.003926 | 0.53 |
| `indicators.alltrees.103` | 0.004926, 0.003296 | 1.11 | 0.004704, 0.004444 | 0.20 |
| `indicators.alltrees.104` | 0.003741, 0.003518 | 0.16 | 0.006407, 0.006481 | 0.04 |
| `indicators.alltrees.105` | 0.004, 0.004296 | 0.23 | 0.003259, 0.006074 | 2.27 |
| `indicators.alltrees.106` | 0.003481, 0.002037 | 1.57 | 0.004444, 0.003481 | 0.96 |
| `indicators.alltrees.107` | 0.002889, 0.002926 | 0.04 | 0.003481, 0.005518 | 1.89 |
| `indicators.alltrees.108` | 0.004037, 0.002148 | 2.07 | 0.003667, 0.005741 | 1.97 |
| `indicators.alltrees.109` | 0.006185, 0.004926 | 0.78 | 0.004037, 0.003889 | 0.17 |
| `indicators.alltrees.110` | 0.004481, 0.004666 | 0.17 | 0.004185, 0.006926 | 2.33 |
| `indicators.alltrees.111` | 0.005815, 0.002889 | 2.78 | 0.007, 0.005852 | 0.85 |
| `indicators.alltrees.112` | 0.003889, 0.004555 | 0.63 | 0.005815, 0.004666 | 1.02 |
| `indicators.alltrees.113` | 0.005074, 0.004889 | 0.16 | 0.004852, 0.005407 | 0.51 |
| `indicators.alltrees.114` | 0.006518, 0.003185 | 2.71 | 0.005666, 0.005889 | 0.20 |
| `indicators.alltrees.115` | 0.006666, 0.004926 | 1.50 | 0.007148, 0.009 | 1.17 |
| `indicators.alltrees.116` | 0.007666, 0.005629 | 1.57 | 0.008444, 0.007444 | 0.80 |
| `indicators.alltrees.117` | 0.008037, 0.006444 | 1.30 | 0.007629, 0.01048 | 1.90 |
| `indicators.alltrees.118` | 0.006815, 0.00874 | 1.26 | 0.01163, 0.01263 | 0.56 |
| `indicators.alltrees.119` | 0.01048, 0.009592 | 0.56 | 0.01259, 0.01374 | 0.65 |
| `indicators.alltrees.120` | 0.01415, 0.0137 | 0.23 | 0.01555, 0.01852 | 1.38 |
| `indicators.alltrees.121` | 0.01555, 0.01811 | 1.15 | 0.01948, 0.02352 | 1.68 |
| `indicators.alltrees.122` | 0.02274, 0.02544 | 0.93 | 0.02904, 0.02744 | 0.52 |
| `indicators.alltrees.123` | 0.03389, 0.02996 | 1.15 | 0.03392, 0.03385 | 0.02 |
| `indicators.alltrees.124` | 0.03092, 0.02922 | 0.55 | 0.03755, 0.03526 | 0.64 |
| `indicators.alltrees.125` | 0.0297, 0.0257 | 1.27 | 0.03318, 0.03655 | 1.00 |
| `indicators.alltrees.126` | 0.02085, 0.023 | 0.99 | 0.02004, 0.02111 | 0.55 |
| `indicators.alltrees.127` | 0.02763, 0.02789 | 0.12 | 0.02274, 0.02633 | 1.86 |
| `indicators.alltrees.128` | 0.04455, 0.04444 | 0.03 | 0.03378, 0.03144 | 0.96 |
| `populationMean.alltrees` | 40.37, 41.67 | 1.29 | 42.58, 42.5 | 0.08 |
| `popSizes.alltrees.1` | 38.31, 38.09 | 0.90 | 37.3, 37.24 | 0.24 |
| `popSizes.alltrees.2` | 18.52, 20.66 | 1.21 | 42.37, 42.15 | 0.18 |
| `popSizes.alltrees.3` | 19.7, 22.37 | 1.38 | 42.78, 42.66 | 0.10 |
| `popSizes.alltrees.4` | 24.56, 22.85 | 0.69 | 41.94, 42.72 | 0.63 |
| `popSizes.alltrees.5` | 21.7, 20.91 | 0.36 | 42.38, 42.9 | 0.41 |
| `popSizes.alltrees.6` | 17.81, 20.05 | 1.12 | 43.18, 42.32 | 0.68 |
| `popSizes.alltrees.7` | 20.77, 24.72 | 1.69 | 42.26, 42.48 | 0.17 |
| `popSizes.alltrees.8` | 21.25, 21.06 | 0.08 | 42.63, 42.27 | 0.29 |
| `popSizes.alltrees.9` | 17.51, 23.06 | 2.82 | 42.72, 43.09 | 0.28 |
| `popSizes.alltrees.10` | 20.88, 22.47 | 0.73 | 42.96, 42.38 | 0.47 |
| `popSizes.alltrees.11` | 19.8, 20.13 | 0.18 | 43.24, 42.87 | 0.27 |
| `popSizes.alltrees.12` | 20.25, 22.7 | 1.22 | 42.16, 41.68 | 0.40 |
| `popSizes.alltrees.13` | 20.34, 21.12 | 0.42 | 42.41, 42.36 | 0.04 |
| `popSizes.alltrees.14` | 19.58, 24.6 | 2.18 | 42.96, 42.17 | 0.64 |
| `popSizes.alltrees.15` | 18.7, 21.38 | 1.26 | 42.66, 43.07 | 0.31 |
| `popSizes.alltrees.16` | 21.73, 22.8 | 0.46 | 42.83, 42.36 | 0.38 |
| `popSizes.alltrees.17` | 19.83, 20.44 | 0.31 | 42.36, 41.85 | 0.41 |
| `popSizes.alltrees.18` | 20.4, 21.08 | 0.35 | 42.42, 41.81 | 0.47 |
| `popSizes.alltrees.19` | 21.12, 21.04 | 0.03 | 42.46, 41.92 | 0.41 |
| `popSizes.alltrees.20` | 22.33, 19.08 | 1.51 | 42.81, 42.69 | 0.09 |
| `popSizes.alltrees.21` | 18.5, 22.33 | 1.92 | 42.71, 42.9 | 0.15 |
| `popSizes.alltrees.22` | 21.35, 22.26 | 0.34 | 41.97, 42.5 | 0.44 |
| `popSizes.alltrees.23` | 20.7, 19.94 | 0.40 | 42.79, 43.2 | 0.31 |
| `popSizes.alltrees.24` | 20.4, 21.62 | 0.60 | 42.74, 42.78 | 0.04 |
| `popSizes.alltrees.25` | 19.57, 19.11 | 0.25 | 42.48, 41.67 | 0.67 |
| `popSizes.alltrees.26` | 20.25, 22.01 | 0.66 | 42.75, 42.36 | 0.30 |
| `popSizes.alltrees.27` | 21.76, 21.44 | 0.14 | 42.36, 43.24 | 0.66 |
| `popSizes.alltrees.28` | 20.35, 23.03 | 1.17 | 43.13, 43.59 | 0.36 |
| `popSizes.alltrees.29` | 22.89, 23.5 | 0.23 | 42.58, 42.35 | 0.18 |
| `popSizes.alltrees.30` | 21.49, 19.71 | 0.89 | 43.14, 43.03 | 0.08 |
| `popSizes.alltrees.31` | 18.98, 21.94 | 1.20 | 43.18, 42.41 | 0.63 |
| `popSizes.alltrees.32` | 22.29, 21.51 | 0.32 | 42.67, 42.71 | 0.03 |
| `popSizes.alltrees.33` | 21.33, 20.42 | 0.32 | 43.14, 41.82 | 1.05 |
| `popSizes.alltrees.34` | 20.07, 23.88 | 1.84 | 43.07, 41.76 | 1.09 |
| `popSizes.alltrees.35` | 19.2, 23.43 | 1.70 | 42.01, 42.12 | 0.09 |
| `popSizes.alltrees.36` | 19.75, 22.52 | 1.29 | 42.88, 42.33 | 0.43 |
| `popSizes.alltrees.37` | 21.01, 21.15 | 0.06 | 42.79, 41.71 | 0.90 |
| `popSizes.alltrees.38` | 22.89, 20.67 | 0.90 | 42.09, 42.86 | 0.59 |
| `popSizes.alltrees.39` | 19.39, 20.15 | 0.36 | 42.72, 42.46 | 0.22 |
| `popSizes.alltrees.40` | 19.12, 22.12 | 1.29 | 42.11, 42.83 | 0.60 |
| `popSizes.alltrees.41` | 20.24, 22.27 | 1.07 | 42.51, 42.94 | 0.34 |
| `popSizes.alltrees.42` | 23.43, 21.18 | 0.96 | 42.87, 42.8 | 0.06 |
| `popSizes.alltrees.43` | 20.79, 23.3 | 1.28 | 42.07, 42.41 | 0.27 |
| `popSizes.alltrees.44` | 20.5, 24.6 | 1.48 | 42.83, 42.24 | 0.45 |
| `popSizes.alltrees.45` | 21.39, 20.52 | 0.42 | 43.43, 43.1 | 0.25 |
| `popSizes.alltrees.46` | 18.12, 20.49 | 1.24 | 42.64, 43.17 | 0.42 |
| `popSizes.alltrees.47` | 18.15, 18.59 | 0.23 | 42.25, 43.52 | 0.99 |
| `popSizes.alltrees.48` | 21.42, 23.5 | 1.02 | 42.58, 42.52 | 0.05 |
| `popSizes.alltrees.49` | 20.01, 21.85 | 0.82 | 42.03, 42.77 | 0.61 |
| `popSizes.alltrees.50` | 22.12, 20.39 | 0.68 | 42.64, 42.12 | 0.42 |
| `popSizes.alltrees.51` | 19.91, 20.67 | 0.35 | 42.68, 43.04 | 0.27 |
| `popSizes.alltrees.52` | 19.53, 20.27 | 0.45 | 41.14, 41.59 | 0.41 |
| `popSizes.alltrees.53` | 18.59, 22.2 | 1.91 | 42.85, 42.28 | 0.45 |
| `popSizes.alltrees.54` | 20.84, 21.83 | 0.41 | 42.3, 41.8 | 0.40 |
| `popSizes.alltrees.55` | 20.63, 19.55 | 0.42 | 42.42, 43.39 | 0.76 |
| `popSizes.alltrees.56` | 20.66, 20.94 | 0.13 | 42.91, 42.69 | 0.17 |
| `popSizes.alltrees.57` | 20.71, 20.72 | 0.00 | 42.88, 43.37 | 0.36 |
| `popSizes.alltrees.58` | 20.27, 20.5 | 0.11 | 42.12, 42.17 | 0.04 |
| `popSizes.alltrees.59` | 18.39, 23.85 | 2.18 | 42.53, 42.39 | 0.11 |
| `popSizes.alltrees.60` | 20.32, 21.35 | 0.48 | 42.99, 42.64 | 0.27 |
| `popSizes.alltrees.61` | 20.86, 20.5 | 0.18 | 43.8, 42.93 | 0.68 |
| `popSizes.alltrees.62` | 22.88, 20.47 | 0.97 | 42.51, 42.66 | 0.11 |
| `popSizes.alltrees.63` | 19.32, 23.2 | 1.62 | 41.83, 42.92 | 0.87 |
| `popSizes.alltrees.64` | 20.05, 24.28 | 1.81 | 41.67, 42.12 | 0.36 |
| `popSizes.alltrees.65` | 20.03, 20.6 | 0.22 | 44.13, 43.33 | 0.59 |
| `popSizes.alltrees.66` | 22.11, 20.51 | 0.65 | 42.44, 42.44 | 0.00 |
| `popSizes.alltrees.67` | 18.88, 23.24 | 1.95 | 42.54, 42.78 | 0.19 |
| `popSizes.alltrees.68` | 19.92, 20.9 | 0.47 | 42.41, 43.38 | 0.77 |
| `popSizes.alltrees.69` | 21.92, 20.18 | 0.92 | 42.94, 42.29 | 0.50 |
| `popSizes.alltrees.70` | 21.36, 20.39 | 0.45 | 42.59, 41.72 | 0.72 |
| `popSizes.alltrees.71` | 21.1, 21.7 | 0.31 | 42.66, 41.4 | 1.05 |
| `popSizes.alltrees.72` | 19.99, 20.33 | 0.15 | 41.55, 42.58 | 0.82 |
| `popSizes.alltrees.73` | 21.47, 21.27 | 0.08 | 42.53, 43.28 | 0.60 |
| `popSizes.alltrees.74` | 20.47, 19.74 | 0.37 | 43.1, 42.5 | 0.46 |
| `popSizes.alltrees.75` | 18.85, 21.05 | 1.16 | 43.25, 44.32 | 0.78 |
| `popSizes.alltrees.76` | 21.16, 20.07 | 0.50 | 42.31, 41.99 | 0.25 |
| `popSizes.alltrees.77` | 20.56, 20.01 | 0.25 | 42.88, 41.89 | 0.79 |
| `popSizes.alltrees.78` | 20.33, 23.48 | 1.21 | 43.03, 42.23 | 0.62 |
| `popSizes.alltrees.79` | 19.21, 21.56 | 1.12 | 42.2, 42.1 | 0.08 |
| `popSizes.alltrees.80` | 20.4, 22.2 | 0.90 | 41.68, 42.37 | 0.57 |
| `popSizes.alltrees.81` | 22.34, 21.1 | 0.57 | 42.06, 42.02 | 0.04 |
| `popSizes.alltrees.82` | 18.31, 18.07 | 0.14 | 43.27, 42.04 | 0.99 |
| `popSizes.alltrees.83` | 21.78, 18.17 | 1.91 | 42.27, 42.63 | 0.29 |
| `popSizes.alltrees.84` | 21.42, 21.17 | 0.12 | 42.15, 42.22 | 0.05 |
| `popSizes.alltrees.85` | 21.69, 21.13 | 0.25 | 42.47, 43.07 | 0.47 |
| `popSizes.alltrees.86` | 20.52, 20.93 | 0.20 | 42.79, 43.67 | 0.66 |
| `popSizes.alltrees.87` | 20.4, 23.42 | 1.20 | 42.66, 43.57 | 0.69 |
| `popSizes.alltrees.88` | 21.17, 20.32 | 0.38 | 42.45, 42.56 | 0.09 |
| `popSizes.alltrees.89` | 21.32, 20.66 | 0.28 | 42.39, 42.01 | 0.30 |
| `popSizes.alltrees.90` | 19.09, 19.19 | 0.06 | 41.6, 42.35 | 0.61 |
| `popSizes.alltrees.91` | 25.65, 20.96 | 1.71 | 42.27, 42.67 | 0.31 |
| `popSizes.alltrees.92` | 18.7, 20.99 | 1.13 | 42.97, 41.94 | 0.85 |
| `popSizes.alltrees.93` | 18.9, 20.17 | 0.72 | 41.97, 42.88 | 0.71 |
| `popSizes.alltrees.94` | 18.62, 21.17 | 1.41 | 42.1, 42.62 | 0.43 |
| `popSizes.alltrees.95` | 18.35, 19.7 | 0.73 | 42.29, 42.33 | 0.03 |
| `popSizes.alltrees.96` | 20.43, 19.77 | 0.32 | 43.37, 41.43 | 1.53 |
| `popSizes.alltrees.97` | 21.39, 22.88 | 0.63 | 42.65, 42.13 | 0.42 |
| `popSizes.alltrees.98` | 21.2, 18.73 | 1.17 | 42.56, 42.21 | 0.29 |
| `popSizes.alltrees.99` | 21.49, 19.29 | 1.01 | 42.65, 43.06 | 0.31 |
| `popSizes.alltrees.100` | 23.8, 22.4 | 0.63 | 42.53, 42.98 | 0.37 |
| `popSizes.alltrees.101` | 20.42, 23.78 | 1.20 | 42.52, 41.99 | 0.44 |
| `popSizes.alltrees.102` | 20.17, 22.12 | 0.98 | 42.86, 42.08 | 0.62 |
| `popSizes.alltrees.103` | 20.42, 22.88 | 1.11 | 42.4, 42.01 | 0.30 |
| `popSizes.alltrees.104` | 23.3, 21.3 | 0.83 | 42.95, 42.34 | 0.47 |
| `popSizes.alltrees.105` | 19.23, 25.21 | 2.94 | 42.41, 41.81 | 0.49 |
| `popSizes.alltrees.106` | 20.94, 22.13 | 0.52 | 43.4, 42.47 | 0.71 |
| `popSizes.alltrees.107` | 18.83, 18.82 | 0.00 | 43.32, 43.07 | 0.19 |
| `popSizes.alltrees.108` | 21.08, 18.29 | 1.44 | 42.46, 41.98 | 0.37 |
| `popSizes.alltrees.109` | 18.98, 22.29 | 1.33 | 42.4, 42.12 | 0.24 |
| `popSizes.alltrees.110` | 21.67, 21.29 | 0.18 | 42.66, 42.65 | 0.01 |
| `popSizes.alltrees.111` | 22.33, 21.64 | 0.34 | 42.16, 42.19 | 0.02 |
| `popSizes.alltrees.112` | 23.96, 17.13 | 2.79 | 43.24, 42.64 | 0.47 |
| `popSizes.alltrees.113` | 20.79, 21.13 | 0.16 | 42.54, 41.77 | 0.60 |
| `popSizes.alltrees.114` | 22.26, 21.91 | 0.16 | 42.88, 41.9 | 0.75 |
| `popSizes.alltrees.115` | 21.51, 16.96 | 2.06 | 43.15, 42.33 | 0.68 |
| `popSizes.alltrees.116` | 20.89, 22.39 | 0.67 | 42.3, 42.81 | 0.39 |
| `popSizes.alltrees.117` | 21.72, 20.92 | 0.41 | 42.03, 41.73 | 0.24 |
| `popSizes.alltrees.118` | 23.12, 23.64 | 0.21 | 42.42, 42.65 | 0.19 |
| `popSizes.alltrees.119` | 21.28, 21.66 | 0.15 | 42.66, 42.92 | 0.21 |
| `popSizes.alltrees.120` | 22.64, 22.88 | 0.11 | 42.06, 41.01 | 0.89 |
| `popSizes.alltrees.121` | 21.87, 21.28 | 0.30 | 42.29, 41.42 | 0.68 |
| `popSizes.alltrees.122` | 21.95, 25.06 | 1.35 | 41.76, 42.85 | 0.85 |
| `popSizes.alltrees.123` | 21.25, 22.19 | 0.50 | 41.67, 40.62 | 0.91 |
| `popSizes.alltrees.124` | 23.06, 23.66 | 0.25 | 41.21, 41.6 | 0.30 |
| `popSizes.alltrees.125` | 22.15, 24.13 | 0.85 | 42.41, 42.2 | 0.15 |
| `popSizes.alltrees.126` | 23.44, 21.44 | 0.92 | 40.97, 40.65 | 0.27 |
| `popSizes.alltrees.127` | 21.92, 24.2 | 0.94 | 42.19, 41.61 | 0.45 |
| `popSizes.alltrees.128` | 24.76, 23.09 | 0.87 | 41.88, 42.55 | 0.52 |
| `popSizes.alltrees.129` | 22.54, 26.04 | 1.35 | 41.05, 41.98 | 0.74 |
| `sum(indicators.alltrees)` | 0.5736, 0.5603 | 0.68 | 0.7052, 0.7304 | 1.16 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 21m16s | 4630 | 13067 | 1931 (`popSizes.alltrees.59`) |
| scale | 53m40s | 5142 | 5749 | 5727 (`prior`) |

Run-time ratio scale / default: 2.52

