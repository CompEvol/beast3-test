# Posterior comparison: testOpSubSchedule

**Verdict: matched**

- beast2: `beast2/log/testOpSubSchedule/rep1`, `beast2/log/testOpSubSchedule/rep2`
- beast3: `beast3/log/testOpSubSchedule/rep1`, `beast3/log/testOpSubSchedule/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 2676; max z: 1.286; max clade |Δp|: 0.002

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** tree files read from `/Users/adru001/Library/CloudStorage/Dropbox/beast3-test`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testOpSubSchedule/rep1/test.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 3s |  |
| beast2 | rep2 | `beast2/log/testOpSubSchedule/rep2/test.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 3s |  |
| beast3 | rep1 | `beast3/log/testOpSubSchedule/rep1/test.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 2s |  |
| beast3 | rep2 | `beast3/log/testOpSubSchedule/rep2/test.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 2s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -1815.68 | [-1819.24, -1812.93] | 8201 (4053) | -1815.66 | [-1819.10, -1812.83] | 8783 (4325) | 0.47 | 98% | ok |
| `hky.kappa` | 29.91 | [14.92, 48.05] | 5513 (2676) | 30.12 | [14.09, 48.26] | 8654 (4257) | 1.29 | 100% | ok |
| `tree.height` | 0.06417 | [0.05251, 0.07686] | 7971 (3934) | 0.06415 | [0.05241, 0.07632] | 9001 (4500) | 0.28 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -1815.69, -1815.66 | 0.91 | -1815.65, -1815.67 | 0.49 |
| `hky.kappa` | 29.84, 29.99 | 0.57 | 30.23, 30.02 | 1.01 |
| `tree.height` | 0.06415, 0.06419 | 0.29 | 0.06413, 0.06417 | 0.29 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.009, beast3 0.020.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.137 | 0.135 | 0.002 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.831 | 0.829 | 0.001 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 7s | 8201 | 4378828 | 2943656 (`hky.kappa`) |
| beast3 | 4s | 8783 | 7474570 | 7365520 (`hky.kappa`) |

Run-time ratio beast3 / beast2: 0.63

