# Posterior comparison: C01-g06-vs-C01-fine

**Verdict: matched**

- ref: `beast3/log/C01-fine/rep1`, `beast3/log/C01-fine/rep2`
- g06: `beast3/log/C01-g06/rep1`, `beast3/log/C01-g06/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3653; max z: 0.7902; max clade |Δp|: 0.019

## Findings

- **NOTE** Trace log file names differ: ref `CN-fine.log` paired with g06 `CN-gN.log`
- **NOTE** Tree file names differ: ref `CN-fine-anolis.trees` paired with g06 `CN-gN-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| ref | rep1 | `beast3/log/C01-fine/rep1/C01-fine.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |
| ref | rep2 | `beast3/log/C01-fine/rep2/C01-fine.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m01s |  |
| g06 | rep1 | `beast3/log/C01-g06/rep1/C01-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m04s |  |
| g06 | rep2 | `beast3/log/C01-g06/rep2/C01-g06.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m04s |  |

## Parameters: `CN-fine.log / CN-gN.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | ref mean | ref 95% HPD | ref ESS | g06 mean | g06 95% HPD | g06 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23364.59 | [-23372.57, -23356.81] | 7603 (3774) | -23364.56 | [-23372.72, -23357.12] | 10012 (4458) | 0.48 | 99% | ok |
| `likelihood` | -23386.57 | [-23394.30, -23378.88] | 7434 (3653) | -23386.53 | [-23394.44, -23379.21] | 9698 (4305) | 0.55 | 99% | ok |
| `prior` | 21.98 | [20.34, 23.31] | 40914 (20157) | 21.98 | [20.32, 23.3] | 41258 (20141) | 0.72 | 100% | ok |
| `treeLikelihood` | -23386.57 | [-23394.30, -23378.88] | 7434 (3653) | -23386.53 | [-23394.44, -23379.21] | 9698 (4305) | 0.55 | 99% | ok |
| `Tree.height` | 0.1925 | [0.1849, 0.2003] | 11370 (5577) | 0.1925 | [0.1848, 0.2004] | 17501 (8590) | 0.19 | 100% | ok |
| `Tree.treeLength` | 3.63 | [3.528, 3.739] | 47843 (23837) | 3.631 | [3.525, 3.738] | 47060 (23329) | 0.75 | 100% | ok |
| `YuleModel` | 28.71 | [27.04, 30.04] | 40472 (19927) | 28.7 | [26.99, 30.01] | 41060 (20124) | 0.53 | 99% | ok |
| `birthRate` | 7.693 | [4.933, 10.54] | 42348 (21079) | 7.701 | [4.992, 10.64] | 40977 (20369) | 0.79 | 99% | ok |

### Replicate agreement (baseline noise): `CN-fine.log / CN-gN.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | ref rep means | ref max z | g06 rep means | g06 max z |
|---|---|---:|---|---:|
| `posterior` | -23364.51, -23364.66 | 1.50 | -23364.51, -23364.60 | 1.13 |
| `likelihood` | -23386.50, -23386.64 | 1.53 | -23386.49, -23386.58 | 1.11 |
| `prior` | 21.98, 21.98 | 0.23 | 21.98, 21.98 | 0.31 |
| `treeLikelihood` | -23386.50, -23386.64 | 1.53 | -23386.49, -23386.58 | 1.11 |
| `Tree.height` | 0.1925, 0.1926 | 1.53 | 0.1926, 0.1925 | 0.57 |
| `Tree.treeLength` | 3.631, 3.63 | 0.35 | 3.631, 3.631 | 0.15 |
| `YuleModel` | 28.7, 28.71 | 0.40 | 28.7, 28.7 | 0.18 |
| `birthRate` | 7.689, 7.698 | 0.71 | 7.698, 7.705 | 0.51 |

## Trees: `CN-fine-anolis.trees / CN-gN-anolis.trees`

5402 trees (ref) and 5402 trees (g06) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: ref 0.062, g06 0.069.

| Clade | Size | p ref | p g06 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.563 | 0.582 | 0.019 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.427 | 0.410 | 0.017 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.410 | 0.419 | 0.009 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.189 | 0.182 | 0.007 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.586 | 0.579 | 0.007 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.616 | 0.621 | 0.005 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.723 | 0.718 | 0.005 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.083 | 0.087 | 0.004 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.997 | 0.999 | 0.002 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.084 | 0.086 | 0.002 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.997 | 0.998 | 0.001 | ok |
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.888 | 0.889 | 0.001 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.086 | 0.086 | 0.001 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 0.999 | 0.999 | 0.000 | ok |
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

(3 more clades with |Δp| ≤ 0.1 not shown; see the .clades.tsv file)

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| ref | 4m03s | 7603 | 112673 | 110166 (`likelihood`) |
| g06 | 4m07s | 10012 | 145754 | 141180 (`likelihood`) |

Run-time ratio g06 / ref: 1.02

