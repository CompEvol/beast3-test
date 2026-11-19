# Package check

Do the main BEAST packages still work with the current BEAST 3, and do they give the same
answers as with the last release candidate?

`check_packages.sh` answers that in one run. It is meant to be run before each release
candidate, and whenever a change to `beast-base` could affect packages.

```bash
packages/check_packages.sh -B ../beast3 -a 2.8.0-rc1
```

The result is [reports/packages-check.md](../reports/packages-check.md). The script exits with
status 1 if a package does not build, fails its unit tests, or does something worse with the
new BEAST 3 than with the baseline.

## What is tested

The packages are listed in [packages.tsv](packages.tsv): ORC, SA, MM, SSM, bModelTest,
StarBeast3 and CCD. Five of them (bModelTest, ORC, SA, StarBeast3, CCD) are bundled with
BEAST 2.8.0 ([beast3#248](https://github.com/CompEvol/beast3/issues/248)). Each is taken from the default branch of its repository and built from source. **The
released package zips that users install are not tested.**

| Step | What it does | Where it is defined |
|---|---|---|
| `install` | Builds the beast3 checkout and installs it in the local Maven repository | |
| `build` | Clones each package, builds it against that BEAST 3, runs its unit tests, and unpacks the package zip into one folder, as if installed | [packages.tsv](packages.tsv) |
| `examples` | Runs the packages' example XMLs with the new BEAST 3 and with the baseline, in replicates with the same seeds, and compares the posteriors with [`scripts/compare.py`](../scripts/compare.py) | [examples.tsv](examples.tsv) |
| `beauti` | Starts the real BEAUti off-screen with all packages installed, sets up a model as a user would, saves the XML and runs it for 200,000 steps. Done with both versions | [scenarios.sh](scenarios.sh) |
| `trees` | Runs TreeAnnotator with the CCD package's point estimates (CCD0, CCD1) and MCC on the same tree file, from the bModelTest example, with both versions. The summary trees must be identical | `check_packages.sh` |
| `report` | Writes the report | [report.py](report.py) |

"New" is the beast3 checkout given with `-B`. "Baseline" is a released BEAST 3 version on Maven
Central, given with `-a`.

## Reading the report

- **Regression**: fails with the new version and passes with the baseline. This is what the
  check is for.
- **Known problem**: fails with both versions. It is a bug in the package or in BEAST, but not
  one caused by changes since the baseline. Each should have an issue in the repository it
  belongs to.
- **Verdict** of an example: the verdict of `scripts/compare.py`. "ESS < 200" in a verdict means
  the chain was too short for some parameter; it does not mean the versions disagree. Raise the
  chain length in `examples.tsv` if it keeps happening.
- **"not matched" is a reason to look, not yet a finding.** Rerun that example with more
  replicates and a longer chain (`-e NAME -n 8`, and raise its chain length) before believing
  it. On 11 Nov 2026, `M3982` with 2 replicates of 5M steps gave z = 3.4 on the Yule density
  with an estimated ESS in the thousands; with 4 replicates of 10M the versions agreed (largest
  z 1.5). The ESS estimate had missed slow mixing of the tree.
- An example that is **identical** in both versions (same seed, same numbers) means that no
  change since the baseline touched anything that example uses.

The work folder (`packages/work/`, not in git) keeps everything: the package clones in `src/`,
the build logs, each run in `examples/<new|base>/<example>/rep<N>/`, the full comparison of each
example in `summary/`, and each BEAUti scenario in `beauti/<new|base>/<scenario>/` with the
BEAUti output (`beauti.out`), the saved XML and the BEAST output (`beast.out`).

## Prerequisites

- JDK 25 or later and Maven, as for building beast3. `JAVA_HOME` is used when set, otherwise
  the JDK Maven runs on.
- A beast3 checkout. The `install` step runs `mvn install -DskipTests` in it, which replaces the
  BEAST 3 snapshot in your local Maven repository (`~/.m2`).
- git, Python 3 (standard library only) and network access: the packages are cloned from GitHub
  and the baseline comes from Maven Central.
- About 300 MB of disk and, with the defaults, about an hour and a half on a recent laptop.

Nothing in your BEAST folder (`~/Library/Application Support/BEAST`, `~/.beast`) is read or
changed. The runs use the packages built here and their own settings folder.

So far this has only been run on macOS.

## Options

```
-B DIR      beast3 checkout to test (default ../beast3, next to this repository)
-a VERSION  baseline BEAST 3 version on Maven Central (default 2.8.0-rc1)
-w DIR      work folder (default packages/work)
-n N        replicates per example and version (default 4; seeds 1..N)
-j N        BEAST runs in parallel (default 4; run times are only comparable with -j 1)
-e NAMES    comma-separated examples to run (default: all in examples.tsv)
-f          run every example replicate again, also those that already finished
-s STEPS    comma-separated steps (default install,build,examples,beauti,trees,report)
-o FILE     report file, relative to this repository (default reports/packages-check.md)
```

Example replicates that already finished with the same XML and chain length are kept, so an
interrupted run can be started again and only the missing runs are done; `-f` runs them all.

To repeat one part after a full run, name the steps: `-s beauti,report` reruns the BEAUti
scenarios and rebuilds the report from what is in the work folder.

## Adding to it

- **A package**: one line in `packages.tsv`, in build order (a package after the ones it
  depends on).
- **An example**: one line in `examples.tsv`. Pick a chain length that takes a few minutes and
  gets most parameters to ESS 200.
- **A BEAUti scenario**: one `sc` line in `scenarios.sh`. The steps are described at the top of
  that file. To find the names of the controls, add the steps `dump` (combo boxes), `windows`
  (buttons) or `providers` (importers) and read `beauti.out`.

## How BEAUti is driven

[`Driver.java`](Driver.java) starts the real BEAUti window with headless JavaFX (Monocle, the
same as beast3's GUI tests) and carries out the steps on the JavaFX thread: it selects tabs and
combo box items and fires buttons, so the same listeners run as when a user clicks. Packages
are loaded the way an installed BEAST loads them, from a package folder, not from the class
path.

It uses BEAUti's internal classes and the ids of its controls. It is compiled against the new
BEAST 3 on every run, so if those internals change, the `beauti` step stops with a compile
error, or a scenario fails with "could not pick" or "no button". That is a reason to update the
driver or the scenario, not a regression in a package.

## Installer check

`check_packages.sh` builds the packages from source and never touches an installer, so it cannot
see what is missing from one: the rc3 installer could not install a package from Maven at all
([beast3#297](https://github.com/CompEvol/beast3/issues/297)). `check_installer.sh` tests an
installer as shipped, through its own `bin/` scripts. Run it on every release candidate, from
rc4 on:

```bash
packages/check_installer.sh -d BEAST.v2.8.0-rc4.dmg          # macOS: mounted read-only
packages/check_installer.sh -i "/Applications/BEAST 2.8.0"   # an installed or unpacked BEAST
```

It takes a few minutes and writes [reports/installer-check.md](../reports/installer-check.md).

| Check | What it does |
|---|---|
| `beast` | `bin/beast` runs the installer's `examples/testHKY.xml` for 200,000 steps (its trees are used below) |
| `bundled-list` | `applauncher -list` on a new package folder: the bundled packages are unpacked on first launch, and their apps (CCD's EntropyCalculator among them) are listed |
| `bundled-run` | `applauncher EntropyCalculator -trees ... -output ...`: a bundled package's app runs with its arguments and writes its output |
| `maven-install` | `packagemanager -maven io.github.compevol:ccd:1.2.2` in another new package folder, with the bundled CCD removed first, so CCD comes from Maven Central |
| `maven-list` | `applauncher -list` shows the apps of that Maven-installed CCD ([beast3#82](https://github.com/CompEvol/beast3/issues/82)) |
| `maven-run` | its EntropyCalculator runs with arguments, as for the bundled copy |
| `maven-load` | `packagemanager -maven io.github.beast2-dev:beast-labs:2.1.0-beta2` in that folder, then `bin/beast` must load BEASTLabs. Its Nashorn needs the JDK module `jdk.dynalink`, which the launchers' boot layer does not have; when the JVM rejects the load plan, BEAST runs without any of its packages, which a run needing only the core does not show |
| `maven-first` | `packagemanager -maven io.github.compevol:ccd:1.2.2` in an empty package folder, before any other program has run: `packagemanager` must unpack the bundled core itself, or every Maven package is refused as needing BEAST.base |
| `load-plan` | no log of the checks above says "rejected the load plan" or "Loading BEAST without its packages" |

Everything runs headless (`-Djava.awt.headless=true`), so no window opens; each command is
stopped after 300 s (`-t`). The package folders are in `packages/work/installer/`, given to BEAST
with `-Dbeast.user.package.dir`, so your own BEAST folder is not read or changed. Each check's
output is kept there too.

A failure caused by an open issue is reported as KNOWN with a link to it, and does not make the
script fail; the list is `KNOWN=` at the top of the script. A line can end with a text from the
check's log (`work/installer/<check>.out`); then the failure is KNOWN only when the log has it,
so the same check failing for another reason still fails. `maven-first` and `maven-load` are
KNOWN only for the missing resolver of #297. Remove a line when its issue is fixed, so that the
check counts again. The script exits with status 1 on any other failure.

On rc3: `beast`, `bundled-list` and `bundled-run` pass; the Maven checks fail (#297, and #82 for
the list).

`maven-load`, `maven-first` and `load-plan` were added after an unsigned bundle of beast3#315
merged with #308 passed the first six checks while BEAST loaded none of its Maven packages once
BEASTLabs was installed, and `packagemanager` refused every package on a new install. Both are
fixed in beast3#315 (411d4af, 116710d); on that bundle without the two fixes the three new checks
fail, with them all nine pass.

## Limits

- Default branches built from source, not released zips (the [installer check](#installer-check)
  covers the zips bundled with an installer).
- An example run compares two versions of BEAST 3 with the same package build. It does not
  compare with BEAST 2.
- A BEAUti scenario shows that the XML BEAUti writes is valid and samples. It does not compare
  posteriors.
- BEAST exits with status 0 after an exception in the run
  ([beast3#265](https://github.com/CompEvol/beast3/issues/265)), so the script decides that a run
  finished from the "End likelihood" line in its output.
- StarBeast3 cannot be started with `mvn exec:exec` from its own project
  ([starbeast3#19](https://github.com/rbouckaert/starbeast3/issues/19)); here it is run as an
  installed package, which works.
