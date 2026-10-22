# Code for Paper E

Python >= 3.10 (numpy >= 2.0, scipy >= 1.11, sympy, mpmath, matplotlib; see `../requirements.txt`) and C. Run every script from its own directory, or let `../verify.sh` run them all and compare the output with the numbers of the paper. The full table "result in paper -> script -> output file" with run times is in `../README.md`.

Build the C libraries (once): `make` in this directory (needs gcc; see `Makefile`).

| file | content |
|---|---|
| `ori_model.py` | Ori thin-null-shell model for a general closure (eqs. 3-5 of the paper); also the closure `hn` (additive Hayward-NED, G = M_N'(r)) used for the comparison with the double-null evolution |
| `make_results.py` | validation tables, closure classes, fold table, figure (`../fig_ori_classes.png`) -> `results.json` |
| `extra_runs.py` | passage through m = infinity and the small-s fold runs -> `results_extra_runs.txt` |
| `evap_coupling.py`, `evap_table.py` | evaporation-integrated inner-horizon exponent (Sec. 5), table -> `evap_table.json` |
| `evap_alpha.py` | near-M* constants alpha = 1.513e-4 and 2 sqrt(2)/(3 alpha) = 6233 -> `evap_alpha.log` |
| `symbolic_checks.py` | sympy: closure identities, field equations (all Einstein components, exact), conservation law, ray equations, Kretschmann decomposition, constants (`CHECK <id>: OK` lines) -> `symbolic_checks.log` |
| `text_numbers.py` | the regime I/III numbers of Sec. 4, the 10 solar-mass numbers of Sec. 5 and the transfer-function gain -> `text_numbers.log/.json` |
| `fold_integrator_scan.py` | integrator dependence of the `D0 = 1e-12` rows of the fold table (LSODA rtol sweep, DOP853, Radau, RK45) -> `fold_integrator_scan.log` |
| `nonlinear/` | double-null Einstein-NED-scalar evolution used in Section 6 (own `README.md`: scripts, wall times) |
| `eh_init/` | event-horizon-regular data, kernel and ray integration (own `README.md`) |

Run:  `cd code && python3 make_results.py && python3 evap_table.py && python3 evap_alpha.py`  (about 3 min), or everything at once: `bash ../verify.sh` (README of the repository root, section "Verify").

Event-horizon-regular data, kernel and ray integration are the subject of Paper G (repository `bh-paperG-late-time-method`, doi:10.5281/zenodo.23455605); the code stays in `eh_init/`. Paper E uses from it: `check_field_equations.py`, `conserv_num.py`, `e15_extend.py`, `raylib_sc.py` with `e8_semiclassical.py` and `e8_flip_ratio.py` (Hawking-flux anomaly term, Section 6.8), `e12_ratio.py` (flux to v = 420) and `kernel_smoothing_test.py`.

Notes
* `evap_table.json`, `results.json`, `results_extra_runs.txt` are the stored outputs of the scripts of the same name.
* Provenance: files written after the original work, and the two modified files (`make_results.py`: figure path; `nonlinear/run_curvature.py`: additional output rows), are listed in `../PROVENANCE.md` and labelled in their docstrings. Shipped result files are the author's original outputs; `verify.sh` regenerates into `../verification/regen_quick/` and compares.
