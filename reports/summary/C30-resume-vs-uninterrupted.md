# Posterior comparison: C30-resume-vs-uninterrupted

**Verdict: matched (run problems)**

- uninterrupted: `beast3/log/C30/rep1`, `beast3/log/C30/rep2`
- resumed: `beast3/log/C30_resume/rep1`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 323; max z: 0.863; max clade |Δp|: –

## Findings

- **FAIL** uninterrupted rep2: beast.out has no 'End likelihood' line (run did not finish?)
- **WARN** resumed has only 1 replicate (README asks for >= 2)
- **NOTE** resumed rep1: no beast.out
- **NOTE** Trace log file names differ: uninterrupted `CN_bN_rN.log` paired with resumed `CN_bN_resume.log`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| uninterrupted | rep1 | `beast3/log/C30/rep1/C30_b3_r1.log` | 10001 (9001) | 2000 | 2.8.0 rc2 | yes | 7m16s |  |
| uninterrupted | rep2 | `beast3/log/C30/rep2/C30_b3_r2.log` | 5661 (5095) | 2000 | 2.8.0 rc2 | **no** | – |  |
| resumed | rep1 | `beast3/log/C30_resume/rep1/C30_b3_resume.log` | 10001 (9001) | 2000 | – | – | – |  |

## Parameters: `CN_bN_rN.log / CN_bN_resume.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | uninterrupted mean | uninterrupted 95% HPD | uninterrupted ESS | resumed mean | resumed 95% HPD | resumed ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -5992.45 | [-5998.12, -5987.42] | 5099 (1889) | -5992.47 | [-5997.89, -5987.32] | 2964 (2964) | 0.30 | 99% | ok |
| `likelihood` | -5996.12 | [-6001.72, -5991.37] | 4793 (1756) | -5996.14 | [-6001.54, -5991.38] | 2828 (2828) | 0.29 | 100% | ok |
| `prior` | 3.677 | [2.041, 4.922] | 11037 (4387) | 3.676 | [2.092, 4.885] | 7744 (7744) | 0.12 | 100% | ok |
| `treeLikelihood.1stpos` | -1442.68 | [-1449.14, -1436.69] | 2545 (875) | -1442.68 | [-1449.09, -1436.63] | 1968 (1968) | 0.07 | 100% | ok |
| `treeLikelihood.2ndpos` | -1060.44 | [-1073.64, -1047.65] | 3815 (1363) | -1060.50 | [-1073.82, -1047.86] | 2516 (2516) | 0.36 | 99% | ok |
| `treeLikelihood.3rdpos` | -2457.76 | [-2479.81, -2436.19] | 7197 (3119) | -2457.68 | [-2479.64, -2436.09] | 3909 (3909) | 0.35 | 100% | ok |
| `treeLikelihood.noncoding` | -1035.25 | [-1043.51, -1027.21] | 5458 (2403) | -1035.28 | [-1043.34, -1026.82] | 2639 (2639) | 0.28 | 99% | ok |
| `Tree.height` | 0.251 | [0.2307, 0.2728] | 11025 (5095) | 0.2509 | [0.2296, 0.2725] | 7766 (7766) | 0.86 | 99% | ok |
| `Tree.treeLength` | 1.548 | [1.455, 1.644] | 11002 (4597) | 1.548 | [1.452, 1.646] | 7006 (7006) | 0.76 | 100% | ok |
| `YuleModel` | 10.08 | [8.428, 11.23] | 13472 (5095) | 10.08 | [8.387, 11.29] | 9001 (9001) | 0.14 | 100% | ok |
| `birthRate` | 7.055 | [3.244, 11.38] | 12898 (4179) | 7.064 | [3.13, 11.22] | 8433 (8433) | 0.31 | 99% | ok |
| `kappa` | 5.014 | [4.363, 5.669] | 3825 (1369) | 5.014 | [4.349, 5.671] | 2277 (2277) | 0.00 | 100% | ok |
| `freqParameter.1` | 0.3126 | [0.2893, 0.3326] | 961 (323) | 0.3127 | [0.2918, 0.3349] | 823 (823) | 0.31 | 95% | ok |
| `freqParameter.2` | 0.2917 | [0.2717, 0.3111] | 1088 (345) | 0.2919 | [0.2725, 0.3132] | 669 (669) | 0.31 | 98% | ok |
| `freqParameter.3` | 0.1056 | [0.09408, 0.1186] | 1386 (552) | 0.1055 | [0.09267, 0.1173] | 871 (871) | 0.41 | 95% | ok |
| `freqParameter.4` | 0.2901 | [0.2715, 0.3097] | 1311 (459) | 0.2899 | [0.2692, 0.3087] | 762 (762) | 0.46 | 97% | ok |

### Replicate agreement (baseline noise): `CN_bN_rN.log / CN_bN_resume.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | uninterrupted rep means | uninterrupted max z | resumed rep means | resumed max z |
|---|---|---:|---|---:|
| `posterior` | -5992.48, -5992.39 | 1.09 | -5992.47 | – |
| `likelihood` | -5996.16, -5996.06 | 1.12 | -5996.14 | – |
| `prior` | 3.678, 3.676 | 0.11 | 3.676 | – |
| `treeLikelihood.1stpos` | -1442.65, -1442.72 | 0.47 | -1442.68 | – |
| `treeLikelihood.2ndpos` | -1060.49, -1060.34 | 0.68 | -1060.50 | – |
| `treeLikelihood.3rdpos` | -2457.72, -2457.83 | 0.40 | -2457.68 | – |
| `treeLikelihood.noncoding` | -1035.29, -1035.18 | 0.93 | -1035.28 | – |
| `Tree.height` | 0.251, 0.251 | 0.23 | 0.2509 | – |
| `Tree.treeLength` | 1.548, 1.547 | 1.18 | 1.548 | – |
| `YuleModel` | 10.07, 10.08 | 0.69 | 10.08 | – |
| `birthRate` | 7.045, 7.074 | 0.72 | 7.064 | – |
| `kappa` | 5.016, 5.01 | 0.52 | 5.014 | – |
| `freqParameter.1` | 0.3124, 0.3128 | 0.49 | 0.3127 | – |
| `freqParameter.2` | 0.292, 0.2912 | 1.24 | 0.2919 | – |
| `freqParameter.3` | 0.1058, 0.1053 | 1.43 | 0.1055 | – |
| `freqParameter.4` | 0.2898, 0.2907 | 1.58 | 0.2899 | – |

## Speed

Run time not available (no `Total calculation time` in beast.out).

