# BEAUti by hand: results

Results per combination for the BEAUti track ([ASSIGNMENTS.md](../ASSIGNMENTS.md)). Comparison
tables are in `reports/summary/<ID>.md`, made with `python3 scripts/compare.py <ID> -b 10`.

Versions: BEAST 2.7.9 Prerelease (BEAST.base 2.7.9) and BEAST 3 v2.8.0-rc2, macOS. Seeds 1 and 2.
Burn-in 10 %.

## Results

| ID | Tester | Chain | Min ESS (b2 / b3, combined) | Verdict | Notes |
|----|--------|------:|----------------------------:|---------|-------|
| C01 | Eva | 3M | 4113 / 3494 | matched | largest z = 2.97, just under the flag threshold |
| C06 | Eva | 10M | 542 / 471 | matched (ESS < 200) | `freqParameter.1stpos.1` has ESS 199 in one BEAST 3 replicate; z = 0.41 |
| C10 | Eva | 10M | 852 / 4644 | matched | |
| C13 🐢 | Eva | 30M | 592 / 684 | matched | `EBSP.log` not compared (non-numeric `popsSize0` column); main log matches |
| C18 | Eva | 10M | 2527 / 2553 | matched, constant offset in `prior` | see [Findings](#findings): script flags `prior` (z = 9.1) |
| C26 | Eva | 20M | 985 / 1434 | matched | every marginal also matches its analytic prior, below |

No `*.trees` files were committed for these runs, so clades were not compared.

### C26: marginals against the analytic prior

Pooled replicates; z = |mean − analytic mean| / (sd / √ESS).

| Parameter | Prior | Analytic mean | BEAST 2 mean (z) | BEAST 3 mean (z) |
|-----------|-------|--------------:|-----------------:|-----------------:|
| birthRate | Gamma(2, scale 2) | 4.000 | 4.012 (0.47) | 3.989 (0.47) |
| gammaShape | Exponential(1), lower 0.1 | 1.100 | 1.085 (1.17) | 1.098 (0.17) |
| kappa | LogNormal(1, 1.25) | 5.937 | 5.826 (0.73) | 5.911 (0.17) |
| freqParameter.1–4 | Dirichlet(4, 4, 4, 4) | 0.250 | z ≤ 1.01 | z ≤ 1.49 |

## Findings

- **C18, gamma-shape prior normalisation.** BEAST 3 `prior` = BEAST 2 `prior` + 0.1 exactly, in
  every sample. BEAUti 3 writes the gamma-shape prior as `TruncatedReal(Exponential(1), lower=0.1)`,
  which normalises the density by 1/P(X > 0.1) = e^0.1. BEAUti 2.7.9 writes `Prior(Exponential(1))`
  on a parameter with `lower="0.1"`, which only enforces the bound. The offset is constant, so the
  posterior is the same. Expect it in any analysis with a gamma shape whose prior has mass below
  0.1. Not raised as an issue.

## Deviations from the run protocol

- Eva's files are named `C01-b2.xml` / `C01-b3.xml` and `log/C01/`, not `beauti-C01.xml` and
  `log/beauti-C01/`, and stdout is `<name>.out`, not `beast.out`. `compare.py` handles both.
- `beast3/log/C18/rep1/` and `rep2/` also hold `18-b3.out`, from a second seed-1 run whose log is
  not in the repo. `C18-b3.out` is the one that matches the committed log.

## BEAUti oddities

None recorded yet.
