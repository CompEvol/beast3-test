# Posterior comparison: testJukesCantorShortUncertain2MLE

**Verdict: matched**

- beast2: `beast2/log/testJukesCantorShortUncertain2MLE/rep1`, `beast2/log/testJukesCantorShortUncertain2MLE/rep2`
- beast3: `beast3/log/testJukesCantorShortUncertain2MLE/rep1`, `beast3/log/testJukesCantorShortUncertain2MLE/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 4220; max z: 1.365; max clade |Δp|: 0.053

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testJukesCantorShortUncertain2MLE/rep1/test.1.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 25s |  |
| beast2 | rep2 | `beast2/log/testJukesCantorShortUncertain2MLE/rep2/test.2.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 26s |  |
| beast3 | rep1 | `beast3/log/testJukesCantorShortUncertain2MLE/rep1/test.1.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 19s |  |
| beast3 | rep2 | `beast3/log/testJukesCantorShortUncertain2MLE/rep2/test.2.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 19s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -1927.25 | [-1930.85, -1924.19] | 8721 (4220) | -1927.26 | [-1930.81, -1924.24] | 8690 (4291) | 0.14 | 100% | ok |
| `tree.height` | 0.1645 | [0.1431, 0.1876] | 9002 (4501) | 0.1643 | [0.1428, 0.1875] | 9002 (4501) | 1.36 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -1927.27, -1927.24 | 0.67 | -1927.27, -1927.24 | 0.91 |
| `tree.height` | 0.1644, 0.1645 | 0.33 | 0.1644, 0.1641 | 1.06 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.050, beast3 0.016.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, gorilla, orangutan} | 3 | 0.000 | 0.053 | 0.053 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.286 | 0.269 | 0.017 | ok |
| {bonobo, chimp, siamang} | 3 | 0.125 | 0.137 | 0.012 | ok |
| {bonobo, chimp} | 2 | 0.159 | 0.150 | 0.009 | ok |
| {bonobo, chimp, gorilla, orangutan, siamang} | 5 | 0.122 | 0.131 | 0.008 | ok |
| {bonobo, gorilla, orangutan, siamang} | 4 | 0.122 | 0.114 | 0.008 | ok |
| {chimp, gorilla, human, orangutan} | 4 | 0.189 | 0.182 | 0.007 | ok |
| {gorilla, human, orangutan} | 3 | 0.342 | 0.348 | 0.006 | ok |
| {bonobo, siamang} | 2 | 0.544 | 0.549 | 0.006 | ok |
| {chimp, gorilla, orangutan} | 3 | 0.076 | 0.072 | 0.004 | ok |
| {bonobo, human} | 2 | 0.079 | 0.075 | 0.004 | ok |
| {bonobo, chimp, human} | 3 | 0.103 | 0.099 | 0.003 | ok |
| {bonobo, gorilla, human, orangutan, siamang} | 5 | 0.265 | 0.268 | 0.003 | ok |
| {bonobo, chimp, human, siamang} | 4 | 0.097 | 0.098 | 0.001 | ok |
| {bonobo, gorilla, human, orangutan} | 4 | 0.078 | 0.079 | 0.001 | ok |
| {bonobo, human, siamang} | 3 | 0.067 | 0.068 | 0.001 | ok |
| {gorilla, orangutan} | 2 | 0.994 | 0.994 | 0.000 | ok |
| {chimp, human} | 2 | 0.116 | 0.115 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 50s | 8721 | 623843 | 623843 (`treeLikelihood`) |
| beast3 | 38s | 8690 | 832302 | 832302 (`treeLikelihood`) |

Run-time ratio beast3 / beast2: 0.75

