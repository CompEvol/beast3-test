# Posterior comparison: testTwoCalibrationsPrior

**Verdict: matched**

- beast2: `beast2/log/testTwoCalibrationsPrior/rep1`, `beast2/log/testTwoCalibrationsPrior/rep2`
- beast3: `beast3/log/testTwoCalibrationsPrior/rep1`, `beast3/log/testTwoCalibrationsPrior/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 6215; max z: 0.6876; max clade |Δp|: 0.003

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testTwoCalibrationsPrior/rep1/test_two_calibrations.1.log` | 10001 (9001) | 100 | 2.7.9 Prerelease | yes | 2s |  |
| beast2 | rep2 | `beast2/log/testTwoCalibrationsPrior/rep2/test_two_calibrations.2.log` | 10001 (9001) | 100 | 2.7.9 Prerelease | yes | 2s |  |
| beast3 | rep1 | `beast3/log/testTwoCalibrationsPrior/rep1/test_two_calibrations.1.log` | 10001 (9001) | 100 | 2.8.0 rc2 | yes | 1s |  |
| beast3 | rep2 | `beast3/log/testTwoCalibrationsPrior/rep2/test_two_calibrations.2.log` | 10001 (9001) | 100 | 2.8.0 rc2 | yes | 1s |  |

## Parameters: `test_two_calibrations.N.log`

Constant columns (skipped): `monophyletic(all)` = 1, `monophyletic(ingroup)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -14.21 | [-16.33, -12.87] | 14164 (6925) | -14.21 | [-16.31, -12.84] | 16686 (8119) | 0.25 | 100% | ok |
| `yule` | -10.35 | [-12.04, -9.112] | 15813 (7482) | -10.36 | [-12.04, -9.1] | 17427 (8426) | 0.54 | 100% | ok |
| `mrca.age(all)` | 8.955 | [7.6, 10] | 12938 (6215) | 8.961 | [7.597, 10] | 15525 (7377) | 0.69 | 100% | ok |
| `mrca.age(ingroup)` | 8.11 | [6.746, 9.556] | 13493 (6343) | 8.11 | [6.726, 9.581] | 15752 (7518) | 0.02 | 100% | ok |

### Replicate agreement (baseline noise): `test_two_calibrations.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -14.2, -14.22 | 0.76 | -14.22, -14.21 | 0.64 |
| `yule` | -10.35, -10.35 | 0.12 | -10.35, -10.36 | 0.76 |
| `mrca.age(all)` | 8.958, 8.951 | 0.61 | 8.952, 8.969 | 1.43 |
| `mrca.age(ingroup)` | 8.12, 8.101 | 1.47 | 8.102, 8.119 | 1.50 |

## Trees: `test_two_calibrations.N.trees`

18002 trees (beast2) and 18002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.003, beast3 0.002.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {2, 3} | 2 | 0.333 | 0.336 | 0.003 | ok |
| {1, 3} | 2 | 0.335 | 0.333 | 0.002 | ok |
| {1, 2} | 2 | 0.332 | 0.332 | 0.000 | ok |
| {1, 2, 3} | 3 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 4s | 14164 | 13347880 | 12192472 (`mrca.age(all)`) |
| beast3 | 3s | 16686 | 22322857 | 20768624 (`mrca.age(all)`) |

Run-time ratio beast3 / beast2: 0.70

