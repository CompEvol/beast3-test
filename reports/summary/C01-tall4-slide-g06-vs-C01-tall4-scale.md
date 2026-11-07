# Posterior comparison: C01-tall4-slide-g06-vs-C01-tall4-scale

**Verdict: matched**

- ref: `beast3/log/C01-tall4-scale/rep1`, `beast3/log/C01-tall4-scale/rep2`
- g06: `beast3/log/C01-tall4-slide-g06/rep1`, `beast3/log/C01-tall4-slide-g06/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 4395; max z: 1.628; max clade |Δp|: 0.012

## Findings

- **NOTE** Trace log file names differ: ref `CN-tallN-scale.log` paired with g06 `CN-tallN-slide-gN.log`
- **NOTE** Tree file names differ: ref `CN-tallN-scale-anolis.trees` paired with g06 `CN-tallN-slide-gN-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| ref | rep1 | `beast3/log/C01-tall4-scale/rep1/C01-tall4-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| ref | rep2 | `beast3/log/C01-tall4-scale/rep2/C01-tall4-scale.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m03s |  |
| g06 | rep1 | `beast3/log/C01-tall4-slide-g06/rep1/C01-tall4-slide-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |
| g06 | rep2 | `beast3/log/C01-tall4-slide-g06/rep2/C01-tall4-slide-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |

## Parameters: `CN-tallN-scale.log / CN-tallN-slide-gN.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | ref mean | ref 95% HPD | ref ESS | g06 mean | g06 95% HPD | g06 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23613.21 | [-23621.55, -23605.93] | 9138 (4491) | -23613.19 | [-23621.31, -23605.66] | 12980 (6293) | 0.36 | 98% | ok |
| `likelihood` | -23386.48 | [-23394.40, -23379.19] | 8935 (4395) | -23386.47 | [-23394.51, -23379.21] | 12614 (6141) | 0.20 | 100% | ok |
| `prior` | -226.72 | [-228.36, -225.39] | 42378 (21046) | -226.72 | [-228.43, -225.45] | 41439 (20700) | 1.63 | 98% | ok |
| `treeLikelihood` | -23386.48 | [-23394.40, -23379.19] | 8935 (4395) | -23386.47 | [-23394.51, -23379.21] | 12614 (6141) | 0.20 | 100% | ok |
| `Tree.height` | 1925.09 | [1848.21, 2004.08] | 15224 (7529) | 1924.97 | [1847.79, 2003.28] | 16910 (8151) | 0.27 | 100% | ok |
| `Tree.treeLength` | 36305.82 | [35271.13, 37389.16] | 47205 (23539) | 36303.20 | [35242.10, 37354.92] | 48267 (24131) | 0.75 | 99% | ok |
| `YuleModel` | -229.19 | [-230.89, -227.85] | 41878 (20842) | -229.18 | [-230.86, -227.86] | 40375 (19940) | 1.61 | 100% | ok |
| `birthRate` | 7.723e-04 | [4.918e-04, 0.001058] | 41751 (20439) | 7.721e-04 | [4.960e-04, 0.001061] | 41378 (20051) | 0.17 | 100% | ok |

### Replicate agreement (baseline noise): `CN-tallN-scale.log / CN-tallN-slide-gN.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | ref rep means | ref max z | g06 rep means | g06 max z |
|---|---|---:|---|---:|
| `posterior` | -23613.31, -23613.10 | 2.50 | -23613.12, -23613.26 | 1.95 |
| `likelihood` | -23386.58, -23386.38 | 2.40 | -23386.40, -23386.54 | 1.94 |
| `prior` | -226.73, -226.72 | 1.38 | -226.71, -226.72 | 0.21 |
| `treeLikelihood` | -23386.58, -23386.38 | 2.40 | -23386.40, -23386.54 | 1.94 |
| `Tree.height` | 1925.15, 1925.03 | 0.18 | 1925.20, 1924.74 | 0.76 |
| `Tree.treeLength` | 36309.75, 36301.89 | 1.58 | 36303.84, 36302.57 | 0.26 |
| `YuleModel` | -229.20, -229.19 | 1.02 | -229.18, -229.18 | 0.23 |
| `birthRate` | 7.734e-04, 7.712e-04 | 1.53 | 7.722e-04, 7.721e-04 | 0.06 |

## Trees: `CN-tallN-scale-anolis.trees / CN-tallN-slide-gN-anolis.trees`

5402 trees (ref) and 5402 trees (g06) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: ref 0.073, g06 0.058.

| Clade | Size | p ref | p g06 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.554 | 0.566 | 0.012 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.435 | 0.425 | 0.010 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.578 | 0.587 | 0.009 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.417 | 0.409 | 0.008 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.892 | 0.899 | 0.007 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.722 | 0.726 | 0.004 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.622 | 0.618 | 0.004 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.086 | 0.088 | 0.002 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.085 | 0.083 | 0.002 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.081 | 0.083 | 0.002 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.999 | 0.997 | 0.002 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 1.000 | 0.999 | 0.000 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.997 | 0.998 | 0.000 | ok |
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
| ref | 4m03s | 9138 | 135578 | 132568 (`likelihood`) |
| g06 | 4m04s | 12980 | 191429 | 186022 (`likelihood`) |

Run-time ratio g06 / ref: 1.01

