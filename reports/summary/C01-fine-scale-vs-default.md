# Posterior comparison: C01-fine-scale-vs-default

**Verdict: matched**

- default: `beast3/log/C01-fine/rep1`, `beast3/log/C01-fine/rep2`
- scale: `beast3/log/C01-fine-scale/rep1`, `beast3/log/C01-fine-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3653; max z: 2.851; max clade |Δp|: 0.014

## Findings

- **NOTE** Trace log file names differ: default `CN-fine.log` paired with scale `CN-fine-scale.log`
- **NOTE** Tree file names differ: default `CN-fine-anolis.trees` paired with scale `CN-fine-scale-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C01-fine/rep1/C01-fine.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |
| default | rep2 | `beast3/log/C01-fine/rep2/C01-fine.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m01s |  |
| scale | rep1 | `beast3/log/C01-fine-scale/rep1/C01-fine-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m55s |  |
| scale | rep2 | `beast3/log/C01-fine-scale/rep2/C01-fine-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m51s |  |

## Parameters: `CN-fine.log / CN-fine-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23364.59 | [-23372.57, -23356.81] | 7603 (3774) | -23364.51 | [-23372.49, -23357.00] | 9096 (4465) | 1.12 | 100% | ok |
| `likelihood` | -23386.57 | [-23394.30, -23378.88] | 7434 (3653) | -23386.48 | [-23394.32, -23379.17] | 8826 (4335) | 1.38 | 100% | ok |
| `prior` | 21.98 | [20.34, 23.31] | 40914 (20157) | 21.97 | [20.3, 23.3] | 42404 (20573) | 2.85 | 100% | ok |
| `treeLikelihood` | -23386.57 | [-23394.30, -23378.88] | 7434 (3653) | -23386.48 | [-23394.32, -23379.17] | 8826 (4335) | 1.38 | 100% | ok |
| `Tree.height` | 0.1925 | [0.1849, 0.2003] | 11370 (5577) | 0.1926 | [0.1847, 0.2005] | 14334 (6655) | 1.03 | 100% | ok |
| `Tree.treeLength` | 3.63 | [3.528, 3.739] | 47843 (23837) | 3.631 | [3.522, 3.736] | 48228 (23631) | 0.93 | 99% | ok |
| `YuleModel` | 28.71 | [27.04, 30.04] | 40472 (19927) | 28.69 | [26.96, 30.03] | 41810 (20303) | 2.76 | 99% | ok |
| `birthRate` | 7.693 | [4.933, 10.54] | 42348 (21079) | 7.699 | [4.935, 10.62] | 41796 (20501) | 0.50 | 100% | ok |

### Replicate agreement (baseline noise): `CN-fine.log / CN-fine-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -23364.51, -23364.66 | 1.50 | -23364.51, -23364.52 | 0.13 |
| `likelihood` | -23386.50, -23386.64 | 1.53 | -23386.46, -23386.50 | 0.36 |
| `prior` | 21.98, 21.98 | 0.23 | 21.96, 21.98 | 2.50 |
| `treeLikelihood` | -23386.50, -23386.64 | 1.53 | -23386.46, -23386.50 | 0.36 |
| `Tree.height` | 0.1925, 0.1926 | 1.53 | 0.1926, 0.1926 | 0.50 |
| `Tree.treeLength` | 3.631, 3.63 | 0.35 | 3.631, 3.631 | 0.06 |
| `YuleModel` | 28.7, 28.71 | 0.40 | 28.68, 28.7 | 2.23 |
| `birthRate` | 7.689, 7.698 | 0.71 | 7.708, 7.689 | 1.26 |

## Trees: `CN-fine-anolis.trees / CN-fine-scale-anolis.trees`

5402 trees (default) and 5402 trees (scale) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: default 0.062, scale 0.016.

| Clade | Size | p default | p scale | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.723 | 0.736 | 0.014 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.888 | 0.900 | 0.013 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.616 | 0.628 | 0.012 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.563 | 0.571 | 0.009 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.189 | 0.181 | 0.008 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.427 | 0.420 | 0.007 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.083 | 0.078 | 0.005 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.086 | 0.090 | 0.004 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.586 | 0.585 | 0.001 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.997 | 0.998 | 0.001 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.410 | 0.411 | 0.001 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.084 | 0.085 | 0.001 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 0.999 | 1.000 | 0.001 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.997 | 0.997 | 0.000 | ok |
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
| default | 4m03s | 7603 | 112673 | 110166 (`likelihood`) |
| scale | 3m45s | 9096 | 145464 | 141148 (`likelihood`) |

Run-time ratio scale / default: 0.93

