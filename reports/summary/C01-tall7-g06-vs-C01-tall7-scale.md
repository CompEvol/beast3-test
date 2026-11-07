# Posterior comparison: C01-tall7-g06-vs-C01-tall7-scale

**Verdict: matched**

- ref: `beast3/log/C01-tall7-scale/rep1`, `beast3/log/C01-tall7-scale/rep2`
- g06: `beast3/log/C01-tall7-g06/rep1`, `beast3/log/C01-tall7-g06/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3831; max z: 1.23; max clade |Δp|: 0.053

## Findings

- **NOTE** Trace log file names differ: ref `CN-tallN-scale.log` paired with g06 `CN-tallN-gN.log`
- **NOTE** Tree file names differ: ref `CN-tallN-scale-anolis.trees` paired with g06 `CN-tallN-gN-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| ref | rep1 | `beast3/log/C01-tall7-scale/rep1/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| ref | rep2 | `beast3/log/C01-tall7-scale/rep2/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| g06 | rep1 | `beast3/log/C01-tall7-g06/rep1/C01-tall7-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |
| g06 | rep2 | `beast3/log/C01-tall7-g06/rep2/C01-tall7-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m45s |  |

## Parameters: `CN-tallN-scale.log / CN-tallN-gN.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | ref mean | ref 95% HPD | ref ESS | g06 mean | g06 95% HPD | g06 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23799.72 | [-23807.71, -23792.07] | 8580 (3831) | -23799.78 | [-23807.89, -23792.25] | 11317 (5126) | 0.98 | 99% | ok |
| `likelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.48 | [-23394.33, -23379.05] | 11309 (5225) | 0.89 | 100% | ok |
| `prior` | -413.30 | [-414.98, -412.00] | 42378 (21145) | -413.30 | [-414.95, -411.96] | 42974 (21451) | 1.12 | 99% | ok |
| `treeLikelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.48 | [-23394.33, -23379.05] | 11309 (5225) | 0.89 | 100% | ok |
| `Tree.height` | 1.925e+06 | [1.846e+06, 2.003e+06] | 15338 (7147) | 1.925e+06 | [1.848e+06, 2.004e+06] | 16173 (7950) | 0.27 | 99% | ok |
| `Tree.treeLength` | 3.630e+07 | [3.524e+07, 3.736e+07] | 47907 (23366) | 3.630e+07 | [3.524e+07, 3.736e+07] | 45950 (22788) | 0.20 | 100% | ok |
| `YuleModel` | -422.60 | [-424.29, -421.29] | 41916 (20869) | -422.61 | [-424.31, -421.27] | 41894 (20571) | 1.23 | 100% | ok |
| `birthRate` | 7.726e-07 | [5.021e-07, 1.065e-06] | 43478 (21672) | 7.723e-07 | [4.968e-07, 1.066e-06] | 42151 (21005) | 0.33 | 100% | ok |

### Replicate agreement (baseline noise): `CN-tallN-scale.log / CN-tallN-gN.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | ref rep means | ref max z | g06 rep means | g06 max z |
|---|---|---:|---|---:|
| `posterior` | -23799.70, -23799.75 | 0.53 | -23799.77, -23799.80 | 0.36 |
| `likelihood` | -23386.41, -23386.45 | 0.40 | -23386.46, -23386.50 | 0.53 |
| `prior` | -413.29, -413.30 | 1.45 | -413.31, -413.30 | 1.48 |
| `treeLikelihood` | -23386.41, -23386.45 | 0.40 | -23386.46, -23386.50 | 0.53 |
| `Tree.height` | 1.925e+06, 1.926e+06 | 1.25 | 1.925e+06, 1.925e+06 | 0.80 |
| `Tree.treeLength` | 3.630e+07, 3.631e+07 | 1.86 | 3.631e+07, 3.630e+07 | 2.17 |
| `YuleModel` | -422.60, -422.60 | 1.19 | -422.61, -422.60 | 1.65 |
| `birthRate` | 7.718e-07, 7.734e-07 | 1.14 | 7.718e-07, 7.729e-07 | 0.79 |

## Trees: `CN-tallN-scale-anolis.trees / CN-tallN-gN-anolis.trees`

5402 trees (ref) and 5402 trees (g06) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: ref 0.013, g06 0.053.

| Clade | Size | p ref | p g06 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, Anolis_krugi, … (12 taxa)} | 12 | 0.000 | 0.053 | 0.053 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.439 | 0.425 | 0.014 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.552 | 0.565 | 0.013 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.414 | 0.427 | 0.012 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.581 | 0.571 | 0.010 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.093 | 0.083 | 0.010 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.733 | 0.726 | 0.007 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.907 | 0.904 | 0.003 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.190 | 0.193 | 0.002 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.999 | 0.998 | 0.001 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 0.999 | 0.001 | ok |
| {Anolis_insolitus, Anolis_olssoni} | 2 | 1.000 | 0.999 | 0.001 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 0.999 | 0.999 | 0.001 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.999 | 0.999 | 0.001 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.621 | 0.620 | 0.001 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.086 | 0.085 | 0.001 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.085 | 0.085 | 0.000 | ok |
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

(4 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| ref | 3m23s | 8580 | 152417 | 149685 (`likelihood`) |
| g06 | 3m47s | 11317 | 179435 | 179305 (`likelihood`) |

Run-time ratio g06 / ref: 1.12

