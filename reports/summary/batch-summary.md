# Batch comparison (beast2 vs beast3, burn-in 10%)

| Name | Reps (beast2/beast3) | Min ESS | Max z | Max clade Δp | Flagged | Verdict |
|---|---|---:|---:|---:|---:|---|
| C01 | 2/2 | 1663 | 2.966 | – | 0 | matched |
| C02 | 2/2 | 1275 | 1.84 | – | 0 | matched |
| C03 | 2/2 | 146 | 1.683 | – | 0 | matched (ESS < 200) |
| C04 | 2/2 | 220 | 1.805 | – | 0 | matched (run problems) |
| C05 | 2/2 | 223 | 1.359 | 0.007 | 0 | matched |
| C06 | 4/4 | 288 | 9.109 | – | 3 | not matched (constant `prior` offset, see beauti-manual) |
| C07 | 2/2 | 872 | 1.18 | – | 0 | matched |
| C08 | 2/2 | – | – | – | 0 | no comparison |
| C09 | 2/2 | 282 | 2.583 | – | 0 | matched |
| C10 | 2/2 | 383 | 1.904 | – | 0 | matched |
| C11 | 2/2 | 338 | 2.295 | – | 0 | matched |
| C12 | 2/2 | 1180 | 167.3 | – | 9 | not matched (run problems) |
| C13 | 2/2 | 243 | 2.884 | – | 0 | matched |
| C14 | 2/2 | 253 | 2.724 | 0.010 | 0 | matched (run problems) |
| C15 | 2/2 | 427 | 5.295 | 0.052 | 222 | not matched |
| C16 | 2/2 | 206 | 1.124 | – | 0 | matched (run problems) |
| C17 | 2/2 | 286 | 2.104 | 0.008 | 0 | matched |
| C18 | 2/2 | 1146 | 9.096 | – | 1 | not matched |
| C19 | 2/2 | 1253 | 0.9438 | – | 0 | matched |
| C20 | 2/2 | 1182 | 1.019 | – | 0 | matched (run problems) |
| C21 | 2/2 | 6040 | 377.96 | 0.052 | 7 | not matched |
| C22 | 2/2 | 149 | 2.401 | – | 0 | matched (ESS < 200) |
| C23 | 2/2 | 305 | 2.283 | – | 0 | matched |
| C24 | 2/2 | 246 | 2.286 | 0.001 | 0 | matched |
| C25 | 2/2 | 246 | 2.159 | – | 0 | matched (run problems) |
| C26 | 2/2 | 475 | 1.733 | – | 0 | matched |
| C27 | 2/2 | 207 | 8.229 | – | 1 | not matched |
| C29 | 2/2 | 242 | 1.692 | – | 0 | matched (run problems) |
| C30 | 2/2 | 227 | 2.246 | – | 0 | matched (run problems) |
| bitflip | 2/2 | 3510 | 0 | – | 0 | matched |
| testBSP | 2/2 | 2429 | 1.911 | 0.018 | 0 | matched |
| testCalYule_5t_2c | 2/2 | 355 | 2.098 | 0.005 | 0 | matched |
| testCalYule_5t_2c-analytic | 4/4 | 4089 | 1.054 | 0.006 | 0 | matched |
| testCalYule_5t_2c-v278 | 2/2 | 355 | 2.925 | 0.010 | 0 | matched |
| testCalibration | 2/2 | 571 | 1.328 | 0.000 | 0 | matched |
| testClassicRootCalibrationPrior | 2/2 | 3318 | 0.6507 | 0.009 | 0 | matched |
| testClassicRootCalibrationPrior-v278 | 2/2 | 3624 | 1.462 | 0.009 | 0 | matched |
| testCoalescent | 2/2 | 1977 | 1.88 | 0.007 | 0 | matched |
| testCoalescent-v278 | 2/2 | 1187 | 0.4141 | 0.011 | 0 | matched |
| testConditionalRootCalibrationPrior | 2/2 | 9 | 4.859 | 0.083 | 2 | not matched (ESS < 200) |
| testConditionalRootCalibrationPrior-analytic | 2/2 | 9 | 4.859 | 0.083 | 2 | not matched (ESS < 200) |
| testEBSP | 2/2 | 475 | 2.657 | 0.010 | 0 | matched |
| testExponentialGrowth | 2/2 | 1898 | 1.058 | 0.010 | 0 | matched |
| testExponentialGrowth-v278 | 2/2 | 1540 | 2.386 | 0.010 | 0 | matched |
| testGTR | 2/2 | 264 | 678.18 | 0.002 | 2 | not matched |
| testHKY | 2/2 | 4060 | 1.466 | 0.005 | 0 | matched |
| testHKY-json | 2/2 | 4060 | 1.466 | 0.005 | 0 | matched |
| testJukesCantor | 2/2 | 3962 | 1.944 | 0.030 | 0 | matched |
| testJukesCantorShort | 2/2 | 3778 | 0.5126 | 0.005 | 0 | matched |
| testJukesCantorShortUncertain | 2/2 | 3955 | 2.531 | 0.014 | 0 | matched |
| testJukesCantorShortUncertain2 | 2/2 | 3970 | 0.1711 | 0.009 | 0 | matched |
| testJukesCantorShortUncertain2MLE | 2/2 | 4220 | 1.365 | 0.053 | 0 | matched |
| testOpSubSchedule | 2/2 | 2676 | 1.286 | 0.002 | 0 | matched |
| testPlates | 2/2 | 224 | 0.9307 | 0.009 | 0 | matched |
| testRNA | 2/2 | 264 | 678.18 | 0.002 | 2 | not matched |
| testRestrictedGTR | 2/2 | 221 | 1056.12 | 0.001 | 2 | not matched |
| testSYM | 4/4 | 583 | 892.66 | 0.004 | 2 | not matched |
| testTIM | 2/2 | 313 | 1044.94 | 0.001 | 2 | not matched |
| testTN93 | 2/2 | 216 | 1063.12 | 0.004 | 2 | not matched |
| testTVM | 2/2 | 287 | 752.57 | 0.002 | 2 | not matched |
| testTwoCalibrationsPrior | 2/2 | 3725 | 1.625 | 0.004 | 0 | matched |
| testTwoCalibrationsPrior-v278 | 2/2 | 3788 | 1.652 | 0.002 | 0 | matched |
| testYuleCalibrated | 2/2 | 566 | 1.317 | 0.006 | 0 | matched |
| testYuleOneSite | 2/2 | 2955 | 1.114 | – | 0 | matched |
| testYuleUncalibrated | 4/4 | 590 | 2.103 | 0.002 | 0 | matched |

Only in one version (not compared): C01-fine, C01-fine-scale, C01-fine-slide, C01-g06, C01-scale, C01-slide, C01-tall4, C01-tall4-g06, C01-tall4-scale, C01-tall4-slide, C01-tall4-slide-g06, C01-tall7, C01-tall7-g06, C01-tall7-scale, C01-tall7-slide, C01-tall7-slide-g06, C01-tall7-slide-sqrt, C01-tall7-sqrt, C06-g06, C06-scale, C06-slide, C10-g06, C10-scale, C10-slide, C13-g06, C13-scale, C13-slide, C18-fine, C18-fine-g06, C18-fine-scale, C18-fine-slide, C18-scale, C18-slide, C26-scale, C26-slide, C30_resume, bitflip-v278
