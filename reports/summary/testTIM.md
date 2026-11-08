# Posterior comparison: testTIM

**Verdict: not matched**

- beast2: `beast2/log/testTIM/rep1`, `beast2/log/testTIM/rep2`
- beast3: `beast3/log/testTIM/rep1`, `beast3/log/testTIM/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 313; max z: 1044.94; max clade |Δp|: 0.001

## Findings

- **FLAG** `posterior`: z = 182.97 (beast2 mean -5976.76, beast3 mean -5990.59)
- **FLAG** `posterior`: 95% HPD intervals overlap only 0% of the narrower one
- **FLAG** `prior`: z = 1044.94 (beast2 mean 8.409, beast3 mean -5.413)
- **FLAG** `prior`: 95% HPD intervals overlap only 0% of the narrower one
- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **WARN** `prior`: beast3 replicates disagree with each other (z = 3.26)
- **WARN** `YuleModel`: beast3 replicates disagree with each other (z = 3.06)
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** `posterior` is shifted by -13.83 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -13.82 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** column map used: `reports/maps/testTIM.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testTIM/rep1/primate-mtDNA-TIM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m05s |  |
| beast2 | rep2 | `beast2/log/testTIM/rep2/primate-mtDNA-TIM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m09s |  |
| beast3 | rep1 | `beast3/log/testTIM/rep1/primate-mtDNA-TIM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m48s |  |
| beast3 | rep2 | `beast3/log/testTIM/rep2/primate-mtDNA-TIM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m48s |  |

## Parameters: `primate-mtDNA-TIM.log`

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5976.76 | [-5982.70, -5971.25] | 2801 (1328) | -5990.59 | [-5996.79, -5985.12] | 3993 (1765) | 182.97 | 0% | **z**, **HPD** |
| `likelihood` | -5985.17 | [-5990.89, -5979.76] | 2731 (1308) | -5985.17 | [-5991.22, -5980.07] | 3893 (1756) | 0.05 | 97% | ok |
| `prior` | 8.409 | [6.805, 9.643] | 7269 (3092) | -5.413 | [-7.1, -4.205] | 7331 (3587) | 1044.94 | 0% | **z**, **HPD** |
| `treeLikelihood.coding` | -4954.68 | [-4964.52, -4945.62] | 2645 (1255) | -4954.69 | [-4964.64, -4945.49] | 3217 (1462) | 0.03 | 100% | ok |
| `treeLikelihood.noncoding` | -1030.48 | [-1039.01, -1022.37] | 2083 (988) | -1030.48 | [-1039.08, -1022.36] | 3043 (1389) | 0.00 | 100% | ok |
| `TreeHeight → Tree.height` | 0.2502 | [0.2295, 0.272] | 7392 (3444) | 0.2499 | [0.2287, 0.2714] | 7443 (3685) | 1.52 | 99% | ok |
| `YuleModel` | 10.12 | [8.547, 11.36] | 7746 (3434) | 10.12 | [8.506, 11.35] | 7861 (3904) | 0.21 | 100% | ok |
| `birthRate` | 7.749 | [3.772, 12.29] | 8477 (4131) | 7.813 | [3.761, 12.41] | 8661 (4160) | 1.85 | 100% | ok |
| `rateAG` | 0.773 | [0.6195, 0.9386] | 744 (364) | 0.7776 | [0.6291, 0.9345] | 1257 (601) | 1.23 | 100% | ok |
| `rateTransversions1` | 0.2376 | [0.1978, 0.2787] | 1259 (543) | 0.2385 | [0.1979, 0.2839] | 2590 (1255) | 1.20 | 100% | ok |
| `rateTransversions2` | 0.1302 | [0.09936, 0.1641] | 1710 (758) | 0.1305 | [0.09641, 0.1615] | 2386 (913) | 0.66 | 96% | ok |
| `freqParameter.1` | 0.3228 | [0.3005, 0.347] | 710 (317) | 0.3224 | [0.2982, 0.3452] | 1008 (473) | 0.62 | 96% | ok |
| `freqParameter.2` | 0.2779 | [0.2591, 0.2987] | 822 (369) | 0.2777 | [0.2583, 0.2992] | 1099 (483) | 0.25 | 100% | ok |
| `freqParameter.3` | 0.1137 | [0.09898, 0.1274] | 709 (313) | 0.1135 | [0.09933, 0.1282] | 1485 (689) | 0.49 | 99% | ok |
| `freqParameter.4` | 0.2856 | [0.264, 0.3045] | 779 (338) | 0.2863 | [0.263, 0.3066] | 1045 (464) | 1.29 | 100% | ok |

### Replicate agreement (baseline noise): `primate-mtDNA-TIM.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -5976.77, -5976.74 | 0.27 | -5990.53, -5990.64 | 1.07 |
| `likelihood` | -5985.19, -5985.14 | 0.43 | -5985.15, -5985.19 | 0.46 |
| `prior` | 8.418, 8.401 | 0.95 | -5.382, -5.444 | 3.26 |
| `treeLikelihood.coding` | -4954.62, -4954.75 | 0.71 | -4954.85, -4954.53 | 1.85 |
| `treeLikelihood.noncoding` | -1030.58, -1030.39 | 0.99 | -1030.30, -1030.67 | 2.37 |
| `TreeHeight → Tree.height` | 0.2503, 0.2501 | 0.76 | 0.2497, 0.2501 | 1.50 |
| `YuleModel` | 10.13, 10.12 | 0.93 | 10.15, 10.09 | 3.06 |
| `birthRate` | 7.747, 7.751 | 0.09 | 7.806, 7.82 | 0.30 |
| `rateAG` | 0.7726, 0.7734 | 0.13 | 0.7742, 0.7811 | 1.51 |
| `rateTransversions1` | 0.2377, 0.2375 | 0.13 | 0.2384, 0.2386 | 0.30 |
| `rateTransversions2` | 0.1303, 0.1301 | 0.25 | 0.1302, 0.1308 | 0.94 |
| `freqParameter.1` | 0.3226, 0.323 | 0.49 | 0.323, 0.3219 | 1.45 |
| `freqParameter.2` | 0.2785, 0.2772 | 1.77 | 0.277, 0.2784 | 2.21 |
| `freqParameter.3` | 0.1134, 0.1139 | 0.92 | 0.1138, 0.1133 | 1.26 |
| `freqParameter.4` | 0.2855, 0.2858 | 0.43 | 0.2862, 0.2864 | 0.28 |

## Trees: `primate.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.002, beast3 0.000.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (10 taxa)} | 10 | 0.964 | 0.963 | 0.001 | ok |
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
| beast2 | 4m14s | 2801 | 39638 | 10028 (`freqParameter.3`) |
| beast3 | 3m36s | 3993 | 66405 | 16762 (`freqParameter.1`) |

Run-time ratio beast3 / beast2: 0.85

