# Posterior comparison: C18-slide-vs-default

**Verdict: matched**

- default: `beast3/log/C18/rep1`, `beast3/log/C18/rep2`
- slide: `beast3/log/C18-slide/rep1`, `beast3/log/C18-slide/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 1070; max z: 1.743; max clade |Δp|: –

## Findings

- **NOTE** Trace log file names differ: default `CN-bN.log` paired with slide `CN-bN-slide.log`
- **NOTE** tree files present in only one version; clades not compared

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| default | rep1 | `beast3/log/C18/rep1/C18-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 20m24s |  |
| default | rep2 | `beast3/log/C18/rep2/C18-b3.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 20m24s |  |
| slide | rep1 | `beast3/log/C18-slide/rep1/C18-b3-slide.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 1h14m |  |
| slide | rep2 | `beast3/log/C18-slide/rep2/C18-b3-slide.log` | 10001 (9001) | 1000 | 2.8.0 rc2 | yes | 1h15m |  |

## Parameters: `CN-bN.log / CN-bN-slide.log`

ESS column: combined ESS (minimum over replicates).

| Parameter | default mean | default 95% HPD | default ESS | slide mean | slide 95% HPD | slide ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `posterior` | -1924.50 | [-1929.62, -1920.19] | 13605 (6109) | -1924.48 | [-1929.42, -1920.00] | 11707 (5800) | 0.38 | 98% | ok |
| `likelihood` | -1925.91 | [-1930.53, -1921.98] | 12573 (5712) | -1925.88 | [-1930.36, -1922.01] | 11450 (5473) | 1.14 | 100% | ok |
| `prior` | 1.414 | [-0.6846, 3.426] | 12620 (6281) | 1.392 | [-0.7948, 3.367] | 13735 (6647) | 1.67 | 99% | ok |
| `treeLikelihood` | -1925.91 | [-1930.53, -1921.98] | 12573 (5712) | -1925.88 | [-1930.36, -1922.01] | 11450 (5473) | 1.14 | 100% | ok |
| `Tree.height` | 0.2455 | [0.1975, 0.2996] | 16407 (8054) | 0.2456 | [0.1944, 0.2961] | 16831 (7830) | 0.33 | 97% | ok |
| `Tree.treeLength` | 1.204 | [0.9884, 1.437] | 15537 (7329) | 1.204 | [0.9872, 1.427] | 15349 (7634) | 0.64 | 100% | ok |
| `YuleModel` | 8.647 | [6.504, 10.84] | 16218 (7553) | 8.625 | [6.307, 10.69] | 16226 (8018) | 1.74 | 96% | ok |
| `birthRate` | 7.496 | [2.899, 12.51] | 17572 (8571) | 7.485 | [2.755, 12.55] | 17452 (8451) | 0.39 | 100% | ok |
| `gammaShape` | 0.6771 | [0.421, 0.9727] | 2553 (1153) | 0.6805 | [0.4255, 0.9779] | 2322 (1070) | 0.80 | 99% | ok |

### Replicate agreement (baseline noise): `CN-bN.log / CN-bN-slide.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | default rep means | default max z | slide rep means | slide max z |
|---|---|---:|---|---:|
| `posterior` | -1924.47, -1924.53 | 1.43 | -1924.48, -1924.49 | 0.10 |
| `likelihood` | -1925.88, -1925.94 | 1.47 | -1925.86, -1925.89 | 0.55 |
| `prior` | 1.415, 1.413 | 0.12 | 1.383, 1.402 | 1.04 |
| `treeLikelihood` | -1925.88, -1925.94 | 1.47 | -1925.86, -1925.89 | 0.55 |
| `Tree.height` | 0.2458, 0.2452 | 1.31 | 0.2457, 0.2454 | 0.72 |
| `Tree.treeLength` | 1.205, 1.203 | 1.19 | 1.205, 1.204 | 0.18 |
| `YuleModel` | 8.642, 8.651 | 0.50 | 8.613, 8.638 | 1.42 |
| `birthRate` | 7.466, 7.527 | 1.56 | 7.502, 7.469 | 0.82 |
| `gammaShape` | 0.6756, 0.6787 | 0.55 | 0.6765, 0.6844 | 1.30 |

## Speed

| Version | Total run time | Combined ESS of `posterior` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| default | 40m48s | 13605 | 20008 | 3754 (`gammaShape`) |
| slide | 2h30m | 11707 | 4675 | 927 (`gammaShape`) |

Run-time ratio slide / default: 3.68

