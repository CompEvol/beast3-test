# Posterior comparison: testConditionalRootCalibrationPrior-analytic

**Verdict: not matched (ESS < 200)**

- beast2: `beast2/log/testConditionalRootCalibrationPrior-analytic/rep1`, `beast2/log/testConditionalRootCalibrationPrior-analytic/rep2`
- beast3: `beast3/log/testConditionalRootCalibrationPrior-analytic/rep1`, `beast3/log/testConditionalRootCalibrationPrior-analytic/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 9; max z: 4.859; max clade |Δp|: 0.083

## Findings

- **FLAG** `posterior`: z = 4.86 (beast2 mean -1.65, beast3 mean -2.766)
- **FLAG** `cyule`: z = 3.43 (beast2 mean 2.28, beast3 mean -0.6312)
- **WARN** beast2 replicates disagree on a clade (|Δp| = 0.178): tree sampling not converged?
- **WARN** ESS < 200 in at least one replicate for 3 column(s): `birthRate` (beast2/beast3), `cyule` (beast2/beast3), `posterior` (beast2/beast3). README: rerun longer before comparing
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `tree.height`
- **NOTE** `posterior` is shifted by -1.116 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** column map used: `reports/maps/testConditionalRootCalibrationPrior-analytic.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testConditionalRootCalibrationPrior-analytic/rep1/cond_root_prior.1.log` | 5001 (4501) | 80000 | 2.7.9 Prerelease | yes | 2m17s |  |
| beast2 | rep2 | `beast2/log/testConditionalRootCalibrationPrior-analytic/rep2/cond_root_prior.2.log` | 5001 (4501) | 80000 | 2.7.9 Prerelease | yes | 2m20s |  |
| beast3 | rep1 | `beast3/log/testConditionalRootCalibrationPrior-analytic/rep1/cond_root_prior.1.log` | 5001 (4501) | 80000 | 2.8.0 rc2 | yes | 2m11s |  |
| beast3 | rep2 | `beast3/log/testConditionalRootCalibrationPrior-analytic/rep2/cond_root_prior.2.log` | 5001 (4501) | 80000 | 2.8.0 rc2 | yes | 2m12s |  |

## Parameters: `cond_root_prior.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1.65 | [-7.956, 6.991] | 428 (13) ⚠ | -2.766 | [-9.564, 3.972] | 1647 (158) ⚠ | 4.86 | 88% | **z**, low ESS |
| `cyule` | 2.28 | [-7.68, 24.58] | 177 (9) ⚠ | -0.6312 | [-8.082, 13.76] | 314 (31) ⚠ | 3.43 | 98% | **z**, low ESS |
| `cal` | 7.54 | [4.725, 10.61] | 8679 (4178) | 7.547 | [4.828, 10.67] | 8842 (4341) | 0.29 | 99% | ok |
| `birthRate` | 1.212e+05 | [4.038e-14, 7.805e+05] | 147 (13) ⚠ | 770.89 | [2.743e-13, 3981.74] | 227 (63) ⚠ | 2.87 | 100% | low ESS |
| `TreeHeight → tree.height` | 7.54 | [4.725, 10.61] | 8679 (4178) | 7.547 | [4.828, 10.67] | 8842 (4341) | 0.29 | 99% | ok |

### Replicate agreement (baseline noise): `cond_root_prior.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -0.9726, -2.327 | 1.01 | -2.56, -2.972 | 1.35 |
| `cyule` | 4.273, 0.2867 | 1.00 | 0.3081, -1.57 | 1.39 |
| `cal` | 7.524, 7.556 | 0.98 | 7.579, 7.514 | 2.02 |
| `birthRate` | 2.334e+05, 8985.68 | 1.17 | 1299.50, 242.29 | 1.76 |
| `TreeHeight → tree.height` | 7.524, 7.556 | 0.98 | 7.579, 7.514 | 2.02 |

## Trees: `cond_root_prior.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.178, beast3 0.091.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {3, 4} | 2 | 0.298 | 0.216 | 0.083 | ok |
| {1, 2} | 2 | 0.281 | 0.203 | 0.078 | ok |
| {1, 4} | 2 | 0.215 | 0.258 | 0.044 | ok |
| {1, 2, 4} | 3 | 0.135 | 0.176 | 0.040 | ok |
| {1, 3, 4} | 3 | 0.159 | 0.189 | 0.030 | ok |
| {2, 4} | 2 | 0.194 | 0.220 | 0.026 | ok |
| {1, 3} | 2 | 0.197 | 0.216 | 0.019 | ok |
| {2, 3} | 2 | 0.210 | 0.215 | 0.005 | ok |
| {2, 3, 4} | 3 | 0.156 | 0.152 | 0.004 | ok |
| {1, 2, 3} | 3 | 0.153 | 0.155 | 0.001 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 4m37s | 428 | 5567 | 1912 (`birthRate`) |
| beast3 | 4m22s | 1647 | 22599 | 3114 (`birthRate`) |

Run-time ratio beast3 / beast2: 0.95

