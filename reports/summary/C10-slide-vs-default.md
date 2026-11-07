# Posterior comparison: C10-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C10/rep1`, `beast3/log/C10/rep2`
- slide: `beast3/log/C10-slide/rep1`, `beast3/log/C10-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 2229; max z: 1.847; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with slide `CN-bN-slide.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C10/rep1/C10-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 10m26s |  |
| default | rep2 | `beast3/log/C10/rep2/C10-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 10m38s |  |
| slide | rep1 | `beast3/log/C10-slide/rep1/C10-b3-slide.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 40m36s |  |
| slide | rep2 | `beast3/log/C10-slide/rep2/C10-b3-slide.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 40m29s |  |

## Parameters: `CN-bN.log / CN-bN-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -6041.04 | [-6065.30, -6016.70] | 4644 (2235) | -6040.69 | [-6063.90, -6017.00] | 5528 (2577) | 1.42 | 100% | ok |
| `likelihood` | -5445.42 | [-5462.81, -5426.88] | 5083 (2277) | -5445.29 | [-5463.13, -5427.74] | 5643 (2229) | 0.72 | 99% | ok |
| `prior` | -595.62 | [-616.76, -573.69] | 5371 (2608) | -595.40 | [-616.82, -573.77] | 4910 (2363) | 1.00 | 100% | ok |
| `treeLikelihood` | -5445.42 | [-5462.81, -5426.88] | 5083 (2277) | -5445.29 | [-5463.13, -5427.74] | 5643 (2229) | 0.72 | 99% | ok |
| `Tree.height` | 56.02 | [51.73, 60.9] | 7863 (3787) | 56.07 | [51.61, 60.94] | 7597 (3663) | 1.40 | 100% | ok |
| `Tree.treeLength` | 546.50 | [496.11, 599.90] | 5939 (2704) | 546.45 | [495.26, 600.39] | 5617 (2438) | 0.09 | 100% | ok |
| `gammaShape` | 0.9357 | [0.7149, 1.166] | 5978 (2768) | 0.9333 | [0.7218, 1.168] | 5849 (2802) | 1.11 | 99% | ok |
| `kappa` | 11.9 | [9.682, 14.21] | 6300 (3063) | 11.92 | [9.718, 14.19] | 5716 (2695) | 0.98 | 100% | ok |
| `freqParameter.1` | 0.3859 | [0.3544, 0.4166] | 6408 (2803) | 0.3861 | [0.3547, 0.417] | 6675 (3270) | 0.68 | 100% | ok |
| `freqParameter.2` | 0.3546 | [0.3258, 0.3834] | 7050 (3509) | 0.3549 | [0.3268, 0.3837] | 7296 (3531) | 1.21 | 99% | ok |
| `freqParameter.3` | 0.08265 | [0.06981, 0.09582] | 5957 (2854) | 0.08242 | [0.06942, 0.09554] | 5690 (2788) | 1.85 | 99% | ok |
| `freqParameter.4` | 0.1768 | [0.1573, 0.1975] | 7034 (3456) | 0.1765 | [0.1565, 0.1971] | 6902 (3407) | 1.46 | 99% | ok |
| `clockRate` | 0.002428 | [0.002099, 0.002777] | 9164 (4413) | 0.00243 | [0.002108, 0.002787] | 9458 (4586) | 0.99 | 99% | ok |
| `popSize` | 35.76 | [27.64, 44.42] | 7986 (3770) | 35.73 | [27.52, 44.58] | 7600 (3515) | 0.43 | 100% | ok |
| `CoalescentConstant` | -585.32 | [-606.53, -563.72] | 5379 (2612) | -585.10 | [-606.18, -563.49] | 4841 (2293) | 1.05 | 99% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -6041.28, -6040.79 | 1.36 | -6040.45, -6040.93 | 1.47 |
| `likelihood` | -5445.48, -5445.35 | 0.48 | -5444.92, -5445.66 | 2.99 |
| `prior` | -595.80, -595.44 | 1.22 | -595.53, -595.27 | 0.84 |
| `treeLikelihood` | -5445.48, -5445.35 | 0.48 | -5444.92, -5445.66 | 2.99 |
| `Tree.height` | 56.03, 56.01 | 0.53 | 56.06, 56.09 | 0.47 |
| `Tree.treeLength` | 546.81, 546.18 | 0.91 | 546.67, 546.22 | 0.62 |
| `gammaShape` | 0.9353, 0.936 | 0.22 | 0.9346, 0.932 | 0.83 |
| `kappa` | 11.91, 11.9 | 0.11 | 11.91, 11.94 | 0.86 |
| `freqParameter.1` | 0.3856, 0.3863 | 1.85 | 0.3857, 0.3866 | 2.29 |
| `freqParameter.2` | 0.3549, 0.3544 | 1.41 | 0.3551, 0.3547 | 1.15 |
| `freqParameter.3` | 0.08267, 0.08264 | 0.18 | 0.08243, 0.08242 | 0.02 |
| `freqParameter.4` | 0.1769, 0.1767 | 0.88 | 0.1768, 0.1763 | 1.98 |
| `clockRate` | 0.002427, 0.002428 | 0.36 | 0.002429, 0.002431 | 0.59 |
| `popSize` | 35.81, 35.71 | 0.98 | 35.77, 35.69 | 0.79 |
| `CoalescentConstant` | -585.51, -585.14 | 1.23 | -585.23, -584.96 | 0.85 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 21m05s | 4644 | 13220 | 13220 (`posterior`) |
| slide | 1h21m | 5528 | 4091 | 3582 (`CoalescentConstant`) |

Run-time ratio slide / default: 3.85

