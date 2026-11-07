# Posterior comparison: C01-tall7-slide-sqrt-vs-scale

**Verdict: matched**

- scale: `beast3/log/C01-tall7-scale/rep1`, `beast3/log/C01-tall7-scale/rep2`
- sqrt: `beast3/log/C01-tall7-slide-sqrt/rep1`, `beast3/log/C01-tall7-slide-sqrt/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3831; max z: 2.487; max clade |Δp|: 0.067

## Findings

- **NOTE** Trace log file names differ: scale `CN-tallN-scale.log` paired with sqrt `CN-tallN-slide-sqrt.log`
- **NOTE** Tree file names differ: scale `CN-tallN-scale-anolis.trees` paired with sqrt `CN-tallN-slide-sqrt-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| scale | rep1 | `beast3/log/C01-tall7-scale/rep1/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| scale | rep2 | `beast3/log/C01-tall7-scale/rep2/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| sqrt | rep1 | `beast3/log/C01-tall7-slide-sqrt/rep1/C01-tall7-slide-sqrt.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m50s |  |
| sqrt | rep2 | `beast3/log/C01-tall7-slide-sqrt/rep2/C01-tall7-slide-sqrt.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m50s |  |

## Parameters: `CN-tallN-scale.log / CN-tallN-slide-sqrt.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | scale mean | scale 95% HPD | scale ESS | sqrt mean | sqrt 95% HPD | sqrt ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23799.72 | [-23807.71, -23792.07] | 8580 (3831) | -23799.87 | [-23808.01, -23792.26] | 10602 (4568) | 2.49 | 99% | ok |
| `likelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.57 | [-23394.40, -23379.03] | 10356 (4497) | 2.37 | 100% | ok |
| `prior` | -413.30 | [-414.98, -412.00] | 42378 (21145) | -413.30 | [-415.00, -412.00] | 42060 (20839) | 1.50 | 100% | ok |
| `treeLikelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.57 | [-23394.40, -23379.03] | 10356 (4497) | 2.37 | 100% | ok |
| `Tree.height` | 1.925e+06 | [1.846e+06, 2.003e+06] | 15338 (7147) | 1.926e+06 | [1.847e+06, 2.005e+06] | 15493 (7692) | 1.20 | 99% | ok |
| `Tree.treeLength` | 3.630e+07 | [3.524e+07, 3.736e+07] | 47907 (23366) | 3.631e+07 | [3.526e+07, 3.738e+07] | 47120 (23475) | 0.72 | 99% | ok |
| `YuleModel` | -422.60 | [-424.29, -421.29] | 41916 (20869) | -422.61 | [-424.28, -421.23] | 41758 (20479) | 2.04 | 100% | ok |
| `birthRate` | 7.726e-07 | [5.021e-07, 1.065e-06] | 43478 (21672) | 7.704e-07 | [4.935e-07, 1.063e-06] | 42630 (21186) | 2.22 | 100% | ok |

### Replicate agreement (baseline noise): `CN-tallN-scale.log / CN-tallN-slide-sqrt.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | scale rep means | scale max z | sqrt rep means | sqrt max z |
|---|---|---:|---|---:|
| `posterior` | -23799.70, -23799.75 | 0.53 | -23799.82, -23799.92 | 1.21 |
| `likelihood` | -23386.41, -23386.45 | 0.40 | -23386.52, -23386.62 | 1.21 |
| `prior` | -413.29, -413.30 | 1.45 | -413.30, -413.30 | 0.08 |
| `treeLikelihood` | -23386.41, -23386.45 | 0.40 | -23386.52, -23386.62 | 1.21 |
| `Tree.height` | 1.925e+06, 1.926e+06 | 1.25 | 1.926e+06, 1.926e+06 | 0.04 |
| `Tree.treeLength` | 3.630e+07, 3.631e+07 | 1.86 | 3.631e+07, 3.631e+07 | 0.31 |
| `YuleModel` | -422.60, -422.60 | 1.19 | -422.61, -422.61 | 0.13 |
| `birthRate` | 7.718e-07, 7.734e-07 | 1.14 | 7.698e-07, 7.711e-07 | 0.96 |

## Trees: `CN-tallN-scale-anolis.trees / CN-tallN-slide-sqrt-anolis.trees`

5402 trees (scale) and 5402 trees (sqrt) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: scale 0.013, sqrt 0.050.

| Clade | Size | p scale | p sqrt | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_coelestinus, Anolis_cuvieri, Anolis_equestris, … (12 taxa)} | 12 | 0.000 | 0.067 | 0.067 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.907 | 0.875 | 0.032 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.621 | 0.604 | 0.017 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.733 | 0.718 | 0.015 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.552 | 0.567 | 0.015 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.439 | 0.426 | 0.014 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.581 | 0.591 | 0.010 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.414 | 0.405 | 0.009 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.085 | 0.077 | 0.008 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.093 | 0.085 | 0.008 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.086 | 0.082 | 0.004 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.999 | 0.998 | 0.001 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.190 | 0.190 | 0.001 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.999 | 0.998 | 0.001 | ok |
| {Anolis_insolitus, Anolis_olssoni} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_aliniger, Anolis_coelestinus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_alutaceus, Anolis_vanidicus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_angusticeps, Anolis_paternus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_barahonae, Anolis_cuvieri} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_brevirostris, Anolis_distichus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_equestris, Anolis_luteogularis} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_garmani, Anolis_grahami} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_marcanoi, Anolis_strahmi} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_ophiolepis, Anolis_sagrei} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_angusticeps, Anolis_loysiana, Anolis_paternus} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_cristatellus, Anolis_krugi, Anolis_stratulus} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_paternus, Anolis_vanidicus} | 5 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, Anolis_krugi, Anolis_stratulus} | 5 | 1.000 | 1.000 | 0.000 | ok |

(4 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| scale | 3m23s | 8580 | 152417 | 149685 (`likelihood`) |
| sqrt | 3m39s | 10602 | 173980 | 169939 (`likelihood`) |

Run-time ratio sqrt / scale: 1.08

