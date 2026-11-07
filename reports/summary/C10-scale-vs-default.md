# Posterior comparison: C10-scale-vs-default

**Verdict: matched**

- default: `beast3/log/C10/rep1`, `beast3/log/C10/rep2`
- scale: `beast3/log/C10-scale/rep1`, `beast3/log/C10-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 2235; max z: 1.938; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with scale `CN-bN-scale.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C10/rep1/C10-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 10m26s |  |
| default | rep2 | `beast3/log/C10/rep2/C10-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 10m38s |  |
| scale | rep1 | `beast3/log/C10-scale/rep1/C10-b3-scale.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 41m23s |  |
| scale | rep2 | `beast3/log/C10-scale/rep2/C10-b3-scale.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 41m32s |  |

## Parameters: `CN-bN.log / CN-bN-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -6041.04 | [-6065.30, -6016.70] | 4644 (2235) | -6040.56 | [-6065.55, -6017.66] | 5225 (2589) | 1.94 | 99% | ok |
| `likelihood` | -5445.42 | [-5462.81, -5426.88] | 5083 (2277) | -5445.23 | [-5463.35, -5428.10] | 4972 (2426) | 1.04 | 98% | ok |
| `prior` | -595.62 | [-616.76, -573.69] | 5371 (2608) | -595.33 | [-617.37, -574.01] | 5572 (2727) | 1.38 | 99% | ok |
| `treeLikelihood` | -5445.42 | [-5462.81, -5426.88] | 5083 (2277) | -5445.23 | [-5463.35, -5428.10] | 4972 (2426) | 1.04 | 98% | ok |
| `Tree.height` | 56.02 | [51.73, 60.9] | 7863 (3787) | 56.06 | [51.52, 60.97] | 7325 (3612) | 1.08 | 100% | ok |
| `Tree.treeLength` | 546.50 | [496.11, 599.90] | 5939 (2704) | 546.39 | [493.98, 599.71] | 6197 (3022) | 0.22 | 100% | ok |
| `gammaShape` | 0.9357 | [0.7149, 1.166] | 5978 (2768) | 0.9344 | [0.7193, 1.167] | 5900 (2933) | 0.60 | 100% | ok |
| `kappa` | 11.9 | [9.682, 14.21] | 6300 (3063) | 11.93 | [9.67, 14.15] | 6238 (2985) | 1.09 | 100% | ok |
| `freqParameter.1` | 0.3859 | [0.3544, 0.4166] | 6408 (2803) | 0.3863 | [0.356, 0.4172] | 6816 (3218) | 1.40 | 99% | ok |
| `freqParameter.2` | 0.3546 | [0.3258, 0.3834] | 7050 (3509) | 0.3547 | [0.3264, 0.3837] | 6238 (3103) | 0.07 | 99% | ok |
| `freqParameter.3` | 0.08265 | [0.06981, 0.09582] | 5957 (2854) | 0.08248 | [0.06951, 0.0955] | 6096 (2931) | 1.44 | 99% | ok |
| `freqParameter.4` | 0.1768 | [0.1573, 0.1975] | 7034 (3456) | 0.1766 | [0.1571, 0.1971] | 7115 (3365) | 1.31 | 99% | ok |
| `clockRate` | 0.002428 | [0.002099, 0.002777] | 9164 (4413) | 0.002429 | [0.002104, 0.002795] | 8546 (4000) | 0.42 | 99% | ok |
| `popSize` | 35.76 | [27.64, 44.42] | 7986 (3770) | 35.71 | [27.35, 44.28] | 8612 (4187) | 0.72 | 99% | ok |
| `CoalescentConstant` | -585.32 | [-606.53, -563.72] | 5379 (2612) | -585.02 | [-606.55, -563.37] | 5571 (2724) | 1.43 | 100% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -6041.28, -6040.79 | 1.36 | -6040.56, -6040.55 | 0.00 |
| `likelihood` | -5445.48, -5445.35 | 0.48 | -5445.39, -5445.06 | 1.28 |
| `prior` | -595.80, -595.44 | 1.22 | -595.16, -595.49 | 1.11 |
| `treeLikelihood` | -5445.48, -5445.35 | 0.48 | -5445.39, -5445.06 | 1.28 |
| `Tree.height` | 56.03, 56.01 | 0.53 | 56.06, 56.07 | 0.21 |
| `Tree.treeLength` | 546.81, 546.18 | 0.91 | 546.12, 546.66 | 0.79 |
| `gammaShape` | 0.9353, 0.936 | 0.22 | 0.9348, 0.934 | 0.27 |
| `kappa` | 11.91, 11.9 | 0.11 | 11.92, 11.93 | 0.42 |
| `freqParameter.1` | 0.3856, 0.3863 | 1.85 | 0.3861, 0.3866 | 1.23 |
| `freqParameter.2` | 0.3549, 0.3544 | 1.41 | 0.3546, 0.3547 | 0.05 |
| `freqParameter.3` | 0.08267, 0.08264 | 0.18 | 0.08259, 0.08237 | 1.31 |
| `freqParameter.4` | 0.1769, 0.1767 | 0.88 | 0.1767, 0.1764 | 1.09 |
| `clockRate` | 0.002427, 0.002428 | 0.36 | 0.00243, 0.002427 | 0.72 |
| `popSize` | 35.81, 35.71 | 0.98 | 35.64, 35.78 | 1.44 |
| `CoalescentConstant` | -585.51, -585.14 | 1.23 | -584.86, -585.18 | 1.07 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 21m05s | 4644 | 13220 | 13220 (`posterior`) |
| scale | 1h22m | 5225 | 3781 | 3598 (`likelihood`) |

Run-time ratio scale / default: 3.93

