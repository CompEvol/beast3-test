# Posterior comparison: testConditionalRootCalibrationPrior

**Verdict: not matched (ESS < 200)**

- beast2: `beast2/log/testConditionalRootCalibrationPrior/rep1`, `beast2/log/testConditionalRootCalibrationPrior/rep2`
- beast3: `beast3/log/testConditionalRootCalibrationPrior/rep1`, `beast3/log/testConditionalRootCalibrationPrior/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 4; max z: 9.562; max clade |Δp|: 0.500

## Findings

- **FLAG** `posterior`: z = 9.56 (beast2 mean 21.34, beast3 mean 13.74)
- **FLAG** `posterior`: 95% HPD intervals overlap only 41% of the narrower one
- **FLAG** `cyule`: z = 9.56 (beast2 mean 21.34, beast3 mean 13.74)
- **FLAG** `cyule`: 95% HPD intervals overlap only 41% of the narrower one
- **FLAG** `birthRate`: z = 5.31 (beast2 mean 1.020e+06, beast3 mean 16577.93)
- **FLAG** clade {1, 2, 4}: p = 0.000 (beast2) vs 0.500 (beast3), |Δp| = 0.500
- **FLAG** clade {1, 3, 4}: p = 0.500 (beast2) vs 0.000 (beast3), |Δp| = 0.500
- **FLAG** clade {2, 3, 4}: p = 0.500 (beast2) vs 0.000 (beast3), |Δp| = 0.500
- **FLAG** clade {1, 2, 3}: p = 0.000 (beast2) vs 0.358 (beast3), |Δp| = 0.358
- **FLAG** clade {1, 2}: p = 0.000 (beast2) vs 0.322 (beast3), |Δp| = 0.322
- **FLAG** clade {2, 3}: p = 0.379 (beast2) vs 0.188 (beast3), |Δp| = 0.191
- **FLAG** clade {1, 4}: p = 0.404 (beast2) vs 0.236 (beast3), |Δp| = 0.168
- **FLAG** clade {3, 4}: p = 0.033 (beast2) vs 0.142 (beast3), |Δp| = 0.110
- **WARN** beast2 replicates disagree on a clade (|Δp| = 1.000): tree sampling not converged?
- **WARN** beast3 replicates disagree on a clade (|Δp| = 1.000): tree sampling not converged?
- **WARN** ESS < 200 in at least one replicate for 3 column(s): `birthRate` (beast2/beast3), `cyule` (beast2/beast3), `posterior` (beast2/beast3). README: rerun longer before comparing
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `tree.height`
- **NOTE** column map used: `reports/maps/testConditionalRootCalibrationPrior.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testConditionalRootCalibrationPrior/rep1/cond_root_prior.1.log` | 5001 (4501) | 8000 | 2.7.9 Prerelease | yes | 12s |  |
| beast2 | rep2 | `beast2/log/testConditionalRootCalibrationPrior/rep2/cond_root_prior.2.log` | 5001 (4501) | 8000 | 2.7.9 Prerelease | yes | 12s |  |
| beast3 | rep1 | `beast3/log/testConditionalRootCalibrationPrior/rep1/cond_root_prior.1.log` | 5001 (4501) | 8000 | 2.8.0 rc2 | yes | 13s |  |
| beast3 | rep2 | `beast3/log/testConditionalRootCalibrationPrior/rep2/cond_root_prior.2.log` | 5001 (4501) | 8000 | 2.8.0 rc2 | yes | 14s |  |

## Parameters: `cond_root_prior.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | 21.34 | [14.66, 25.44] | 19 (4) ⚠ | 13.74 | [9.808, 18] | 37 (9) ⚠ | 9.56 | 41% | **z**, **HPD**, low ESS |
| `cyule` | 21.34 | [14.66, 25.44] | 19 (4) ⚠ | 13.74 | [9.808, 18] | 37 (9) ⚠ | 9.56 | 41% | **z**, **HPD**, low ESS |
| `cal` | 7.543 | [4.888, 10.75] | 8757 (4322) | 7.542 | [4.761, 10.52] | 8872 (4371) | 0.08 | 98% | ok |
| `birthRate` | 1.020e+06 | [126.15, 3.076e+06] | 31 (8) ⚠ | 16577.93 | [9.451, 48138.10] | 38 (14) ⚠ | 5.31 | 100% | **z**, low ESS |
| `TreeHeight → tree.height` | 7.543 | [4.888, 10.75] | 8757 (4322) | 7.542 | [4.761, 10.52] | 8872 (4371) | 0.08 | 98% | ok |

### Replicate agreement (baseline noise): `cond_root_prior.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | 22.63, 20.04 | 1.56 | 14.02, 13.46 | 0.76 |
| `cyule` | 22.63, 20.04 | 1.56 | 14.02, 13.46 | 0.76 |
| `cal` | 7.554, 7.533 | 0.63 | 7.494, 7.589 | 2.95 |
| `birthRate` | 1.427e+06, 6.143e+05 | 2.30 | 19211.46, 13944.40 | 0.89 |
| `TreeHeight → tree.height` | 7.554, 7.533 | 0.63 | 7.494, 7.589 | 2.95 |

## Trees: `cond_root_prior.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 1.000, beast3 1.000.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {1, 2, 4} | 3 | 0.000 | 0.500 | 0.500 | **Δp** |
| {1, 3, 4} | 3 | 0.500 | 0.000 | 0.500 | **Δp** |
| {2, 3, 4} | 3 | 0.500 | 0.000 | 0.500 | **Δp** |
| {1, 2, 3} | 3 | 0.000 | 0.358 | 0.358 | **Δp** |
| {1, 2} | 2 | 0.000 | 0.322 | 0.322 | **Δp** |
| {2, 3} | 2 | 0.379 | 0.188 | 0.191 | **Δp** |
| {1, 4} | 2 | 0.404 | 0.236 | 0.168 | **Δp** |
| {3, 4} | 2 | 0.033 | 0.142 | 0.110 | **Δp** |
| {2, 4} | 2 | 0.109 | 0.159 | 0.050 | ok |
| {1, 3} | 2 | 0.063 | 0.095 | 0.032 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 23s | 19 | 2867 | 2867 (`cyule`) |
| beast3 | 27s | 37 | 4903 | 4903 (`cyule`) |

Run-time ratio beast3 / beast2: 1.17

