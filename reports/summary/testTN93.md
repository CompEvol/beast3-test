# Posterior comparison: testTN93

**Verdict: not matched**

- beast2: `beast2/log/testTN93/rep1`, `beast2/log/testTN93/rep2`
- beast3: `beast3/log/testTN93/rep1`, `beast3/log/testTN93/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 216; max z: 1063.12; max clade |Δp|: 0.004

## Findings

- **FLAG** `posterior`: z = 161.31 (beast2 mean -5983.29, beast3 mean -5997.02)
- **FLAG** `posterior`: 95% HPD intervals overlap only 0% of the narrower one
- **FLAG** `prior`: z = 1063.12 (beast2 mean 10.1, beast3 mean -3.716)
- **FLAG** `prior`: 95% HPD intervals overlap only 0% of the narrower one
- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** `posterior` is shifted by -13.73 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -13.81 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** column map used: `reports/maps/testTN93.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testTN93/rep1/primate-mtDNA-tn93.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 1m37s |  |
| beast2 | rep2 | `beast2/log/testTN93/rep2/primate-mtDNA-tn93.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 1m35s |  |
| beast3 | rep1 | `beast3/log/testTN93/rep1/primate-mtDNA-tn93.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 1m18s |  |
| beast3 | rep2 | `beast3/log/testTN93/rep2/primate-mtDNA-tn93.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 1m17s |  |

## Parameters: `primate-mtDNA-tnN.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5983.29 | [-5989.35, -5977.91] | 1773 (839) | -5997.02 | [-6002.65, -5991.74] | 3835 (1657) | 161.31 | 0% | **z**, **HPD** |
| `likelihood` | -5993.39 | [-5999.16, -5988.23] | 1680 (769) | -5993.31 | [-5998.84, -5988.32] | 3582 (1459) | 1.02 | 100% | ok |
| `prior` | 10.1 | [8.493, 11.34] | 7924 (3765) | -3.716 | [-5.283, -2.452] | 7474 (3372) | 1063.12 | 0% | **z**, **HPD** |
| `treeLikelihood.coding` | -4962.46 | [-4972.07, -4952.90] | 1916 (923) | -4962.41 | [-4971.72, -4952.85] | 2452 (1193) | 0.33 | 100% | ok |
| `treeLikelihood.noncoding` | -1030.93 | [-1039.69, -1022.28] | 1474 (660) | -1030.90 | [-1039.92, -1022.90] | 2319 (1089) | 0.25 | 99% | ok |
| `TreeHeight → Tree.height` | 0.2508 | [0.2302, 0.2737] | 7380 (3675) | 0.2508 | [0.2298, 0.2717] | 6609 (3207) | 0.03 | 99% | ok |
| `YuleModel` | 10.1 | [8.493, 11.34] | 7924 (3765) | 10.1 | [8.533, 11.36] | 7474 (3372) | 0.11 | 99% | ok |
| `birthRate` | 7.78 | [3.747, 12.31] | 9002 (4501) | 7.753 | [3.601, 12.13] | 8841 (4340) | 0.80 | 98% | ok |
| `rateAG` | 4.25 | [3.507, 5.114] | 677 (332) | 4.254 | [3.45, 5.068] | 1646 (799) | 0.19 | 97% | ok |
| `rateCT` | 5.558 | [4.704, 6.364] | 769 (339) | 5.548 | [4.705, 6.341] | 1552 (755) | 0.55 | 100% | ok |
| `freqParameter.1` | 0.3244 | [0.299, 0.348] | 516 (245) | 0.324 | [0.2989, 0.3477] | 555 (276) | 0.59 | 100% | ok |
| `freqParameter.2` | 0.2829 | [0.263, 0.3038] | 557 (271) | 0.2826 | [0.2632, 0.3042] | 709 (341) | 0.45 | 100% | ok |
| `freqParameter.3` | 0.1129 | [0.09731, 0.1272] | 562 (257) | 0.1128 | [0.09979, 0.1285] | 1066 (531) | 0.20 | 96% | ok |
| `freqParameter.4` | 0.2798 | [0.2592, 0.3013] | 486 (216) | 0.2806 | [0.2606, 0.301] | 807 (372) | 1.30 | 100% | ok |

### Replicate agreement (baseline noise): `primate-mtDNA-tnN.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -5983.19, -5983.40 | 1.44 | -5997.05, -5997.00 | 0.48 |
| `likelihood` | -5993.29, -5993.49 | 1.41 | -5993.33, -5993.29 | 0.41 |
| `prior` | 10.1, 10.09 | 0.38 | -3.719, -3.713 | 0.32 |
| `treeLikelihood.coding` | -4962.45, -4962.47 | 0.12 | -4962.42, -4962.40 | 0.05 |
| `treeLikelihood.noncoding` | -1030.85, -1031.02 | 0.73 | -1030.91, -1030.88 | 0.16 |
| `TreeHeight → Tree.height` | 0.2507, 0.251 | 1.19 | 0.2507, 0.2509 | 0.78 |
| `YuleModel` | 10.1, 10.09 | 0.38 | 10.1, 10.1 | 0.32 |
| `birthRate` | 7.806, 7.755 | 1.08 | 7.775, 7.731 | 0.91 |
| `rateAG` | 4.233, 4.267 | 1.03 | 4.266, 4.241 | 1.24 |
| `rateCT` | 5.561, 5.555 | 0.18 | 5.564, 5.531 | 1.52 |
| `freqParameter.1` | 0.3253, 0.3235 | 1.63 | 0.325, 0.3229 | 1.94 |
| `freqParameter.2` | 0.2824, 0.2834 | 1.10 | 0.2825, 0.2827 | 0.21 |
| `freqParameter.3` | 0.113, 0.1128 | 0.29 | 0.1127, 0.113 | 0.67 |
| `freqParameter.4` | 0.2793, 0.2803 | 1.04 | 0.2798, 0.2814 | 2.12 |

## Trees: `primate-mtDNA-tnN.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.001, beast3 0.002.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (10 taxa)} | 10 | 0.960 | 0.956 | 0.004 | ok |
| {Homo_sapiens, Pan} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Lemur_catta, Tarsius_syrichta} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {M._mulatta, Macaca_fuscata} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Gorilla, Homo_sapiens, Pan} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {M._fascicularis, M._mulatta, Macaca_fuscata} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {Gorilla, Homo_sapiens, Pan, Pongo} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {M._fascicularis, M._mulatta, M._sylvanus, Macaca_fuscata} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Gorilla, Homo_sapiens, Hylobates, Pan, Pongo} | 5 | 1.000 | 1.000 | 0.000 | ok |
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (9 taxa)} | 9 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 3m12s | 1773 | 33249 | 9116 (`freqParameter.4`) |
| beast3 | 2m34s | 3835 | 89472 | 12957 (`freqParameter.1`) |

Run-time ratio beast3 / beast2: 0.80

