# Posterior comparison: C30-resume-vs-uninterrupted

**Verdict: matched**

- uninterrupted: `beast3/log/C30/rep1`, `beast3/log/C30/rep2`
- resumed: `beast3/log/C30_resume/rep1`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 638; max z: 1.553; max clade |Δp|: 0.006

## Findings

- **WARN** resumed has only 1 replicate (README asks for >= 2)
- **NOTE** resumed rep1: no beast.out
- **NOTE** Trace log file names differ: uninterrupted `CN_bN_rN.log` paired with resumed `CN_bN_resume.log`
- **NOTE** tree files read from `/Users/adru001/Library/CloudStorage/Dropbox/beast3-test`
- **NOTE** Tree file names differ: uninterrupted `CN_bN_rN-noncoding.trees` paired with resumed `CN_bN_resume-noncoding.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| uninterrupted | rep1 | `beast3/log/C30/rep1/C30_b3_r1.log` | 10001 (9001) | 2000 | 2.8.0 rc2 | yes | 7m16s |  |
| uninterrupted | rep2 | `beast3/log/C30/rep2/C30_b3_r2.log` | 10001 (9001) | 2000 | 2.8.0 rc2 | yes | 2m59s |  |
| resumed | rep1 | `beast3/log/C30_resume/rep1/C30_b3_resume.log` | 10001 (9001) | 2000 | – | – | – |  |

## Parameters: `CN_bN_rN.log / CN_bN_resume.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | uninterrupted mean | uninterrupted 95% HPD | uninterrupted ESS | resumed mean | resumed 95% HPD | resumed ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5992.45 | [-5998.15, -5987.42] | 6704 (3210) | -5992.47 | [-5997.89, -5987.32] | 2964 (2964) | 0.18 | 99% | ok |
| `likelihood` | -5996.13 | [-6001.67, -5991.31] | 6535 (3036) | -5996.14 | [-6001.54, -5991.38] | 2828 (2828) | 0.18 | 100% | ok |
| `prior` | 3.676 | [2.033, 4.902] | 14361 (6650) | 3.676 | [2.092, 4.885] | 7744 (7744) | 0.02 | 100% | ok |
| `treeLikelihood.1stpos` | -1442.71 | [-1449.09, -1436.69] | 3384 (1670) | -1442.68 | [-1449.09, -1436.63] | 1968 (1968) | 0.33 | 100% | ok |
| `treeLikelihood.2ndpos` | -1060.46 | [-1073.98, -1047.97] | 5155 (2452) | -1060.50 | [-1073.82, -1047.86] | 2516 (2516) | 0.22 | 100% | ok |
| `treeLikelihood.3rdpos` | -2457.63 | [-2479.82, -2436.04] | 9383 (4078) | -2457.68 | [-2479.64, -2436.09] | 3909 (3909) | 0.22 | 100% | ok |
| `treeLikelihood.noncoding` | -1035.32 | [-1043.62, -1027.21] | 6944 (3055) | -1035.28 | [-1043.34, -1026.82] | 2639 (2639) | 0.43 | 98% | ok |
| `Tree.height` | 0.251 | [0.2301, 0.2726] | 13575 (5930) | 0.2509 | [0.2296, 0.2725] | 7766 (7766) | 1.17 | 100% | ok |
| `Tree.treeLength` | 1.549 | [1.454, 1.646] | 13854 (6406) | 1.548 | [1.452, 1.646] | 7006 (7006) | 1.55 | 100% | ok |
| `YuleModel` | 10.07 | [8.454, 11.24] | 17378 (8377) | 10.08 | [8.387, 11.29] | 9001 (9001) | 0.44 | 100% | ok |
| `birthRate` | 7.053 | [3.303, 11.36] | 16396 (7677) | 7.064 | [3.13, 11.22] | 8433 (8433) | 0.39 | 98% | ok |
| `kappa` | 5.014 | [4.362, 5.655] | 4844 (2388) | 5.014 | [4.349, 5.671] | 2277 (2277) | 0.00 | 100% | ok |
| `freqParameter.1` | 0.3123 | [0.2902, 0.3326] | 1324 (638) | 0.3127 | [0.2918, 0.3349] | 823 (823) | 0.92 | 96% | ok |
| `freqParameter.2` | 0.2921 | [0.2717, 0.3114] | 1645 (743) | 0.2919 | [0.2725, 0.3132] | 669 (669) | 0.52 | 98% | ok |
| `freqParameter.3` | 0.1056 | [0.09359, 0.1177] | 1906 (834) | 0.1055 | [0.09267, 0.1173] | 871 (871) | 0.65 | 98% | ok |
| `freqParameter.4` | 0.29 | [0.2716, 0.3099] | 1682 (830) | 0.2899 | [0.2692, 0.3087] | 762 (762) | 0.09 | 97% | ok |

### Replicate agreement (baseline noise): `CN_bN_rN.log / CN_bN_resume.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | uninterrupted rep means | uninterrupted max z | resumed rep means | resumed max z |
|---|---|---:|---|---:|
| `posterior` | -5992.48, -5992.43 | 0.68 | -5992.47 | – |
| `likelihood` | -5996.16, -5996.10 | 0.76 | -5996.14 | – |
| `prior` | 3.678, 3.674 | 0.35 | 3.676 | – |
| `treeLikelihood.1stpos` | -1442.65, -1442.77 | 1.08 | -1442.68 | – |
| `treeLikelihood.2ndpos` | -1060.49, -1060.43 | 0.32 | -1060.50 | – |
| `treeLikelihood.3rdpos` | -2457.72, -2457.55 | 0.74 | -2457.68 | – |
| `treeLikelihood.noncoding` | -1035.29, -1035.35 | 0.61 | -1035.28 | – |
| `Tree.height` | 0.251, 0.2511 | 0.28 | 0.2509 | – |
| `Tree.treeLength` | 1.548, 1.549 | 0.35 | 1.548 | – |
| `YuleModel` | 10.07, 10.07 | 0.08 | 10.08 | – |
| `birthRate` | 7.045, 7.061 | 0.50 | 7.064 | – |
| `kappa` | 5.016, 5.012 | 0.43 | 5.014 | – |
| `freqParameter.1` | 0.3124, 0.3121 | 0.51 | 0.3127 | – |
| `freqParameter.2` | 0.292, 0.2922 | 0.44 | 0.2919 | – |
| `freqParameter.3` | 0.1058, 0.1055 | 0.84 | 0.1055 | – |
| `freqParameter.4` | 0.2898, 0.2901 | 0.68 | 0.2899 | – |

## Trees: `CN_bN_rN-noncoding.trees / CN_bN_resume-noncoding.trees`

14096 trees (uninterrupted) and 9001 trees (resumed) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: uninterrupted 0.003, resumed –.

| Clade | Size | p uninterrupted | p resumed | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Gorilla, Homo_sapiens, Hylobates, M._fascicularis, M._mulatta, M._sylvanus, … (10 taxa)} | 10 | 0.948 | 0.954 | 0.006 | ok |
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
| uninterrupted | 10m15s | 6704 | 39254 | 7754 (`freqParameter.1`) |

