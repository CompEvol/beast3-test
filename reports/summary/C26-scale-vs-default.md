# Posterior comparison: C26-scale-vs-default

**Verdict: matched**

- default: `beast3/log/C26/rep1`, `beast3/log/C26/rep2`
- scale: `beast3/log/C26-scale/rep1`, `beast3/log/C26-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 497; max z: 0.9504; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with scale `CN-bN-scale.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C26/rep1/C26-b3.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 37s |  |
| default | rep2 | `beast3/log/C26/rep2/C26-b3.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 35s |  |
| scale | rep1 | `beast3/log/C26-scale/rep1/C26-b3-scale.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 38s |  |
| scale | rep2 | `beast3/log/C26-scale/rep2/C26-b3-scale.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 37s |  |

## Parameters: `CN-bN.log / CN-bN-scale.log`

Constant columns (skipped): `likelihood` = – vs –, `treeLikelihood` = – vs –

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | 0.1213 | [-44.74, 41.18] | 10533 (4909) | 0.3952 | [-46.53, 38.73] | 10544 (5268) | 0.88 | 98% | ok |
| `prior` | 0.1213 | [-44.74, 41.18] | 10533 (4909) | 0.3952 | [-46.53, 38.73] | 10544 (5268) | 0.88 | 98% | ok |
| `Tree.height` | 1.458 | [0.1009, 4.241] | 9635 (4243) | 1.448 | [0.1111, 4.201] | 10381 (4952) | 0.27 | 100% | ok |
| `Tree.treeLength` | 13.8 | [1.131, 40.05] | 9185 (4085) | 13.73 | [1.22, 39.97] | 10114 (4972) | 0.20 | 100% | ok |
| `YuleModel` | 3.143 | [-44.68, 43.88] | 10726 (4978) | 3.412 | [-42.12, 45.49] | 10747 (5305) | 0.85 | 98% | ok |
| `birthRate` | 3.989 | [0.1012, 9.504] | 14765 (7055) | 4.02 | [0.08609, 9.548] | 14402 (7016) | 0.95 | 100% | ok |
| `gammaShape` | 1.098 | [0.1, 3.07] | 6061 (2760) | 1.101 | [0.1, 3.132] | 6833 (3289) | 0.20 | 100% | ok |
| `kappa` | 5.911 | [0.02635, 20.61] | 5259 (2515) | 5.978 | [0.05107, 21.54] | 5598 (2724) | 0.31 | 100% | ok |
| `freqParameter.1` | 0.2459 | [0.04899, 0.4437] | 1455 (514) | 0.247 | [0.05107, 0.4399] | 1126 (497) | 0.26 | 100% | ok |
| `freqParameter.2` | 0.2518 | [0.07297, 0.4617] | 1552 (587) | 0.253 | [0.07071, 0.4662] | 1158 (521) | 0.29 | 100% | ok |
| `freqParameter.3` | 0.25 | [0.06106, 0.4598] | 1448 (671) | 0.2479 | [0.06625, 0.4488] | 1244 (602) | 0.53 | 100% | ok |
| `freqParameter.4` | 0.2523 | [0.0534, 0.449] | 1434 (587) | 0.2522 | [0.05685, 0.447] | 1203 (597) | 0.04 | 100% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | 0.04411, 0.1985 | 0.35 | 0.5819, 0.2084 | 0.85 |
| `prior` | 0.04411, 0.1985 | 0.35 | 0.5819, 0.2084 | 0.85 |
| `Tree.height` | 1.502, 1.414 | 1.54 | 1.429, 1.466 | 0.71 |
| `Tree.treeLength` | 14.18, 13.43 | 1.39 | 13.55, 13.91 | 0.72 |
| `YuleModel` | 3.097, 3.19 | 0.21 | 3.651, 3.172 | 1.08 |
| `birthRate` | 4.005, 3.973 | 0.69 | 4.04, 4.001 | 0.83 |
| `gammaShape` | 1.101, 1.095 | 0.24 | 1.108, 1.094 | 0.59 |
| `kappa` | 6.081, 5.741 | 1.06 | 6.087, 5.868 | 0.73 |
| `freqParameter.1` | 0.2457, 0.2461 | 0.07 | 0.2472, 0.2468 | 0.06 |
| `freqParameter.2` | 0.2464, 0.2571 | 1.95 | 0.2522, 0.2537 | 0.25 |
| `freqParameter.3` | 0.2518, 0.2483 | 0.61 | 0.2516, 0.2442 | 1.26 |
| `freqParameter.4` | 0.2561, 0.2485 | 1.33 | 0.249, 0.2553 | 1.04 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 1m12s | 10533 | 527419 | 71785 (`freqParameter.4`) |
| scale | 1m15s | 10544 | 504446 | 53856 (`freqParameter.1`) |

Run-time ratio scale / default: 1.05

