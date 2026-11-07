# Posterior comparison: C01-tall4-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C01-tall4/rep1`, `beast3/log/C01-tall4/rep2`
- slide: `beast3/log/C01-tall4-slide/rep1`, `beast3/log/C01-tall4-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3801; max z: 0.7491; max clade |Δp|: 0.026

## Findings

- **NOTE** Trace log file names differ: default `CN-tallN.log` paired with slide `CN-tallN-slide.log`
- **NOTE** Tree file names differ: default `CN-tallN-anolis.trees` paired with slide `CN-tallN-slide-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C01-tall4/rep1/C01-tall4.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| default | rep2 | `beast3/log/C01-tall4/rep2/C01-tall4.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| slide | rep1 | `beast3/log/C01-tall4-slide/rep1/C01-tall4-slide.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| slide | rep2 | `beast3/log/C01-tall4-slide/rep2/C01-tall4-slide.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |

## Parameters: `CN-tallN.log / CN-tallN-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23613.19 | [-23621.27, -23605.75] | 9858 (4584) | -23613.17 | [-23621.23, -23605.73] | 9043 (4366) | 0.31 | 100% | ok |
| `likelihood` | -23386.47 | [-23394.44, -23379.26] | 10168 (5071) | -23386.45 | [-23394.43, -23379.28] | 8314 (3801) | 0.36 | 100% | ok |
| `prior` | -226.72 | [-228.39, -225.42] | 42976 (21275) | -226.72 | [-228.35, -225.37] | 42162 (21061) | 0.58 | 99% | ok |
| `treeLikelihood` | -23386.47 | [-23394.44, -23379.26] | 10168 (5071) | -23386.45 | [-23394.43, -23379.28] | 8314 (3801) | 0.36 | 100% | ok |
| `Tree.height` | 1925.28 | [1848.05, 2004.56] | 17005 (8251) | 1925.14 | [1848.55, 2003.55] | 13606 (6762) | 0.30 | 100% | ok |
| `Tree.treeLength` | 36306.62 | [35229.33, 37356.30] | 47917 (23915) | 36304.78 | [35231.44, 37351.31] | 47600 (23602) | 0.52 | 100% | ok |
| `YuleModel` | -229.19 | [-230.84, -227.82] | 42463 (20973) | -229.19 | [-230.85, -227.84] | 41616 (20753) | 0.43 | 100% | ok |
| `birthRate` | 7.713e-04 | [4.985e-04, 0.001063] | 42259 (20595) | 7.721e-04 | [4.947e-04, 0.001061] | 42862 (21413) | 0.75 | 100% | ok |

### Replicate agreement (baseline noise): `CN-tallN.log / CN-tallN-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -23613.14, -23613.23 | 1.12 | -23613.17, -23613.17 | 0.07 |
| `likelihood` | -23386.42, -23386.51 | 1.18 | -23386.44, -23386.45 | 0.14 |
| `prior` | -226.72, -226.72 | 0.09 | -226.73, -226.72 | 0.87 |
| `treeLikelihood` | -23386.42, -23386.51 | 1.18 | -23386.44, -23386.45 | 0.14 |
| `Tree.height` | 1925.51, 1925.04 | 0.76 | 1924.76, 1925.52 | 1.11 |
| `Tree.treeLength` | 36311.38, 36301.86 | 1.91 | 36303.56, 36306.00 | 0.49 |
| `YuleModel` | -229.19, -229.19 | 0.34 | -229.19, -229.19 | 0.81 |
| `birthRate` | 7.705e-04, 7.721e-04 | 1.19 | 7.723e-04, 7.718e-04 | 0.39 |

## Trees: `CN-tallN-anolis.trees / CN-tallN-slide-anolis.trees`

5402 trees (default) and 5402 trees (slide) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: default 0.055, slide 0.052.

| Clade | Size | p default | p slide | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_coelestinus, Anolis_cuvieri, Anolis_equestris, … (12 taxa)} | 12 | 0.027 | 0.053 | 0.026 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.576 | 0.596 | 0.020 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.420 | 0.400 | 0.020 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.082 | 0.095 | 0.012 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.725 | 0.713 | 0.012 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.902 | 0.890 | 0.012 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.179 | 0.187 | 0.009 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.086 | 0.080 | 0.006 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.572 | 0.575 | 0.003 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.632 | 0.634 | 0.002 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.087 | 0.089 | 0.002 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.418 | 0.419 | 0.001 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.998 | 0.997 | 0.001 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.998 | 0.997 | 0.000 | ok |
| {Anolis_insolitus, Anolis_olssoni} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 1.000 | 0.000 | ok |
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
| default | 3m58s | 9858 | 148909 | 148909 (`posterior`) |
| slide | 3m59s | 9043 | 136473 | 125473 (`likelihood`) |

Run-time ratio slide / default: 1.00

