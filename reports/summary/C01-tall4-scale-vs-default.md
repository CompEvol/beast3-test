# Posterior comparison: C01-tall4-scale-vs-default

**Verdict: matched**

- default: `beast3/log/C01-tall4/rep1`, `beast3/log/C01-tall4/rep2`
- scale: `beast3/log/C01-tall4-scale/rep1`, `beast3/log/C01-tall4-scale/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 4395; max z: 1.019; max clade |Δp|: 0.018

## Findings

- **NOTE** Trace log file names differ: default `CN-tallN.log` paired with scale `CN-tallN-scale.log`
- **NOTE** Tree file names differ: default `CN-tallN-anolis.trees` paired with scale `CN-tallN-scale-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C01-tall4/rep1/C01-tall4.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| default | rep2 | `beast3/log/C01-tall4/rep2/C01-tall4.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| scale | rep1 | `beast3/log/C01-tall4-scale/rep1/C01-tall4-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| scale | rep2 | `beast3/log/C01-tall4-scale/rep2/C01-tall4-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m03s |  |

## Parameters: `CN-tallN.log / CN-tallN-scale.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | scale mean | scale 95% HPD | scale ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23613.19 | [-23621.27, -23605.75] | 9858 (4584) | -23613.21 | [-23621.55, -23605.93] | 9138 (4491) | 0.35 | 99% | ok |
| `likelihood` | -23386.47 | [-23394.44, -23379.26] | 10168 (5071) | -23386.48 | [-23394.40, -23379.19] | 8935 (4395) | 0.26 | 100% | ok |
| `prior` | -226.72 | [-228.39, -225.42] | 42976 (21275) | -226.72 | [-228.36, -225.39] | 42378 (21046) | 1.02 | 99% | ok |
| `treeLikelihood` | -23386.47 | [-23394.44, -23379.26] | 10168 (5071) | -23386.48 | [-23394.40, -23379.19] | 8935 (4395) | 0.26 | 100% | ok |
| `Tree.height` | 1925.28 | [1848.05, 2004.56] | 17005 (8251) | 1925.09 | [1848.21, 2004.08] | 15224 (7529) | 0.41 | 100% | ok |
| `Tree.treeLength` | 36306.62 | [35229.33, 37356.30] | 47917 (23915) | 36305.82 | [35271.13, 37389.16] | 47205 (23539) | 0.23 | 98% | ok |
| `YuleModel` | -229.19 | [-230.84, -227.82] | 42463 (20973) | -229.19 | [-230.89, -227.85] | 41878 (20842) | 0.82 | 99% | ok |
| `birthRate` | 7.713e-04 | [4.985e-04, 0.001063] | 42259 (20595) | 7.723e-04 | [4.918e-04, 0.001058] | 41751 (20439) | 0.97 | 99% | ok |

### Replicate agreement (baseline noise): `CN-tallN.log / CN-tallN-scale.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | scale rep means | scale max z |
|---|---|---:|---|---:|
| `posterior` | -23613.14, -23613.23 | 1.12 | -23613.31, -23613.10 | 2.50 |
| `likelihood` | -23386.42, -23386.51 | 1.18 | -23386.58, -23386.38 | 2.40 |
| `prior` | -226.72, -226.72 | 0.09 | -226.73, -226.72 | 1.38 |
| `treeLikelihood` | -23386.42, -23386.51 | 1.18 | -23386.58, -23386.38 | 2.40 |
| `Tree.height` | 1925.51, 1925.04 | 0.76 | 1925.15, 1925.03 | 0.18 |
| `Tree.treeLength` | 36311.38, 36301.86 | 1.91 | 36309.75, 36301.89 | 1.58 |
| `YuleModel` | -229.19, -229.19 | 0.34 | -229.20, -229.19 | 1.02 |
| `birthRate` | 7.705e-04, 7.721e-04 | 1.19 | 7.734e-04, 7.712e-04 | 1.53 |

## Trees: `CN-tallN-anolis.trees / CN-tallN-scale-anolis.trees`

5402 trees (default) and 5402 trees (scale) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: default 0.055, scale 0.073.

| Clade | Size | p default | p scale | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.572 | 0.554 | 0.018 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.418 | 0.435 | 0.017 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.632 | 0.622 | 0.010 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.902 | 0.892 | 0.010 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.179 | 0.187 | 0.008 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.725 | 0.722 | 0.003 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.087 | 0.085 | 0.003 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.420 | 0.417 | 0.002 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.576 | 0.578 | 0.002 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.082 | 0.081 | 0.001 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.998 | 0.999 | 0.001 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.998 | 0.997 | 0.000 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 1.000 | 1.000 | 0.000 | ok |
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
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis, Anolis_occultus} | 6 | 1.000 | 1.000 | 0.000 | ok |

(3 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 3m58s | 9858 | 148909 | 148909 (`posterior`) |
| scale | 4m03s | 9138 | 135578 | 132568 (`likelihood`) |

Run-time ratio scale / default: 1.02

