# Posterior comparison: testBSP

**Verdict: matched**

- beast2: `beast2/log/testBSP/rep1`, `beast2/log/testBSP/rep2`
- beast3: `beast3/log/testBSP/rep1`, `beast3/log/testBSP/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3114; max z: 1.998; max clade |Δp|: 0.015

## Findings

- **NOTE** column renamed (mapping): beast2 `treeModel.rootHeight` = beast3 `tree.height`
- **NOTE** column map used: `reports/maps/testBSP.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testBSP/rep1/test.1.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m19s |  |
| beast2 | rep2 | `beast2/log/testBSP/rep2/test.2.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m18s |  |
| beast3 | rep1 | `beast3/log/testBSP/rep1/test.1.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 2m47s |  |
| beast3 | rep2 | `beast3/log/testBSP/rep2/test.2.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 2m46s |  |

## Parameters: `test.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -3870.60 | [-3881.46, -3860.70] | 6885 (3390) | -3870.68 | [-3881.59, -3860.67] | 15885 (7700) | 1.02 | 100% | ok |
| `siteModel.alpha` | 0.05473 | [0.001009, 0.1155] | 7272 (3425) | 0.05458 | [1.863e-04, 0.1162] | 16018 (7806) | 0.31 | 100% | ok |
| `clock.rate` | 9.469e-04 | [6.988e-04, 0.001189] | 6732 (3296) | 9.471e-04 | [6.940e-04, 0.00119] | 16340 (8049) | 0.10 | 100% | ok |
| `skyline.popSize.1` | 65.89 | [7.84, 187.16] | 7722 (3543) | 66.47 | [6.646, 193.37] | 17008 (8262) | 0.32 | 100% | ok |
| `skyline.popSize.2` | 26.25 | [1.578, 66.9] | 7410 (3432) | 25.52 | [1.755, 64.16] | 16291 (7961) | 2.00 | 100% | ok |
| `skyline.popSize.3` | 32.13 | [3.141, 73.5] | 7072 (3440) | 32.27 | [2.771, 74.69] | 13361 (6463) | 0.42 | 100% | ok |
| `skyline.popSize.4` | 41.55 | [5.412, 89.43] | 7828 (3801) | 41.31 | [5.039, 88.69] | 15378 (7427) | 0.68 | 100% | ok |
| `skyline.popSize.5` | 32.94 | [0.01112, 80.15] | 8348 (3847) | 32.93 | [0.01248, 79.25] | 16038 (7960) | 0.03 | 100% | ok |
| `skyline.groupSize.1` | 2.469 | [1, 7] | 7823 (3819) | 2.465 | [1, 7] | 9760 (4585) | 0.15 | 100% | ok |
| `skyline.groupSize.2` | 3.377 | [1, 8] | 8673 (4307) | 3.392 | [1, 8] | 12396 (5187) | 0.49 | 100% | ok |
| `skyline.groupSize.3` | 3.305 | [1, 8] | 8266 (4064) | 3.295 | [1, 8] | 13274 (6155) | 0.33 | 100% | ok |
| `skyline.groupSize.4` | 3.655 | [1, 8] | 7587 (3384) | 3.647 | [1, 8] | 11424 (5223) | 0.20 | 100% | ok |
| `skyline.groupSize.5` | 3.194 | [1, 9] | 6732 (3357) | 3.201 | [1, 9] | 8491 (3727) | 0.18 | 100% | ok |
| `hky.kappa` | 19.9 | [13.32, 27.55] | 8748 (4247) | 19.94 | [13.31, 27.54] | 17589 (8588) | 0.79 | 100% | ok |
| `treeModel.rootHeight → tree.height` | 70.29 | [57.76, 83.77] | 7017 (3470) | 70.3 | [57.91, 84.34] | 14491 (5839) | 0.08 | 99% | ok |
| `likelihood` | -3773.05 | [-3779.86, -3767.10] | 8575 (4168) | -3773.11 | [-3779.89, -3767.01] | 16314 (8116) | 1.35 | 100% | ok |
| `skyline` | -69.73 | [-76.11, -63.12] | 6229 (3114) | -69.73 | [-76.04, -63.02] | 14642 (7221) | 0.08 | 99% | ok |
| `eml1` | -22.44 | [-26.5, -18.45] | 7250 (3245) | -22.45 | [-26.68, -18.58] | 16027 (7965) | 0.35 | 98% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -3870.58, -3870.62 | 0.36 | -3870.71, -3870.65 | 0.74 |
| `siteModel.alpha` | 0.05476, 0.05469 | 0.08 | 0.05432, 0.05483 | 0.91 |
| `clock.rate` | 9.479e-04, 9.459e-04 | 0.63 | 9.451e-04, 9.491e-04 | 2.04 |
| `skyline.popSize.1` | 67.78, 64 | 1.29 | 66.71, 66.24 | 0.22 |
| `skyline.popSize.2` | 26.18, 26.32 | 0.21 | 25.34, 25.69 | 0.97 |
| `skyline.popSize.3` | 32.05, 32.21 | 0.29 | 32.41, 32.13 | 0.71 |
| `skyline.popSize.4` | 41.3, 41.8 | 0.88 | 41.15, 41.46 | 0.75 |
| `skyline.popSize.5` | 32.39, 33.49 | 1.86 | 32.73, 33.12 | 0.93 |
| `skyline.groupSize.1` | 2.449, 2.49 | 0.89 | 2.47, 2.46 | 0.24 |
| `skyline.groupSize.2` | 3.35, 3.404 | 1.16 | 3.401, 3.383 | 0.46 |
| `skyline.groupSize.3` | 3.346, 3.264 | 1.72 | 3.299, 3.291 | 0.20 |
| `skyline.groupSize.4` | 3.617, 3.693 | 1.35 | 3.651, 3.643 | 0.18 |
| `skyline.groupSize.5` | 3.238, 3.149 | 1.47 | 3.179, 3.223 | 0.81 |
| `hky.kappa` | 19.9, 19.91 | 0.07 | 19.95, 19.94 | 0.17 |
| `treeModel.rootHeight → tree.height` | 70.22, 70.36 | 0.84 | 70.39, 70.2 | 1.53 |
| `likelihood` | -3773.01, -3773.09 | 1.02 | -3773.12, -3773.11 | 0.29 |
| `skyline` | -69.74, -69.73 | 0.11 | -69.77, -69.7 | 1.21 |
| `eml1` | -22.45, -22.43 | 0.40 | -22.44, -22.46 | 0.56 |

