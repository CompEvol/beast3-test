# Posterior comparison: C01-fine-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C01-fine/rep1`, `beast3/log/C01-fine/rep2`
- slide: `beast3/log/C01-fine-slide/rep1`, `beast3/log/C01-fine-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3653; max z: 1.768; max clade |Δp|: 0.010

## Findings

- **NOTE** Trace log file names differ: default `CN-fine.log` paired with slide `CN-fine-slide.log`
- **NOTE** Tree file names differ: default `CN-fine-anolis.trees` paired with slide `CN-fine-slide-anolis.trees`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C01-fine/rep1/C01-fine.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |
| default | rep2 | `beast3/log/C01-fine/rep2/C01-fine.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m01s |  |
| slide | rep1 | `beast3/log/C01-fine-slide/rep1/C01-fine-slide.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 2m02s |  |
| slide | rep2 | `beast3/log/C01-fine-slide/rep2/C01-fine-slide.log` | 30001 (27001) | 100 | 2.8.0 rc2 | yes | 1m57s |  |

## Parameters: `CN-fine.log / CN-fine-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -23364.59 | [-23372.57, -23356.81] | 7603 (3774) | -23364.50 | [-23372.62, -23357.04] | 9586 (4336) | 1.41 | 100% | ok |
| `likelihood` | -23386.57 | [-23394.30, -23378.88] | 7434 (3653) | -23386.47 | [-23394.42, -23379.20] | 9302 (4211) | 1.54 | 99% | ok |
| `prior` | 21.98 | [20.34, 23.31] | 40914 (20157) | 21.97 | [20.35, 23.31] | 40927 (19226) | 1.41 | 100% | ok |
| `treeLikelihood` | -23386.57 | [-23394.30, -23378.88] | 7434 (3653) | -23386.47 | [-23394.42, -23379.20] | 9302 (4211) | 1.54 | 99% | ok |
| `Tree.height` | 0.1925 | [0.1849, 0.2003] | 11370 (5577) | 0.1926 | [0.185, 0.2006] | 17028 (8275) | 1.23 | 99% | ok |
| `Tree.treeLength` | 3.63 | [3.528, 3.739] | 47843 (23837) | 3.631 | [3.524, 3.736] | 47628 (23575) | 1.77 | 99% | ok |
| `YuleModel` | 28.71 | [27.04, 30.04] | 40472 (19927) | 28.7 | [27.01, 30.04] | 40399 (19275) | 1.63 | 100% | ok |
| `birthRate` | 7.693 | [4.933, 10.54] | 42348 (21079) | 7.685 | [5.029, 10.64] | 40858 (20011) | 0.88 | 98% | ok |

### Replicate agreement (baseline noise): `CN-fine.log / CN-fine-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -23364.51, -23364.66 | 1.50 | -23364.56, -23364.43 | 1.50 |
| `likelihood` | -23386.50, -23386.64 | 1.53 | -23386.53, -23386.41 | 1.49 |
| `prior` | 21.98, 21.98 | 0.23 | 21.97, 21.97 | 0.18 |
| `treeLikelihood` | -23386.50, -23386.64 | 1.53 | -23386.53, -23386.41 | 1.49 |
| `Tree.height` | 0.1925, 0.1926 | 1.53 | 0.1926, 0.1926 | 0.67 |
| `Tree.treeLength` | 3.631, 3.63 | 0.35 | 3.631, 3.631 | 0.27 |
| `YuleModel` | 28.7, 28.71 | 0.40 | 28.7, 28.7 | 0.27 |
| `birthRate` | 7.689, 7.698 | 0.71 | 7.682, 7.687 | 0.32 |

## Trees: `CN-fine-anolis.trees / CN-fine-slide-anolis.trees`

5402 trees (default) and 5402 trees (slide) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: default 0.062, slide 0.069.

| Clade | Size | p default | p slide | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {Anolis_alutaceus, Anolis_angusticeps, Anolis_loysiana, Anolis_marcanoi, Anolis_paternus, Anolis_strahmi, … (7 taxa)} | 7 | 0.888 | 0.898 | 0.010 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_valencienni} | 3 | 0.410 | 0.419 | 0.009 | ok |
| {Anolis_garmani, Anolis_grahami, Anolis_lineatopus} | 3 | 0.586 | 0.578 | 0.008 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, Anolis_cristatellus, … (15 taxa)} | 15 | 0.723 | 0.727 | 0.004 | ok |
| {Anolis_barahonae, Anolis_cuvieri, Anolis_insolitus, Anolis_olssoni} | 4 | 0.563 | 0.566 | 0.004 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, Anolis_coelestinus, … (22 taxa)} | 22 | 0.086 | 0.083 | 0.002 | ok |
| {Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, Anolis_brevirostris, … (22 taxa)} | 22 | 0.189 | 0.191 | 0.002 | ok |
| {Anolis_ahli, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, Anolis_valencienni} | 5 | 0.997 | 0.999 | 0.002 | ok |
| {Anolis_aliniger, Anolis_bahorucoensis, Anolis_coelestinus, Anolis_equestris, Anolis_insolitus, Anolis_luteogularis, … (8 taxa)} | 8 | 0.427 | 0.425 | 0.002 | ok |
| {Anolis_ahli, Anolis_aliniger, Anolis_alutaceus, Anolis_angusticeps, Anolis_bahorucoensis, Anolis_barahonae, … (24 taxa)} | 24 | 0.083 | 0.081 | 0.001 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_brevirostris, Anolis_cristatellus, Anolis_distichus, … (19 taxa)} | 19 | 0.084 | 0.083 | 0.001 | ok |
| {Anolis_cristatellus, Anolis_stratulus} | 2 | 0.997 | 0.998 | 0.001 | ok |
| {Anolis_ahli, Anolis_alutaceus, Anolis_angusticeps, Anolis_garmani, Anolis_grahami, Anolis_lineatopus, … (14 taxa)} | 14 | 0.616 | 0.616 | 0.001 | ok |
| {Anolis_bahorucoensis, Anolis_occultus} | 2 | 0.999 | 0.999 | 0.000 | ok |
| {Anolis_aliniger, Anolis_coelestinus, Anolis_equestris, Anolis_luteogularis} | 4 | 1.000 | 1.000 | 0.000 | ok |
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
| slide | 3m58s | 9586 | 144778 | 140485 (`likelihood`) |

Run-time ratio slide / default: 0.98

