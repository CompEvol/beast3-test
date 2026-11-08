# Posterior comparison: bitflip

**Verdict: matched**

- beast2: `beast2/log/bitflip/rep1`, `beast2/log/bitflip/rep2`
- beast3: `beast3/log/bitflip/rep1`, `beast3/log/bitflip/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3510; max z: 0; max clade |Δp|: –

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/bitflip/rep1/bitflip.log` | 5001 (4501) | 20 | 2.7.9 Prerelease | yes | 0s |  |
| beast2 | rep2 | `beast2/log/bitflip/rep2/bitflip.log` | 5001 (4501) | 20 | 2.7.9 Prerelease | yes | 0s |  |
| beast3 | rep1 | `beast3/log/bitflip/rep1/bitflip.log` | 5001 (4501) | 20 | 2.8.0 rc2 | yes | 0s |  |
| beast3 | rep2 | `beast3/log/bitflip/rep2/bitflip.log` | 5001 (4501) | 20 | 2.8.0 rc2 | yes | 0s |  |

## Parameters: `bitflip.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `indicators.1` | 0.4949 | [0, 1] | 7928 (3856) | 0.4949 | [0, 1] | 7928 (3856) | 0.00 | 100% | ok |
| `indicators.2` | 0.4931 | [0, 1] | 8164 (3962) | 0.4931 | [0, 1] | 8164 (3962) | 0.00 | 100% | ok |
| `indicators.3` | 0.4913 | [0, 1] | 8217 (4069) | 0.4913 | [0, 1] | 8217 (4069) | 0.00 | 100% | ok |
| `indicators.4` | 0.508 | [0, 1] | 7366 (3510) | 0.508 | [0, 1] | 7366 (3510) | 0.00 | 100% | ok |
| `indicators.5` | 0.5013 | [0, 1] | 7947 (3874) | 0.5013 | [0, 1] | 7947 (3874) | 0.00 | 100% | ok |

### Replicate agreement (baseline noise): `bitflip.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `indicators.1` | 0.4892, 0.5006 | 1.01 | 0.4892, 0.5006 | 1.01 |
| `indicators.2` | 0.4908, 0.4954 | 0.42 | 0.4908, 0.4954 | 0.42 |
| `indicators.3` | 0.4923, 0.4903 | 0.18 | 0.4923, 0.4903 | 0.18 |
| `indicators.4` | 0.5121, 0.5039 | 0.70 | 0.5121, 0.5039 | 0.70 |
| `indicators.5` | 0.5081, 0.4946 | 1.21 | 0.5081, 0.4946 | 1.21 |

## Speed

| Version | Total run time | Combined ESS of `indicators.1` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 1s | 7928 | 50697149 | 47099418 (`indicators.4`) |
| beast3 | 0s | 7928 | 232052803 | 215585139 (`indicators.4`) |

Run-time ratio beast3 / beast2: 0.22

