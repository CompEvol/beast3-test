# Posterior comparison: testTwoCalibrationsPrior-v278

**Verdict: matched**

- beast2: `beast2/log/testTwoCalibrationsPrior-v278/rep1`, `beast2/log/testTwoCalibrationsPrior-v278/rep2`
- beast3: `beast3/log/testTwoCalibrationsPrior-v278/rep1`, `beast3/log/testTwoCalibrationsPrior-v278/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3788; max z: 1.652; max clade |Δp|: 0.002

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testTwoCalibrationsPrior-v278/rep1/test_two_calibrations.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 1s |  |
| beast2 | rep2 | `beast2/log/testTwoCalibrationsPrior-v278/rep2/test_two_calibrations.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 2s |  |
| beast3 | rep1 | `beast3/log/testTwoCalibrationsPrior-v278/rep1/test_two_calibrations.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |
| beast3 | rep2 | `beast3/log/testTwoCalibrationsPrior-v278/rep2/test_two_calibrations.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |

## Parameters: `test_two_calibrations.N.log`

Constant columns (skipped): `monophyletic(all)` = 1, `monophyletic(ingroup)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -14.22 | [-16.36, -12.88] | 8804 (4303) | -14.2 | [-16.27, -12.84] | 8844 (4343) | 1.65 | 99% | ok |
| `yule` | -10.36 | [-12.07, -9.147] | 8870 (4369) | -10.35 | [-12.02, -9.139] | 8289 (3788) | 0.43 | 100% | ok |
| `mrca.age(all)` | 8.95 | [7.586, 10] | 8413 (4138) | 8.961 | [7.608, 9.999] | 8879 (4378) | 0.98 | 100% | ok |
| `mrca.age(ingroup)` | 8.106 | [6.723, 9.556] | 8701 (4200) | 8.124 | [6.739, 9.557] | 8883 (4382) | 1.58 | 100% | ok |

### Replicate agreement (baseline noise): `test_two_calibrations.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -14.22, -14.22 | 0.10 | -14.2, -14.19 | 0.53 |
| `yule` | -10.36, -10.35 | 0.54 | -10.35, -10.36 | 0.66 |
| `mrca.age(all)` | 8.95, 8.95 | 0.00 | 8.949, 8.973 | 1.50 |
| `mrca.age(ingroup)` | 8.111, 8.101 | 0.64 | 8.122, 8.126 | 0.22 |

## Trees: `test_two_calibrations.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.003, beast3 0.019.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {1, 2} | 2 | 0.334 | 0.336 | 0.002 | ok |
| {1, 3} | 2 | 0.328 | 0.326 | 0.002 | ok |
| {2, 3} | 2 | 0.338 | 0.338 | 0.000 | ok |
| {1, 2, 3} | 3 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 3s | 8804 | 10502293 | 10035210 (`mrca.age(all)`) |
| beast3 | 1s | 8844 | 29949866 | 28072742 (`yule`) |

Run-time ratio beast3 / beast2: 0.35

