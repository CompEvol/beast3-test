# Posterior comparison: testTwoCalibrationsPrior

**Verdict: matched**

- beast2: `beast2/log/testTwoCalibrationsPrior/rep1`, `beast2/log/testTwoCalibrationsPrior/rep2`
- beast3: `beast3/log/testTwoCalibrationsPrior/rep1`, `beast3/log/testTwoCalibrationsPrior/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3725; max z: 1.625; max clade |Δp|: 0.004

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testTwoCalibrationsPrior/rep1/test_two_calibrations.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 2s |  |
| beast2 | rep2 | `beast2/log/testTwoCalibrationsPrior/rep2/test_two_calibrations.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 2s |  |
| beast3 | rep1 | `beast3/log/testTwoCalibrationsPrior/rep1/test_two_calibrations.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |
| beast3 | rep2 | `beast3/log/testTwoCalibrationsPrior/rep2/test_two_calibrations.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |

## Parameters: `test_two_calibrations.N.log`

Constant columns (skipped): `monophyletic(all)` = 1, `monophyletic(ingroup)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -14.8 | [-16.92, -13.51] | 8798 (4387) | -14.8 | [-16.86, -13.52] | 8188 (4088) | 0.16 | 100% | ok |
| `yule` | -10.38 | [-11.99, -9.162] | 9002 (4501) | -10.36 | [-11.98, -9.163] | 8864 (4363) | 1.62 | 100% | ok |
| `mrca.age(all)` | 9.017 | [7.677, 10] | 7511 (3725) | 9.003 | [7.671, 9.999] | 8597 (4289) | 1.26 | 100% | ok |
| `mrca.age(ingroup)` | 8.156 | [6.771, 9.561] | 8696 (4286) | 8.143 | [6.776, 9.558] | 9002 (4501) | 1.17 | 100% | ok |

### Replicate agreement (baseline noise): `test_two_calibrations.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -14.79, -14.8 | 0.63 | -14.8, -14.79 | 0.37 |
| `yule` | -10.38, -10.38 | 0.16 | -10.37, -10.35 | 1.06 |
| `mrca.age(all)` | 9.022, 9.013 | 0.55 | 8.993, 9.013 | 1.29 |
| `mrca.age(ingroup)` | 8.159, 8.152 | 0.42 | 8.146, 8.139 | 0.43 |

## Trees: `test_two_calibrations.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.016, beast3 0.014.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {2, 3} | 2 | 0.331 | 0.326 | 0.004 | ok |
| {1, 3} | 2 | 0.341 | 0.344 | 0.003 | ok |
| {1, 2} | 2 | 0.329 | 0.330 | 0.001 | ok |
| {1, 2, 3} | 3 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 4s | 8798 | 8235588 | 7030782 (`mrca.age(all)`) |
| beast3 | 1s | 8188 | 19929136 | 19929136 (`posterior`) |

Run-time ratio beast3 / beast2: 0.38

