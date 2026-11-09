# Posterior comparison: testHKY-json

**Verdict: matched**

- beast2: `beast2/log/testHKY-json/rep1`, `beast2/log/testHKY-json/rep2`
- beast3: `beast3/log/testHKY-json/rep1`, `beast3/log/testHKY-json/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 4060; max z: 1.466; max clade |Δp|: 0.005

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming
- **NOTE** tree files read from `/Users/adru001/Library/CloudStorage/Dropbox/beast3-test`

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testHKY-json/rep1/test.$(seed).log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 11s |  |
| beast2 | rep2 | `beast2/log/testHKY-json/rep2/test.$(seed).log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 12s |  |
| beast3 | rep1 | `beast3/log/testHKY-json/rep1/test.$(seed).log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 8s |  |
| beast3 | rep2 | `beast3/log/testHKY-json/rep2/test.$(seed).log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 9s |  |

## Parameters: `test.$(seed).log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -1815.69 | [-1819.08, -1812.82] | 8966 (4465) | -1815.65 | [-1819.19, -1812.89] | 9002 (4501) | 1.47 | 99% | ok |
| `hky.kappa` | 29.79 | [14.33, 47.87] | 8715 (4214) | 29.97 | [14.54, 48.1] | 8664 (4163) | 1.32 | 99% | ok |
| `tree.height` | 0.06424 | [0.05216, 0.07619] | 8563 (4062) | 0.06413 | [0.05216, 0.07592] | 8466 (4060) | 1.18 | 100% | ok |

### Replicate agreement (baseline noise): `test.$(seed).log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -1815.70, -1815.69 | 0.24 | -1815.65, -1815.66 | 0.22 |
| `hky.kappa` | 29.8, 29.77 | 0.13 | 29.96, 29.99 | 0.14 |
| `tree.height` | 0.06424, 0.06424 | 0.04 | 0.06407, 0.06419 | 0.91 |

## Trees: `test.$(seed).trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.004, beast3 0.011.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.826 | 0.831 | 0.005 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.137 | 0.135 | 0.002 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 23s | 8966 | 1383108 | 1320839 (`tree.height`) |
| beast3 | 17s | 9002 | 1906418 | 1792905 (`tree.height`) |

Run-time ratio beast3 / beast2: 0.73

