# Posterior comparison: testSYM

**Verdict: not matched**

- beast2: `beast2/log/testSYM/rep1`, `beast2/log/testSYM/rep2`, `beast2/log/testSYM/rep3`, `beast2/log/testSYM/rep4`
- beast3: `beast3/log/testSYM/rep1`, `beast3/log/testSYM/rep2`, `beast3/log/testSYM/rep3`, `beast3/log/testSYM/rep4`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 583; max z: 892.66; max clade |Δp|: 0.004

## Findings

- **FLAG** `posterior`: z = 329.97 (beast2 mean -5996.45, beast3 mean -6010.30)
- **FLAG** `posterior`: 95% HPD intervals overlap only 0% of the narrower one
- **FLAG** `prior`: z = 892.66 (beast2 mean 6.47, beast3 mean -7.349)
- **FLAG** `prior`: 95% HPD intervals overlap only 0% of the narrower one
- **WARN** column `Tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **WARN** `treeLikelihood.coding`: beast2 replicates disagree with each other (z = 3.02)
- **NOTE** column renamed (mapping): beast2 `TreeHeight` = beast3 `Tree.height`
- **NOTE** `posterior` is shifted by -13.84 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -13.82 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** column map used: `reports/maps/testSYM.tsv` (1 entries)

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testSYM/rep1/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m09s |  |
| beast2 | rep2 | `beast2/log/testSYM/rep2/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m10s |  |
| beast2 | rep3 | `beast2/log/testSYM/rep3/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m09s |  |
| beast2 | rep4 | `beast2/log/testSYM/rep4/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.7.9 Prerelease | yes | 2m09s |  |
| beast3 | rep1 | `beast3/log/testSYM/rep1/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m49s |  |
| beast3 | rep2 | `beast3/log/testSYM/rep2/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m49s |  |
| beast3 | rep3 | `beast3/log/testSYM/rep3/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m52s |  |
| beast3 | rep4 | `beast3/log/testSYM/rep4/primate-mtDNA-SYM.log` | 5001 (4501) | 1400 | 2.8.0 rc2 | yes | 1m49s |  |

## Parameters: `primate-mtDNA-SYM.log`

Constant columns (skipped): `freqParameter.1` = 0.25, `freqParameter.2` = 0.25, `freqParameter.3` = 0.25, `freqParameter.4` = 0.25

Not compared: only in beast2: –; only in beast3: `Tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5996.45 | [-6002.39, -5991.26] | 8497 (2001) | -6010.30 | [-6016.09, -6004.93] | 11930 (2430) | 329.97 | 0% | **z**, **HPD** |
| `likelihood` | -6002.92 | [-6008.82, -5997.76] | 7310 (1698) | -6002.95 | [-6008.86, -5997.82] | 11550 (2506) | 0.55 | 100% | ok |
| `prior` | 6.47 | [4.175, 8.223] | 8706 (1950) | -7.349 | [-9.453, -5.41] | 11009 (2614) | 892.66 | 0% | **z**, **HPD** |
| `treeLikelihood.coding` | -4972.43 | [-4980.59, -4964.40] | 11586 (2840) | -4972.34 | [-4980.62, -4964.24] | 15105 (3494) | 1.63 | 100% | ok |
| `treeLikelihood.noncoding` | -1030.49 | [-1037.48, -1023.89] | 12667 (2977) | -1030.60 | [-1037.47, -1023.82] | 15163 (3539) | 2.62 | 100% | ok |
| `TreeHeight → Tree.height` | 0.2223 | [0.2045, 0.2413] | 16019 (3529) | 0.2226 | [0.2038, 0.2407] | 16761 (3683) | 2.48 | 98% | ok |
| `YuleModel` | 11.24 | [9.547, 12.41] | 17592 (4200) | 11.25 | [9.58, 12.4] | 17401 (4224) | 1.59 | 100% | ok |
| `birthRate` | 8.657 | [3.967, 13.61] | 17439 (4050) | 8.618 | [4.012, 13.46] | 17744 (4241) | 1.45 | 100% | ok |
| `rateAC` | 0.327 | [0.2758, 0.3834] | 3548 (778) | 0.327 | [0.272, 0.3794] | 6252 (1289) | 0.09 | 97% | ok |
| `rateAG` | 0.4276 | [0.3594, 0.5007] | 3012 (645) | 0.4273 | [0.3552, 0.4971] | 6575 (1557) | 0.40 | 97% | ok |
| `rateAT` | 0.162 | [0.1225, 0.202] | 3788 (760) | 0.1627 | [0.1218, 0.2026] | 7461 (1634) | 1.70 | 100% | ok |
| `rateCG` | 0.04214 | [0.02026, 0.0676] | 3895 (824) | 0.04226 | [0.01908, 0.06607] | 7534 (1541) | 0.53 | 97% | ok |
| `rateGT` | 0.02202 | [0.005579, 0.0389] | 2740 (583) | 0.0218 | [0.006941, 0.04027] | 7401 (1715) | 1.12 | 96% | ok |

