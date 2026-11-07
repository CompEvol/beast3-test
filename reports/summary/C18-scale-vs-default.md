# Posterior comparison: C18-scale-vs-default

**Verdict: matched**

- default: `beast3/log/C18/rep1`, `beast3/log/C18/rep2`
- scale: `beast3/log/C18-scale/rep1`, `beast3/log/C18-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1153; max z: 2.202; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with scale `CN-bN-scale.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C18/rep1/C18-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 20m24s |  |
| default | rep2 | `beast3/log/C18/rep2/C18-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 20m24s |  |
| scale | rep1 | `beast3/log/C18-scale/rep1/C18-b3-scale.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 1h16m |  |
| scale | rep2 | `beast3/log/C18-scale/rep2/C18-b3-scale.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 1h16m |  |

## Parameters: `CN-bN.log / CN-bN-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1924.50 | [-1929.62, -1920.19] | 13605 (6109) | -1924.53 | [-1929.66, -1920.13] | 12255 (5348) | 0.94 | 100% | ok |
| `likelihood` | -1925.91 | [-1930.53, -1921.98] | 12573 (5712) | -1925.91 | [-1930.44, -1921.90] | 11821 (5564) | 0.12 | 99% | ok |
| `prior` | 1.414 | [-0.6846, 3.426] | 12620 (6281) | 1.388 | [-0.6867, 3.484] | 13542 (6462) | 2.01 | 100% | ok |
| `treeLikelihood` | -1925.91 | [-1930.53, -1921.98] | 12573 (5712) | -1925.91 | [-1930.44, -1921.90] | 11821 (5564) | 0.12 | 99% | ok |
| `Tree.height` | 0.2455 | [0.1975, 0.2996] | 16407 (8054) | 0.2458 | [0.1973, 0.2979] | 16260 (7395) | 1.19 | 100% | ok |
| `Tree.treeLength` | 1.204 | [0.9884, 1.437] | 15537 (7329) | 1.205 | [0.9878, 1.427] | 14595 (6550) | 1.03 | 100% | ok |
| `YuleModel` | 8.647 | [6.504, 10.84] | 16218 (7553) | 8.619 | [6.345, 10.69] | 15869 (7818) | 2.20 | 97% | ok |
| `birthRate` | 7.496 | [2.899, 12.51] | 17572 (8571) | 7.468 | [2.806, 12.49] | 17586 (8585) | 1.01 | 100% | ok |
| `gammaShape` | 0.6771 | [0.421, 0.9727] | 2553 (1153) | 0.6817 | [0.425, 0.9651] | 2668 (1330) | 1.13 | 100% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -1924.47, -1924.53 | 1.43 | -1924.52, -1924.53 | 0.36 |
| `likelihood` | -1925.88, -1925.94 | 1.47 | -1925.92, -1925.91 | 0.08 |
| `prior` | 1.415, 1.413 | 0.12 | 1.398, 1.378 | 1.08 |
| `treeLikelihood` | -1925.88, -1925.94 | 1.47 | -1925.92, -1925.91 | 0.08 |
| `Tree.height` | 0.2458, 0.2452 | 1.31 | 0.2457, 0.2459 | 0.42 |
| `Tree.treeLength` | 1.205, 1.203 | 1.19 | 1.205, 1.205 | 0.39 |
| `YuleModel` | 8.642, 8.651 | 0.50 | 8.627, 8.611 | 0.93 |
| `birthRate` | 7.466, 7.527 | 1.56 | 7.456, 7.481 | 0.64 |
| `gammaShape` | 0.6756, 0.6787 | 0.55 | 0.6813, 0.6821 | 0.15 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 40m48s | 13605 | 20008 | 3754 (`gammaShape`) |
| scale | 2h33m | 12255 | 4786 | 1042 (`gammaShape`) |

Run-time ratio scale / default: 3.77

