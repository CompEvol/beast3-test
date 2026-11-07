# Posterior comparison: C01-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C01/rep1`, `beast3/log/C01/rep2`
- slide: `beast3/log/C01-slide/rep1`, `beast3/log/C01-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1663; max z: 2.061; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with slide `CN-bN-slide.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C01/rep1/C01-b3.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 48s |  |
| default | rep2 | `beast3/log/C01/rep2/C01-b3.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 48s |  |
| slide | rep1 | `beast3/log/C01-slide/rep1/C01-b3-slide.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 2m39s |  |
| slide | rep2 | `beast3/log/C01-slide/rep2/C01-b3-slide.log` | 3001 (2701) | 1000 | 2.8.0 rc2 | yes | 2m38s |  |

## Parameters: `CN-bN.log / CN-bN-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23364.67 | [-23372.63, -23356.96] | 3630 (1710) | -23364.49 | [-23372.63, -23357.09] | 4395 (2115) | 2.06 | 100% | ok |
| `likelihood` | -23386.65 | [-23394.44, -23379.05] | 3494 (1663) | -23386.48 | [-23394.21, -23378.97] | 4330 (2070) | 1.85 | 99% | ok |
| `prior` | 21.97 | [20.33, 23.25] | 4963 (2381) | 21.99 | [20.52, 23.39] | 5402 (2701) | 1.29 | 95% | ok |
| `treeLikelihood` | -23386.65 | [-23394.44, -23379.05] | 3494 (1663) | -23386.48 | [-23394.21, -23378.97] | 4330 (2070) | 1.85 | 99% | ok |
| `Tree.height` | 0.1926 | [0.1851, 0.2008] | 4700 (2282) | 0.1926 | [0.1847, 0.2004] | 5228 (2613) | 0.06 | 98% | ok |
| `Tree.treeLength` | 3.632 | [3.521, 3.742] | 5256 (2555) | 3.63 | [3.522, 3.732] | 5402 (2701) | 1.67 | 100% | ok |
| `YuleModel` | 28.7 | [26.98, 30] | 4989 (2407) | 28.72 | [27.19, 30.07] | 5402 (2701) | 1.08 | 98% | ok |
| `birthRate` | 7.722 | [4.98, 10.54] | 5234 (2533) | 7.698 | [5.097, 10.54] | 5307 (2606) | 0.86 | 100% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -23364.62, -23364.73 | 0.74 | -23364.65, -23364.32 | 2.64 |
| `likelihood` | -23386.60, -23386.69 | 0.67 | -23386.64, -23386.32 | 2.66 |
| `prior` | 21.98, 21.97 | 0.44 | 21.99, 21.99 | 0.01 |
| `treeLikelihood` | -23386.60, -23386.69 | 0.67 | -23386.64, -23386.32 | 2.66 |
| `Tree.height` | 0.1926, 0.1926 | 0.18 | 0.1926, 0.1926 | 0.38 |
| `Tree.treeLength` | 3.632, 3.631 | 0.44 | 3.63, 3.63 | 0.43 |
| `YuleModel` | 28.71, 28.7 | 0.28 | 28.72, 28.72 | 0.03 |
| `birthRate` | 7.707, 7.737 | 0.76 | 7.701, 7.695 | 0.17 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 1m35s | 3630 | 136845 | 131711 (`likelihood`) |
| slide | 5m17s | 4395 | 49941 | 49194 (`likelihood`) |

Run-time ratio slide / default: 3.32

