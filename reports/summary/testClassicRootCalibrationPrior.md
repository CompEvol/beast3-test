# Posterior comparison: testClassicRootCalibrationPrior

**Verdict: not matched**

- beast2: `beast2/log/testClassicRootCalibrationPrior/rep1`, `beast2/log/testClassicRootCalibrationPrior/rep2`
- beast3: `beast3/log/testClassicRootCalibrationPrior/rep1`, `beast3/log/testClassicRootCalibrationPrior/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 6218; max z: 290.77; max clade |Δp|: 0.007

## Findings

- **FLAG** `posterior`: z = 290.77 (beast2 mean -8.929, beast3 mean -12.53)
- **FLAG** `posterior`: 95% HPD intervals overlap only 8% of the narrower one
- **NOTE** `posterior` is shifted by -3.602 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testClassicRootCalibrationPrior/rep1/classic_root_prior_oneOnX.1.log` | 10001 (9001) | 100 | 2.7.9 Prerelease | yes | 2s |  |
| beast2 | rep2 | `beast2/log/testClassicRootCalibrationPrior/rep2/classic_root_prior_oneOnX.2.log` | 10001 (9001) | 100 | 2.7.9 Prerelease | yes | 2s |  |
| beast3 | rep1 | `beast3/log/testClassicRootCalibrationPrior/rep1/classic_root_prior_oneOnX.1.log` | 10001 (9001) | 100 | 2.8.0 rc2 | yes | 1s |  |
| beast3 | rep2 | `beast3/log/testClassicRootCalibrationPrior/rep2/classic_root_prior_oneOnX.2.log` | 10001 (9001) | 100 | 2.8.0 rc2 | yes | 1s |  |

## Parameters: `classic_root_prior_oneOnX.N.log`

Constant columns (skipped): `monophyletic(all)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -8.929 | [-11.25, -7.328] | 16939 (8236) | -12.53 | [-14.88, -10.93] | 17460 (8459) | 290.77 | 8% | **z**, **HPD** |
| `yule` | -9.204 | [-11.28, -7.242] | 17041 (8498) | -9.191 | [-11.33, -7.255] | 17934 (8933) | 1.20 | 100% | ok |
| `mrca.age(all)` | 7.254 | [4.581, 10.16] | 16250 (8111) | 7.241 | [4.566, 10.16] | 17918 (8917) | 0.84 | 100% | ok |
| `birthRate` | 0.1558 | [0.01235, 0.3504] | 12859 (6218) | 0.1562 | [0.01079, 0.352] | 17827 (8826) | 0.34 | 100% | ok |

### Replicate agreement (baseline noise): `classic_root_prior_oneOnX.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -8.933, -8.924 | 0.54 | -12.53, -12.53 | 0.05 |
| `yule` | -9.212, -9.196 | 1.01 | -9.191, -9.19 | 0.09 |
| `mrca.age(all)` | 7.264, 7.244 | 0.87 | 7.241, 7.241 | 0.02 |
| `birthRate` | 0.1564, 0.1551 | 0.76 | 0.1561, 0.1563 | 0.13 |

## Trees: `classic_root_prior_oneOnX.N.trees`

18002 trees (beast2) and 18002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.013, beast3 0.012.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {1, 3} | 2 | 0.224 | 0.217 | 0.007 | ok |
| {3, 4} | 2 | 0.222 | 0.229 | 0.006 | ok |
| {1, 2} | 2 | 0.216 | 0.221 | 0.005 | ok |
| {1, 4} | 2 | 0.221 | 0.226 | 0.004 | ok |
| {2, 4} | 2 | 0.225 | 0.221 | 0.004 | ok |
| {2, 3} | 2 | 0.224 | 0.221 | 0.002 | ok |
| {2, 3, 4} | 3 | 0.169 | 0.168 | 0.001 | ok |
| {1, 2, 4} | 3 | 0.166 | 0.165 | 0.001 | ok |
| {1, 2, 3} | 3 | 0.162 | 0.161 | 0.001 | ok |
| {1, 3, 4} | 3 | 0.170 | 0.171 | 0.001 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 4s | 16939 | 15897109 | 12067562 (`birthRate`) |
| beast3 | 3s | 17460 | 22320450 | 22320450 (`posterior`) |

Run-time ratio beast3 / beast2: 0.73

