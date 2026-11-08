# Posterior comparison: testRestrictedGTR

**Verdict: not matched**

- beast2: `beast2/log/testRestrictedGTR/rep1`, `beast2/log/testRestrictedGTR/rep2`
- beast3: `beast3/log/testRestrictedGTR/rep1`, `beast3/log/testRestrictedGTR/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 221; max z: 1056.12; max clade |Δp|: 0.001

## Findings

- **FLAG** `posterior`: z = 196.87 (beast2 mean -5984.56, beast3 mean -5998.31)
- **FLAG** `posterior`: 95% HPD intervals overlap only 0% of the narrower one
- **FLAG** `prior`: z = 1056.12 (beast2 mean 8.847, beast3 mean -4.968)
- **FLAG** `prior`: 95% HPD intervals overlap only 0% of the narrower one
- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** `posterior` is shifted by -13.75 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -13.82 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** column map used: `reports/maps/testRestrictedGTR.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testRestrictedGTR/rep1/primate-mtDNA-restrictedGTR.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m02s |  |
| beast2 | rep2 | `beast2/log/testRestrictedGTR/rep2/primate-mtDNA-restrictedGTR.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m02s |  |
| beast3 | rep1 | `beast3/log/testRestrictedGTR/rep1/primate-mtDNA-restrictedGTR.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m48s |  |
| beast3 | rep2 | `beast3/log/testRestrictedGTR/rep2/primate-mtDNA-restrictedGTR.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m50s |  |

## Parameters: `primate-mtDNA-restrictedGTR.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5984.56 | [-5990.13, -5979.08] | 2996 (1412) | -5998.31 | [-6003.94, -5992.85] | 4343 (1634) | 196.87 | 0% | **z**, **HPD** |
| `likelihood` | -5993.41 | [-5998.93, -5988.28] | 2756 (1299) | -5993.34 | [-5998.90, -5988.23] | 4197 (1462) | 0.90 | 100% | ok |
| `prior` | 8.847 | [7.249, 10.17] | 7799 (3814) | -4.968 | [-6.552, -3.727] | 7428 (3643) | 1056.12 | 0% | **z**, **HPD** |
| `treeLikelihood.coding` | -4962.67 | [-4972.47, -4953.17] | 1664 (664) | -4962.24 | [-4971.92, -4952.83] | 2651 (1143) | 2.77 | 98% | ok |
| `treeLikelihood.noncoding` | -1030.73 | [-1039.24, -1022.19] | 1752 (659) | -1031.11 | [-1039.63, -1022.65] | 2544 (1258) | 2.76 | 98% | ok |
| `TreeHeight → Tree.height` | 0.2505 | [0.2299, 0.2729] | 7007 (3152) | 0.2506 | [0.2292, 0.2712] | 7286 (3421) | 0.65 | 98% | ok |
| `YuleModel` | 10.11 | [8.495, 11.36] | 8499 (4135) | 10.12 | [8.564, 11.33] | 8590 (4089) | 0.75 | 100% | ok |
| `birthRate` | 7.773 | [3.726, 12.28] | 7754 (3253) | 7.733 | [3.663, 12.08] | 8751 (4250) | 1.14 | 99% | ok |
| `rateTransversion` | 0.1827 | [0.1561, 0.2084] | 1012 (416) | 0.1835 | [0.1585, 0.2122] | 1837 (901) | 1.43 | 95% | ok |
| `rateAG` | 0.7621 | [0.613, 0.9204] | 715 (287) | 0.7705 | [0.6179, 0.9312] | 1214 (573) | 2.18 | 98% | ok |
| `freqParameter.1` | 0.3247 | [0.3012, 0.3498] | 507 (221) | 0.3247 | [0.3004, 0.3468] | 727 (356) | 0.08 | 98% | ok |
| `freqParameter.2` | 0.2815 | [0.2616, 0.3036] | 668 (273) | 0.2829 | [0.263, 0.3049] | 992 (493) | 2.60 | 97% | ok |
| `freqParameter.3` | 0.1137 | [0.09989, 0.1288] | 819 (398) | 0.1128 | [0.09912, 0.1282] | 1319 (603) | 2.94 | 98% | ok |
| `freqParameter.4` | 0.2801 | [0.2587, 0.3012] | 840 (395) | 0.2797 | [0.2584, 0.3003] | 1048 (472) | 0.76 | 99% | ok |

### Replicate agreement (baseline noise): `primate-mtDNA-restrictedGTR.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -5984.62, -5984.50 | 1.18 | -5998.31, -5998.31 | 0.01 |
| `likelihood` | -5993.48, -5993.33 | 1.36 | -5993.33, -5993.36 | 0.31 |
| `prior` | 8.858, 8.837 | 1.15 | -4.983, -4.952 | 1.64 |
| `treeLikelihood.coding` | -4962.81, -4962.53 | 1.11 | -4962.14, -4962.33 | 0.98 |
| `treeLikelihood.noncoding` | -1030.67, -1030.80 | 0.61 | -1031.19, -1031.03 | 0.95 |
| `TreeHeight → Tree.height` | 0.2502, 0.2507 | 2.21 | 0.2508, 0.2503 | 2.07 |
| `YuleModel` | 10.12, 10.1 | 1.22 | 10.11, 10.13 | 1.58 |
| `birthRate` | 7.787, 7.759 | 0.52 | 7.78, 7.686 | 1.98 |
| `rateTransversion` | 0.183, 0.1823 | 0.81 | 0.1833, 0.1836 | 0.38 |
| `rateAG` | 0.7625, 0.7618 | 0.11 | 0.772, 0.7689 | 0.67 |
| `freqParameter.1` | 0.3254, 0.324 | 1.19 | 0.3245, 0.3248 | 0.28 |
| `freqParameter.2` | 0.2809, 0.2821 | 1.36 | 0.2829, 0.2828 | 0.13 |
| `freqParameter.3` | 0.1137, 0.1138 | 0.28 | 0.1124, 0.1131 | 1.59 |
| `freqParameter.4` | 0.2801, 0.2801 | 0.02 | 0.2801, 0.2793 | 1.25 |

## Trees: `primate-mtDNA-restrictedGTR-primate.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.003, beast3 0.006.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (10 taxa)} | 10 | 0.957 | 0.958 | 0.001 | ok |
| {Gorilla, Homo_sapiens, Pan, Pongo} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (9 taxa)} | 9 | 1.000 | 1.000 | 0.000 | ok |
| {Homo_sapiens, Pan} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Lemur_catta, Tarsius_syrichta} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {M._mulatta, Macaca_fuscata} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Gorilla, Homo_sapiens, Pan} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {M._fascicularis, M._mulatta, Macaca_fuscata} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {M._fascicularis, M._mulatta, M._sylvanus, Macaca_fuscata} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Gorilla, Homo_sapiens, Hylobates, Pan, Pongo} | 5 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 4m04s | 2996 | 44230 | 7477 (`freqParameter.1`) |
| beast3 | 3m38s | 4343 | 71718 | 12012 (`freqParameter.1`) |

Run-time ratio beast3 / beast2: 0.89

