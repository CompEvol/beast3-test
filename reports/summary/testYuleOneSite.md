# Posterior comparison: testYuleOneSite

**Verdict: matched**

- beast2: `beast2/log/testYuleOneSite/rep1`, `beast2/log/testYuleOneSite/rep2`
- beast3: `beast3/log/testYuleOneSite/rep1`, `beast3/log/testYuleOneSite/rep2`
- burn-in 10% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS
- thresholds: flag z ≥ 3 (fail ≥ 4), HPD overlap < 50%, ESS < 200, clades p ≥ 0.05 with |Δp| > 0.1 (fail > 0.2); borderline = at most 1 flagged item(s), none failing
- min ESS (any replicate): 2955; max z: 1.114; max clade |Δp|: –

## Findings

- **WARN** column `tree.treeLength` only in beast3; add a line to the --map file if it is a renaming

## Runs

| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |
|---|---|---|---:|---:|---|---|---:|---|
| beast2 | rep1 | `beast2/log/testYuleOneSite/rep1/1.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 1s |  |
| beast2 | rep2 | `beast2/log/testYuleOneSite/rep2/2.log` | 5001 (4501) | 200 | 2.7.9 Prerelease | yes | 1s |  |
| beast3 | rep1 | `beast3/log/testYuleOneSite/rep1/1.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 0s |  |
| beast3 | rep2 | `beast3/log/testYuleOneSite/rep2/2.log` | 5001 (4501) | 200 | 2.8.0 rc2 | yes | 0s |  |

## Parameters: `N.log`

Not compared: only in beast2: –; only in beast3: `tree.treeLength`

ESS column: combined ESS (minimum over replicates).

| Parameter | beast2 mean | beast2 95% HPD | beast2 ESS | beast3 mean | beast3 95% HPD | beast3 ESS | z | HPD overlap | Flag |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| `yule` | -1.493 | [-3.179, -0.1568] | 7120 (3477) | -1.509 | [-3.224, -0.1478] | 8696 (4195) | 1.11 | 100% | ok |
| `tree.height` | 0.5403 | [0.05445, 1.18] | 6550 (2955) | 0.5453 | [0.04574, 1.197] | 8595 (4094) | 0.94 | 100% | ok |

### Replicate agreement (baseline noise): `N.log`

Largest z between two replicates of the same version (same formula as above, per-replicate se).

| Parameter | beast2 rep means | beast2 max z | beast3 rep means | beast3 max z |
|---|---|---:|---|---:|
| `yule` | -1.49, -1.496 | 0.27 | -1.5, -1.517 | 0.88 |
| `tree.height` | 0.5377, 0.5429 | 0.64 | 0.5422, 0.5484 | 0.86 |

## Speed

| Version | Total run time | Combined ESS of `yule` | ESS/hour | Min ESS/hour (any column) |
|---|---:|---:|---:|---:|
| beast2 | 2s | 7120 | 10787987 | 9924511 (`tree.height`) |
| beast3 | 1s | 8696 | 34978111 | 34573706 (`tree.height`) |

Run-time ratio beast3 / beast2: 0.38

