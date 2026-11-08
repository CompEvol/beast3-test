# Posterior comparison: testGTR

**Verdict: not matched**

- beast2: `beast2/log/testGTR/rep1`, `beast2/log/testGTR/rep2`
- beast3: `beast3/log/testGTR/rep1`, `beast3/log/testGTR/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 264; max z: 678.18; max clade |Δp|: 0.002

## Findings

- **FLAG** `posterior`: z = 168.97 (beast2 mean -5943.15, beast3 mean -5956.94)
- **FLAG** `posterior`: 95% HPD intervals overlap only 0% of the narrower one
- **FLAG** `prior`: z = 678.18 (beast2 mean 6.339, beast3 mean -7.454)
- **FLAG** `prior`: 95% HPD intervals overlap only 0% of the narrower one
- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** `posterior` is shifted by -13.78 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -13.79 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** column map used: `reports/maps/testGTR.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testGTR/rep1/primate-mtDNA.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m10s |  |
| beast2 | rep2 | `beast2/log/testGTR/rep2/primate-mtDNA.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m07s |  |
| beast3 | rep1 | `beast3/log/testGTR/rep1/primate-mtDNA.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m48s |  |
| beast3 | rep2 | `beast3/log/testGTR/rep2/primate-mtDNA.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m49s |  |

## Parameters: `primate-mtDNA.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5943.15 | [-5949.51, -5937.55] | 2619 (1212) | -5956.94 | [-5963.39, -5951.26] | 3731 (1745) | 168.97 | 0% | **z**, **HPD** |
| `likelihood` | -5949.49 | [-5955.70, -5943.89] | 2631 (1296) | -5949.48 | [-5955.73, -5943.81] | 3655 (1661) | 0.13 | 100% | ok |
| `prior` | 6.339 | [4.298, 8.032] | 4156 (2062) | -7.454 | [-9.369, -5.762] | 5775 (2752) | 678.18 | 0% | **z**, **HPD** |
| `treeLikelihood.coding` | -4926.67 | [-4936.18, -4917.80] | 2567 (1194) | -4926.80 | [-4935.98, -4917.75] | 3370 (1644) | 1.07 | 100% | ok |
| `treeLikelihood.noncoding` | -1022.82 | [-1031.17, -1014.76] | 1920 (931) | -1022.68 | [-1030.75, -1014.66] | 2777 (1379) | 1.17 | 99% | ok |
| `TreeHeight → Tree.height` | 0.2454 | [0.225, 0.2666] | 5761 (2575) | 0.2452 | [0.2243, 0.2664] | 6901 (3359) | 1.01 | 99% | ok |
| `YuleModel` | 10.25 | [8.633, 11.53] | 6950 (3387) | 10.27 | [8.601, 11.46] | 9002 (4501) | 1.85 | 99% | ok |
| `birthRate` | 7.915 | [3.721, 12.52] | 8953 (4458) | 7.929 | [3.76, 12.38] | 8705 (4204) | 0.41 | 100% | ok |
| `rateAC` | 0.3215 | [0.2638, 0.3803] | 1071 (517) | 0.3222 | [0.2652, 0.3841] | 1800 (785) | 0.59 | 99% | ok |
| `rateAG` | 0.7411 | [0.5923, 0.8943] | 817 (360) | 0.7399 | [0.5886, 0.8959] | 1136 (543) | 0.35 | 100% | ok |
| `rateAT` | 0.1524 | [0.1126, 0.1892] | 1694 (754) | 0.1514 | [0.113, 0.1907] | 2924 (1461) | 1.68 | 100% | ok |
| `rateCG` | 0.08112 | [0.04048, 0.1267] | 1620 (590) | 0.0814 | [0.03887, 0.1284] | 3023 (1425) | 0.40 | 100% | ok |
| `rateGT` | 0.03632 | [0.01161, 0.06977] | 1511 (736) | 0.03619 | [0.009663, 0.0649] | 3694 (1724) | 0.29 | 96% | ok |
| `freqParameter.1` | 0.3039 | [0.2824, 0.3284] | 626 (299) | 0.3043 | [0.2817, 0.328] | 958 (466) | 0.63 | 99% | ok |
| `freqParameter.2` | 0.2703 | [0.249, 0.2894] | 803 (354) | 0.2699 | [0.2476, 0.2894] | 1084 (539) | 0.83 | 100% | ok |
| `freqParameter.3` | 0.1313 | [0.1131, 0.1484] | 623 (295) | 0.1313 | [0.1143, 0.1499] | 1017 (498) | 0.12 | 97% | ok |
| `freqParameter.4` | 0.2945 | [0.274, 0.3143] | 544 (264) | 0.2945 | [0.274, 0.3176] | 925 (433) | 0.05 | 100% | ok |

### Replicate agreement (baseline noise): `primate-mtDNA.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -5943.15, -5943.16 | 0.13 | -5956.89, -5956.98 | 0.91 |
| `likelihood` | -5949.52, -5949.47 | 0.40 | -5949.46, -5949.50 | 0.39 |
| `prior` | 6.371, 6.306 | 2.05 | -7.427, -7.481 | 2.12 |
| `treeLikelihood.coding` | -4926.59, -4926.75 | 0.81 | -4926.85, -4926.76 | 0.54 |
| `treeLikelihood.noncoding` | -1022.92, -1022.72 | 1.06 | -1022.61, -1022.74 | 0.82 |
| `TreeHeight → Tree.height` | 0.2454, 0.2453 | 0.28 | 0.2451, 0.2453 | 0.84 |
| `YuleModel` | 10.26, 10.24 | 1.30 | 10.3, 10.25 | 2.66 |
| `birthRate` | 7.885, 7.945 | 1.22 | 7.891, 7.967 | 1.55 |
| `rateAC` | 0.3223, 0.3208 | 0.81 | 0.3229, 0.3215 | 0.92 |
| `rateAG` | 0.744, 0.7383 | 1.02 | 0.7423, 0.7374 | 1.03 |
| `rateAT` | 0.1523, 0.1525 | 0.27 | 0.1511, 0.1517 | 0.83 |
| `rateCG` | 0.08127, 0.08096 | 0.26 | 0.08264, 0.08017 | 2.91 |
| `rateGT` | 0.03709, 0.03555 | 1.96 | 0.03618, 0.03619 | 0.01 |
| `freqParameter.1` | 0.3035, 0.3043 | 0.87 | 0.3039, 0.3047 | 1.04 |
| `freqParameter.2` | 0.2708, 0.2698 | 1.36 | 0.2699, 0.2699 | 0.03 |
| `freqParameter.3` | 0.1311, 0.1315 | 0.55 | 0.1309, 0.1318 | 1.63 |
| `freqParameter.4` | 0.2946, 0.2944 | 0.23 | 0.2953, 0.2936 | 2.29 |

## Trees: `primate.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.005, beast3 0.004.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (10 taxa)} | 10 | 0.955 | 0.957 | 0.002 | ok |
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
| beast2 | 4m17s | 2619 | 36736 | 7631 (`freqParameter.4`) |
| beast3 | 3m37s | 3731 | 61972 | 15367 (`freqParameter.4`) |

Run-time ratio beast3 / beast2: 0.84

