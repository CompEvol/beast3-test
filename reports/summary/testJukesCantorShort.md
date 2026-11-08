# Posterior comparison: testJukesCantorShort

**Verdict: matched**

- beast2: `beast2/log/testJukesCantorShort/rep1`, `beast2/log/testJukesCantorShort/rep2`
- beast3: `beast3/log/testJukesCantorShort/rep1`, `beast3/log/testJukesCantorShort/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3778; max z: 0.5126; max clade |Δp|: 0.005

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testJukesCantorShort/rep1/test.1.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 10s |  |
| beast2 | rep2 | `beast2/log/testJukesCantorShort/rep2/test.2.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 10s |  |
| beast3 | rep1 | `beast3/log/testJukesCantorShort/rep1/test.1.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 8s |  |
| beast3 | rep2 | `beast3/log/testJukesCantorShort/rep2/test.2.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 7s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -998.21 | [-1001.89, -995.49] | 8254 (4110) | -998.20 | [-1001.85, -995.40] | 8279 (3778) | 0.42 | 99% | ok |
| `tree.height` | 0.0518 | [0.03803, 0.06622] | 9002 (4501) | 0.05185 | [0.03815, 0.06617] | 8949 (4448) | 0.51 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -998.22, -998.21 | 0.06 | -998.17, -998.23 | 1.40 |
| `tree.height` | 0.05179, 0.0518 | 0.07 | 0.05178, 0.05193 | 0.92 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.004, beast3 0.057.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {gorilla, orangutan} | 2 | 0.111 | 0.106 | 0.005 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 0.888 | 0.893 | 0.005 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.912 | 0.909 | 0.003 | ok |
| {bonobo, chimp} | 2 | 0.994 | 0.992 | 0.002 | ok |
| {bonobo, chimp, human} | 3 | 0.993 | 0.993 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 20s | 8254 | 1471794 | 1471794 (`treeLikelihood`) |
| beast3 | 15s | 8279 | 2006525 | 2006525 (`treeLikelihood`) |

Run-time ratio beast3 / beast2: 0.74

