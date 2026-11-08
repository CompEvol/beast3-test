# Posterior comparison: testClassicRootCalibrationPrior-v278

**Verdict: matched**

- beast2: `beast2/log/testClassicRootCalibrationPrior-v278/rep1`, `beast2/log/testClassicRootCalibrationPrior-v278/rep2`
- beast3: `beast3/log/testClassicRootCalibrationPrior-v278/rep1`, `beast3/log/testClassicRootCalibrationPrior-v278/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3624; max z: 1.462; max clade |Δp|: 0.009

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testClassicRootCalibrationPrior-v278/rep1/classic_root_prior_oneOnX.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 1s |  |
| beast2 | rep2 | `beast2/log/testClassicRootCalibrationPrior-v278/rep2/classic_root_prior_oneOnX.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 2s |  |
| beast3 | rep1 | `beast3/log/testClassicRootCalibrationPrior-v278/rep1/classic_root_prior_oneOnX.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |
| beast3 | rep2 | `beast3/log/testClassicRootCalibrationPrior-v278/rep2/classic_root_prior_oneOnX.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 1s |  |

## Parameters: `classic_root_prior_oneOnX.N.log`

Constant columns (skipped): `monophyletic(all)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -8.926 | [-11.25, -7.328] | 9002 (4501) | -8.901 | [-11.12, -7.322] | 8109 (3832) | 1.46 | 100% | ok |
| `yule` | -9.196 | [-11.28, -7.242] | 9002 (4501) | -9.205 | [-11.16, -7.175] | 7993 (3624) | 0.58 | 98% | ok |
| `mrca.age(all)` | 7.263 | [4.519, 10.16] | 9002 (4501) | 7.259 | [4.631, 10.14] | 8743 (4297) | 0.22 | 100% | ok |
| `birthRate` | 0.1552 | [0.01275, 0.3462] | 8491 (4102) | 0.1534 | [0.009797, 0.3436] | 8583 (4203) | 1.18 | 99% | ok |

### Replicate agreement (baseline noise): `classic_root_prior_oneOnX.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -8.925, -8.928 | 0.14 | -8.881, -8.921 | 1.60 |
| `yule` | -9.195, -9.198 | 0.14 | -9.18, -9.231 | 2.16 |
| `mrca.age(all)` | 7.263, 7.264 | 0.03 | 7.257, 7.261 | 0.13 |
| `birthRate` | 0.1565, 0.1538 | 1.24 | 0.1533, 0.1535 | 0.06 |

## Trees: `classic_root_prior_oneOnX.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.017, beast3 0.019.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {1, 3, 4} | 3 | 0.169 | 0.160 | 0.009 | ok |
| {1, 2, 3} | 3 | 0.161 | 0.168 | 0.008 | ok |
| {2, 3, 4} | 3 | 0.168 | 0.173 | 0.005 | ok |
| {1, 3} | 2 | 0.225 | 0.221 | 0.005 | ok |
| {3, 4} | 2 | 0.222 | 0.220 | 0.002 | ok |
| {2, 3} | 2 | 0.225 | 0.223 | 0.002 | ok |
| {1, 4} | 2 | 0.219 | 0.220 | 0.002 | ok |
| {1, 2, 4} | 3 | 0.169 | 0.170 | 0.001 | ok |
| {1, 2} | 2 | 0.218 | 0.219 | 0.001 | ok |
| {2, 4} | 2 | 0.225 | 0.225 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 3s | 9002 | 11064254 | 10436647 (`birthRate`) |
| beast3 | 1s | 8109 | 27106253 | 26718489 (`yule`) |

Run-time ratio beast3 / beast2: 0.37

