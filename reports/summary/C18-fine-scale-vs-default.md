# Posterior comparison: C18-fine-scale-vs-default

**Verdict: matched**

- default: `beast3/log/C18-fine/rep1`, `beast3/log/C18-fine/rep2`
- scale: `beast3/log/C18-fine-scale/rep1`, `beast3/log/C18-fine-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1216; max z: 0.9087; max clade |Δp|: 0.002

## Findings

- **NOTE** Trace log file names differ: default `CN-fine.log` paired with scale `CN-fine-scale.log`
- **NOTE** Tree file names differ: default `CN-fine-protein.trees` paired with scale `CN-fine-scale-protein.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C18-fine/rep1/C18-fine.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 57m32s |  |
| default | rep2 | `beast3/log/C18-fine/rep2/C18-fine.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 56m20s |  |
| scale | rep1 | `beast3/log/C18-fine-scale/rep1/C18-fine-scale.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 59m46s |  |
| scale | rep2 | `beast3/log/C18-fine-scale/rep2/C18-fine-scale.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 48m09s |  |

## Parameters: `CN-fine.log / CN-fine-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1924.48 | [-1929.56, -1920.06] | 27529 (13668) | -1924.50 | [-1929.61, -1920.09] | 23678 (11693) | 0.91 | 100% | ok |
| `likelihood` | -1925.88 | [-1930.46, -1921.93] | 25398 (12308) | -1925.90 | [-1930.46, -1921.92] | 22374 (11075) | 0.84 | 100% | ok |
| `prior` | 1.403 | [-0.7159, 3.392] | 37998 (17445) | 1.4 | [-0.7109, 3.433] | 36045 (17721) | 0.37 | 100% | ok |
| `treeLikelihood` | -1925.88 | [-1930.46, -1921.93] | 25398 (12308) | -1925.90 | [-1930.46, -1921.92] | 22374 (11075) | 0.84 | 100% | ok |
| `Tree.height` | 0.2457 | [0.196, 0.2983] | 97630 (48488) | 0.2456 | [0.1952, 0.2976] | 86793 (42123) | 0.72 | 99% | ok |
| `Tree.treeLength` | 1.204 | [0.9832, 1.428] | 69194 (32897) | 1.204 | [0.9895, 1.433] | 61379 (30393) | 0.30 | 99% | ok |
| `YuleModel` | 8.634 | [6.446, 10.75] | 86363 (39553) | 8.633 | [6.374, 10.7] | 79910 (38752) | 0.21 | 99% | ok |
| `birthRate` | 7.485 | [2.794, 12.57] | 130402 (65152) | 7.487 | [2.764, 12.54] | 124280 (59288) | 0.24 | 100% | ok |
| `gammaShape` | 0.6783 | [0.4252, 0.9709] | 2506 (1218) | 0.6797 | [0.4202, 0.9616] | 2452 (1216) | 0.35 | 99% | ok |

### Replicate agreement (baseline noise): `CN-fine.log / CN-fine-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -1924.48, -1924.48 | 0.25 | -1924.50, -1924.50 | 0.13 |
| `likelihood` | -1925.89, -1925.88 | 0.41 | -1925.91, -1925.90 | 0.25 |
| `prior` | 1.405, 1.4 | 0.38 | 1.401, 1.398 | 0.32 |
| `treeLikelihood` | -1925.89, -1925.88 | 0.41 | -1925.91, -1925.90 | 0.25 |
| `Tree.height` | 0.2457, 0.2456 | 0.67 | 0.2455, 0.2457 | 0.70 |
| `Tree.treeLength` | 1.205, 1.204 | 0.16 | 1.204, 1.204 | 0.36 |
| `YuleModel` | 8.634, 8.633 | 0.16 | 8.631, 8.634 | 0.42 |
| `birthRate` | 7.487, 7.482 | 0.34 | 7.484, 7.491 | 0.46 |
| `gammaShape` | 0.6764, 0.6801 | 0.65 | 0.6771, 0.6824 | 0.90 |

## Trees: `CN-fine-protein.trees / CN-fine-scale-protein.trees`

18002 trees (default) and 18002 trees (scale) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: default 0.002, scale 0.010.

| Clade | Size | p default | p scale | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Cow, Human, Mouse, Rat, Seal, Whale} | 6 | 0.930 | 0.932 | 0.002 | ok |
| {Carp, Chicken, Cow, Frog, Loach, Mouse, … (9 taxa)} | 9 | 0.061 | 0.060 | 0.001 | ok |
| {Cow, Seal} | 2 | 0.606 | 0.606 | 0.001 | ok |
| {Carp, Chicken, Frog, Loach} | 4 | 0.946 | 0.946 | 0.000 | ok |
| {Cow, Seal, Whale} | 3 | 0.996 | 0.996 | 0.000 | ok |
| {Carp, Frog, Loach} | 3 | 0.999 | 0.998 | 0.000 | ok |
| {Cow, Whale} | 2 | 0.382 | 0.382 | 0.000 | ok |
| {Carp, Loach} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Mouse, Rat} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Cow, Mouse, Rat, Seal, Whale} | 5 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 1h53m | 27529 | 14504 | 1320 (`gammaShape`) |
| scale | 1h47m | 23678 | 13164 | 1363 (`gammaShape`) |

Run-time ratio scale / default: 0.95