### Replicate agreement (baseline noise): `primate-mtDNA-SYM.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -5996.41, -5996.36, -5996.48, -5996.56 | 2.22 | -6010.36, -6010.20, -6010.34, -6010.29 | 2.04 |
| `likelihood` | -6002.86, -6002.79, -6002.98, -6003.07 | 2.89 | -6002.99, -6002.85, -6003.00, -6002.95 | 2.01 |
| `prior` | 6.444, 6.43, 6.5, 6.508 | 2.30 | -7.376, -7.349, -7.332, -7.339 | 1.53 |
| `treeLikelihood.coding` | -4972.47, -4972.25, -4972.41, -4972.59 | 3.02 | -4972.31, -4972.32, -4972.41, -4972.32 | 1.02 |
| `treeLikelihood.noncoding` | -1030.39, -1030.53, -1030.57, -1030.48 | 2.09 | -1030.67, -1030.53, -1030.59, -1030.62 | 1.84 |
| `TreeHeight → Tree.height` | 0.2223, 0.2225, 0.2223, 0.2222 | 1.39 | 0.2226, 0.2225, 0.2226, 0.2225 | 0.73 |
| `YuleModel` | 11.23, 11.23, 11.24, 11.25 | 1.07 | 11.23, 11.26, 11.26, 11.25 | 1.80 |
| `birthRate` | 8.656, 8.61, 8.757, 8.604 | 2.76 | 8.64, 8.581, 8.589, 8.663 | 1.55 |
| `rateAC` | 0.3253, 0.3267, 0.328, 0.3281 | 2.19 | 0.327, 0.3265, 0.3268, 0.3276 | 1.06 |
| `rateAG` | 0.4267, 0.4265, 0.4297, 0.4275 | 1.81 | 0.4284, 0.4276, 0.4266, 0.4265 | 1.46 |
| `rateAT` | 0.1611, 0.1609, 0.1633, 0.1625 | 2.65 | 0.1629, 0.1628, 0.1624, 0.1625 | 0.68 |
| `rateCG` | 0.04167, 0.04202, 0.04247, 0.0424 | 1.50 | 0.04225, 0.04235, 0.04216, 0.0423 | 0.48 |
| `rateGT` | 0.02184, 0.02137, 0.02243, 0.02244 | 2.36 | 0.02189, 0.02161, 0.02185, 0.02184 | 0.92 |

## Trees: `primate.trees`

18004 trees (beast2) and 18004 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.009, beast3 0.007.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (10 taxa)} | 10 | 0.934 | 0.938 | 0.004 | ok |
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
| beast2 | 8m37s | 8497 | 59141 | 19069 (`rateGT`) |
| beast3 | 7m19s | 11930 | 97765 | 51238 (`rateAC`) |

Run-time ratio beast3 / beast2: 0.85

