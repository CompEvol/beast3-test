# Posterior comparison: testCalibration

**Verdict: not matched**

- beast2: `beast2/log/testCalibration/rep1`, `beast2/log/testCalibration/rep2`
- beast3: `beast3/log/testCalibration/rep1`, `beast3/log/testCalibration/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 279; max z: 149.04; max clade |Δp|: 0.000

## Findings

- **FLAG** `posterior`: z = 58.10 (beast2 mean -1968.12, beast3 mean -1971.66)
- **FLAG** `prior`: z = 149.04 (beast2 mean -139.61, beast3 mean -143.19)
- **FLAG** `prior`: 95% HPD intervals overlap only 24% of the narrower one
- **NOTE** `posterior` is shifted by -3.544 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.
- **NOTE** `prior` is shifted by -3.58 with about the same sd: if all model parameters match, this is probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), not a different posterior. Check the XMLs before raising an issue.

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testCalibration/rep1/test.1.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 19s |  |
| beast2 | rep2 | `beast2/log/testCalibration/rep2/test.2.log` | 5001 (4501) | 2000 | 2.7.9 Prerelease | yes | 19s |  |
| beast3 | rep1 | `beast3/log/testCalibration/rep1/test.1.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 23s |  |
| beast3 | rep2 | `beast3/log/testCalibration/rep2/test.2.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 24s |  |

## Parameters: `test.N.log`

Constant columns (skipped): `monophyletic(human,chimp)` = 1

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1968.12 | [-1973.01, -1964.02] | 2362 (679) | -1971.66 | [-1976.39, -1967.49] | 5249 (2606) | 58.10 | 62% | **z** |
| `prior` | -139.61 | [-142.14, -137.39] | 3731 (1204) | -143.19 | [-145.72, -141.02] | 11747 (5735) | 149.04 | 24% | **z**, **HPD** |
| `tree.height` | 0.06419 | [0.05299, 0.07691] | 8193 (4054) | 0.06409 | [0.05251, 0.07621] | 16231 (7625) | 1.17 | 98% | ok |
| `mrca.age(human,chimp)` | 0.01704 | [0.01181, 0.02256] | 7503 (3544) | 0.01702 | [0.01189, 0.0226] | 12155 (5907) | 0.56 | 100% | ok |
| `popSize` | 0.1054 | [0.03162, 0.2221] | 9002 (4501) | 0.1048 | [0.02972, 0.2155] | 16753 (8306) | 0.73 | 99% | ok |
| `hky.kappa` | 27.13 | [14.02, 41.96] | 1719 (279) | 26.89 | [14.23, 41.49] | 6376 (2942) | 0.97 | 100% | ok |
| `hky.frequencies.1` | 0.3267 | [0.2955, 0.3563] | 1430 (678) | 0.3262 | [0.2969, 0.3583] | 1678 (792) | 0.87 | 98% | ok |
| `hky.frequencies.2` | 0.2579 | [0.2313, 0.288] | 1620 (804) | 0.258 | [0.2298, 0.2863] | 2018 (907) | 0.17 | 97% | ok |
| `hky.frequencies.3` | 0.155 | [0.1317, 0.1764] | 1554 (733) | 0.1547 | [0.1335, 0.1772] | 2745 (1339) | 0.63 | 98% | ok |
| `hky.frequencies.4` | 0.2604 | [0.2324, 0.2887] | 1461 (691) | 0.2611 | [0.2319, 0.2884] | 2090 (974) | 1.30 | 99% | ok |
| `likelihood` | -1828.51 | [-1832.80, -1824.83] | 2199 (784) | -1828.47 | [-1832.69, -1824.87] | 4254 (2092) | 0.62 | 100% | ok |
| `coalescent` | 6.85 | [5.094, 8.262] | 8308 (4066) | 6.865 | [5.081, 8.281] | 17461 (8460) | 1.27 | 100% | ok |

### Replicate agreement (baseline noise): `test.N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `posterior` | -1968.09, -1968.15 | 0.51 | -1971.61, -1971.72 | 1.68 |
| `prior` | -139.63, -139.59 | 0.80 | -143.18, -143.20 | 0.84 |
| `tree.height` | 0.06416, 0.06421 | 0.33 | 0.06409, 0.06409 | 0.00 |
| `mrca.age(human,chimp)` | 0.01699, 0.01709 | 1.62 | 0.01703, 0.01701 | 0.37 |
| `popSize` | 0.1066, 0.1042 | 1.84 | 0.1042, 0.1054 | 1.30 |
| `hky.kappa` | 27.39, 26.87 | 0.78 | 26.86, 26.93 | 0.39 |
| `hky.frequencies.1` | 0.3271, 0.3264 | 0.87 | 0.3263, 0.3262 | 0.16 |
| `hky.frequencies.2` | 0.2575, 0.2582 | 1.03 | 0.2582, 0.2578 | 0.64 |
| `hky.frequencies.3` | 0.1549, 0.155 | 0.11 | 0.1546, 0.1549 | 0.67 |
| `hky.frequencies.4` | 0.2605, 0.2604 | 0.10 | 0.2609, 0.2612 | 0.39 |
| `likelihood` | -1828.46, -1828.55 | 0.98 | -1828.42, -1828.52 | 1.39 |
| `coalescent` | 6.852, 6.848 | 0.20 | 6.865, 6.864 | 0.14 |

## Trees: `test.N.trees`

9002 trees (beast2) and 18002 trees (beast3) after burn-in. Clades with p ≥ 0.05 in either version; flag |Δp| > 0.1. Largest |Δp| between replicates: beast2 0.000, beast3 0.000.

| Clade | Size | p beast2 | p beast3 | abs Δp | Flag |
|---|---:|---:|---:|---:|---|
| {chimp, human} | 2 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, human} | 3 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human} | 4 | 1.000 | 1.000 | 0.000 | ok |
| {bonobo, chimp, gorilla, human, orangutan} | 5 | 1.000 | 1.000 | 0.000 | ok |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 38s | 2362 | 221181 | 133916 (`hky.frequencies.1`) |
| beast3 | 47s | 5249 | 405413 | 129627 (`hky.frequencies.1`) |

Run-time ratio beast3 / beast2: 1.21

