# Posterior comparison: testCoalescent

**Verdict: matched**

- beast2: `beast2/log/testCoalescent/rep1`, `beast2/log/testCoalescent/rep2`
- beast3: `beast3/log/testCoalescent/rep1`, `beast3/log/testCoalescent/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1781; max z: 0.1302; max clade |Δp|: 0.002

## Findings

- none

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testCoalescent/rep1/test.1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast2 | rep2 | `beast2/log/testCoalescent/rep2/test.2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 4s |  |
| beast3 | rep1 | `beast3/log/testCoalescent/rep1/test.1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 2s |  |
| beast3 | rep2 | `beast3/log/testCoalescent/rep2/test.2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 2s |  |

## Parameters: `test.N.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `coalescent` | 6.965 | [4.553, 8.714] | 3881 (1937) | 6.968 | [4.598, 8.694] | 8227 (4099) | 0.13 | 100% | ok |
| `treeLikelihood` | -1815.70 | [-1819.31, -1812.85] | 7448 (3684) | -1815.70 | [-1819.30, -1812.83] | 8480 (4160) | 0.06 | 100% | ok |
| `popSize` | 0.1312 | [0.0303, 0.2974] | 3597 (1781) | 0.131 | [0.03318, 0.2956] | 8057 (3621) | 0.11 | 100% | ok |
| `hky.kappa` | 32.84 | [15.13, 54.17] | 5921 (2750) | 32.85 | [15.84, 54.75] | 8803 (4302) | 0.10 | 99% | ok |
| `posterior` | -1808.74 | [-1812.99, -1805.23] | 5932 (2928) | -1808.73 | [-1812.98, -1805.24] | 8332 (4089) | 0.13 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `coalescent` | 6.947, 6.984 | 1.01 | 6.976, 6.96 | 0.65 |
| `treeLikelihood` | -1815.72, -1815.68 | 1.01 | -1815.72, -1815.68 | 0.92 |
| `popSize` | 0.1322, 0.1302 | 0.65 | 0.1306, 0.1314 | 0.38 |
| `hky.kappa` | 32.83, 32.84 | 0.03 | 32.74, 32.97 | 0.97 |
| `posterior` | -1808.78, -1808.70 | 1.42 | -1808.74, -1808.72 | 0.42 |

## Trees: `test.N.trees`

9002 trees (beast2) and 9002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.011, beast3 0.009.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {bonobo, chimp, gorilla, human, siamang} | 5 | 0.126 | 0.124 | 0.002 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 0.846 | 0.844 | 0.001 | ok |
| {bonobo, chimp, human} | 3 | 0.998 | 0.999 | 0.001 | ok |
| {bonobo, chimp} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 8s | 5932 | 2811090 | 1704555 (`popSize`) |
| beast3 | 4s | 8332 | 7761104 | 7504168 (`popSize`) |

Run-time ratio beast3 / beast2: 0.51

