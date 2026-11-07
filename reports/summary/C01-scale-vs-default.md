# Posterior comparison: C01-scale-vs-default

**Verdict: matched**

- default: `beast3/log/C01/rep1`, `beast3/log/C01/rep2`
- scale: `beast3/log/C01-scale/rep1`, `beast3/log/C01-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1663; max z: 2.857; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with scale `CN-bN-scale.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C01/rep1/C01-b3.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 48s |  |
| default | rep2 | `beast3/log/C01/rep2/C01-b3.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 48s |  |
| scale | rep1 | `beast3/log/C01-scale/rep1/C01-b3-scale.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 2m34s |  |
| scale | rep2 | `beast3/log/C01-scale/rep2/C01-b3-scale.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 2m32s |  |

## Parameters: `CN-bN.log / CN-bN-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23364.67 | [-23372.63, -23356.96] | 3630 (1710) | -23364.44 | [-23372.41, -23357.06] | 4429 (2191) | 2.61 | 100% | ok |
| `likelihood` | -23386.65 | [-23394.44, -23379.05] | 3494 (1663) | -23386.39 | [-23394.21, -23379.15] | 4503 (2177) | 2.86 | 100% | ok |
| `prior` | 21.97 | [20.33, 23.25] | 4963 (2381) | 21.95 | [20.31, 23.27] | 4769 (2353) | 1.16 | 100% | ok |
| `treeLikelihood` | -23386.65 | [-23394.44, -23379.05] | 3494 (1663) | -23386.39 | [-23394.21, -23379.15] | 4503 (2177) | 2.86 | 100% | ok |
| `Tree.height` | 0.1926 | [0.1851, 0.2008] | 4700 (2282) | 0.1926 | [0.1847, 0.2004] | 4577 (2192) | 0.01 | 98% | ok |
| `Tree.treeLength` | 3.632 | [3.521, 3.742] | 5256 (2555) | 3.631 | [3.526, 3.736] | 5170 (2543) | 0.76 | 100% | ok |
| `YuleModel` | 28.7 | [26.98, 30] | 4989 (2407) | 28.68 | [27.04, 30.08] | 5086 (2385) | 1.32 | 98% | ok |
| `birthRate` | 7.722 | [4.98, 10.54] | 5234 (2533) | 7.711 | [4.947, 10.63] | 5402 (2701) | 0.38 | 100% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -23364.62, -23364.73 | 0.74 | -23364.45, -23364.42 | 0.18 |
| `likelihood` | -23386.60, -23386.69 | 0.67 | -23386.39, -23386.39 | 0.00 |
| `prior` | 21.98, 21.97 | 0.44 | 21.94, 21.97 | 0.92 |
| `treeLikelihood` | -23386.60, -23386.69 | 0.67 | -23386.39, -23386.39 | 0.00 |
| `Tree.height` | 0.1926, 0.1926 | 0.18 | 0.1926, 0.1926 | 0.34 |
| `Tree.treeLength` | 3.632, 3.631 | 0.44 | 3.63, 3.632 | 0.86 |
| `YuleModel` | 28.71, 28.7 | 0.28 | 28.67, 28.69 | 0.53 |
| `birthRate` | 7.707, 7.737 | 0.76 | 7.749, 7.674 | 1.87 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 1m35s | 3630 | 136845 | 131711 (`likelihood`) |
| scale | 5m06s | 4429 | 52138 | 52138 (`posterior`) |

Run-time ratio scale / default: 3.20

