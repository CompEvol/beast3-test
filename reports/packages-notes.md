# Package check: notes

Hand-written notes on the results in [packages-check.md](packages-check.md), which is rewritten
by every run of `packages/check_packages.sh`.

## 11–12 Nov 2026: beast3 `master` (c8744a3) against 2.8.0-rc1

No regressions. The points below needed a closer look.

### M3982 (MM): a false "not matched"

With 2 replicates of 5M steps, the Yule density and the prior differed between the versions by
z = 3.4, with an estimated ESS in the thousands and close agreement between the two replicates
of each version (prior 48.82 and 48.76 with rc1, 48.33 and 48.28 with master).

It was not real. With 4 replicates of 10M steps the versions agree: prior 48.52 against 48.47,
largest z over all columns 1.5. The same seeds, run on from 5M to 10M, drifted back together,
so the ESS estimate had missed slow mixing of the tree.

Variants of the XML, 4 replicates of 10M each:

| Variant | rc1 against master |
|---|---|
| full model | matched, largest z 1.5 |
| without `BactrianSubtreeSlide` | identical to the last digit |
| prior only (`sampleFromPrior`) | matched, largest z 0.6 |
| prior only, without `BactrianSubtreeSlide` | identical |

So `BactrianSubtreeSlide` is the only thing this analysis uses that changed since rc1, and with
it the two versions sample the same posterior. The example now runs 4 replicates of 10M.

### gophers (StarBeast3): one parameter borderline, not explained

With 8 replicates of 15M steps, `SpeciesTreeRelaxedClockSD` is 0.2837 with rc1 and 0.2752 with
master, z = 3.2. The spread between the replicate means gives the same z, so it does not depend
on the ESS estimate:

| | Replicate means | Mean | Standard error |
|---|---|---:|---:|
| rc1 | 0.2935 0.2762 0.2824 0.2892 0.2782 0.2820 0.2793 0.2885 | 0.2837 | 0.0022 |
| master | 0.2799 0.2716 0.2782 0.2672 0.2768 0.2772 0.2778 0.2732 | 0.2752 | 0.0015 |

The other 59 columns agree (the variance and coefficient of variation of the species-tree rates,
which measure the same thing, have z = 2.6 and 2.7). One column in 60 at this level is expected
by chance about one time in three, so this is suggestive and not a finding.

What is known:

- gophers uses the operators that changed most since rc1: three AVMN operators, ten
  `AdaptableOperatorSampler`s and `BactrianSubtreeSlide`. Two of the changes were corrections to
  the Hastings ratio of AVMN, so if the difference is real, master may be the correct one.
- Sampling from the prior (8 replicates of 5M), where this parameter is exactly Gamma(5, 0.05)
  with mean 0.25, both versions are right: 0.2529 with rc1 and 0.2495 with master. Mixing under
  the prior is poor for several other parameters (ESS 5 to 15), so that run says nothing about
  them.

To settle it: more replicates of gophers (`packages/check_packages.sh -e gophers -n 16 -s
examples,report`), or the well-calibrated simulation study in
[starbeast3#18](https://github.com/rbouckaert/starbeast3/issues/18).

### Known problems, present with rc1 too

- The six SSM models with estimated rates give a BEAUti XML that crashes at the first posterior
  calculation: [substmodels#8](https://github.com/BEAST2-Dev/substmodels/issues/8).
- BEAST exits with status 0 after that crash:
  [beast3#265](https://github.com/CompEvol/beast3/issues/265).

### Low ESS

Several examples have parameters below ESS 200 at the chain lengths in
`packages/examples.tsv` (bears and bears_ranges as low as 3 to 7, beast2-paper 3). For the three
SA examples it does not matter: the two versions give identical numbers. For the others, a
"matched" verdict with "ESS < 200" is weaker than it sounds; the chains would have to be much
longer to compare those parameters.
