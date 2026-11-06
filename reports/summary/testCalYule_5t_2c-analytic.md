# Posterior comparison: testCalYule_5t_2c-analytic

**Verdict: matched**

- beast2: `beast2/log/testCalYule_5t_2c-analytic/rep11`, `beast2/log/testCalYule_5t_2c-analytic/rep12`, `beast2/log/testCalYule_5t_2c-analytic/rep13`, `beast2/log/testCalYule_5t_2c-analytic/rep14`
- beast3: `beast3/log/testCalYule_5t_2c-analytic/rep11`, `beast3/log/testCalYule_5t_2c-analytic/rep12`, `beast3/log/testCalYule_5t_2c-analytic/rep13`, `beast3/log/testCalYule_5t_2c-analytic/rep14`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 4089; max z: 1.054; max clade |Δp|: 0.006

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep11 | `beast2/log/testCalYule_5t_2c-analytic/rep11/test_5t_2c_i.11.log` | 5001 (4501) | 28000 | 2.7.9 Prerelease | yes | 47s |  |
| beast2 | rep12 | `beast2/log/testCalYule_5t_2c-analytic/rep12/test_5t_2c_i.12.log` | 5001 (4501) | 28000 | 2.7.9 Prerelease | yes | 48s |  |
| beast2 | rep13 | `beast2/log/testCalYule_5t_2c-analytic/rep13/test_5t_2c_i.13.log` | 5001 (4501) | 28000 | 2.7.9 Prerelease | yes | 47s |  |
| beast2 | rep14 | `beast2/log/testCalYule_5t_2c-analytic/rep14/test_5t_2c_i.14.log` | 5001 (4501) | 28000 | 2.7.9 Prerelease | yes | 47s |  |
| beast3 | rep11 | `beast3/log/testCalYule_5t_2c-analytic/rep11/test_5t_2c_i.11.log` | 5001 (4501) | 28000 | 2.8.0 rc2 | yes | 39s |  |
| beast3 | rep12 | `beast3/log/testCalYule_5t_2c-analytic/rep12/test_5t_2c_i.12.log` | 5001 (4501) | 28000 | 2.8.0 rc2 | yes | 38s |  |
| beast3 | rep13 | `beast3/log/testCalYule_5t_2c-analytic/rep13/test_5t_2c_i.13.log` | 5001 (4501) | 28000 | 2.8.0 rc2 | yes | 37s |  |
| beast3 | rep14 | `beast3/log/testCalYule_5t_2c-analytic/rep14/test_5t_2c_i.14.log` | 5001 (4501) | 28000 | 2.8.0 rc2 | yes | 38s |  |

## Parameters: `test_Nt_Nc_i.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -2.005 | [-5.564, 0.6112] | 17874 (4408) | -2.025 | [-5.378, 0.6636] | 17779 (4328) | 1.05 | 99% | ok |
| `cyule` | -2.005 | [-5.564, 0.6112] | 17874 (4408) | -2.025 | [-5.378, 0.6636] | 17779 (4328) | 1.05 | 99% | ok |
| `cal` | 5.5 | [4.028, 6.871] | 17669 (4328) | 5.496 | [4.116, 6.957] | 17415 (4089) | 0.46 | 97% | ok |

### Replicate agreement (baseline noise): `test_Nt_Nc_i.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -2.023, -2.047, -1.969, -1.982 | 2.12 | -2.03, -2.005, -2.05, -2.016 | 1.21 |
| `cyule` | -2.023, -2.047, -1.969, -1.982 | 2.12 | -2.03, -2.005, -2.05, -2.016 | 1.21 |
| `cal` | 5.492, 5.501, 5.508, 5.5 | 0.91 | 5.493, 5.505, 5.502, 5.484 | 1.09 |

## Trees: `test_Nt_Nc_i.N.trees`

18004 trees (beast2) and 18004 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.014, beast3 0.012.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {c, d} | 2 | 0.334 | 0.328 | 0.006 | ok |
| {c, e} | 2 | 0.333 | 0.337 | 0.004 | ok |
| {d, e} | 2 | 0.333 | 0.335 | 0.003 | ok |
| {c, d, e} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {a, b} | 2 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 3m09s | 17874 | 339785 | 335894 (`cal`) |
| beast3 | 2m33s | 17779 | 419436 | 410842 (`cal`) |

Run-time ratio beast3 / beast2: 0.81

