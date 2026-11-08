# Posterior comparison: testHKY-json

**Verdict: not matched**

- beast2: `beast2/log/testHKY-json/rep1`, `beast2/log/testHKY-json/rep2`
- beast3: `beast3/log/testHKY-json/rep1`, `beast3/log/testHKY-json/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 3946; max z: 116.39; max clade |Δp|: 0.006

## Findings

- **FLAG** `treeLikelihood`: z = 48.17 (beast2 mean -1815.63, beast3 mean -1817.12)
- **FLAG** `hky.kappa`: z = 116.39 (beast2 mean 30.1, beast3 mean 17.58)
- **FLAG** `tree.height`: z = 4.95 (beast2 mean 0.06416, beast3 mean 0.0637)
- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testHKY-json/rep1/test.$(seed).log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 14s |  |
| beast2 | rep2 | `beast2/log/testHKY-json/rep2/test.$(seed).log` | 5001 (4501) | 1000 | 2.7.9 Prerelease | yes | 13s |  |
| beast3 | rep1 | `beast3/log/testHKY-json/rep1/test.$(seed).log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 10s |  |
| beast3 | rep2 | `beast3/log/testHKY-json/rep2/test.$(seed).log` | 5001 (4501) | 1000 | 2.8.0 rc2 | yes | 10s |  |

## Parameters: `test.$(seed).log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `treeLikelihood` | -1815.63 | [-1819.01, -1812.75] | 8937 (4436) | -1817.12 | [-1821.69, -1813.24] | 8878 (4377) | 48.17 | 92% | **z** |
| `hky.kappa` | 30.1 | [14.91, 48.51] | 8652 (4257) | 17.58 | [10.83, 25.44] | 8447 (3946) | 116.39 | 72% | **z** |
| `tree.height` | 0.06416 | [0.05273, 0.07629] | 8750 (4249) | 0.0637 | [0.05172, 0.0752] | 8676 (4175) | 4.95 | 96% | **z** |

### Replicate agreement (baseline noise): `test.$(seed).log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `treeLikelihood` | -1815.66, -1815.61 | 1.41 | -1817.12, -1817.12 | 0.04 |
| `hky.kappa` | 30.07, 30.14 | 0.34 | 17.59, 17.57 | 0.28 |
| `tree.height` | 0.06433, 0.064 | 2.53 | 0.06369, 0.06371 | 0.18 |

## Trees: `test.$(seed).trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.013, beast3 0.006.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.831 | 0.825 | 0.006 | ok |
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.133 | 0.137 | 0.004 | ok |
| {bonobo, chimp, human} | 3 | 0.999 | 0.999 | 0.000 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `treeLikelihood` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 27s | 8937 | 1174959 | 1137485 (`hky.kappa`) |
| beast3 | 21s | 8878 | 1538065 | 1463335 (`hky.kappa`) |

Run-time ratio beast3 / beast2: 0.76

