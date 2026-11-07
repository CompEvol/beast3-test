# Posterior comparison: C01-tall7-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C01-tall7/rep1`, `beast3/log/C01-tall7/rep2`
- slide: `beast3/log/C01-tall7-slide/rep1`, `beast3/log/C01-tall7-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3068; max z: 1.403; max clade |Δp|: 0.022

## Findings

- **NOTE** Trace log file names differ: default `CN-tallN.log` paired with slide `CN-tallN-slide.log`
- **NOTE** Tree file names differ: default `CN-tallN-anolis.trees` paired with slide `CN-tallN-slide-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C01-tall7/rep1/C01-tall7.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m01s |  |
| default | rep2 | `beast3/log/C01-tall7/rep2/C01-tall7.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m01s |  |
| slide | rep1 | `beast3/log/C01-tall7-slide/rep1/C01-tall7-slide.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |
| slide | rep2 | `beast3/log/C01-tall7-slide/rep2/C01-tall7-slide.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m01s |  |

## Parameters: `CN-tallN.log / CN-tallN-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23799.67 | [-23807.85, -23792.44] | 8628 (4148) | -23799.77 | [-23807.86, -23792.29] | 6934 (3127) | 1.40 | 100% | ok |
| `likelihood` | -23386.38 | [-23394.29, -23379.25] | 8346 (4029) | -23386.47 | [-23394.44, -23379.17] | 6763 (3068) | 1.33 | 100% | ok |
| `prior` | -413.29 | [-414.94, -412.01] | 42062 (20626) | -413.30 | [-415.00, -411.99] | 43352 (21613) | 0.94 | 100% | ok |
| `treeLikelihood` | -23386.38 | [-23394.29, -23379.25] | 8346 (4029) | -23386.47 | [-23394.44, -23379.17] | 6763 (3068) | 1.33 | 100% | ok |
| `Tree.height` | 1.925e+06 | [1.849e+06, 2.005e+06] | 10753 (5367) | 1.925e+06 | [1.848e+06, 2.004e+06] | 9823 (4593) | 0.13 | 99% | ok |
| `Tree.treeLength` | 3.631e+07 | [3.525e+07, 3.738e+07] | 47458 (23539) | 3.631e+07 | [3.525e+07, 3.738e+07] | 45895 (22790) | 0.88 | 100% | ok |
| `YuleModel` | -422.60 | [-424.25, -421.26] | 41456 (20165) | -422.61 | [-424.34, -421.27] | 42819 (21248) | 0.74 | 100% | ok |
| `birthRate` | 7.701e-07 | [4.975e-07, 1.058e-06] | 43309 (21513) | 7.711e-07 | [4.967e-07, 1.064e-06] | 42537 (20984) | 0.98 | 100% | ok |

### Replicate agreement (baseline noise): `CN-tallN.log / CN-tallN-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -23799.65, -23799.70 | 0.64 | -23799.75, -23799.78 | 0.37 |
| `likelihood` | -23386.35, -23386.41 | 0.62 | -23386.44, -23386.49 | 0.50 |
| `prior` | -413.29, -413.30 | 0.24 | -413.31, -413.29 | 1.58 |
| `treeLikelihood` | -23386.35, -23386.41 | 0.62 | -23386.44, -23386.49 | 0.50 |
| `Tree.height` | 1.926e+06, 1.925e+06 | 0.25 | 1.925e+06, 1.925e+06 | 0.31 |
| `Tree.treeLength` | 3.631e+07, 3.630e+07 | 1.51 | 3.631e+07, 3.630e+07 | 0.43 |
| `YuleModel` | -422.60, -422.60 | 0.26 | -422.61, -422.60 | 1.74 |
| `birthRate` | 7.701e-07, 7.702e-07 | 0.05 | 7.707e-07, 7.715e-07 | 0.57 |

## Trees: `CN-tallN-anolis.trees / CN-tallN-slide-anolis.trees`

5402 trees (default) and 5402 trees (slide) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: default 0.043, slide 0.052.

| Clade | Size | p default | p slide | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.745 | 0.723 | 0.022 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.417 | 0.435 | 0.018 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.573 | 0.556 | 0.017 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.912 | 0.902 | 0.010 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.586 | 0.594 | 0.008 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.410 | 0.403 | 0.007 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.091 | 0.084 | 0.006 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.080 | 0.085 | 0.005 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.187 | 0.183 | 0.004 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.997 | 0.999 | 0.002 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.088 | 0.090 | 0.002 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.629 | 0.631 | 0.001 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.998 | 0.998 | 0.001 | ok |
| {Anolis_insolitus, Anolis_olssoni} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 0.999 | 0.999 | 0.000 | ok |
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

(3 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 4m03s | 8628 | 127964 | 123789 (`likelihood`) |
| slide | 4m03s | 6934 | 102728 | 100190 (`likelihood`) |

Run-time ratio slide / default: 1.00

