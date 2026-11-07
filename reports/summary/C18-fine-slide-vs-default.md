# Posterior comparison: C18-fine-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C18-fine/rep1`, `beast3/log/C18-fine/rep2`
- slide: `beast3/log/C18-fine-slide/rep1`, `beast3/log/C18-fine-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1133; max z: 1.106; max clade |Δp|: 0.005

## Findings

- **NOTE** Trace log file names differ: default `CN-fine.log` paired with slide `CN-fine-slide.log`
- **NOTE** Tree file names differ: default `CN-fine-protein.trees` paired with slide `CN-fine-slide-protein.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C18-fine/rep1/C18-fine.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 57m32s |  |
| default | rep2 | `beast3/log/C18-fine/rep2/C18-fine.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 56m20s |  |
| slide | rep1 | `beast3/log/C18-fine-slide/rep1/C18-fine-slide.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 58m16s |  |
| slide | rep2 | `beast3/log/C18-fine-slide/rep2/C18-fine-slide.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 58m09s |  |

## Parameters: `CN-fine.log / CN-fine-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1924.48 | [-1929.56, -1920.06] | 27529 (13668) | -1924.47 | [-1929.54, -1920.12] | 29470 (12126) | 0.73 | 100% | ok |
| `likelihood` | -1925.88 | [-1930.46, -1921.93] | 25398 (12308) | -1925.87 | [-1930.43, -1921.97] | 27819 (11696) | 0.81 | 100% | ok |
| `prior` | 1.403 | [-0.7159, 3.392] | 37998 (17445) | 1.402 | [-0.7088, 3.395] | 37541 (16709) | 0.08 | 100% | ok |
| `treeLikelihood` | -1925.88 | [-1930.46, -1921.93] | 25398 (12308) | -1925.87 | [-1930.43, -1921.97] | 27819 (11696) | 0.81 | 100% | ok |
| `Tree.height` | 0.2457 | [0.196, 0.2983] | 97630 (48488) | 0.2456 | [0.1953, 0.2973] | 94767 (47157) | 0.60 | 99% | ok |
| `Tree.treeLength` | 1.204 | [0.9832, 1.428] | 69194 (32897) | 1.204 | [0.985, 1.428] | 68176 (33859) | 0.45 | 100% | ok |
| `YuleModel` | 8.634 | [6.446, 10.75] | 86363 (39553) | 8.635 | [6.382, 10.68] | 91372 (44796) | 0.25 | 99% | ok |
| `birthRate` | 7.485 | [2.794, 12.57] | 130402 (65152) | 7.496 | [2.849, 12.64] | 130479 (64680) | 1.11 | 99% | ok |
| `gammaShape` | 0.6783 | [0.4252, 0.9709] | 2506 (1218) | 0.6787 | [0.4253, 0.9652] | 2572 (1133) | 0.11 | 100% | ok |

### Replicate agreement (baseline noise): `CN-fine.log / CN-fine-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -1924.48, -1924.48 | 0.25 | -1924.47, -1924.46 | 0.41 |
| `likelihood` | -1925.89, -1925.88 | 0.41 | -1925.88, -1925.86 | 0.80 |
| `prior` | 1.405, 1.4 | 0.38 | 1.407, 1.397 | 0.92 |
| `treeLikelihood` | -1925.89, -1925.88 | 0.41 | -1925.88, -1925.86 | 0.80 |
| `Tree.height` | 0.2457, 0.2456 | 0.67 | 0.2455, 0.2457 | 1.31 |
| `Tree.treeLength` | 1.205, 1.204 | 0.16 | 1.204, 1.205 | 1.45 |
| `YuleModel` | 8.634, 8.633 | 0.16 | 8.635, 8.635 | 0.08 |
| `birthRate` | 7.487, 7.482 | 0.34 | 7.49, 7.502 | 0.81 |
| `gammaShape` | 0.6764, 0.6801 | 0.65 | 0.6747, 0.6827 | 1.41 |

## Trees: `CN-fine-protein.trees / CN-fine-slide-protein.trees`

18002 trees (default) and 18002 trees (slide) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: default 0.002, slide 0.006.

| Clade | Size | p default | p slide | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Cow, Seal} | 2 | 0.606 | 0.610 | 0.005 | ok |
| {Cow, Whale} | 2 | 0.382 | 0.378 | 0.005 | ok |
| {Cow, Human, Mouse, Rat, Seal, Whale} | 6 | 0.930 | 0.933 | 0.004 | ok |
| {Carp, Chicken, Cow, Frog, Loach, Mouse, … (9 taxa)} | 9 | 0.061 | 0.058 | 0.003 | ok |
| {Carp, Chicken, Frog, Loach} | 4 | 0.946 | 0.948 | 0.002 | ok |
| {Carp, Frog, Loach} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {Cow, Seal, Whale} | 3 | 0.996 | 0.996 | 0.000 | ok |
| {Carp, Loach} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Mouse, Rat} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Cow, Mouse, Rat, Seal, Whale} | 5 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 1h53m | 27529 | 14504 | 1320 (`gammaShape`) |
| slide | 1h56m | 29470 | 15189 | 1326 (`gammaShape`) |

Run-time ratio slide / default: 1.02

