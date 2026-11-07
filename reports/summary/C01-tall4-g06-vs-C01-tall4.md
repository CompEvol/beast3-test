# Posterior comparison: C01-tall4-g06-vs-C01-tall4

**Verdict: matched**

- ref: `beast3/log/C01-tall4/rep1`, `beast3/log/C01-tall4/rep2`
- g06: `beast3/log/C01-tall4-g06/rep1`, `beast3/log/C01-tall4-g06/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3729; max z: 1.091; max clade |Δp|: 0.034

## Findings

- **NOTE** Trace log file names differ: ref `CN-tallN.log` paired with g06 `CN-tallN-gN.log`
- **NOTE** Tree file names differ: ref `CN-tallN-anolis.trees` paired with g06 `CN-tallN-gN-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| ref | rep1 | `beast3/log/C01-tall4/rep1/C01-tall4.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| ref | rep2 | `beast3/log/C01-tall4/rep2/C01-tall4.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| g06 | rep1 | `beast3/log/C01-tall4-g06/rep1/C01-tall4-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m59s |  |
| g06 | rep2 | `beast3/log/C01-tall4-g06/rep2/C01-tall4-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |

## Parameters: `CN-tallN.log / CN-tallN-gN.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | ref mean | ref 95% HPD | ref ESS | g06 mean | g06 95% HPD | g06 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23613.19 | [-23621.27, -23605.75] | 9858 (4584) | -23613.22 | [-23621.38, -23605.75] | 9138 (3915) | 0.53 | 100% | ok |
| `likelihood` | -23386.47 | [-23394.44, -23379.26] | 10168 (5071) | -23386.49 | [-23394.50, -23379.20] | 8462 (3729) | 0.43 | 100% | ok |
| `prior` | -226.72 | [-228.39, -225.42] | 42976 (21275) | -226.72 | [-228.42, -225.44] | 42248 (20808) | 1.09 | 99% | ok |
| `treeLikelihood` | -23386.47 | [-23394.44, -23379.26] | 10168 (5071) | -23386.49 | [-23394.50, -23379.20] | 8462 (3729) | 0.43 | 100% | ok |
| `Tree.height` | 1925.28 | [1848.05, 2004.56] | 17005 (8251) | 1925.36 | [1849.64, 2005.09] | 16531 (8156) | 0.20 | 100% | ok |
| `Tree.treeLength` | 36306.62 | [35229.33, 37356.30] | 47917 (23915) | 36307.01 | [35256.39, 37373.71] | 46576 (22795) | 0.11 | 99% | ok |
| `YuleModel` | -229.19 | [-230.84, -227.82] | 42463 (20973) | -229.19 | [-230.87, -227.86] | 41653 (20574) | 1.02 | 99% | ok |
| `birthRate` | 7.713e-04 | [4.985e-04, 0.001063] | 42259 (20595) | 7.717e-04 | [4.957e-04, 0.001063] | 42262 (20904) | 0.37 | 100% | ok |

### Replicate agreement (baseline noise): `CN-tallN.log / CN-tallN-gN.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | ref rep means | ref max z | g06 rep means | g06 max z |
|---|---|---:|---|---:|
| `posterior` | -23613.14, -23613.23 | 1.12 | -23613.17, -23613.27 | 1.13 |
| `likelihood` | -23386.42, -23386.51 | 1.18 | -23386.45, -23386.54 | 0.99 |
| `prior` | -226.72, -226.72 | 0.09 | -226.72, -226.73 | 1.40 |
| `treeLikelihood` | -23386.42, -23386.51 | 1.18 | -23386.45, -23386.54 | 0.99 |
| `Tree.height` | 1925.51, 1925.04 | 0.76 | 1925.27, 1925.46 | 0.31 |
| `Tree.treeLength` | 36311.38, 36301.86 | 1.91 | 36305.40, 36308.63 | 0.65 |
| `YuleModel` | -229.19, -229.19 | 0.34 | -229.19, -229.20 | 0.88 |
| `birthRate` | 7.705e-04, 7.721e-04 | 1.19 | 7.701e-04, 7.733e-04 | 2.26 |

## Trees: `CN-tallN-anolis.trees / CN-tallN-gN-anolis.trees`

5402 trees (ref) and 5402 trees (g06) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: ref 0.055, g06 0.019.

| Clade | Size | p ref | p g06 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_coelestinus, Anolis_cuvieri, Anolis_equestris, … (12 taxa)} | 12 | 0.027 | 0.061 | 0.034 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.632 | 0.616 | 0.017 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.902 | 0.888 | 0.014 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.576 | 0.588 | 0.012 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.420 | 0.409 | 0.011 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.418 | 0.428 | 0.010 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.572 | 0.563 | 0.009 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.179 | 0.184 | 0.005 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.082 | 0.078 | 0.005 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.725 | 0.721 | 0.004 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.086 | 0.084 | 0.002 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.998 | 0.996 | 0.002 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.998 | 0.999 | 0.001 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.087 | 0.086 | 0.001 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 1.000 | 1.000 | 0.000 | ok |
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
| ref | 3m58s | 9858 | 148909 | 148909 (`posterior`) |
| g06 | 4m01s | 9138 | 136234 | 126153 (`likelihood`) |

Run-time ratio g06 / ref: 1.01

