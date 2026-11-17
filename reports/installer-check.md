# Installer check

Installer: `BEAST.v2.8.0-rc3.dmg` (beast-pkgmgmt 2.8.0-SNAPSHOT), run 2026-11-18 11:31 on Darwin arm64.
Made by [packages/check_installer.sh](../packages/check_installer.sh); see [packages/README.md](../packages/README.md#installer-check).

| Check | Result | What | Detail |
|---|---|---|---|
| beast | PASS | bin/beast runs examples/testHKY.xml (200,000 steps) | trees: 401 |
| bundled-list | PASS | applauncher -list shows the apps of bundled packages | 15 apps; packages seeded: BEAST.app BEAST.base bModelTest CCD ORC SA starbeast3  |
| bundled-run | PASS | applauncher EntropyCalculator (bundled CCD) with arguments | entropy 0.5860880277326023 |
| maven-install | KNOWN | packagemanager -maven io.github.compevol:ccd:1.2.2 | UnsupportedOperationException: Maven resolver not available on the module path. Maven package install/load requires maven-resolver-supplier-mvn4. ([297](https://github.com/CompEvol/beast3/issues/297)) |
| maven-list | KNOWN | applauncher -list shows the apps of a Maven-installed package | EntropyCalculator not listed ([82](https://github.com/CompEvol/beast3/issues/82)) |
| maven-run | KNOWN | applauncher EntropyCalculator (Maven-installed) with arguments | see work/installer/maven-run.out ([297](https://github.com/CompEvol/beast3/issues/297)) |

KNOWN: fails because of the open issue linked. Logs are in `packages/work/installer/` (not in git).
