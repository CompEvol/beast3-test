# Posterior comparison: testBSP

**Verdict: matched**

- beast2: `beast2/log/testBSP/rep1`, `beast2/log/testBSP/rep2`
- beast3: `beast3/log/testBSP/rep1`, `beast3/log/testBSP/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 2429; max z: 1.911; max clade |Δp|: 0.018

## Findings

- **NOTE** column renamed (mapping): beast2 `treeModel.rootHeight` = beast3 `tree.height`
- **NOTE** column map used: `reports/maps/testBSP.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testBSP/rep1/test.1.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 1m58s |  |
| beast2 | rep2 | `beast2/log/testBSP/rep2/test.2.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 2m09s |  |
| beast3 | rep1 | `beast3/log/testBSP/rep1/test.1.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 3m07s |  |
| beast3 | rep2 | `beast3/log/testBSP/rep2/test.2.log` | 5001 (4501) | 2000 | 2.8.0 rc2 | yes | 3m09s |  |

## Parameters: `test.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -3876.22 | [-3888.11, -3865.65] | 6397 (3063) | -3876.22 | [-3888.04, -3865.59] | 8920 (4419) | 0.05 | 100% | ok |
| `siteModel.alpha` | 0.05327 | [0.001006, 0.113] | 7279 (3592) | 0.05384 | [1.845e-04, 0.1145] | 9002 (4501) | 1.05 | 100% | ok |
| `clock.rate` | 9.330e-04 | [6.911e-04, 0.001178] | 5857 (2581) | 9.313e-04 | [6.917e-04, 0.001173] | 8427 (3954) | 0.82 | 100% | ok |
| `skyline.popSize.1` | 61.77 | [6.831, 178.93] | 6078 (2429) | 62.17 | [6.739, 176.52] | 8944 (4443) | 0.23 | 100% | ok |
| `skyline.popSize.2` | 26.08 | [1.908, 64.79] | 7329 (3498) | 26.24 | [2.014, 64.73] | 8621 (4120) | 0.43 | 100% | ok |
| `skyline.popSize.3` | 33.06 | [3.717, 76.96] | 6689 (3113) | 33.43 | [2.558, 78.1] | 8309 (3996) | 0.92 | 100% | ok |
| `skyline.popSize.4` | 42.61 | [5.839, 92.03] | 7682 (3825) | 42.41 | [4.154, 90.78] | 8621 (4120) | 0.48 | 99% | ok |
| `skyline.popSize.5` | 33.6 | [0.06757, 80.45] | 8234 (4021) | 34.43 | [0.02916, 82.9] | 9002 (4501) | 1.91 | 100% | ok |
| `skyline.groupSize.1` | 2.535 | [1, 7] | 6589 (2937) | 2.564 | [1, 7] | 7349 (3339) | 0.82 | 100% | ok |
| `skyline.groupSize.2` | 3.384 | [1, 8] | 8546 (4181) | 3.362 | [1, 8] | 7057 (3277) | 0.63 | 100% | ok |
| `skyline.groupSize.3` | 3.263 | [1, 7] | 8382 (4010) | 3.263 | [1, 7] | 7564 (3782) | 0.01 | 100% | ok |
| `skyline.groupSize.4` | 3.633 | [1, 8] | 8293 (4099) | 3.623 | [1, 8] | 7383 (3538) | 0.26 | 100% | ok |
| `skyline.groupSize.5` | 3.185 | [1, 9] | 6861 (3419) | 3.188 | [1, 9] | 6081 (2825) | 0.07 | 100% | ok |
| `skyline.popSizeInitialMean` | 659.27 | [1.646, 851.61] | 6865 (2698) | 618.24 | [1.776, 785.78] | 7835 (3334) | 0.11 | 100% | ok |
| `hky.kappa` | 19.87 | [13.4, 27.6] | 8155 (3929) | 19.84 | [13.05, 27.01] | 8951 (4450) | 0.47 | 97% | ok |
| `treeModel.rootHeight → tree.height` | 70.88 | [58.36, 85.16] | 6148 (2978) | 70.95 | [57.64, 84.61] | 8802 (4366) | 0.59 | 98% | ok |
| `likelihood` | -3773.05 | [-3779.65, -3766.75] | 8024 (3793) | -3773.04 | [-3779.60, -3766.80] | 8624 (4123) | 0.27 | 100% | ok |
| `skyline` | -70 | [-76.36, -63.32] | 5817 (2829) | -70.02 | [-76.58, -63.33] | 8664 (4235) | 0.46 | 100% | ok |
| `eml1` | -24 | [-28.47, -20.07] | 6695 (3216) | -24 | [-28.32, -19.84] | 8936 (4435) | 0.16 | 98% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -3876.16, -3876.29 | 0.88 | -3876.25, -3876.18 | 0.52 |
| `siteModel.alpha` | 0.05341, 0.05313 | 0.34 | 0.05385, 0.05383 | 0.03 |
| `clock.rate` | 9.342e-04, 9.319e-04 | 0.70 | 9.296e-04, 9.330e-04 | 1.28 |
| `skyline.popSize.1` | 61.15, 62.39 | 0.45 | 61.74, 62.6 | 0.38 |
| `skyline.popSize.2` | 25.68, 26.48 | 1.37 | 26.37, 26.11 | 0.52 |
| `skyline.popSize.3` | 32.88, 33.25 | 0.63 | 33.44, 33.42 | 0.04 |
| `skyline.popSize.4` | 42.85, 42.37 | 0.77 | 42.82, 42 | 1.42 |
| `skyline.popSize.5` | 33.53, 33.67 | 0.24 | 34.6, 34.26 | 0.52 |
| `skyline.groupSize.1` | 2.535, 2.536 | 0.03 | 2.552, 2.577 | 0.49 |
| `skyline.groupSize.2` | 3.372, 3.396 | 0.51 | 3.395, 3.329 | 1.27 |
| `skyline.groupSize.3` | 3.244, 3.282 | 0.79 | 3.251, 3.275 | 0.48 |
| `skyline.groupSize.4` | 3.634, 3.632 | 0.03 | 3.605, 3.641 | 0.64 |
| `skyline.groupSize.5` | 3.216, 3.155 | 1.02 | 3.198, 3.178 | 0.30 |
| `skyline.popSizeInitialMean` | 291.92, 1026.63 | 1.23 | 716.37, 520.11 | 0.43 |
| `hky.kappa` | 19.9, 19.83 | 0.81 | 19.84, 19.84 | 0.02 |
| `treeModel.rootHeight → tree.height` | 70.84, 70.93 | 0.49 | 71.07, 70.83 | 1.57 |
| `likelihood` | -3773.04, -3773.06 | 0.23 | -3773.09, -3772.99 | 1.32 |
| `skyline` | -69.95, -70.04 | 1.13 | -70.06, -69.99 | 1.01 |
| `eml1` | -23.98, -24.01 | 0.58 | -24, -24.01 | 0.18 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.013, beast3 0.050.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {D4Brazi82, D4ElSal83, D4NewCal81} | 3 | 0.198 | 0.216 | 0.018 | ok |
| {D4ElSal83, D4Mexico84} | 2 | 0.248 | 0.233 | 0.015 | ok |
| {D4Brazi82, D4ElSal83} | 2 | 0.228 | 0.238 | 0.010 | ok |
| {D4ElSal83, D4Mexico84, D4NewCal81} | 3 | 0.171 | 0.161 | 0.010 | ok |
| {D4Tahiti79, D4Tahiti85} | 2 | 0.179 | 0.170 | 0.009 | ok |
| {D4ElSal83, D4NewCal81} | 2 | 0.202 | 0.210 | 0.009 | ok |
| {D4Indon76, D4Indon77} | 2 | 0.208 | 0.199 | 0.009 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4PRico86, … (7 taxa)} | 7 | 0.228 | 0.236 | 0.008 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Indon76, D4Mexico84, D4NewCal81, … (9 taxa)} | 9 | 0.176 | 0.180 | 0.005 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Indon77, D4Mexico84, D4NewCal81, … (9 taxa)} | 9 | 0.616 | 0.620 | 0.004 | ok |
| {D4Brazi82, D4ElSal83, D4Mexico84} | 3 | 0.169 | 0.172 | 0.003 | ok |
| {D4Brazi82, D4Mexico84} | 2 | 0.151 | 0.147 | 0.003 | ok |
| {D4ElSal83, D4ElSal94} | 2 | 0.071 | 0.069 | 0.003 | ok |
| {D4Brazi82, D4ElSal83, D4Mexico84, D4NewCal81} | 4 | 0.777 | 0.774 | 0.002 | ok |
| {D4Brazi82, D4NewCal81} | 2 | 0.182 | 0.180 | 0.002 | ok |
| {D4Philip56, D4Philip64, D4Philip84, D4SLanka78, D4Thai78, D4Thai84} | 6 | 0.972 | 0.974 | 0.002 | ok |
| {D4Mexico84, D4NewCal81} | 2 | 0.148 | 0.146 | 0.002 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4Tahiti79} | 6 | 0.064 | 0.062 | 0.002 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Indon76, D4Indon77, D4Mexico84, … (16 taxa)} | 16 | 0.906 | 0.908 | 0.002 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81} | 5 | 0.538 | 0.539 | 0.001 | ok |
| {D4PRico86, D4Tahiti85} | 2 | 0.283 | 0.284 | 0.001 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4PRico86, … (7 taxa)} | 7 | 0.470 | 0.471 | 0.001 | ok |
| {D4Brazi82, D4ElSal83, D4Mexico84, D4NewCal81, D4PRico86} | 5 | 0.160 | 0.159 | 0.001 | ok |
| {D4Brazi82, D4Mexico84, D4NewCal81} | 3 | 0.095 | 0.094 | 0.001 | ok |
| {D4ElSal94, D4PRico86} | 2 | 0.237 | 0.236 | 0.001 | ok |
| {D4Brazi82, D4ElSal83, D4ElSal94, D4Mexico84, D4NewCal81, D4PRico86} | 6 | 0.684 | 0.683 | 0.001 | ok |
| {D4Philip56, D4Philip64, D4Philip84, D4SLanka78, D4Thai63, D4Thai78, … (7 taxa)} | 7 | 0.077 | 0.078 | 0.001 | ok |
| {D4Philip64, D4Philip84} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {D4Thai78, D4Thai84} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {D4Philip56, D4Philip64, D4Philip84} | 3 | 1.000 | 1.000 | 0.000 | ok |

(3 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 4m07s | 6397 | 93278 | 84822 (`skyline`) |
| beast3 | 6m16s | 8920 | 85343 | 58183 (`skyline.groupSize.5`) |

Run-time ratio beast3 / beast2: 1.52

