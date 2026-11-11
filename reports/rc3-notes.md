<!-- Panels under the table on the rc3 page (scripts/build_status_page.py).
     Same format as reports/status-notes.md. -->

## Before the round

1. **rc3 is released** with the five packages bundled and seeded on first launch ([beast3#248](https://github.com/CompEvol/beast3/issues/248)).
1. **BEAST 2.7.9** has the 2.7 versions of bModelTest, ORC, SA, StarBeast3 and CCD installed, plus SSM for the GTR comparisons. Check that SA's 2.7 package ships `bears.nex`.
1. **The automated package check** has run on rc3: build, unit tests, examples, BEAUti scenarios and TreeAnnotator with CCD for all five packages.

## What is different from the rc2 round

- Everything is built with the rc3 installer as shipped; nothing is installed through the package manager in BEAST 3.
- The 2.7.9 side of the GTR combinations (R01, R03, R09, R10) uses SSM's GTR, which has the same Dirichlet prior on the rates as BEAUti 3's GTR ([beast3#251](https://github.com/CompEvol/beast3/pull/251)).
- **Default priors differ between the versions.** rc3's BEAUti uses wide log-normal default priors (beast3#208); the matching change for BEAUti 2.7, BeastFX#111, is not merged. So a model built with defaults gets different priors in the two versions: set every prior by hand to match the 2.7.9 XML, and record it.
- R18 is not built in BEAUti: TreeAnnotator with CCD0 and CCD1 on the same tree file in both versions must give identical summary trees.
- The 18 rc2 combinations that passed are not rebuilt by hand; their BEAST 3 XMLs are rerun on rc3 and compared automatically.
