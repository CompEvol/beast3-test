# Batch comparison (beast2 vs beast3, burn-in 10%)

| Name | Reps (beast2/beast3) | Min ESS | Max z | Max clade Δp | Flagged | Verdict |
|---|---|---:|---:|---:|---:|---|
| testBSP | 2/2 | 3114 | 1.998 | 0.015 | 0 | matched |
| testCalYule_5t_2c | 2/2 | 355 | 2.098 | 0.005 | 0 | matched |
| testCalibration | 2/2 | 279 | 149.04 | 0.000 | 2 | not matched |
| testClassicRootCalibrationPrior | 2/2 | 6218 | 290.77 | 0.007 | 1 | not matched |
| testCoalescent | 2/2 | 1781 | 0.1302 | 0.002 | 0 | matched |
| testConditionalRootCalibrationPrior | 2/2 | 4 | 9.562 | 0.500 | 11 | not matched (ESS < 200) |
| testExponentialGrowth | 2/2 | 1540 | 0.8504 | 0.005 | 0 | matched |
| testTwoCalibrationsPrior | 2/2 | 6215 | 0.6876 | 0.003 | 0 | matched |
| testYuleCalibrated | 2/2 | 473 | 1.998 | 0.004 | 0 | matched |
| testYuleUncalibrated | 2/2 | 557 | 1.601 | 0.001 | 0 | matched |
