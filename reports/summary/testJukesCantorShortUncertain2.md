# Posterior comparison: testJukesCantorShortUncertain2

**Verdict: matched**

- beast2: `beast2/log/testJukesCantorShortUncertain2/rep1`, `beast2/log/testJukesCantorShortUncertain2/rep2`
- beast3: `beast3/log/testJukesCantorShortUncertain2/rep1`, `beast3/log/testJukesCantorShortUncertain2/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3970; max z: 0.1711; max clade |Δp|: 0.009

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testJukesCantorShortUncertain2/rep1/test.1.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 1m09s |  |
| beast2 | rep2 | `beast2/log/testJukesCantorShortUncertain2/rep2/test.2.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 1m09s |  |
| beast3 | rep1 | `beast3/log/testJukesCantorShortUncertain2/rep1/test.1.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 1m02s |  |
| beast3 | rep2 | `beast3/log/testJukesCantorShortUncertain2/rep2/test.2.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 1m02s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -12280.16 | [-12283.87, -12277.38] | 9002 (4501) | -12280.16 | [-12283.78, -12277.39] | 8604 (4103) | 0.17 | 100% | ok |
| `tree.height` | 0.04651 | [0.03159, 0.06263] | 8890 (4389) | 0.04652 | [0.03212, 0.06294] | 8390 (3970) | 0.09 | 99% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -12280.15, -12280.17 | 0.44 | -12280.14, -12280.17 | 0.81 |
| `tree.height` | 0.04646, 0.04656 | 0.58 | 0.04647, 0.04656 | 0.50 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.013, beast3 0.010.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.671 | 0.662 | 0.009 | ok |
| {gorilla, orangutan} | 2 | 0.490 | 0.482 | 0.008 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 0.496 | 0.503 | 0.007 | ok |
| {orangutan, siamang} | 2 | 0.147 | 0.149 | 0.003 | ok |
| {bonobo, chimp, human, siamang} | 4 | 0.073 | 0.075 | 0.003 | ok |
| {bonobo, chimp} | 2 | 0.992 | 0.994 | 0.002 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.088 | 0.086 | 0.002 | ok |
| {bonobo, chimp, human} | 3 | 0.897 | 0.897 | 0.001 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2m18s | 9002 | 234791 | 231872 (`tree.height`) |
| beast3 | 2m04s | 8604 | 249298 | 243102 (`tree.height`) |

Run-time ratio beast3 / beast2: 0.90

