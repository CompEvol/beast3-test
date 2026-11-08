# Posterior comparison: testOpSubSchedule

**Verdict: not matched**

- beast2: `beast2/log/testOpSubSchedule/rep1`, `beast2/log/testOpSubSchedule/rep2`
- beast3: `beast3/log/testOpSubSchedule/rep1`, `beast3/log/testOpSubSchedule/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 2795; max z: 95.44; max clade |Δp|: 0.005

## Findings

- **FLAG** `treeLikelihood`: z = 46.29 (beast2 mean -1815.67, beast3 mean -1817.14)
- **FLAG** `hky.kappa`: z = 95.44 (beast2 mean 29.96, beast3 mean 17.51)
- **FLAG** `tree.height`: z = 6.07 (beast2 mean 0.06424, beast3 mean 0.06365)
- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testOpSubSchedule/rep1/test.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast2 | rep2 | `beast2/log/testOpSubSchedule/rep2/test.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast3 | rep1 | `beast3/log/testOpSubSchedule/rep1/test.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 3s |  |
| beast3 | rep2 | `beast3/log/testOpSubSchedule/rep2/test.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 3s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -1815.67 | [-1819.15, -1812.81] | 8223 (4016) | -1817.14 | [-1821.58, -1813.19] | 8725 (4224) | 46.29 | 94% | **z** |
| `hky.kappa` | 29.96 | [15.2, 48.19] | 5696 (2795) | 17.51 | [10.6, 25.38] | 8108 (4049) | 95.44 | 69% | **z** |
| `tree.height` | 0.06424 | [0.05244, 0.07664] | 7411 (3629) | 0.06365 | [0.05227, 0.07627] | 9002 (4501) | 6.07 | 99% | **z** |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -1815.65, -1815.69 | 0.92 | -1817.14, -1817.14 | 0.02 |
| `hky.kappa` | 30.07, 29.84 | 0.97 | 17.52, 17.49 | 0.29 |
| `tree.height` | 0.06426, 0.06421 | 0.32 | 0.0636, 0.0637 | 0.79 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.004, beast3 0.010.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.140 | 0.135 | 0.005 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.824 | 0.829 | 0.004 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 8s | 8223 | 3728455 | 2582685 (`hky.kappa`) |
| beast3 | 5s | 8725 | 6106117 | 5674292 (`hky.kappa`) |

Run-time ratio beast3 / beast2: 0.65

