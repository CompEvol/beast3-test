# Posterior comparison: C01-tall7-slide-g06-vs-C01-tall7-scale

**Verdict: matched**

- ref: `beast3/log/C01-tall7-scale/rep1`, `beast3/log/C01-tall7-scale/rep2`
- g06: `beast3/log/C01-tall7-slide-g06/rep1`, `beast3/log/C01-tall7-slide-g06/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3831; max z: 1.763; max clade |Δp|: 0.020

## Findings

- **NOTE** Trace log file names differ: ref `CN-tallN-scale.log` paired with g06 `CN-tallN-slide-gN.log`
- **NOTE** Tree file names differ: ref `CN-tallN-scale-anolis.trees` paired with g06 `CN-tallN-slide-gN-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| ref | rep1 | `beast3/log/C01-tall7-scale/rep1/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| ref | rep2 | `beast3/log/C01-tall7-scale/rep2/C01-tall7-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m41s |  |
| g06 | rep1 | `beast3/log/C01-tall7-slide-g06/rep1/C01-tall7-slide-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m45s |  |
| g06 | rep2 | `beast3/log/C01-tall7-slide-g06/rep2/C01-tall7-slide-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m45s |  |

## Parameters: `CN-tallN-scale.log / CN-tallN-slide-gN.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | ref mean | ref 95% HPD | ref ESS | g06 mean | g06 95% HPD | g06 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23799.72 | [-23807.71, -23792.07] | 8580 (3831) | -23799.81 | [-23807.99, -23792.39] | 9798 (4532) | 1.41 | 98% | ok |
| `likelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.51 | [-23394.47, -23379.24] | 9421 (4364) | 1.28 | 100% | ok |
| `prior` | -413.30 | [-414.98, -412.00] | 42378 (21145) | -413.30 | [-414.98, -411.96] | 43093 (21020) | 1.51 | 100% | ok |
| `treeLikelihood` | -23386.43 | [-23394.40, -23379.16] | 8426 (3840) | -23386.51 | [-23394.47, -23379.24] | 9421 (4364) | 1.28 | 100% | ok |
| `Tree.height` | 1.925e+06 | [1.846e+06, 2.003e+06] | 15338 (7147) | 1.925e+06 | [1.847e+06, 2.004e+06] | 15005 (7487) | 0.69 | 99% | ok |
| `Tree.treeLength` | 3.630e+07 | [3.524e+07, 3.736e+07] | 47907 (23366) | 3.630e+07 | [3.525e+07, 3.738e+07] | 47352 (23148) | 0.16 | 99% | ok |
| `YuleModel` | -422.60 | [-424.29, -421.29] | 41916 (20869) | -422.61 | [-424.29, -421.23] | 42649 (20916) | 1.76 | 100% | ok |
| `birthRate` | 7.726e-07 | [5.021e-07, 1.065e-06] | 43478 (21672) | 7.717e-07 | [5.059e-07, 1.076e-06] | 41717 (20212) | 0.94 | 99% | ok |

### Replicate agreement (baseline noise): `CN-tallN-scale.log / CN-tallN-slide-gN.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | ref rep means | ref max z | g06 rep means | g06 max z |
|---|---|---:|---|---:|
| `posterior` | -23799.70, -23799.75 | 0.53 | -23799.84, -23799.78 | 0.82 |
| `likelihood` | -23386.41, -23386.45 | 0.40 | -23386.53, -23386.48 | 0.69 |
| `prior` | -413.29, -413.30 | 1.45 | -413.31, -413.30 | 1.43 |
| `treeLikelihood` | -23386.41, -23386.45 | 0.40 | -23386.53, -23386.48 | 0.69 |
| `Tree.height` | 1.925e+06, 1.926e+06 | 1.25 | 1.925e+06, 1.925e+06 | 0.91 |
| `Tree.treeLength` | 3.630e+07, 3.631e+07 | 1.86 | 3.631e+07, 3.630e+07 | 0.43 |
| `YuleModel` | -422.60, -422.60 | 1.19 | -422.61, -422.61 | 1.08 |
| `birthRate` | 7.718e-07, 7.734e-07 | 1.14 | 7.728e-07, 7.706e-07 | 1.55 |

## Trees: `CN-tallN-scale-anolis.trees / CN-tallN-slide-gN-anolis.trees`

5402 trees (ref) and 5402 trees (g06) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: ref 0.013, g06 0.056.

| Clade | Size | p ref | p g06 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.552 | 0.572 | 0.020 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.439 | 0.422 | 0.017 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.733 | 0.721 | 0.012 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.907 | 0.895 | 0.012 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.581 | 0.593 | 0.011 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.414 | 0.403 | 0.011 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.190 | 0.180 | 0.011 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.085 | 0.095 | 0.009 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.621 | 0.629 | 0.008 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.093 | 0.086 | 0.007 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.086 | 0.082 | 0.004 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.999 | 0.998 | 0.001 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 0.999 | 0.001 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 0.999 | 0.999 | 0.000 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.999 | 0.999 | 0.000 | ok |
| {Anolis_aliniger, Anolis_coelestinus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_alutaceus, Anolis_vanidicus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_angusticeps, Anolis_paternus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_barahonae, Anolis_cuvieri} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_brevirostris, Anolis_distichus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_equestris, Anolis_luteogularis} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_garmani, Anolis_grahami} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_insolitus, Anolis_olssoni} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_marcanoi, Anolis_strahmi} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_ophiolepis, Anolis_sagrei} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_angusticeps, Anolis_loysiana, Anolis_paternus} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_cristatellus, Anolis_krugi, Anolis_stratulus} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_paternus, Anolis_vanidicus} | 5 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, Anolis_krugi, Anolis_stratulus} | 5 | 1.000 | 1.000 | 0.000 | ok |

(3 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| ref | 3m23s | 8580 | 152417 | 149685 (`likelihood`) |
| g06 | 3m30s | 9798 | 168013 | 161552 (`likelihood`) |

Run-time ratio g06 / ref: 1.04

