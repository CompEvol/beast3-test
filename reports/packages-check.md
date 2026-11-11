# Package check

Written by `packages/check_packages.sh`; do not edit by hand. See [packages/README.md](../packages/README.md) for what is tested and how to read this.

**Result: no regressions.** 6 known problem(s), also present in 2.8.0-rc1.

Known problems (fail with both versions, so not caused by changes since 2.8.0-rc1):

- BEAUti scenario `SSM-Standard_K80`: java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be
- BEAUti scenario `SSM-Standard_HKY`: java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be
- BEAUti scenario `SSM-Standard_Tr_N`: java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be
- BEAUti scenario `SSM-Standard_TVM`: java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be
- BEAUti scenario `SSM-Standard_SYM`: java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be
- BEAUti scenario `SSM-Standard_GTR`: java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be

| | |
|---|---|
| Date | 2026-11-12 |
| New | BEAST 2.8.0-SNAPSHOT, beast3 branch `master`, commit `b3427c2` |
| Baseline | BEAST 2.8.0-rc1 from Maven Central |
| Java | openjdk version "26.0.1" 2026-04-21 |
| Machine | Darwin arm64 |
| Example runs | 4 replicate(s) per version in the last run, 4 at a time; an example run with `-e` may have more (column Finished) |

## Build and unit tests against BEAST 2.8.0-SNAPSHOT

Each package's default branch, built from source.

| Package | Repository | Commit | Version | Builds | Unit tests |
|---|---|---|---|---|---|
| ORC | [jordandouglas/ORC](https://github.com/jordandouglas/ORC) | `a19ae1d` | 1.3.1 | yes | no unit tests |
| SA | [CompEvol/sampled-ancestors](https://github.com/CompEvol/sampled-ancestors) | `596bfd0` | 2.3.0 | yes | Tests run: 10, Failures: 0, Errors: 0, Skipped: 0 |
| MM | [CompEvol/morph-models](https://github.com/CompEvol/morph-models) | `39e34c1` | 1.3.1 | yes | Tests run: 8, Failures: 0, Errors: 0, Skipped: 0 |
| SSM | [BEAST2-Dev/substmodels](https://github.com/BEAST2-Dev/substmodels) | `41c4107` | 1.3.2 | yes | Tests run: 22, Failures: 0, Errors: 0, Skipped: 0 |
| bModelTest | [BEAST2-Dev/bModelTest](https://github.com/BEAST2-Dev/bModelTest) | `106a45f` | 1.4.0 | yes | Tests run: 37, Failures: 0, Errors: 0, Skipped: 0 |
| starbeast3 | [rbouckaert/starbeast3](https://github.com/rbouckaert/starbeast3) | `0003b37` | 1.3.1 | yes | no unit tests |
| CCD | [CompEvol/CCD](https://github.com/CompEvol/CCD) | `7e93fb5` | 1.2.2 | yes | Tests run: 110, Failures: 0, Errors: 0, Skipped: 1 |

## Example XMLs: BEAST 2.8.0-SNAPSHOT against 2.8.0-rc1

Each example is run with both versions, same seeds, and the posteriors are compared with `scripts/compare.py` (10% burn-in, flag z ≥ 3, fail z ≥ 4). "ESS < 200" in a verdict means the chain was too short for some parameter, not that the versions disagree.

| Example | Package | Chain | Finished (2.8.0-rc1) | Finished (2.8.0-SNAPSHOT) | Time, s (2.8.0-rc1) | Time, s (2.8.0-SNAPSHOT) | Verdict | Detail |
|---|---|---:|---|---|---:|---:|---|---|
| caterpillars | ORC | 8000000 | 4/4 | 4/4 | 451 | 466 | matched (ESS < 200) | min ESS (any replicate): 116; max z: 1.289; max clade \|Δp\|: – |
| bears | sampled-ancestors | 5000000 | 4/4 | 4/4 | 34 | 34 | identical | min ESS (any replicate): 3; max z: 0; max clade \|Δp\|: – |
| bears_ranges | sampled-ancestors | 5000000 | 4/4 | 4/4 | 28 | 28 | identical | min ESS (any replicate): 7; max z: 0; max clade \|Δp\|: – |
| brachiopods | sampled-ancestors | 5000000 | 4/4 | 4/4 | 18 | 18 | identical | min ESS (any replicate): 659; max z: 0; max clade \|Δp\|: – |
| M3982 | morph-models | 10000000 | 4/4 | 4/4 | 87 | 88 | matched | min ESS (any replicate): 469; max z: 1.48; max clade \|Δp\|: – |
| bModelTest | bModelTest | 3000000 | 4/4 | 4/4 | 91 | 91 | matched (ESS < 200) | min ESS (any replicate): 15; max z: 1.498; max clade \|Δp\|: – |
| beast2-paper | bModelTest | 1000000 | 4/4 | 4/4 | 201 | 199 | matched (ESS < 200) | min ESS (any replicate): 3; max z: 2.54; max clade \|Δp\|: – |
| primates | bModelTest | 3000000 | 4/4 | 4/4 | 143 | 144 | matched (ESS < 200) | min ESS (any replicate): 7; max z: 2.059; max clade \|Δp\|: – |
| gophers | starbeast3 | 15000000 | 16/16 | 16/16 | 1462 | 1466 | matched (ESS < 200) | min ESS (any replicate): 72; max z: 2.299; max clade \|Δp\|: – |

The full comparison of each example is in the work folder, `summary/<example>.md`.

## BEAUti with all packages installed

Each scenario (`packages/scenarios.sh`) starts BEAUti, sets the model up as a user would, saves the XML and runs it for 200,000 steps. "yes" means BEAUti finished the steps without an exception, wrote the XML, and BEAST ran it to the end.

| Scenario | 2.8.0-rc1 | 2.8.0-SNAPSHOT | Problem |
|---|---|---|---|
| default | yes | yes |  |
| core-HKY | yes | yes |  |
| core-TN93 | yes | yes |  |
| core-GTR | yes | yes |  |
| bModelTest | yes | yes |  |
| SSM-Standard_K80 | **XML does not run** | **XML does not run** | java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be |
| SSM-Standard_HKY | **XML does not run** | **XML does not run** | java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be |
| SSM-Standard_Tr_N | **XML does not run** | **XML does not run** | java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be |
| SSM-Standard_TVM | **XML does not run** | **XML does not run** | java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be |
| SSM-Standard_SYM | **XML does not run** | **XML does not run** | java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be |
| SSM-Standard_GTR | **XML does not run** | **XML does not run** | java.lang.ClassCastException: class beast.base.spec.inference.parameter.RealVectorParam cannot be cast to class beast.base.spec.type.Simplex (beast.base.spec.inference.parameter.RealVectorParam and be |
| ORC | yes | yes |  |
| SA-FBD | yes | yes |  |
| bModelTest-ORC-FBD | yes | yes |  |
| MM-M3982-Yes | yes | yes |  |
| MM-penguins-Yes | yes | yes |  |
| MM-M3982-No | yes | yes |  |
| MM-penguins-No | yes | yes |  |
| StarBeast3 | yes | yes |  |

## TreeAnnotator with the CCD package

Both versions summarise the same tree file (`examples/new/bModelTest/rep1/dna.trees`) with the CCD package's point estimates and, as a control, MCC. "Identical" compares the summary trees, ignoring comment lines.

| Method | Runs (2.8.0-rc1) | Runs (2.8.0-SNAPSHOT) | Identical |
|---|---|---|---|
| CCD0 | yes | yes | yes |
| CCD1 | yes | yes | yes |
| MCC | yes | yes | yes |

