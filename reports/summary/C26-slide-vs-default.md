# Posterior comparison: C26-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C26/rep1`, `beast3/log/C26/rep2`
- slide: `beast3/log/C26-slide/rep1`, `beast3/log/C26-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 371; max z: 1.156; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with slide `CN-bN-slide.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C26/rep1/C26-b3.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 37s |  |
| default | rep2 | `beast3/log/C26/rep2/C26-b3.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 35s |  |
| slide | rep1 | `beast3/log/C26-slide/rep1/C26-b3-slide.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 39s |  |
| slide | rep2 | `beast3/log/C26-slide/rep2/C26-b3-slide.log` | 20001 (18001) | 1000 | 2.8.0 rc2 | yes | 38s |  |

## Parameters: `CN-bN.log / CN-bN-slide.log`

Constant columns (skipped): `likelihood` = – vs –, `treeLikelihood` = – vs –

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | 0.1213 | [-44.74, 41.18] | 10533 (4909) | 0.3086 | [-44.47, 41.25] | 9701 (4460) | 0.59 | 100% | ok |
| `prior` | 0.1213 | [-44.74, 41.18] | 10533 (4909) | 0.3086 | [-44.47, 41.25] | 9701 (4460) | 0.59 | 100% | ok |
| `Tree.height` | 1.458 | [0.1009, 4.241] | 9635 (4243) | 1.454 | [0.1105, 4.207] | 10554 (5189) | 0.10 | 100% | ok |
| `Tree.treeLength` | 13.8 | [1.131, 40.05] | 9185 (4085) | 13.75 | [1.09, 39.48] | 10167 (4807) | 0.16 | 100% | ok |
| `YuleModel` | 3.143 | [-44.68, 43.88] | 10726 (4978) | 3.316 | [-42.39, 45.57] | 9946 (4567) | 0.54 | 98% | ok |
| `birthRate` | 3.989 | [0.1012, 9.504] | 14765 (7055) | 4.003 | [0.09168, 9.519] | 14251 (6957) | 0.43 | 100% | ok |
| `gammaShape` | 1.098 | [0.1, 3.07] | 6061 (2760) | 1.105 | [0.1, 3.107] | 6190 (2924) | 0.38 | 100% | ok |
| `kappa` | 5.911 | [0.02635, 20.61] | 5259 (2515) | 5.932 | [0.03307, 21.14] | 6144 (2929) | 0.10 | 100% | ok |
| `freqParameter.1` | 0.2459 | [0.04899, 0.4437] | 1455 (514) | 0.2488 | [0.05679, 0.4471] | 1026 (444) | 0.69 | 99% | ok |
| `freqParameter.2` | 0.2518 | [0.07297, 0.4617] | 1552 (587) | 0.2504 | [0.05848, 0.4573] | 992 (371) | 0.31 | 99% | ok |
| `freqParameter.3` | 0.25 | [0.06106, 0.4598] | 1448 (671) | 0.2532 | [0.06937, 0.4619] | 1073 (465) | 0.75 | 99% | ok |
| `freqParameter.4` | 0.2523 | [0.0534, 0.449] | 1434 (587) | 0.2475 | [0.07114, 0.4576] | 1168 (554) | 1.16 | 98% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | 0.04411, 0.1985 | 0.35 | 0.2946, 0.3226 | 0.06 |
| `prior` | 0.04411, 0.1985 | 0.35 | 0.2946, 0.3226 | 0.06 |
| `Tree.height` | 1.502, 1.414 | 1.54 | 1.453, 1.456 | 0.06 |
| `Tree.treeLength` | 14.18, 13.43 | 1.39 | 13.71, 13.78 | 0.14 |
| `YuleModel` | 3.097, 3.19 | 0.21 | 3.327, 3.306 | 0.05 |
| `birthRate` | 4.005, 3.973 | 0.69 | 4.008, 3.999 | 0.18 |
| `gammaShape` | 1.101, 1.095 | 0.24 | 1.119, 1.09 | 1.14 |
| `kappa` | 6.081, 5.741 | 1.06 | 6.015, 5.849 | 0.57 |
| `freqParameter.1` | 0.2457, 0.2461 | 0.07 | 0.2479, 0.2498 | 0.29 |
| `freqParameter.2` | 0.2464, 0.2571 | 1.95 | 0.25, 0.2509 | 0.13 |
| `freqParameter.3` | 0.2518, 0.2483 | 0.61 | 0.2542, 0.2522 | 0.31 |
| `freqParameter.4` | 0.2561, 0.2485 | 1.33 | 0.2479, 0.2471 | 0.13 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 1m12s | 10533 | 527419 | 71785 (`freqParameter.4`) |
| slide | 1m18s | 9701 | 450475 | 46083 (`freqParameter.2`) |

Run-time ratio slide / default: 1.08

