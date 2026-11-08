# Posterior comparison: testTVM

**Verdict: not matched**

- beast2: `beast2/log/testTVM/rep1`, `beast2/log/testTVM/rep2`
- beast3: `beast3/log/testTVM/rep1`, `beast3/log/testTVM/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 287; max z: 752.57; max clade |Δp|: 0.002

## Findings

- **FLAG** `posterior`: z = 171.19 (beast2 mean -5947.49, beast3 mean -5961.34)
- **FLAG** `posterior`: 95% HPD intervals overlap only 0% of the narrower one
- **FLAG** `prior`: z = 752.57 (beast2 mean 5.974, beast3 mean -7.849)
- **FLAG** `prior`: 95% HPD intervals overlap only 0% of the narrower one
- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** `posterior` is shifted by -13.85 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -13.82 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** column map used: `reports/maps/testTVM.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testTVM/rep1/primate-mtDNA-TVM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m12s |  |
| beast2 | rep2 | `beast2/log/testTVM/rep2/primate-mtDNA-TVM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m09s |  |
| beast3 | rep1 | `beast3/log/testTVM/rep1/primate-mtDNA-TVM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m48s |  |
| beast3 | rep2 | `beast3/log/testTVM/rep2/primate-mtDNA-TVM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m48s |  |

## Parameters: `primate-mtDNA-TVM.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5947.49 | [-5953.70, -5941.89] | 2434 (1080) | -5961.34 | [-5967.42, -5955.49] | 3860 (1730) | 171.19 | 0% | **z**, **HPD** |
| `likelihood` | -5953.47 | [-5959.19, -5947.83] | 2394 (1070) | -5953.49 | [-5959.49, -5948.16] | 3873 (1783) | 0.31 | 97% | ok |
| `prior` | 5.974 | [4.093, 7.397] | 4338 (2008) | -7.849 | [-9.651, -6.326] | 5556 (2582) | 752.57 | 0% | **z**, **HPD** |
| `treeLikelihood.coding` | -4926.13 | [-4935.25, -4917.55] | 3116 (1553) | -4926.22 | [-4935.78, -4917.65] | 3818 (1886) | 0.76 | 99% | ok |
| `treeLikelihood.noncoding` | -1027.33 | [-1035.34, -1019.91] | 3361 (1537) | -1027.27 | [-1035.29, -1019.87] | 3885 (1856) | 0.66 | 100% | ok |
| `TreeHeight → Tree.height` | 0.2465 | [0.2256, 0.2666] | 6655 (2815) | 0.2464 | [0.2257, 0.2668] | 7187 (3287) | 0.21 | 100% | ok |
| `YuleModel` | 10.19 | [8.507, 11.36] | 7883 (3430) | 10.19 | [8.458, 11.34] | 8637 (4240) | 0.50 | 99% | ok |
| `birthRate` | 7.816 | [3.629, 12.29] | 8754 (4253) | 7.873 | [3.634, 12.35] | 8960 (4459) | 1.68 | 100% | ok |
| `rateGT` | 0.1039 | [0.01911, 0.1954] | 1275 (604) | 0.1033 | [0.02156, 0.1933] | 3581 (1687) | 0.38 | 100% | ok |
| `rateTransitions` | 2.912 | [2.392, 3.382] | 841 (370) | 2.919 | [2.431, 3.43] | 1597 (751) | 0.65 | 96% | ok |
| `rateAT` | 0.481 | [0.3445, 0.6349] | 959 (366) | 0.4807 | [0.3364, 0.6299] | 1792 (838) | 0.10 | 98% | ok |
| `rateCG` | 0.251 | [0.1069, 0.4085] | 1415 (596) | 0.252 | [0.1038, 0.4148] | 2544 (1177) | 0.38 | 100% | ok |
| `freqParameter.1` | 0.2957 | [0.2733, 0.3176] | 747 (287) | 0.296 | [0.2755, 0.3182] | 1120 (457) | 0.57 | 99% | ok |
| `freqParameter.2` | 0.2797 | [0.2611, 0.3005] | 852 (425) | 0.2794 | [0.2585, 0.2995] | 1048 (474) | 0.63 | 97% | ok |
| `freqParameter.3` | 0.1182 | [0.106, 0.1337] | 1105 (484) | 0.1181 | [0.1045, 0.1324] | 1543 (760) | 0.17 | 95% | ok |
| `freqParameter.4` | 0.3064 | [0.286, 0.3275] | 761 (326) | 0.3064 | [0.2856, 0.3274] | 1089 (501) | 0.09 | 100% | ok |

### Replicate agreement (baseline noise): `primate-mtDNA-TVM.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -5947.46, -5947.53 | 0.59 | -5961.39, -5961.29 | 1.02 |
| `likelihood` | -5953.44, -5953.50 | 0.46 | -5953.54, -5953.44 | 1.02 |
| `prior` | 5.983, 5.965 | 0.67 | -7.852, -7.847 | 0.22 |
| `treeLikelihood.coding` | -4926.14, -4926.13 | 0.08 | -4926.24, -4926.19 | 0.31 |
| `treeLikelihood.noncoding` | -1027.30, -1027.37 | 0.52 | -1027.30, -1027.25 | 0.40 |
| `TreeHeight → Tree.height` | 0.2466, 0.2463 | 0.99 | 0.2466, 0.2462 | 1.75 |
| `YuleModel` | 10.19, 10.2 | 0.21 | 10.18, 10.19 | 0.38 |
| `birthRate` | 7.833, 7.799 | 0.69 | 7.918, 7.828 | 1.86 |
| `rateGT` | 0.1041, 0.1036 | 0.21 | 0.1032, 0.1033 | 0.00 |
| `rateTransitions` | 2.908, 2.916 | 0.45 | 2.917, 2.922 | 0.37 |
| `rateAT` | 0.4782, 0.4838 | 1.13 | 0.4786, 0.4829 | 1.21 |
| `rateCG` | 0.2483, 0.2537 | 1.23 | 0.252, 0.252 | 0.02 |
| `freqParameter.1` | 0.2956, 0.2959 | 0.32 | 0.2965, 0.2956 | 1.26 |
| `freqParameter.2` | 0.2795, 0.2799 | 0.56 | 0.2792, 0.2797 | 0.72 |
| `freqParameter.3` | 0.1181, 0.1182 | 0.20 | 0.1179, 0.1183 | 0.91 |
| `freqParameter.4` | 0.3067, 0.306 | 0.95 | 0.3064, 0.3064 | 0.09 |

## Trees: `primate.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.002, beast3 0.010.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (10 taxa)} | 10 | 0.954 | 0.952 | 0.002 | ok |
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
| beast2 | 4m20s | 2434 | 33694 | 10339 (`freqParameter.1`) |
| beast3 | 3m37s | 3860 | 64132 | 17409 (`freqParameter.2`) |

Run-time ratio beast3 / beast2: 0.83

