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
| C13 🐢 | Eva | 30M | 592 / 684 | **not a valid pass** | the versions agree, but both run `SampleOffValues` with the wrong Hastings ratio, so neither samples the posterior; see [Findings](#findings). `EBSP.log` not compared (non-numeric `popsSize0` column) |
| C18 | Eva | 10M | 2527 / 2553 | matched, constant offset in `prior` | see [Findings](#findings): script flags `prior` (z = 9.1) |
| C26 | Eva | 20M | 985 / 1434 | matched | every marginal also matches its analytic prior, below |

Clades and tMRCAs are not compared yet. Tree files go to the Dropbox folder `beast3-test`
(<https://www.dropbox.com/home/beast3-test>), not git; Eva's are not there yet.

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

- **C13, EBSP off values (all EBSP analyses).** `SampleOffValues` redraws the population sizes whose
  indicators are off from their prior, so it should be accepted every time. In BEAST 2.7.9 and BEAST 3
  rc2 its Hastings ratio is wrong (beast2#1222, fixed in beast3#203 after rc2, beast2#1223 still
  open), and it is accepted only about 2 % of the time (1.9 % in BEAST 2, 2.0 % in BEAST 3 rc2). With
  the fix (the #214 build below), acceptance is 100 % and the off values have mean ≈
  `populationMean` (≈ 42), as their Exponential prior requires; without it they average about 21,
  and the `prior` column is about 66 log units higher. The tree, likelihood and clock rate are
  unaffected. Eva's BEAST 2 and BEAST 3 runs agree because both have the bug. C13 needs rerunning
  once rc3 (or a master build) and a BEAST 2 with beast2#1223 are available. testEBSP is affected
  the same way.

## Subtree-slide variants (BEAST 3 only)

Copies of each BEAST 3 analysis made with `scripts/slide_variants.py`, run by Alexei on 7 Nov,
seeds 1 and 2, on a Mac with other chains running (so run times are not comparable):

- `-slide`: `BactrianSubtreeSlide` started at size 0.01 (what BEAUti 3 writes from beast3#201). Run
  with v2.8.0-rc2 built from source (`aa8512e`), like Eva's default runs.
- `-scale`: `BactrianSubtreeScale` at its default size of 0.3 (beast3#214). Run with the #214 branch
  at `1d7e680`, which is based on a later master than rc2 and includes beast3#203.

Final operator size and acceptance are in `reports/summary/slide-size.md`; posterior comparisons
with the default runs are in `reports/summary/<ID>-<variant>-vs-default.md`.

| ID | Default slide: final size, acceptance | `-slide` vs default | `-scale` vs default |
|----|---------------------------------------|---------------------|---------------------|
| C01 | 0.023, **2.8 %** (stuck, beast3#200) | matched | matched |
| C06 | 0.075, 28 % | borderline: `freqParameter.2ndpos.3` z = 3.16, 1 of ~35 columns | matched |
| C10 | 1.03, 30 % | matched | matched |
| C13 | 1.03, 30 % | matched | **not matched**: the #214 build has the `SampleOffValues` fix and the default (rc2) does not, see [Findings](#findings). Not an operator effect |
| C18 | 0.032, 19 % | matched | matched |
| C26 | 0.24, 30 % | matched | matched |

Both variants reach 29–31 % acceptance in every analysis. The default only fails to tune on C01.

### Mixing: ESS per million steps

C01 and C18 logged every 1,000 steps had ESS close to the number of samples, which hides any
difference, so they were rerun with the trace log every 100 steps (`beast3/log/<ID>-fine*/`, same
builds and seeds; all three set-ups match each other). ESS of the two replicates summed, per million
steps after 10 % burn-in:

| ID | Parameter | default | `-slide` | `-scale` |
|----|-----------|--------:|---------:|---------:|
| C01 | likelihood | 2753 | 3445 | 3269 |
| C01 | Tree.height | 4211 | 6307 | 5309 |
| C01 | Tree.treeLength | 17720 | 17640 | 17862 |
| C18 | likelihood | 2822 | 3091 | 2486 |
| C18 | Tree.height | 10848 | 10530 | 9644 |
| C18 | Tree.treeLength | 7688 | 7575 | 6820 |

On C01, where the default slide is stuck, both variants mix better: `-slide` by 25 % (likelihood) and
50 % (tree height), `-scale` by 19 % and 26 %. On C18, where the default tunes, `-slide` is about
the same as the default and `-scale` is 6–12 % lower. `-scale` also ran 1–4 % slower per step. With
two replicates per set-up, differences of about 10 % are within the noise of the ESS estimate.

### Tall trees: C01 with the clock rate fixed at 1e-4 and 1e-7

Does a slide started at 0.01 tune up on a tall tree? None of our analyses has a tree taller than
about 105, but published BEAST analyses do: on PhyloData, 29 of 110 experiments have a mean root
age ≥ 100 and 3 have one ≥ 1000, the tallest 2.3 million (linck-2020-speciation-ncxu, a Yule tree
with the clock fixed at 2.9e-8 per year). Their BEAST 2.5/2.6 XMLs don't load in BEAST 3, so the
same scale was made from C01 by fixing the clock rate at 1e-4 (tree ≈ 1,900 tall) and 1e-7 (≈ 1.9
million). Otherwise these are C01 and its `-slide` and `-scale` variants, trace log every 100 steps
(`beast3/xml-tall/`, `beast3/log/C01-tall4*`, `C01-tall7*`).

| Tree height | Set-up | Final size | Acceptance | Tuned? |
|------------:|--------|-----------:|-----------:|--------|
| ≈ 1,900 | default (starts at 1.0) | 82.7 | 34 % | yes |
| ≈ 1,900 | `-slide` (starts at 0.01) | 36.9 | 73 % | **no**, BEAST suggests ≈ 74 |
| ≈ 1,900 | `-scale` | 0.19 | 30 % | yes |
| ≈ 1.9 M | default (starts at 1.0) | 7,226 | 95 % | **no**, BEAST suggests ≈ 14,450 |
| ≈ 1.9 M | `-slide` (starts at 0.01) | 81 | 99.9 % | **no** |
| ≈ 1.9 M | `-scale` | 0.19 | 30 % | yes |

In 3M steps (about 590,000 slide proposals) the slide's size grew by a factor of about 8,000 at
most, both from 1.0 and from 0.01 (8.9–9.0 in log size). That is the most auto-tuning can move it
up in a run of this length. A slide that starts too small by more than that stays too small.
`BactrianSubtreeScale` ends at the same size (0.19) on all three tree scales, as a scale-invariant
operator should.

All six set-ups sample the same posterior: the tree height divided by 10⁴ or 10⁷ is 0.1925 in every
case, the same as C01, and every comparison with the default is matched. Only mixing differs. ESS
per million steps (two replicates summed):

| Tree height | Parameter | default | `-slide` | `-scale` |
|------------:|-----------|--------:|---------:|---------:|
| ≈ 0.19 (C01) | likelihood | 2753 | 3445 | 3269 |
| ≈ 0.19 (C01) | Tree.height | 4211 | 6307 | 5309 |
| ≈ 1,900 | likelihood | 3766 | 3079 | 3309 |
| ≈ 1,900 | Tree.height | 6298 | 5039 | 5639 |
| ≈ 1.9 M | likelihood | 3091 | 2505 | 3121 |
| ≈ 1.9 M | Tree.height | 3983 | 3638 | 5681 |

Whichever slide start is wrong for the tree costs about 20–35 % of the ESS, not more, because the other
tree operators (UpDown, Uniform, Exchange, Wilson–Balding) do much of the work. `-scale` gives
about the same ESS on every tree scale.

#### Tuning the slide with a slower-shrinking gain

The limit above comes from the tuning gain, 1/n after n proposals, so the log size can move only
about 0.7 · ln N in a run. `OperatorSchedule` has `transform="sqrt"` (gain 1/√n). It applies to
every operator in its schedule, but an operator is tuned by the schedule it belongs to, so the slide
alone can be given it by moving it from the MCMC operator list into a sub-schedule of the same
weight:

```xml
<operatorschedule id="OperatorSchedule" spec="OperatorSchedule">
    <subschedule id="SlideSchedule" spec="OperatorSchedule" transform="sqrt" weight="15.0">
        <operator id="YuleModelSubtreeSlide.t:anolis" spec="kernel.BactrianSubtreeSlide" tree="@Tree.t:anolis" weight="15.0"/>
    </subschedule>
</operatorschedule>
```

The slide must not also stay in the MCMC operator list, because MCMC assigns its operators to the
main schedule; and `operatorPattern` does not work for this, because it does not change the
operator's schedule. On the 1.9-million-tall tree (`C01-tall7-sqrt`, `C01-tall7-slide-sqrt`, rc2,
seeds 1 and 2):

| Slide start | Final size | Acceptance | likelihood ESS/M | Tree.height ESS/M |
|-------------|-----------:|-----------:|-----------------:|------------------:|
| 1.0, default tuning (stuck) | 7,226 | 95 % | 3091 | 3983 |
| 0.01, default tuning (stuck) | 81 | 99.9 % | 2505 | 3638 |
| 1.0, `sqrt` sub-schedule | 87,500 | 31 % | 3272 | 6462 |
| 0.01, `sqrt` sub-schedule | 86,300 | 31 % | 3836 | 5738 |
| `BactrianSubtreeScale` | 0.19 | 30 % | 3121 | 5681 |

With the `sqrt` gain the slide tunes from both starts, to the same size (0.34 × H/√(2n−1), as on
C01), and mixes at least as well as `BactrianSubtreeScale`. Both runs match the `-scale` posterior.

## Deviations from the run protocol

- Eva's files are named `C01-b2.xml` / `C01-b3.xml` and `log/C01/`, not `beauti-C01.xml` and
  `log/beauti-C01/`, and stdout is `<name>.out`, not `beast.out`. `compare.py` handles both.
- `beast3/log/C18/rep1/` and `rep2/` also hold `18-b3.out`, from a second seed-1 run whose log is
  not in the repo. `C18-b3.out` is the one that matches the committed log.

## BEAUti oddities

None recorded yet.
