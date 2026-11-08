# Posterior comparison: testJukesCantor

**Verdict: matched**

- beast2: `beast2/log/testJukesCantor/rep1`, `beast2/log/testJukesCantor/rep2`
- beast3: `beast3/log/testJukesCantor/rep1`, `beast3/log/testJukesCantor/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3962; max z: 1.944; max clade |Δp|: 0.030

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testJukesCantor/rep1/test.1.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 13s |  |
| beast2 | rep2 | `beast2/log/testJukesCantor/rep2/test.2.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 13s |  |
| beast3 | rep1 | `beast3/log/testJukesCantor/rep1/test.1.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 10s |  |
| beast3 | rep2 | `beast3/log/testJukesCantor/rep2/test.2.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 10s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -1977.91 | [-1980.96, -1975.40] | 8969 (4468) | -1977.92 | [-1980.94, -1975.47] | 8938 (4437) | 0.31 | 100% | ok |
| `tree.height` | 0.06081 | [0.0504, 0.07227] | 8157 (3962) | 0.06098 | [0.04993, 0.07182] | 9002 (4501) | 1.94 | 98% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -1977.93, -1977.89 | 1.17 | -1977.95, -1977.89 | 1.60 |
| `tree.height` | 0.06083, 0.06078 | 0.42 | 0.06094, 0.06101 | 0.53 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.004, beast3 0.058.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {orangutan, siamang} | 2 | 0.059 | 0.029 | 0.030 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.764 | 0.769 | 0.005 | ok |
| {bonobo, chimp, human} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.177 | 0.177 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 26s | 8969 | 1226642 | 1115578 (`tree.height`) |
| beast3 | 20s | 8938 | 1624883 | 1624883 (`treeLikelihood`) |

Run-time ratio beast3 / beast2: 0.75

