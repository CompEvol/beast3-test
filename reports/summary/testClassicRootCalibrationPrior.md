# Posterior comparison: testClassicRootCalibrationPrior

**Verdict: matched**

- beast2: `beast2/log/testClassicRootCalibrationPrior/rep1`, `beast2/log/testClassicRootCalibrationPrior/rep2`
- beast3: `beast3/log/testClassicRootCalibrationPrior/rep1`, `beast3/log/testClassicRootCalibrationPrior/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3318; max z: 0.6507; max clade |Δp|: 0.009

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testClassicRootCalibrationPrior/rep1/classic_root_prior_oneOnX.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 2s |  |
| beast2 | rep2 | `beast2/log/testClassicRootCalibrationPrior/rep2/classic_root_prior_oneOnX.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 2s |  |
| beast3 | rep1 | `beast3/log/testClassicRootCalibrationPrior/rep1/classic_root_prior_oneOnX.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |
| beast3 | rep2 | `beast3/log/testClassicRootCalibrationPrior/rep2/classic_root_prior_oneOnX.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |

## Parameters: `classic_root_prior_oneOnX.N.log`

Constant columns (skipped): `monophyletic(all)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -11.97 | [-14.26, -10.3] | 8224 (4032) | -11.96 | [-14.33, -10.38] | 7816 (3318) | 0.06 | 98% | ok |
| `yule` | -9.185 | [-11.16, -7.214] | 8562 (4061) | -9.196 | [-11.28, -7.189] | 8119 (3869) | 0.65 | 100% | ok |
| `mrca.age(all)` | 7.244 | [4.583, 10.22] | 8809 (4308) | 7.253 | [4.634, 10.26] | 9002 (4501) | 0.42 | 99% | ok |
| `birthRate` | 0.1575 | [0.01288, 0.3512] | 7776 (3826) | 0.1575 | [0.0154, 0.3613] | 8334 (3833) | 0.01 | 99% | ok |

### Replicate agreement (baseline noise): `classic_root_prior_oneOnX.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -11.96, -11.97 | 0.56 | -11.99, -11.94 | 1.89 |
| `yule` | -9.175, -9.195 | 0.91 | -9.199, -9.193 | 0.26 |
| `mrca.age(all)` | 7.219, 7.269 | 1.59 | 7.25, 7.256 | 0.21 |
| `birthRate` | 0.1588, 0.1561 | 1.18 | 0.1591, 0.1559 | 1.45 |

## Trees: `classic_root_prior_oneOnX.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.010, beast3 0.023.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {1, 4} | 2 | 0.223 | 0.214 | 0.009 | ok |
| {2, 4} | 2 | 0.218 | 0.226 | 0.008 | ok |
| {3, 4} | 2 | 0.224 | 0.232 | 0.007 | ok |
| {2, 3, 4} | 3 | 0.165 | 0.172 | 0.007 | ok |
| {1, 3} | 2 | 0.222 | 0.215 | 0.007 | ok |
| {2, 3} | 2 | 0.226 | 0.220 | 0.006 | ok |
| {1, 2, 4} | 3 | 0.163 | 0.167 | 0.004 | ok |
| {1, 3, 4} | 3 | 0.166 | 0.163 | 0.003 | ok |
| {1, 2, 3} | 3 | 0.168 | 0.165 | 0.003 | ok |
| {1, 2} | 2 | 0.225 | 0.227 | 0.001 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 3s | 8224 | 8623833 | 8154057 (`birthRate`) |
| beast3 | 1s | 7816 | 22172651 | 22172651 (`posterior`) |

Run-time ratio beast3 / beast2: 0.37