## Trees: `test.N.trees`

9002 trees (beast2) and 18002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.016, beast3 0.016.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Indon77, D4Mexico84, D4NewCal81, … (9 taxa)} | 9 | 0.631 | 0.616 | 0.015 | ok |
| {D4Brazi82, D4ElSal83, D4Mexico84, D4NewCal81, D4PRico86} | 5 | 0.159 | 0.167 | 0.008 | ok |
| {D4ElSal94, D4PRico86} | 2 | 0.242 | 0.235 | 0.008 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Indon76, D4Mexico84, D4NewCal81, … (9 taxa)} | 9 | 0.173 | 0.181 | 0.008 | ok |
| {D4Indon76, D4Indon77} | 2 | 0.196 | 0.204 | 0.007 | ok |
| {D4ElSal83, D4Mexico84} | 2 | 0.249 | 0.242 | 0.006 | ok |
| {D4ElSal83, D4Mexico84, D4NewCal81} | 3 | 0.174 | 0.168 | 0.006 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81} | 5 | 0.532 | 0.526 | 0.006 | ok |
| {D4Philip56, D4Philip64, D4Philip84, D4SLanka78, D4Thai63, D4Thai78, … (7 taxa)} | 7 | 0.078 | 0.073 | 0.005 | ok |
| {D4ElSal83, D4NewCal81} | 2 | 0.208 | 0.211 | 0.004 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4PRico86} | 6 | 0.690 | 0.686 | 0.004 | ok |
| {D4Brazi82, D4NewCal81} | 2 | 0.176 | 0.180 | 0.004 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4PRico86, … (7 taxa)} | 7 | 0.475 | 0.472 | 0.004 | ok |
| {D4Mexico84, D4NewCal81} | 2 | 0.150 | 0.148 | 0.003 | ok |
| {D4Brazi82, D4ElSal83, D4Mexico84, D4NewCal81} | 4 | 0.777 | 0.779 | 0.003 | ok |
| {D4Brazi82, D4ElSal83, D4NewCal81} | 3 | 0.205 | 0.207 | 0.002 | ok |
| {D4Brazi82, D4Mexico84} | 2 | 0.148 | 0.150 | 0.002 | ok |
| {D4Brazi82, D4ElSal83, D4Mexico84} | 3 | 0.175 | 0.173 | 0.002 | ok |
| {D4Brazi82, D4ElSal83} | 2 | 0.227 | 0.229 | 0.002 | ok |
| {D4Philip56, D4Philip64, D4Philip84, D4SLanka78, D4Thai78, D4Thai84} | 6 | 0.973 | 0.972 | 0.002 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4Tahiti79} | 6 | 0.063 | 0.064 | 0.001 | ok |
| {D4Brazi82, D4Mexico84, D4NewCal81} | 3 | 0.095 | 0.096 | 0.001 | ok |
| {D4ElSal83, D4ElSal94} | 2 | 0.068 | 0.067 | 0.001 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Indon76, D4Indon77, D4Mexico84, … (16 taxa)} | 16 | 0.909 | 0.910 | 0.001 | ok |
| {D4Tahiti79, D4Tahiti85} | 2 | 0.177 | 0.178 | 0.001 | ok |
| {D4PRico86, D4Tahiti85} | 2 | 0.278 | 0.277 | 0.001 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4PRico86, … (7 taxa)} | 7 | 0.229 | 0.228 | 0.000 | ok |
| {D4Philip64, D4Philip84} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {D4Thai78, D4Thai84} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {D4Philip56, D4Philip64, D4Philip84} | 3 | 1.000 | 1.000 | 0.000 | ok |

(3 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2m37s | 6885 | 157639 | 142614 (`skyline`) |
| beast3 | 5m33s | 15885 | 171478 | 91664 (`skyline.groupSize.5`) |

Run-time ratio beast3 / beast2: 2.12

