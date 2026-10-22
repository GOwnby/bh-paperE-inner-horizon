# Inner-Horizon Stability of the Hayward Metric: Closure Classes in the Ori Model, the Evaporation Clock and a Nonlinear Double-Null Test

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23455587.svg)](https://doi.org/10.5281/zenodo.23455587)

**Author:** Gracen Ownby  |  **Archive:** <https://doi.org/10.5281/zenodo.23455587>  |  **Licence:** code MIT, text and data CC-BY-4.0 (see `LICENSE.md`)  |  **Paper E** of a seven-paper series on regular (Hayward-type) black holes.

## Abstract

Does the inner (Cauchy) horizon of a regular Hayward black hole survive perturbation, or does mass inflation destroy it? In the Ori thin-null-shell model, reconstructed for an arbitrary closure M(m,r) and checked against Reissner-Nordstrom, the family a(m) ~ m^(1+s) has three regimes: exponential growth for -1 <= s < 0; for the fixed-length closure s = 0 exponential growth followed by M_+ ~ v^(p+1), but only because the Moebius map is continued through m = infinity; and for s > 0 a fold that ends the model at finite advanced time. With the evaporation law of Paper A the integrated inner-horizon exponent of a 10 solar-mass hole is about 10^121 e-folds and diverges near the critical mass. In a nonlinear double-null evolution of the Einstein-NED-massless-scalar system with the additive closure M = mu + M_N(r), the Cauchy-horizon radius stays finite below a critical amplitude while the Misner-Sharp mass inflates; at the threshold the radius vanishes as (A_* - A)^gamma with gamma = 0.4997 +- 0.002. The sign of the inflating mass is that of -r_u. The conformal-anomaly term of the Hawking flux, added along a ray, reverses that sign and makes the area radius increase at an advanced time v_flip. The Kretschmann scalar obeys K >= 16 M^2/r^6, which diverges along the rays computed to v = 280. The closure of the nonlinear test is not the mass-tracking closure of the series, the Ori model is a spherical thin-shell idealisation and extendibility is addressed by indicators only.

## Directory map

| path | content |
|---|---|
| `main.tex`, `references.bib`, `main.bbl` | manuscript source, bibliography, bibliography as built |
| `paperE_inner_horizon.pdf` | the compiled manuscript (26 pages) |
| `fig_ori_classes.png`, `fig_nonlinear.png` | the two figures of the paper (written by `code/make_results.py` and `code/nonlinear/make_fig_nonlinear.py`) |
| `code/ori_model.py`, `make_results.py`, `extra_runs.py` | Ori thin-shell model for a general closure; validation, closure classes, fold table, figure; the passage through m = infinity and the small-s fold runs |
| `code/evap_coupling.py`, `evap_table.py`, `evap_alpha.py` | evaporation law and the integrated inner-horizon exponent (Sec. 5) |
| `code/nonlinear/` | double-null Einstein-NED-scalar evolution (`double_null.c`, `dn2lib.py`) and one script per result of Sec. 6; own `README.md` |
| `code/eh_init/` | event-horizon-regular data, kernel and ray integration (the method of Paper G) of which this paper uses a few scripts; `gen3_*.json` are the stored five-grid inputs; own `README.md` |
| `verify.sh`, `verify.py`, `verification/` | one-command check of the repository: runs the generators, compares ~480 numbers with `main.tex`, writes `verification/REPORT.md` and `verification/logs/` (see "Verify") |
| `code/symbolic_checks.py`, `text_numbers.py`, `fold_integrator_scan.py`, `nonlinear/analyze_stored.py`, `nonlinear/check_saturation.py` | checks added for `verify.sh`: exact (sympy) identities, numbers quoted in the text, integrator dependence of the fold table, numbers re-derived from the stored long runs |
| `code/Makefile` | builds the four C libraries |
| `PROVENANCE.md` | which files differ from the author's original archive (Zenodo v1.0.1), which have no original, which results changed and why, what was reproduced from the original code, and the known limits |
| `requirements.txt`, `LICENSE.md`, `CITATION.cff` | Python requirements, licence, citation metadata |

## Verify

```
bash verify.sh            # quick (default): builds the C kernels, runs every cheap generator, checks ~480 numbers against main.tex
bash verify.sh --full     # quick + the hours-long production runs, regenerated in a scratch copy (verification/regen/); the quick run uses verification/regen_quick/
```

Output: `verification/REPORT.md` (environment, job times, one row per checked number: quantity, place in the paper, paper value, tolerance and its reason, computed value, PASS/FAIL), `verification/logs/<job>.log`, and as last line `RESULT bh-paperE-inner-horizon: PASSED n/n checks (quick)`; exit status 1 on any failure. The quick run executes the generators in a scratch copy of `code/` (`verification/regen_quick/`, not tracked) and never overwrites the shipped result files, which are the author's original outputs; the report lists the difference between each regenerated file and the shipped one and needs no network. Jobs whose Python modules are missing are reported as SKIPPED and the checks that depend on them read the shipped outputs instead (e.g. without sympy the exact checks of `code/symbolic_checks.py` are not re-run and `code/symbolic_checks.log`, made with sympy 1.14.0, is used). Measured: quick = 17.4 CPU-minutes in 30 jobs (about 10 min wall on an idle 2-core machine, 70 min on a machine with load 13; two jobs run in parallel). `--full` adds the production runs (list and expected durations: `python3 verify.py --list`; roughly 12 CPU-hours in all, dominated by the eight five-grid v = 300 runs). Timed so far: `full_gen3_B0.003_k1.5_v300` 53 CPU-min (output bit-identical to the shipped file), `full_gen3_B0.03_k1.5_v110` 1.7 CPU-min (bit-identical), `full_threshold_h0.04` 2.0 CPU-min (relative difference 5e-12); the other full jobs were not run to completion in this check, their durations are those of the original runs.

## Requirements and build

* Python >= 3.10 with `pip install -r requirements.txt`: numpy >= 2.0, scipy >= 1.11, sympy, mpmath, matplotlib. A C compiler (gcc) and make; `verify.sh` runs `make -C code` itself (about 1 s; builds `nonlinear/libdouble_null.so`, `eh_init/libdouble_null.so`, `libstream.so`, `libstream2.so`).
* Every script is run **from its own directory** (they read and write files relative to it); `verify.sh` does that.
* Platform: verified on Linux (gcc 13.3, Python 3.13, numpy 2.5, scipy 1.18, matplotlib 3.11) and earlier with Python 3.10 / numpy 2.2 / gcc 11.4. Windows: use WSL (the `.so` libraries are Linux binaries loaded with `ctypes`). macOS was not tested (it needs `.dylib` names in `dn2lib.py` and `gen*.py`).

## Build the PDF

```
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

(`natbib`, `hyperref`, `booktabs`, `amsmath`: any full TeX Live; if LaTeX still reports "Label(s) may have changed", run `pdflatex main` once more. The result is `main.pdf`, which is the shipped `paperE_inner_horizon.pdf`; 26 pages, 0 undefined references, no BibTeX warnings.)

## Result in paper -> script -> output file

`verify.sh` runs all rows marked **Q** (CPU seconds measured in the quick run on one core of a 2-core Linux machine) and compares the output with the numbers of the paper (ids `S3.*`, `S4.*`, `S5.*`, `S6.*`, `SYM.*` in `verification/REPORT.md`); rows marked **F** are the production runs of `bash verify.sh --full` (duration: estimate from the original runs, to be read as order of magnitude), and `verify.sh` analyses their shipped output in the quick run (`code/nonlinear/analyze_stored.py`). All commands from the directory shown.

| result in the paper | directory | command | mode, time | output |
|---|---|---|---|---|
| exact identities: closure derivatives, Moebius inverse, field equations Eqs. dn1-dn3 (all Einstein components), conservation law, ray equations, Kretschmann decomposition, kappa_- of Sec. 6.5 | `code` | `python3 symbolic_checks.py` (sympy) | Q, 4 s | `symbolic_checks.log` |
| numbers of the text: regime I deviation 3.2e-14 and m_+ ~ 10^601, fold at m_* (588, 58, 5.8), s_min, 10 M_sun values (Lambda = 1.2e121, t = 2 ln r_g ...), transfer-function gain | `code` | `python3 text_numbers.py` | Q, 1 s | `text_numbers.json/.log` |
| validation table (RN growth rate 3.74996, saturation amplitude), closure-class numbers of Sec. 4, fold table, Fig. 1 | `code` | `python3 make_results.py` | Q, 13 s | `results.json`, `../fig_ori_classes.png` |
| integrator dependence of the `D_0 = 1e-12` rows of the fold table | `code` | `python3 fold_integrator_scan.py all` | Q, 145 s | `fold_integrator_scan.log` |
| passage through m = infinity (v = 36.6), s = 1e-3, 1e-2, 1e-1 fold runs | `code` | `python3 extra_runs.py` | Q, 3 s | `results_extra_runs.txt` |
| evaporation table (integrated exponent; Lambda sqrt(eps_f) for M_i = 2 l) | `code` | `python3 evap_table.py` | Q, 14 s | `evap_table.json` and stdout |
| alpha = 1.513e-4 and 6233 (Sec. 5) | `code` | `python3 evap_alpha.py` | Q, 3 s | `evap_alpha.log` |
| field equations (Eqs. dn1-dn3, Kretschmann decomposition), numerically | `code/eh_init` | `python3 check_field_equations.py` | Q, 1 s | `results_check_field_equations.txt` |
| closure uniqueness, divergence formula | `code/eh_init` | `python3 conserv_num.py` | Q, 1 s | stdout (log) |
| static validation, order of convergence | `code/nonlinear` | `python3 run_validation.py` | Q, 9 s | `validation_nonlinear.json` |
| growth-rate table (rate of M vs the Ori ODE) | `code/nonlinear` | `python3 run_rates.py` | Q, 14 s | `rates_nonlinear.json`, `rates.log` |
| A_*, r_inf(A_* - A) at h = 0.08 | `code/nonlinear` | `python3 run_threshold.py 0.08` | Q, 97 s | `threshold_h0.08.json`, `thr_0.08.log` |
| the same at h = 0.04, 0.02 | `code/nonlinear` | `python3 run_threshold.py 0.04` (and 0.02) | F, 2 and ~10 CPU-min | `threshold_h<h>.json`, `thr_<h>.log` |
| gamma = 0.4997 (windows 0.4997, 0.499, 0.498) and prefactors 40.8, 41.2, 41.3 | `code/nonlinear` | `python3 fit_gamma.py` | Q, <1 s | `fit_gamma.log` (reads `threshold_h*.json`) |
| saturation of r_CH(u), 4e-5 and 12% | `code/nonlinear` | `python3 check_saturation.py` | Q, 5 s | `check_saturation.log/.json` |
| A_* vs domain, r_CH(u) profiles | `code/nonlinear` | `python3 run_domain.py` | F, ~25 min | `domain_nonlinear.json`, `dom.log` |
| A_* independent of v_1, saturation, rates near threshold, Raychaudhuri residual | `code/nonlinear` | `python3 run_checks.py` | F, ~30 min | `checks_nonlinear.json`, `checks.log` |
| other data families, Ori exponent q = 2k+2 | `code/nonlinear` | `python3 run_universality.py` | F, ~40 min | `universality_nonlinear.json`, `univ.log` |
| supercritical locus | `code/nonlinear` | `python3 run_supercritical.py` | F, ~10 min | `supercritical_nonlinear.json` |
| every number of Secs. 6.1-6.5 that comes from the long runs, re-derived from their stored output | `code/nonlinear` | `python3 analyze_stored.py` | Q, <1 s | `analyze_stored.json/.log` |
| Fig. 2 | `code/nonlinear` | `python3 make_fig_nonlinear.py` (needs the JSON files above) | Q, 7 s | `../../fig_nonlinear.png` |
| sign mechanism: sign M = -sign r_u, u_*, separatrix | `code/nonlinear` | `python3 sign_mech.py`, `sign_ustar.py`, `sign_separatrix.py` | Q, 3 + 5 + 5 s | `sign_*.log` |
| the monotonicity of r_u/W (17 runs) | `code/nonlinear` | `python3 sign_scan.py` | F, ~60 min | `sign_scan.log` |
| Kretschmann scalar: K(u=2, v=20) = 25.7, static 12.3, K at v = 40-100, growth rate | `code/nonlinear` | `python3 run_curvature.py` | Q, 15 s | `curvature_nonlinear.json`, `curv.log` |
| kappa_- scan, m_N = 5, 3, 2, 1.6, 1.4 | `code/nonlinear` | `python3 run_kappa_scan.py <m_N>` | F, 10-40 min each | `kscan_mN<m_N>.json`, `kscan_<m_N>.log` |
| domain control for m_N = 1.4 (A_* = 0.0497017404, 0.0497017403) | `code/nonlinear` | `python3 domain_mN1.4.py` | Q, 247 s | `domain_mN1.4.log` |
| fixed-domain control of the kappa_- scan (u_1 = v_1 = 30) | `code/nonlinear` | `python3 run_kappa_fixedL.py 5` and `python3 run_kappa_fixedL.py 1.4` | Q, 104 s together | `results_kappa_fixedL.txt` |
| five-grid inputs `gen3_*.json` (eight v = 300 runs, v = 110 and v = 450) | `code/eh_init` | `python3 gen3.py B k A U0 w v1 h1 h2 ...` (parameters are stored in each file; `verify.py --list`) | F, 53 CPU-min (v = 300), ~20 (v = 450), 2 (v = 110) | `gen3_B<B>_k<k>_v<v1>.json` |
| extendibility indicators (table of Sec. 6.5) | `code/eh_init` | `python3 e15_extend.py gen3_<...>.json` for the eight runs | Q, 19 s together | `results_e15_extend.txt` |
| constraint-projected mass, ln K >= 337, 360, 323.5, 343, maximum deviation at v = 280 | `code/eh_init` | `python3 e13_all.py gen3_<...>.json 2` for the eight runs | Q, 49 s together | stdout (`verification/logs/eh_e13.log`) |
| exact ray integration of M against the extrapolated PDE mass (6e-5, 2e-6) | `code/eh_init` | `python3 ray_mass.py gen2_B<B>_k<k>_A0_U1_w0.3_v300.json` | Q, 18 s together | `results_ray_mass_B<B>_k<k>.txt` |
| kernel-driven extension to v = 3000, q_M(2500) = 5.02, 3.01 | `code/eh_init` | `python3 ray_extend.py gen3_B0.003_k<k>_v300.json` | Q, 138 s together | `results_ray_extend_ext_def_B0.003_k<k>.txt` |
| flux to v = 420, PDE/kernel ratio 1.0003 | `code/eh_init` | `python3 e12_ratio.py` (reads `gen3_B0.003_k1.5_v450.json`) | Q, 1 s | `results_e12_ratio.txt` |
| flux at B = 0.03: 3.5% above the static-hole response | `code/eh_init` | `python3 e11_ratio.py` | Q, 2 s | `results_e11_ratio.txt` |
| sensitivity of the kernel to its Gaussian smoothing (variance 0.5) | `code/eh_init` | `python3 kernel_smoothing_test.py` | Q, 4 s | `results_kernel_smoothing.txt` |
| Hawking-flux anomaly term, v_flip (table of Sec. 6.8) | `code/eh_init` | `python3 e8_semiclassical.py gen3_B0.003_k1.5_v300.json` | Q, 84 s | `results_e8_semiclassical.txt/.json` |
| phi_v^2/\|T^q\| at v_flip = 0.96, 0.91, 0.88, 0.44 | `code/eh_init` | `python3 e8_flip_ratio.py gen3_B0.003_k1.5_v300.json` | Q, 43 s | `results_e8_flip_ratio.txt` |

Sensitive item: the two `D_0 = 1e-12` rows of the fold table (`v*` = 49.8 for s = 1 and 50.0 for s = 2, quoted to 0.1) depend on the ODE integrator because the seed is of the order of its tolerance; the `D_0 = 1e-6` and `1e-9` rows do not. `fold_integrator_scan.py` lists the values for LSODA (rtol 1e-10 ... 3e-14; scipy refuses a tolerance below 2.2e-14), DOP853, Radau and RK45: 49.77-49.87 (s = 1) and 49.94-50.03 (s = 2) over all integrators and tolerances tried.

Numbers that Paper E quotes from Paper G (percentages of the metric exponent, the differential Ori relation, the 0.6-0.7%/1.9% above the final-hole kernel) are checked in the repository of Paper G (`bh-paperG-late-time-method`), not here.

## Citation

See `CITATION.cff`. Companion papers (Zenodo): A 10.5281/zenodo.23455575, B 23455580, C 23455582, D 23455586, F 23455596, G 23455606 (Paper G, the method for the late-time regime: repository `bh-paperG-late-time-method`).
