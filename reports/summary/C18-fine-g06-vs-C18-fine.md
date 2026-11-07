# Posterior comparison: C18-fine-g06-vs-C18-fine

**Verdict: matched**

- ref: `beast3/log/C18-fine/rep1`, `beast3/log/C18-fine/rep2`
- g06: `beast3/log/C18-fine-g06/rep1`, `beast3/log/C18-fine-g06/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1218; max z: 1.325; max clade |Δp|: 0.003

## Findings

- **NOTE** Trace log file names differ: ref `CN-fine.log` paired with g06 `CN-fine-gN.log`
- **NOTE** Tree file names differ: ref `CN-fine-protein.trees` paired with g06 `CN-fine-gN-protein.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| ref | rep1 | `beast3/log/C18-fine/rep1/C18-fine.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 57m32s |  |
| ref | rep2 | `beast3/log/C18-fine/rep2/C18-fine.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 56m20s |  |
| g06 | rep1 | `beast3/log/C18-fine-g06/rep1/C18-fine-g06.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 1h27m |  |
| g06 | rep2 | `beast3/log/C18-fine-g06/rep2/C18-fine-g06.log` | 100001 (90001) | 100 | 2.8.0 rc2 | yes | 1h28m |  |

## Parameters: `CN-fine.log / CN-fine-gN.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | ref mean | ref 95% HPD | ref ESS | g06 mean | g06 95% HPD | g06 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1924.48 | [-1929.56, -1920.06] | 27529 (13668) | -1924.50 | [-1929.61, -1920.13] | 27920 (13230) | 0.82 | 99% | ok |
| `likelihood` | -1925.88 | [-1930.46, -1921.93] | 25398 (12308) | -1925.89 | [-1930.49, -1921.97] | 25782 (11893) | 0.48 | 100% | ok |
| `prior` | 1.403 | [-0.7159, 3.392] | 37998 (17445) | 1.395 | [-0.7466, 3.397] | 37574 (18167) | 1.02 | 100% | ok |
| `treeLikelihood` | -1925.88 | [-1930.46, -1921.93] | 25398 (12308) | -1925.89 | [-1930.49, -1921.97] | 25782 (11893) | 0.48 | 100% | ok |
| `Tree.height` | 0.2457 | [0.196, 0.2983] | 97630 (48488) | 0.2456 | [0.1956, 0.2978] | 86217 (40772) | 0.47 | 100% | ok |
| `Tree.treeLength` | 1.204 | [0.9832, 1.428] | 69194 (32897) | 1.204 | [0.9871, 1.43] | 63984 (30895) | 0.15 | 100% | ok |
| `YuleModel` | 8.634 | [6.446, 10.75] | 86363 (39553) | 8.627 | [6.421, 10.76] | 79726 (39730) | 1.33 | 100% | ok |
| `birthRate` | 7.485 | [2.794, 12.57] | 130402 (65152) | 7.482 | [2.795, 12.64] | 121539 (58781) | 0.26 | 100% | ok |
| `gammaShape` | 0.6783 | [0.4252, 0.9709] | 2506 (1218) | 0.6801 | [0.418, 0.952] | 2757 (1374) | 0.46 | 99% | ok |

### Replicate agreement (baseline noise): `CN-fine.log / CN-fine-gN.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | ref rep means | ref max z | g06 rep means | g06 max z |
|---|---|---:|---|---:|
| `posterior` | -1924.48, -1924.48 | 0.25 | -1924.51, -1924.49 | 0.46 |
| `likelihood` | -1925.89, -1925.88 | 0.41 | -1925.90, -1925.88 | 0.60 |
| `prior` | 1.405, 1.4 | 0.38 | 1.396, 1.393 | 0.28 |
| `treeLikelihood` | -1925.89, -1925.88 | 0.41 | -1925.90, -1925.88 | 0.60 |
| `Tree.height` | 0.2457, 0.2456 | 0.67 | 0.2456, 0.2457 | 0.37 |
| `Tree.treeLength` | 1.205, 1.204 | 0.16 | 1.204, 1.204 | 0.32 |
| `YuleModel` | 8.634, 8.633 | 0.16 | 8.629, 8.625 | 0.53 |
| `birthRate` | 7.487, 7.482 | 0.34 | 7.482, 7.482 | 0.01 |
| `gammaShape` | 0.6764, 0.6801 | 0.65 | 0.6805, 0.6797 | 0.15 |

## Trees: `CN-fine-protein.trees / CN-fine-gN-protein.trees`

18002 trees (ref) and 18002 trees (g06) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: ref 0.002, g06 0.011.

| Clade | Size | p ref | p g06 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Cow, Whale} | 2 | 0.382 | 0.386 | 0.003 | ok |
| {Cow, Seal} | 2 | 0.606 | 0.603 | 0.002 | ok |
| {Cow, Human, Mouse, Rat, Seal, Whale} | 6 | 0.930 | 0.931 | 0.001 | ok |
| {Carp, Chicken, Frog, Loach} | 4 | 0.946 | 0.946 | 0.001 | ok |
| {Carp, Chicken, Cow, Frog, Loach, Mouse, … (9 taxa)} | 9 | 0.061 | 0.061 | 0.001 | ok |
| {Cow, Seal, Whale} | 3 | 0.996 | 0.996 | 0.000 | ok |
| {Carp, Loach} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Mouse, Rat} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Cow, Mouse, Rat, Seal, Whale} | 5 | 1.000 | 1.000 | 0.000 | ok |
| {Carp, Frog, Loach} | 3 | 0.999 | 0.999 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| ref | 1h53m | 27529 | 14504 | 1320 (`gammaShape`) |
| g06 | 2h55m | 27920 | 9534 | 941 (`gammaShape`) |

Run-time ratio g06 / ref: 1.54

