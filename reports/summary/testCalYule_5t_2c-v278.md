# Posterior comparison: testCalYule_5t_2c-v278

**Verdict: matched**

- beast2: `beast2/log/testCalYule_5t_2c-v278/rep1`, `beast2/log/testCalYule_5t_2c-v278/rep2`
- beast3: `beast3/log/testCalYule_5t_2c-v278/rep1`, `beast3/log/testCalYule_5t_2c-v278/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 355; max z: 2.925; max clade |Δp|: 0.010

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testCalYule_5t_2c-v278/rep1/test_5t_2c_i.1.log` | 5001 (4501) | 140 | 2.7.9 Prerelease | yes | 1s |  |
| beast2 | rep2 | `beast2/log/testCalYule_5t_2c-v278/rep2/test_5t_2c_i.2.log` | 5001 (4501) | 140 | 2.7.9 Prerelease | yes | 1s |  |
| beast3 | rep1 | `beast3/log/testCalYule_5t_2c-v278/rep1/test_5t_2c_i.1.log` | 5001 (4501) | 140 | 2.8.0 rc2 | yes | 0s |  |
| beast3 | rep2 | `beast3/log/testCalYule_5t_2c-v278/rep2/test_5t_2c_i.2.log` | 5001 (4501) | 140 | 2.8.0 rc2 | yes | 0s |  |

## Parameters: `test_Nt_Nc_i.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -2.058 | [-5.4, 0.6969] | 8645 (4144) | -1.981 | [-5.363, 0.6452] | 8228 (3781) | 2.92 | 100% | ok |
| `cyule` | -2.058 | [-5.4, 0.6969] | 8645 (4144) | -1.981 | [-5.363, 0.6452] | 8228 (3781) | 2.92 | 100% | ok |
| `cal` | 5.467 | [4.002, 6.83] | 748 (355) | 5.473 | [4.001, 6.83] | 904 (427) | 0.14 | 100% | ok |

### Replicate agreement (baseline noise): `test_Nt_Nc_i.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -2.073, -2.044 | 0.78 | -2.009, -1.952 | 1.49 |
| `cyule` | -2.073, -2.044 | 0.78 | -2.009, -1.952 | 1.49 |
| `cal` | 5.462, 5.472 | 0.16 | 5.431, 5.514 | 1.43 |

## Trees: `test_Nt_Nc_i.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.020, beast3 0.024.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {c, e} | 2 | 0.338 | 0.328 | 0.010 | ok |
| {c, d} | 2 | 0.331 | 0.338 | 0.008 | ok |
| {d, e} | 2 | 0.331 | 0.333 | 0.002 | ok |
| {c, d, e} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {a, b} | 2 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2s | 8645 | 12473071 | 1078826 (`cal`) |
| beast3 | 1s | 8228 | 34564038 | 3796674 (`cal`) |

Run-time ratio beast3 / beast2: 0.34

