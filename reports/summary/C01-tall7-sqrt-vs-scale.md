# Posterior comparison: C01-tall7-sqrt-vs-scale

**Verdict: matched**

- scale: `beast3/log/C01-tall7-scale/rep1`, `beast3/log/C01-tall7-scale/rep2`
- sqrt: `beast3/log/C01-tall7-sqrt/rep1`, `beast3/log/C01-tall7-sqrt/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3831; max z: 2.195; max clade |Δp|: 0.018

## Findings

- **NOTE** Trace log file names differ: scale `CN-tallN-scale.log` paired with sqrt `CN-tallN-sqrt.log`
- **NOTE** Tree file names differ: scale `CN-tallN-scale-anolis.trees` paired with sqrt `CN-tallN-sqrt-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| scale | rep1 | `beast3/log/C01-tall7-scale/rep1/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| scale | rep2 | `beast3/log/C01-tall7-scale/rep2/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| sqrt | rep1 | `beast3/log/C01-tall7-sqrt/rep1/C01-tall7-sqrt.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m50s |  |
| sqrt | rep2 | `beast3/log/C01-tall7-sqrt/rep2/C01-tall7-sqrt.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m50s |  |

## Parameters: `CN-tallN-scale.log / CN-tallN-sqrt.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | scale mean | scale 95% HPD | scale ESS | sqrt mean | sqrt 95% HPD | sqrt ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23799.72 | [-23807.71, -23792.07] | 8580 (3831) | -23799.82 | [-23807.96, -23792.26] | 9006 (4367) | 1.51 | 99% | ok |
| `likelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.51 | [-23394.49, -23379.14] | 8833 (4374) | 1.37 | 100% | ok |
| `prior` | -413.30 | [-414.98, -412.00] | 42378 (21145) | -413.31 | [-414.97, -411.97] | 42476 (21220) | 1.80 | 100% | ok |
| `treeLikelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.51 | [-23394.49, -23379.14] | 8833 (4374) | 1.37 | 100% | ok |
| `Tree.height` | 1.925e+06 | [1.846e+06, 2.003e+06] | 15338 (7147) | 1.925e+06 | [1.850e+06, 2.006e+06] | 17448 (8660) | 0.03 | 98% | ok |
| `Tree.treeLength` | 3.630e+07 | [3.524e+07, 3.736e+07] | 47907 (23366) | 3.631e+07 | [3.525e+07, 3.737e+07] | 47700 (23727) | 0.86 | 100% | ok |
| `YuleModel` | -422.60 | [-424.29, -421.29] | 41916 (20869) | -422.61 | [-424.27, -421.24] | 41890 (20870) | 2.20 | 99% | ok |
| `birthRate` | 7.726e-07 | [5.021e-07, 1.065e-06] | 43478 (21672) | 7.711e-07 | [4.920e-07, 1.060e-06] | 43150 (21222) | 1.60 | 99% | ok |

### Replicate agreement (baseline noise): `CN-tallN-scale.log / CN-tallN-sqrt.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | scale rep means | scale max z | sqrt rep means | sqrt max z |
|---|---|---:|---|---:|
| `posterior` | -23799.70, -23799.75 | 0.53 | -23799.74, -23799.89 | 1.78 |
| `likelihood` | -23386.41, -23386.45 | 0.40 | -23386.43, -23386.60 | 2.01 |
| `prior` | -413.29, -413.30 | 1.45 | -413.31, -413.30 | 2.14 |
| `treeLikelihood` | -23386.41, -23386.45 | 0.40 | -23386.43, -23386.60 | 2.01 |
| `Tree.height` | 1.925e+06, 1.926e+06 | 1.25 | 1.925e+06, 1.925e+06 | 0.16 |
| `Tree.treeLength` | 3.630e+07, 3.631e+07 | 1.86 | 3.631e+07, 3.631e+07 | 0.29 |
| `YuleModel` | -422.60, -422.60 | 1.19 | -422.62, -422.60 | 2.19 |
| `birthRate` | 7.718e-07, 7.734e-07 | 1.14 | 7.710e-07, 7.711e-07 | 0.09 |

## Trees: `CN-tallN-scale-anolis.trees / CN-tallN-sqrt-anolis.trees`

5402 trees (scale) and 5402 trees (sqrt) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: scale 0.013, sqrt 0.063.

| Clade | Size | p scale | p sqrt | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.733 | 0.715 | 0.018 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.907 | 0.896 | 0.011 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.190 | 0.181 | 0.009 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.581 | 0.590 | 0.009 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.414 | 0.407 | 0.007 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.552 | 0.558 | 0.005 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.093 | 0.088 | 0.005 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.085 | 0.090 | 0.005 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.621 | 0.625 | 0.004 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.439 | 0.435 | 0.004 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.999 | 0.998 | 0.001 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.999 | 0.998 | 0.001 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.086 | 0.086 | 0.000 | ok |
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
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_paternus, Anolis_vanidicus} | 5 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, Anolis_krugi, Anolis_stratulus} | 5 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis, Anolis_occultus} | 6 | 1.000 | 1.000 | 0.000 | ok |

(3 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| scale | 3m23s | 8580 | 152417 | 149685 (`likelihood`) |
| sqrt | 3m39s | 9006 | 147720 | 144890 (`likelihood`) |

Run-time ratio sqrt / scale: 1.08

