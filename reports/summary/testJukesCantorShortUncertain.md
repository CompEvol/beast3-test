# Posterior comparison: testJukesCantorShortUncertain

**Verdict: matched**

- beast2: `beast2/log/testJukesCantorShortUncertain/rep1`, `beast2/log/testJukesCantorShortUncertain/rep2`
- beast3: `beast3/log/testJukesCantorShortUncertain/rep1`, `beast3/log/testJukesCantorShortUncertain/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3955; max z: 2.531; max clade |Δp|: 0.014

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testJukesCantorShortUncertain/rep1/test.1.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 1m11s |  |
| beast2 | rep2 | `beast2/log/testJukesCantorShortUncertain/rep2/test.2.log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 1m11s |  |
| beast3 | rep1 | `beast3/log/testJukesCantorShortUncertain/rep1/test.1.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 1m03s |  |
| beast3 | rep2 | `beast3/log/testJukesCantorShortUncertain/rep2/test.2.log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 1m03s |  |

## Parameters: `test.N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -10194.21 | [-10198.11, -10190.87] | 8300 (3955) | -10194.29 | [-10198.30, -10190.85] | 8827 (4326) | 2.53 | 100% | ok |
| `tree.height` | 0.04171 | [0.02569, 0.06012] | 8941 (4440) | 0.04195 | [0.02508, 0.05996] | 8491 (3990) | 1.79 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -10194.20, -10194.22 | 0.28 | -10194.32, -10194.26 | 1.20 |
| `tree.height` | 0.04164, 0.04177 | 0.66 | 0.04196, 0.04195 | 0.05 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.019, beast3 0.022.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp} | 2 | 0.622 | 0.608 | 0.014 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 0.667 | 0.654 | 0.013 | ok |
| {gorilla, human} | 2 | 0.446 | 0.434 | 0.012 | ok |
| {human, orangutan} | 2 | 0.103 | 0.112 | 0.009 | ok |
| {bonobo, gorilla} | 2 | 0.171 | 0.178 | 0.008 | ok |
| {bonobo, chimp, gorilla} | 3 | 0.139 | 0.132 | 0.007 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.233 | 0.238 | 0.005 | ok |
| {chimp, human} | 2 | 0.098 | 0.103 | 0.005 | ok |
| {orangutan, siamang} | 2 | 0.242 | 0.237 | 0.004 | ok |
| {bonobo, chimp, human} | 3 | 0.129 | 0.132 | 0.003 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.410 | 0.407 | 0.003 | ok |
| {gorilla, human, orangutan} | 3 | 0.095 | 0.097 | 0.002 | ok |
| {bonobo, gorilla, human} | 3 | 0.064 | 0.066 | 0.001 | ok |
| {bonobo, chimp, siamang} | 3 | 0.121 | 0.121 | 0.001 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2m23s | 8300 | 209427 | 209427 (`treeLikelihood`) |
| beast3 | 2m06s | 8827 | 252738 | 243122 (`tree.height`) |

Run-time ratio beast3 / beast2: 0.88

