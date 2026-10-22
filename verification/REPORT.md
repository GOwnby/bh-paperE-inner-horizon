# Verification report -- Paper E (bh-paperE-inner-horizon)

Mode: **quick**.  Result: **480 / 480 checks passed**.

## Environment

| item | value |
|---|---|
| date | 2026-10-22 03:01 |
| platform | Linux-6.8.0-138-generic-x86_64-with-glibc2.35 |
| python | 3.10.12 |
| numpy | 2.2.6 |
| scipy | not installed |
| sympy | 1.14.0 |
| mpmath | 1.3.0 |
| matplotlib | 3.10.9 |
| gcc | gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 |
| cpus | 2 |
| total wall time | 6044 s (100.7 min) |

## Jobs

| job | status | wall [s] | cpu [s] | what | log |
|---|---|---:|---:|---|---|
| `symbolic` | SKIPPED | 0.0 | 0.0 | sympy: closure identities, field equations dn1-dn3 (all Einstein components), conservation law, ray equations, Kretschmann decomposition, constants -- python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks | `verification/logs/symbolic.log` |
| `text_numbers` | OK | 7.1 | 1.0 | regime I/III numbers of Sec. 4, 10 M_sun numbers of Sec. 5, transfer-function gain | `verification/logs/text_numbers.log` |
| `fold_integrator_scan` | OK | 1121.7 | 149.4 | integrator dependence of the D0 = 1e-12 rows of Table fold (LSODA rtol sweep, DOP853, Radau, RK45) | `verification/logs/fold_integrator_scan.log` |
| `make_results` | OK | 86.8 | 13.4 | Tables validation and fold, Fig. classes (results.json) | `verification/logs/make_results.log` |
| `extra_runs` | OK | 16.8 | 2.6 | passage through m = infinity (v = 36.6) and the small-s fold runs | `verification/logs/extra_runs.log` |
| `evap_table` | OK | 98.1 | 14.8 | Table evap and the M_i = 2 l values of Sec. 5 | `verification/logs/evap_table.log` |
| `evap_alpha` | OK | 18.1 | 2.8 | alpha = 1.513e-4 and 2 sqrt2/(3 alpha) = 6233 | `verification/logs/evap_alpha.log` |
| `nl_validation` | OK | 59.2 | 9.1 | static error and Raychaudhuri residual vs h | `verification/logs/nl_validation.log` |
| `nl_rates` | OK | 92.0 | 14.2 | d ln|M|/dv: PDE against the Ori model (Table nlrate) | `verification/logs/nl_rates.log` |
| `nl_curvature` | OK | 105.0 | 15.5 | Kretschmann scalar on the Cauchy horizon (K = 25.7 at v = 20) | `verification/logs/nl_curvature.log` |
| `nl_sign_mech` | OK | 16.6 | 2.6 | sign of M and of r_u at v = 100 | `verification/logs/nl_sign_mech.log` |
| `nl_sign_ustar` | OK | 44.4 | 5.7 | u_*(v): the zero of r_u is fixed by v = 30 | `verification/logs/nl_sign_ustar.log` |
| `nl_sign_separatrix` | OK | 47.4 | 5.5 | separatrix of the linear ray equation | `verification/logs/nl_sign_separatrix.log` |
| `nl_threshold_h0.08` | OK | 956.1 | 94.6 | A_* by bisection and r_inf(A_*-A), h = 0.08 (h = 0.04, 0.02 are in --full; their stored files are analysed) | `verification/logs/nl_threshold_h0.08.log` |
| `nl_kappa_fixedL` | OK | 1276.7 | 101.2 | fixed-domain control of the kappa_- scan | `verification/logs/nl_kappa_fixedL.log` |
| `nl_domain_mN1.4` | OK | 3177.1 | 240.8 | A_* for m_N = 1.4, kappa_- u1 = 20 and 40 | `verification/logs/nl_domain_mN1.4.log` |
| `nl_saturation` | OK | 57.6 | 4.6 | r_CH(u) saturation at A_*-A = 1e-10 (r_CH(40) vs r_CH(50), r_CH(30) vs r_CH(40)) | `verification/logs/nl_saturation.log` |
| `nl_fit_gamma` | OK | 1.9 | 0.2 | threshold exponent and prefactors from threshold_h*.json | `verification/logs/nl_fit_gamma.log` |
| `nl_figure` | OK | 90.1 | 7.4 | Fig. nl | `verification/logs/nl_figure.log` |
| `nl_analyze_stored` | OK | 2.3 | 0.2 | re-derives the numbers of Sec. 6.1-6.5 from the stored outputs of all (also the long) nonlinear runs | `verification/logs/nl_analyze_stored.log` |
| `eh_field_equations` | OK | 3.6 | 0.3 | finite-difference Riemann tensor: G_ab - 8 pi T_ab = 0, Kretschmann decomposition | `verification/logs/eh_field_equations.log` |
| `eh_conserv` | OK | 2.2 | 0.2 | nabla_a T^a_b for the monopole stress tensor (Eq. consT) | `verification/logs/eh_conserv.log` |
| `eh_kernel_smoothing` | OK | 60.6 | 4.5 | sensitivity of the PDE/kernel flux ratio to the Gaussian window | `verification/logs/eh_kernel_smoothing.log` |
| `eh_e12` | OK | 15.0 | 1.1 | PDE/kernel flux ratio to v = 420 | `verification/logs/eh_e12.log` |
| `eh_e11_ratio` | OK | 27.8 | 2.0 | PDE/kernel flux ratio vs v (3.5% above the static-hole response at B = 0.03) | `verification/logs/eh_e11_ratio.log` |
| `eh_e15` | OK | 237.3 | 18.5 | Table ext: extendibility indicators from the eight five-grid runs | `verification/logs/eh_e15.log` |
| `eh_e13` | OK | 594.2 | 50.4 | constraint-projected mass, ln K >= ... (ray U = 0.9993) | `verification/logs/eh_e13.log` |
| `eh_ray_mass` | OK | 249.9 | 18.0 | exact ray integration of M against the extrapolated PDE mass (6e-5, 2e-6 to v = 108) | `verification/logs/eh_ray_mass.log` |
| `eh_ray_extend` | OK | 1878.2 | 133.5 | kernel-driven extension to v = 3000: q_M(2500) = 5.02 (k = 3/2) and 3.01 (k = 1/2) | `verification/logs/eh_ray_extend.log` |
| `eh_e8_semiclassical` | OK | 1039.4 | 79.9 | anomaly term along the ray: v_flip, r(3000)-r(250), ln|M|(3000) | `verification/logs/eh_e8_semiclassical.log` |
| `eh_e8_flip_ratio` | OK | 422.7 | 44.2 | phi_v^2/|T^q_vv| at v_flip | `verification/logs/eh_e8_flip_ratio.log` |

## Regenerated output (scratch copy) against the SHIPPED version (the author's original output, never overwritten)

Maximum relative difference of the numbers in the file (a number is ignored only if it is below 1e-9 of the largest number on its own line); `None` = layout changed (e.g. timing lines of the original log).  0 = bit-identical.  Informational; differences at the 1e-6 level in near-threshold scans are platform noise (see PROVENANCE.md).

| job | file | max rel. difference |
|---|---|---:|
| `text_numbers` | `text_numbers.json` | 0 |
| `text_numbers` | `text_numbers.log` | 0 |
| `make_results` | `results.json` | 0 |
| `extra_runs` | `results_extra_runs.txt` | 0 |
| `evap_table` | `evap_table.json` | 0 |
| `evap_alpha` | `evap_alpha.log` | 0 |
| `nl_validation` | `validation_nonlinear.json` | 1.4e-15 |
| `nl_rates` | `rates_nonlinear.json` | 0 |
| `nl_rates` | `rates.log` | 0 |
| `nl_curvature` | `curvature_nonlinear.json` | 0 |
| `nl_curvature` | `curv.log` | 3.7e-11 |
| `nl_sign_mech` | `sign_mech.log` | None |
| `nl_sign_ustar` | `sign_ustar.log` | 0 |
| `nl_sign_separatrix` | `sign_separatrix.log` | 0 |
| `nl_threshold_h0.08` | `threshold_h0.08.json` | 0 |
| `nl_threshold_h0.08` | `thr_0.08.log` | 0 |
| `nl_kappa_fixedL` | `results_kappa_fixedL.txt` | None |
| `nl_domain_mN1.4` | `domain_mN1.4.log` | 0 |
| `nl_fit_gamma` | `fit_gamma.log` | 0 |
| `nl_analyze_stored` | `analyze_stored.json` | 0 |
| `nl_analyze_stored` | `analyze_stored.log` | 0 |
| `eh_field_equations` | `results_check_field_equations.txt` | 0 |
| `eh_kernel_smoothing` | `results_kernel_smoothing.txt` | 0 |
| `eh_e12` | `results_e12_ratio.txt` | 0 |
| `eh_e11_ratio` | `results_e11_ratio.txt` | 0 |
| `eh_e15` | `results_e15_extend.txt` | 0 |
| `eh_ray_mass` | `results_ray_mass_B0.03_k0.5.txt` | 0 |
| `eh_ray_mass` | `results_ray_mass_B0.03_k1.5.txt` | 0 |
| `eh_ray_mass` | `results_ray_mass_B0.003_k0.5.txt` | 0 |
| `eh_ray_mass` | `results_ray_mass_B0.003_k1.5.txt` | 0 |
| `eh_ray_extend` | `results_ray_extend_ext_def_B0.003_k0.5.txt` | 0 |
| `eh_ray_extend` | `results_ray_extend_ext_def_B0.003_k1.5.txt` | 0 |
| `eh_e8_semiclassical` | `results_e8_semiclassical.txt` | 0 |
| `eh_e8_semiclassical` | `results_e8_semiclassical.json` | 0 |
| `eh_e8_flip_ratio` | `results_e8_flip_ratio.txt` | 0 |

## Checks (paper value against computed value)

`digits` tolerance = half a unit of the last digit quoted in the paper; other tolerances and their reasons are given in the table. `where` = section of `main.tex`.
A note `text now: ...` marks a number whose current wording in `main.tex` differs from the value tested here (proposed correction, see the final report).

| id | where | quantity | paper | computed | tolerance | status | note |
|---|---|---|---|---|---|---|---|
| SYM.A1 | Sec. 3 | sympy: (dM/dr)_m = 3Ma/[r(r^3+a)] | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A2 | Eq. Gfamily | sympy: G = 6 l0^2 M^2 (m/m0)^s / r^4 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A3 | Sec. 4 II | sympy: Moebius closure: dM/dm = r^6/(r^3+2l^2m)^2 > 0 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A4 | Sec. 4 II | sympy: inverse m = M r^3/(r^3 - 2 l^2 M) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A5 | Sec. 4 II | sympy: m -> infinity at M = r^3/2l^2, pole at m = -r^3/2l^2 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A6 | Sec. 4 II | sympy: G = 6 l^2 M^2/r^4 (n = 2) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A7 | Sec. 4 I | sympy: s = -1: G = (3M/r) a/(r^3+a) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A8 | Sec. 4 I | sympy: -1<s<0, large M: G -> 3M/r independent of s | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A9 | Sec. 4 III | sympy: dM/dm = r^3 (r^3 - s a)/(r^3+a)^2: fold at a = r^3/s | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A10 | Sec. 4 III | sympy: fold value for s = 1: M_max = sqrt(m0 R^3/8 l0^2) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A11 | Sec. 4 III | sympy: fold value for s = 2: (2/3)(m0^2 R^3/4 l0^2)^(1/3) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A12 | Sec. 3 Validation | sympy: linear drive M_m/(R|dr_-/dm|) = kappa_- for any closure | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A13 | Eq. dtr | sympy: DTR relation: dM_+/f_+ = dM_-/f_- | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A14 | Sec. 2 | sympy: M* = 3 sqrt3 l/4: double horizon at r = 4M*/3 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A15 | Sec. 2 | sympy: kappa_+- -> (sqrt2/3) sqrt(eps)/l near M* | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A16 | Sec. 2 | sympy: (sqrt2)/3 = 0.4714 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A17 | Sec. 2 | sympy: m = 10^3 l: kappa_- l = 0.9990, 4 m kappa_+ = 0.9999995 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.A18 | Sec. 4 (end) | sympy: q_a = 16M^3/27l^2: degenerate horizon r = 4M/3, kappa = 0 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.B1 | Sec. 5 | sympy: P = A kappa_+^4/960 pi^2 -> 1/(15360 pi M^2) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.B2 | Sec. 5 | sympy: Lambda = 5120 pi M^3/l for M >> l | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.B3 | Table evap | sympy: 5120 pi = 1.608e4 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.B4 | Sec. 5 | sympy: Lambda = (2 sqrt2/3 alpha) eps_f^(-1/2) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.B5 | Sec. 5 | sympy: 2 sqrt2/(3 alpha) = 6233 at alpha = 1.5126e-4 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C1 | Sec. 6.1 | sympy: G_ab = 8 pi T_ab (all four components) <=> Eqs. dn1, dn2 and the constraints [exact, symbolic] | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C2 | Sec. 6.1 | sympy: the check can fail: omitting dn1, dn2 or a constraint leaves a residual | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C3 | Sec. 6.1 | sympy: Box phi = 0 <=> Eq. dn3 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C4 | Sec. 6.1 | sympy: Misner-Sharp mass: 1-2M/r = g^ab r_a r_b | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C5 | Sec. 6.4 | sympy: Kretschmann = R2^2 + 8 H_AB H^AB/r^2 + 4(2M/r)^2/r^4 [exact, generic jets] | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C6 | Sec. 6.4 | sympy: H_AB H^AB = (8/W^2)(H_uu H_vv + H_uv^2) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C7 | Eq. consT | sympy: nabla_a T^a_u, nabla_a T^a_v [exact] | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C8 | Sec. 6.2 | sympy: conservation => d rho ^ d r = 0 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C9 | Sec. 6.2 | sympy: p_t = -rho - r rho'/2 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C10 | Eq. ray | sympy: (ln y)' = rho/r - sigma_v + S/y | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C11 | Eq. ray | sympy: rho' = sigma_v rho + 4 pi r phi_v^2 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C12 | Eq. muv | sympy: mu_v = -8 pi r^2 (r_u/W) phi_v^2 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C13 | Sec. 6.3 | sympy: d_u(r_u/W) = -4 pi r phi_u^2/W <= 0 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C14 | Eq. Kscalar | sympy: K -> 2048 pi^2 (phi_u phi_v/W)^2 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C15 | Eq. Kscalar | sympy: 2048 pi^2 Y^2 = 128 pi^2 [(grad phi)^2]^2 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C16 | Sec. 6.4 | sympy: Weyl invariant C^2 = K/6 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C17 | Sec. 6.4 | sympy: d ln K/dv = 2 kappa_- - (2k+2)/(v+1) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C18 | Sec. 6.4 | sympy: K >= 16 M^2/r^6 (mass term) | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C19 | Sec. 6.6 | sympy: W_sV = W e^{kappa v}/kappa | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C20 | Eq. Tq | sympy: T^q_vv = -hbar(sigma_v^2 - 2 sigma_vv)/192 pi^2 r^2 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C21 | Sec. 6.7 | sympy: v_flip criterion | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C22 | Sec. 6.1 | sympy: m_N=5, a_N=10: r_- = 1.057475, r_+ = 9.897927, kappa_- = 0.795649, kappa_+ = 0.048969 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C23_mN3 | Sec. 6.5 | sympy: kappa_-(m_N = 3) = 0.653 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C23_mN2 | Sec. 6.5 | sympy: kappa_-(m_N = 2) = 0.463 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C23_mN1.6 | Sec. 6.5 | sympy: kappa_-(m_N = 1.6) = 0.302 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| SYM.C23_mN1.4 | Sec. 6.5 | sympy: kappa_-(m_N = 1.4) = 0.164 | OK | OK | exact | **PASS** | exact symbolic identity (sympy), log: code/symbolic_checks.log; stored output used (job symbolic skipped: python module(s) not installed: sympy; the stored output (symbolic_checks.log) is used by the checks) |
| S4.I1 | Sec. 4 (regime I) | G/(3M/R) - 1 at M = 1e50, s = -1/2 (double-precision limit) | 1e-13 | 3.16414e-14 | <= 1e-13 | **PASS** | bound is the double-precision limit of the log-space inversion; text now: less than 10^{-14} |
| S4.I2 | Sec. 4 (regime I) | s = -1: G = (3M/R) a/(R^3+a) (relative difference) | 1e-12 | 0 | <= 1e-12 | **PASS** | agreement to rounding |
| S4.I3 | Sec. 4 (regime I) | m_+ needed for M = 6e5 at s = -0.01: log10(m_+) | 600 | 601.336 | abs 1.5 | **PASS** | order of magnitude of the exponent ("m_+ ~ 10^600"; computed m_+/m0 = 10^600.6, m_+ = 10^601.3) |
| S4.III1 | Sec. 4 (regime III) | threshold s > R^3/a(m_inf) | 0.12 | 0.118252 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III2_s0.001 | Sec. 4 (regime III) | fold position m_* (analytic, a(m_*) = R^3/s), s = 0.001 | 588 | 588.449 | 0.5 (half unit of the last quoted digit) | **PASS** | analytic fold; the integration stops earlier (event at 1e-4 of dM/dm) |
| S4.III2_s0.01 | Sec. 4 (regime III) | fold position m_* (analytic, a(m_*) = R^3/s), s = 0.01 | 58 | 57.6976 | 0.5 (half unit of the last quoted digit) | **PASS** | text now: m_* = 57 |
| S4.III2_s0.1 | Sec. 4 (regime III) | fold position m_* (analytic, a(m_*) = R^3/s), s = 0.1 | 5.8 | 5.82319 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S4.III3_s0.001 | Sec. 4 (regime III) | M_max/(R^3/2l^2), s = 0.001 | 0.994 | 0.994249 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III3_s0.01 | Sec. 4 (regime III) | M_max/(R^3/2l^2), s = 0.01 | 0.966 | 0.966177 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III3_s0.1 | Sec. 4 (regime III) | M_max/(R^3/2l^2), s = 0.1 | 0.895 | 0.895341 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III4 | Sec. 4 (regime III) | R^3/2l^2 | 0.591 | 0.591262 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III5 | Sec. 4 (regime III) | M_max for s = 1 (numerical max over m equals analytic sqrt(m0 R^3/8)) | 0.859696 | 0.859696 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.III6 | Sec. 4 (regime III) | M_max for s = 2 (numerical max over m) | 1.298590 | 1.29859 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.II1 | Sec. 4 (regime II) | advanced time at which M_+ = R^3/2l^2 (m passes through infinity), D0 = 1e-8 | 36.6 | 36.62 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S4.III7_s0.001 | Sec. 4 (regime III) | run stops at v* (s = 0.001) | 36.55 | 36.55 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III8_s0.001 | Sec. 4 (regime III) | M_+(v*) (s = 0.001) | 0.588 | 0.588 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III7_s0.01 | Sec. 4 (regime III) | run stops at v* (s = 0.01) | 36.17 | 36.17 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III8_s0.01 | Sec. 4 (regime III) | M_+(v*) (s = 0.01) | 0.571 | 0.571 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III7_s0.1 | Sec. 4 (regime III) | run stops at v* (s = 0.1) | 32.41 | 32.41 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III8_s0.1 | Sec. 4 (regime III) | M_+(v*) (s = 0.1) | 0.529 | 0.529 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S4.III9 | Sec. 4 (regime III) | R^3/2 l0^2 in the run output | 0.591 | 0.591 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S3.RN1 | Sec. 3 / Table validation / abstract | RN: kappa_- from the fit of the growth rate | 3.74996 | 3.74996 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S3.RN2 | Table validation | RN: exact kappa_- = (r_+ - r_-)/2 r_-^2 | 3.75 | 3.75 | abs 1e-09 | **PASS** | exact value |
| S3.RN3 | Sec. 3 | RN fit coefficient c1 | -4.995 | -4.99463 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S3.RN4_v20 | Sec. 3 / Table validation | RN: (kappa_- - dlnM/dv) v at v = 20 | 5.07 | 5.07389 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.RN4_v30 | Sec. 3 / Table validation | RN: (kappa_- - dlnM/dv) v at v = 30 | 5.05 | 5.04749 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.RN4_v40 | Sec. 3 / Table validation | RN: (kappa_- - dlnM/dv) v at v = 40 | 5.04 | 5.035 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.RN4_v50 | Sec. 3 / Table validation | RN: (kappa_- - dlnM/dv) v at v = 50 | 5.03 | 5.02772 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.RN4_v60 | Sec. 3 / Table validation | RN: (kappa_- - dlnM/dv) v at v = 60 | 5.02 | 5.02295 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H4_v100 | Sec. 3 | Hayward p=4: v dlnM/dv at v = 100 | 5.22 | 5.22255 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H4_v200 | Sec. 3 | Hayward p=4: v dlnM/dv at v = 200 | 5.10 | 5.10188 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H4_v400 | Sec. 3 | Hayward p=4: v dlnM/dv at v = 400 | 5.05 | 5.04894 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H4_v600 | Sec. 3 | Hayward p=4: v dlnM/dv at v = 600 | 5.03 | 5.03221 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H3_v100 | Sec. 3 / Table validation | Hayward p=3: v dlnM/dv at v = 100 | 4.17 | 4.17346 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H3_v600 | Sec. 3 / Table validation | Hayward p=3: v dlnM/dv at v = 600 | 4.03 | 4.02568 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H6_v200 | Sec. 3 / Table validation | Hayward p=6: v dlnM/dv at v = 200 | 7.15 | 7.14604 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H6_v400 | Sec. 3 / Table validation | Hayward p=6: v dlnM/dv at v = 400 | 7.07 | 7.06928 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.H6_v600 | Sec. 3 / Table validation | Hayward p=6: v dlnM/dv at v = 600 | 7.05 | 7.04543 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S3.Msat_v200 | Sec. 3 / Table validation | Hayward p=4: M_+/M_sat at v = 200 | 0.936 | 0.936311 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S3.Msat_v400 | Sec. 3 / Table validation | Hayward p=4: M_+/M_sat at v = 400 | 0.968 | 0.968375 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S3.Msat_v600 | Sec. 3 / Table validation | Hayward p=4: M_+/M_sat at v = 600 | 0.979 | 0.978963 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S3.Msat_def | Sec. 3 | deficit 1 - M_+/M_sat at v = 600, times v (= 2(p+1)/kappa_-) | 12.6 | 12.6222 | 0.075 (half unit of the last quoted digit x 1.5) | **PASS** | the text gives the leading term 2(p+1)/(kappa_- v) = 12.57/v; the measured deficit at v = 600 is 12.6/v |
| S3.Msat_2pc | Summary | saturation amplitude predicted to 2% at v = 600 | 0.02 | 0.021037 | abs 0.005 | **PASS** | quoted to one digit |
| S3.kappaH | Sec. 3 | Hayward kappa_- (l = 1, m_inf = 5) | 0.7956 | 0.795649 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S3.H1_400 | Table validation | Hayward s = -1, -1/2: late growth rate at v = 400 | 0.7831 | 0.783109 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S3.H1_def | Table validation | Hayward s = -1: deficit (kappa_- - rate) v at v = 400 | 5.0 | 5.01607 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S3.H1_coinc | Sec. 4 (regime I) / Fig. classes | s = -1 and s = -1/2 curves coincide: max |rate difference| | 1e-8 | 1.35003e-10 | <= 1e-08 | **PASS** | coincide to the plotted accuracy |
| S4.T_v_s=1_1e-06 | Table fold | v* for s=1, D0 = 1e-06 | 28.84 | 28.8434 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_M_s=1_1e-06 | Table fold | M_+(v*) for s=1, D0 = 1e-06 | 0.859696 | 0.859696 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_v_s=1_1e-09 | Table fold | v* for s=1, D0 = 1e-09 | 39.63 | 39.6285 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_M_s=1_1e-09 | Table fold | M_+(v*) for s=1, D0 = 1e-09 | 0.859696 | 0.859696 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_v_s=1_1e-12 | Table fold | v* for s=1, D0 = 1e-12 | 49.8 | 49.7958 | abs 0.1 | **PASS** | D0 = 1e-12 is of the order of the integrator tolerance (text: quoted to three digits, +-0.1) |
| S4.T_M_s=1_1e-12 | Table fold | M_+(v*) for s=1, D0 = 1e-12 | 0.859696 | 0.859696 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_v_s=2_1e-06 | Table fold | v* for s=2, D0 = 1e-06 | 29.04 | 29.0391 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_M_s=2_1e-06 | Table fold | M_+(v*) for s=2, D0 = 1e-06 | 1.298590 | 1.29859 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_v_s=2_1e-09 | Table fold | v* for s=2, D0 = 1e-09 | 39.81 | 39.8084 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_M_s=2_1e-09 | Table fold | M_+(v*) for s=2, D0 = 1e-09 | 1.298590 | 1.29859 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_v_s=2_1e-12 | Table fold | v* for s=2, D0 = 1e-12 | 50.0 | 49.9745 | abs 0.1 | **PASS** | D0 = 1e-12 is of the order of the integrator tolerance (text: +-0.1 for s = 2) |
| S4.T_M_s=2_1e-12 | Table fold | M_+(v*) for s=2, D0 = 1e-12 | 1.298590 | 1.29859 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_inc1 | Sec. 4 | v* increment between successive seeds (s = 1), first | 10.8 | 10.7851 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_inc2 | Sec. 4 | v* increment between successive seeds (s = 1), second | 10.2 | 10.1673 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_inc_pe | Sec. 4 | increase per e-fold of D0 (mean of the four increments / ln 10^3) | 1.5 | 1.51597 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S4.T_indep | Sec. 4 | fold value independent of the seed: max relative spread of M_+(v*) over D0 (s = 1, 2) | 1e-6 | 7.72095e-08 | <= 1e-06 | **PASS** |  |
| S4.T_Mmax | Table fold | M_max analytic (s = 1) at the last R | 0.859696 | 0.859696 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S4.INT2 | Reproducibility | LSODA rtol 1e-10 ... 3e-14, s = 1: v*(D0=1e-12) within 49.8 +- 0.1 | True | True | exact | **PASS** | text: "49.8"; computed 49.796-49.804; text now: at relative tolerance 2e-14 the same system gave 49.80 for s=1 [scipy refuses rtol < 2.2e-14] |
| S4.INT3 | Reproducibility | LSODA rtol 1e-10 ... 3e-14, s = 2: v*(D0=1e-12) within 50.0 +- 0.1 | True | True | exact | **PASS** | text: "50.0 (+-0.1 for s = 2)"; computed 49.94-49.98; text now: 49.89-49.96 for s=2 |
| S4.INT4 | Reproducibility | DOP853, Radau, RK45 at rtol 1e-12, 1e-13: all v* within 49.8 +- 0.1 (s = 1) and 50.0 +- 0.1 (s = 2) | True | True | exact | **PASS** | computed 49.77-49.87 (s = 1), 49.97-50.03 (s = 2); no integrator gives 48.5; text now: a different integrator at 1e-12 gave 48.5 |
| S5.u_20_0.1 | Table evap | u for M_i/l = 20, eps_f = 0.1 | 1.31e8 | 1.31240e+08 | 500000 (half unit of the last quoted digit) | **PASS** |  |
| S5.L_20_0.1 | Table evap | Lambda for M_i/l = 20, eps_f = 0.1 | 1.21e8 | 1.21015e+08 | 500000 (half unit of the last quoted digit) | **PASS** |  |
| S5.R_20_0.1 | Table evap | Lambda/(M_i^3/l) for M_i/l = 20, eps_f = 0.1 | 1.51e4 | 15126.8 | 50 (half unit of the last quoted digit) | **PASS** |  |
| S5.u_20_0.0001 | Table evap | u for M_i/l = 20, eps_f = 0.0001 | 2.01e8 | 2.01154e+08 | 500000 (half unit of the last quoted digit) | **PASS** |  |
| S5.L_20_0.0001 | Table evap | Lambda for M_i/l = 20, eps_f = 0.0001 | 1.22e8 | 1.21726e+08 | 500000 (half unit of the last quoted digit) | **PASS** |  |
| S5.R_20_0.0001 | Table evap | Lambda/(M_i^3/l) for M_i/l = 20, eps_f = 0.0001 | 1.52e4 | 15215.7 | 50 (half unit of the last quoted digit) | **PASS** |  |
| S5.u_20_1e-06 | Table evap | u for M_i/l = 20, eps_f = 1e-06 | 6.78e9 | 6.77894e+09 | 5e+06 (half unit of the last quoted digit) | **PASS** |  |
| S5.L_20_1e-06 | Table evap | Lambda for M_i/l = 20, eps_f = 1e-06 | 1.27e8 | 1.27391e+08 | 500000 (half unit of the last quoted digit) | **PASS** |  |
| S5.R_20_1e-06 | Table evap | Lambda/(M_i^3/l) for M_i/l = 20, eps_f = 1e-06 | 1.59e4 | 15923.9 | 50 (half unit of the last quoted digit) | **PASS** |  |
| S5.u_1000_0.1 | Table evap | u for M_i/l = 1000, eps_f = 0.1 | 1.61e13 | 1.60851e+13 | 5e+10 (half unit of the last quoted digit) | **PASS** |  |
| S5.L_1000_0.1 | Table evap | Lambda for M_i/l = 1000, eps_f = 0.1 | 1.61e13 | 1.60609e+13 | 5e+10 (half unit of the last quoted digit) | **PASS** |  |
| S5.R_1000_0.1 | Table evap | Lambda/(M_i^3/l) for M_i/l = 1000, eps_f = 0.1 | 1.606e4 | 16060.9 | 5 (half unit of the last quoted digit) | **PASS** |  |
| S5.R_inf | Table evap | 5120 pi | 1.608e4 | 16085 | 5 (half unit of the last quoted digit) | **PASS** | arithmetic |
| S5.Mi | Sec. 5 | M_i/l for 10 M_sun, l = l_P | 9.1e38 | 9.13609e+38 | 5e+36 (half unit of the last quoted digit) | **PASS** |  |
| S5.Lam | Sec. 5 / abstract | Lambda = 5120 pi M_i^3 for 10 M_sun | 1.2e121 | 1.22659e+121 | 5e+119 (half unit of the last quoted digit) | **PASS** |  |
| S5.alpha | Sec. 5 | alpha = c0/M* | 1.513e-4 | 1.51260e-04 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S5.6233 | Sec. 5 | 2 sqrt2/(3 alpha) | 6233 | 6233.2 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S5.6.23e3 | Sec. 5 | 2 sqrt2/(3 alpha) in units of 1e3 | 6.23 | 6.2332 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S5.Ls_0.0001 | Sec. 5 | Lambda sqrt(eps_f) for M_i = 2 l, eps_f = 0.0001 | 8289 | 8288.81 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S5.Ls_1e-06 | Sec. 5 | Lambda sqrt(eps_f) for M_i = 2 l, eps_f = 1e-06 | 6494 | 6493.98 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S5.Ls_1e-08 | Sec. 5 | Lambda sqrt(eps_f) for M_i = 2 l, eps_f = 1e-08 | 6265 | 6264.75 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S5.rem_0.0001 | Sec. 5 | remainder Lambda - 6233 eps_f^(-1/2) [1e5], eps_f = 0.0001 | 2.1 | 2.05581 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S5.rem_1e-06 | Sec. 5 | remainder Lambda - 6233 eps_f^(-1/2) [1e5], eps_f = 1e-06 | 2.6 | 2.60981 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S5.rem_1e-08 | Sec. 5 | remainder Lambda - 6233 eps_f^(-1/2) [1e5], eps_f = 1e-08 | 3.2 | 3.17451 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S5.div5pc | Sec. 5 | divergent term / Lambda for M_i = 20 l, eps_f = 1e-6 (below 5%) | 0.05 | 0.0489281 | <= 0.05 | **PASS** |  |
| S5.t180 | Sec. 5 | 2 ln(r_g/l)/kappa_- for a 10 M_sun hole | 180 | 180.807 | rel 0.01 | **PASS** | quoted "approximately 180 l" |
| S5.t270 | Sec. 5 | 3 ln(r_g/l)/kappa_- (separation r_g) | 270 | 271.211 | rel 0.01 | **PASS** | quoted "approximately 270 l" |
| S6.1.F1 | Sec. 6.1 | G_ab - 8 pi T_ab: largest component with dn1, dn2, constraints imposed (E_thth) | 3e-6 | 2.63000e-06 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.F2 | Sec. 6.1 | departure when dr_uu (smallest of the four perturbed components) | 0.07 | 0.0667 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.F3 | Sec. 6.1 | departure when ds_uv changes (E_thth) | 1.6 | 1.63 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.F4 | Sec. 6.1 | Box phi with phi_uv = dn3 | 1e-15 | 6.63000e-16 | <= 2e-15 | **PASS** | quoted as an order of magnitude (6.6e-16) |
| S6.4.F5 | Sec. 6.4 | Kretschmann decomposition vs finite-difference Riemann, set 1 | 6.5e-6 | 6.50000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.F6 | Sec. 6.4 | Kretschmann decomposition vs finite-difference Riemann, set 2 | 4.5e-6 | 4.50000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.C1 | Sec. 6.2 (Eq. consT) | brute-force covariant divergence vs formula, both components | 1e-11 | 1.97813e-12 | <= 1e-11 | **PASS** |  |
| S6.1.V1_0.08 | Sec. 6.1 Validation | static interior error, h = 0.08 | 1.1e-3 | 0.00110617 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V1_0.04 | Sec. 6.1 Validation | static interior error, h = 0.04 | 2.8e-4 | 2.77018e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V1_0.02 | Sec. 6.1 Validation | static interior error, h = 0.02 | 6.9e-5 | 6.92881e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V1_0.01 | Sec. 6.1 Validation | static interior error, h = 0.01 | 1.7e-5 | 1.73240e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V2a | Sec. 6.1 Validation | measured order (static), minimum | 1.998 | 1.99753 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V2b | Sec. 6.1 Validation | measured order (static), maximum | 2.000 | 1.99984 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayu_v0_20_0.08 | Sec. 6.1 Validation | Raychaudhuri residual (u, v<=20), h = 0.08 | 2.2e-3 | 0.00215911 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayu_v0_20_0.04 | Sec. 6.1 Validation | Raychaudhuri residual (u, v<=20), h = 0.04 | 5.4e-4 | 5.40600e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayu_v0_20_0.02 | Sec. 6.1 Validation | Raychaudhuri residual (u, v<=20), h = 0.02 | 1.4e-4 | 1.35105e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayu_v20_40_0.08 | Sec. 6.1 Validation | Raychaudhuri residual (u, 20<v<=60), h = 0.08 | 5.3e-3 | 0.00531545 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayu_v20_40_0.04 | Sec. 6.1 Validation | Raychaudhuri residual (u, 20<v<=60), h = 0.04 | 1.3e-3 | 0.00132948 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayu_v20_40_0.02 | Sec. 6.1 Validation | Raychaudhuri residual (u, 20<v<=60), h = 0.02 | 3.3e-4 | 3.32396e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayv_v0_20_0.08 | Sec. 6.1 Validation | Raychaudhuri residual (v, v<=20), h = 0.08 | 1.2e-3 | 0.00117817 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayv_v0_20_0.04 | Sec. 6.1 Validation | Raychaudhuri residual (v, v<=20), h = 0.04 | 2.9e-4 | 2.94188e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayv_v0_20_0.02 | Sec. 6.1 Validation | Raychaudhuri residual (v, v<=20), h = 0.02 | 7.3e-5 | 7.34676e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayv_v20_58_0.08 | Sec. 6.1 Validation | Raychaudhuri residual (v, 20<v<=58), h = 0.08 | 3.4e-4 | 3.37647e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayv_v20_58_0.04 | Sec. 6.1 Validation | Raychaudhuri residual (v, 20<v<=58), h = 0.04 | 8.4e-5 | 8.44190e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V3_rayv_v20_58_0.02 | Sec. 6.1 Validation | Raychaudhuri residual (v, 20<v<=58), h = 0.02 | 2.1e-5 | 2.11052e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V4 | Sec. 6.1 Validation | order of the Raychaudhuri residual (u direction, min) | 2.00 | 1.9978 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.V4b | Sec. 6.1 Validation | order of the Raychaudhuri residual (u direction, max) | 2.00 | 2.00048 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.P1 | Sec. 6.1 | r_- of the static interior (m_N=5, a_N=10) | 1.057475 | 1.05747 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.1.P2 | Sec. 6.1 / 6.2 | kappa_- of the static interior | 0.795649 | 0.795649 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R1 | Table nlrate | Ori model, v = 79, delta = 1e-3 and 1e-2 | 0.73204 | 0.732038 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R2 | Table nlrate | Ori model, v = 98 | 0.74444 | 0.744437 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R2b | Table nlrate | Ori model: delta = 1e-3 and 1e-2 differ by | 1e-6 | 2.87935e-10 | <= 1e-06 | **PASS** |  |
| S6.2.R3 | Table nlrate | PDE rates at v = 79: smallest | 0.73203 | 0.732032 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R4 | Table nlrate | PDE rates at v = 79: largest | 0.73212 | 0.732116 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R5 | Table nlrate | PDE rate at v = 98 | 0.74444 | 0.744437 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R6 | Table nlrate | leading order kappa_- - 5/(v+1), v = 79 | 0.73315 | 0.733149 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R7 | Table nlrate | leading order, v = 98 | 0.74514 | 0.745144 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R8 | Table nlrate | spread of PDE rates at v = 98 | 6e-7 | 5.55752e-07 | <= 6e-07 | **PASS** | bound ("<= 6e-7"); computed 5.6e-7 |
| S6.2.R9 | Table nlrate | smallest amplitude: deviation from 0.732038 at u = -3 | 8e-5 | 7.79708e-05 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R10 | Table nlrate | ... at u = 2 | 2e-5 | 2.01762e-05 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R11 | Table nlrate | ... at u = 0 (absolute value) | 6e-6 | 5.92055e-06 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R12 | Table nlrate | all other runs differ from 0.732038 by less than 1e-6 (v = 79) | 1e-6 | 9.97264e-07 | <= 1e-06 | **PASS** |  |
| S6.2.R13 | Table nlrate | next term at v = 79: coefficient of 1/(v+1)^2 | 7.1 | 7.11043 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R14 | Table nlrate | next term at v = 98: coefficient of 1/(v+1)^2 | 6.9 | 6.93136 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R15 | Table nlrate | PDE vs Ori, v = 79, all runs but the smallest amplitude | 7e-7 | 7.28374e-07 | 7.5e-08 (half unit of the last quoted digit x 1.5) | **PASS** | quoted to one digit (7.3e-7) |
| S6.2.R16 | Table nlrate | PDE vs Ori, v = 98, all runs | 4e-7 | 4.27571e-07 | 5e-08 (half unit of the last quoted digit) | **PASS** | quoted to one digit (4.3e-7) |
| S6.2.R17 | Table nlrate | rate at u = 30, A_*-A = 1e-10, v = 79 | 0.73198 | 0.731982 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R18 | Table nlrate | rate at u = 40 ... v = 98 | 0.74441 | 0.744405 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R19 | Sec. 6.2 | rate at v = 59 (u = 0, A = 0.02, h = 0.04) | 0.7102 | 0.710237 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R20 | Sec. 6.2 | rate at v = 59, u = -3, A = 0.005 | 1.92 | 1.92278 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R21 | Sec. 6.2 | rate at v = 59, u = -3, A = 0.02, B = 0.002, h = 0.04 | 0.7334 | 0.7334 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R22 | Sec. 6.2 | ... h = 0.02 | 0.7388 | 0.738757 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R23 | Sec. 6.2 | sigma_v on the horizon, all runs (absolute value) | 0.795649 | 0.795649 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.R24 | Sec. 6.2 | saturation |r(100)-r(50)|/r at u = 4, A = 0.02 | 2e-11 | 1.93637e-11 | <= 2e-11 | **PASS** | bound ("<= 2e-11"); computed 1.9e-11 |
| S6.2.R25 | Sec. 6.2 | saturation at A_*-A = 1e-10 (max over u) | 4e-5 | 3.72021e-05 | <= 4e-05 | **PASS** | bound ("<= 4e-5"); computed 3.7e-5 |
| S6.2.Q98_k1 | Sec. 6.2 | q = (kappa_- - rate)(v+1) at v = 98, k = 1 | 4.055 | 4.05523 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Q70_k1 | Sec. 6.2 | q at v = 70, k = 1 | 4.080 | 4.07985 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Q98_k1.5 | Sec. 6.2 | q = (kappa_- - rate)(v+1) at v = 98, k = 1.5 | 5.070 | 5.07002 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Q70_k1.5 | Sec. 6.2 | q at v = 70, k = 1.5 | 5.102 | 5.10191 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Q98_k2 | Sec. 6.2 | q = (kappa_- - rate)(v+1) at v = 98, k = 2 | 6.085 | 6.08524 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Q70_k2 | Sec. 6.2 | q at v = 70, k = 2 | 6.125 | 6.12496 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Q98_k2.5 | Sec. 6.2 | q = (kappa_- - rate)(v+1) at v = 98, k = 2.5 | 7.101 | 7.10092 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Q70_k2.5 | Sec. 6.2 | q at v = 70, k = 2.5 | 7.150 | 7.14981 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Mrange | Sec. 6.2 | |M(u=2, v=100)| over the amplitudes: smallest (negative at the smallest amplitude) | 1e11 | 1.17239e+11 | 5e+10 (half unit of the last quoted digit) | **PASS** | quoted "about 1e11" |
| S6.2.Mrange2 | Sec. 6.2 | ... largest | 5e18 | 4.67829e+18 | 5e+17 (half unit of the last quoted digit) | **PASS** | quoted "to 5e18" (4.7e18) |
| S6.2.S1 | Sec. 6.2 / summary | runs of sign_scan | 17 | 17 | exact | **PASS** |  |
| S6.2.S2 | Sec. 6.2 / summary | runs with exactly one sign change of r_u and M at the same u ("fifteen of seventeen") | 15 | 15 | exact | **PASS** |  |
| S6.2.S3 | Sec. 6.2 | fraction with sign M = -sign r_u at |M| > 10 r | 1.0000 | 1 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.S4 | Sec. 6.2 | max increase of r_u/W along u in the 15 monotone runs / its maximum modulus | 7e-5 | 6.80000e-05 | <= 7e-05 | **PASS** | bound ("<= 7e-5"); computed 6.8e-5 |
| S6.2.S5_h0.04 | Sec. 6.2 | violation of monotonicity at the smallest amplitude, h = 0.04 | 6e-2 | 0.063 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.S5_h0.02 | Sec. 6.2 | violation of monotonicity at the smallest amplitude, h = 0.02 | 3e-2 | 0.029 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.S5_h0.01 | Sec. 6.2 | violation of monotonicity at the smallest amplitude, h = 0.01 | 8e-3 | 0.0081 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.S6 | Sec. 6.2 | smallest amplitude, h = 0.01: single sign change at u | -1.24 | -1.24 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.S6b | Sec. 6.2 | smallest amplitude, h = 0.01: number of sign changes | 1 | 1 | exact | **PASS** |  |
| S6.2.U1_A0.005 | Sec. 6.2 | u_* for A = 0.005, B = 0.002, h = 0.04 | -1.44 | -1.44 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U1_A0.01 | Sec. 6.2 | u_* for A = 0.01, B = 0.002, h = 0.04 | -1.68 | -1.68 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U1_A0.02 | Sec. 6.2 | u_* for A = 0.02, B = 0.002, h = 0.04 | -1.88 | -1.88 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U1_A0.0204 | Sec. 6.2 | u_* for A = 0.0204, B = 0.002, h = 0.04 | -1.92 | -1.92 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U2_B0.0005 | Sec. 6.2 | u_* for B = 0.0005, A = 0.02 | -2.04 | -2.04 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U2_B0.002 | Sec. 6.2 | u_* for B = 0.002, A = 0.02 | -1.88 | -1.88 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U2_B0.01 | Sec. 6.2 | u_* for B = 0.01, A = 0.02 | -1.48 | -1.48 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U2_B0.02 | Sec. 6.2 | u_* for B = 0.02, A = 0.02 | -1.0 | -1 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U3_h0.08 | Sec. 6.2 | u_* for h = 0.08 | -1.84 | -1.84 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U3_h0.04 | Sec. 6.2 | u_* for h = 0.04 | -1.88 | -1.88 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U3_h0.02 | Sec. 6.2 | u_* for h = 0.02 | -1.94 | -1.94 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U3_h0.01 | Sec. 6.2 | u_* for h = 0.01 | -1.94 | -1.94 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U4a | Sec. 6.6 (vi) | smallest u_* over the monotone runs | -2.04 | -2.04 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U4b | Sec. 6.6 (vi) | largest u_* over the monotone runs | -1.0 | -1 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.M1 | Sec. 6.2 | sign change of M at v = 100 (A = 0.02, B = 0.002, h = 0.04) | -1.88 | -1.88 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.M2 | Sec. 6.2 | sign change of r_u at v = 100 | -1.88 | -1.88 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.M3 | Sec. 6.2 | maximum of r_CH(u) | -1.92 | -1.92 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.M4 | Sec. 6.2 | r_u(v=100) = r_u(v=50) at every listed u (max relative difference) | 1e-6 | 0 | <= 1e-06 | **PASS** | printed to the digits of the log |
| S6.2.U5_0.02 | Sec. 6.2 | u_* for v = 30 ... 100, A = 0.02 | -1.8790 | -1.879 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U6_0.02 | Sec. 6.2 | spread of u_* over v = 30 ... 100, A = 0.02 | 0 | 0 | abs 1e-09 | **PASS** | to the printed digits |
| S6.2.U5_0.01 | Sec. 6.2 | u_* for v = 30 ... 100, A = 0.01 | -1.1565 | -1.1565 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U6_0.01 | Sec. 6.2 | spread of u_* over v = 30 ... 100, A = 0.01 | 0 | 0 | abs 1e-09 | **PASS** | to the printed digits |
| S6.2.U5_0.005 | Sec. 6.2 | u_* for v = 30 ... 100, A = 0.005 | -1.5430 | -1.543 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.U6_0.005 | Sec. 6.2 | spread of u_* over v = 30 ... 100, A = 0.005 | 0 | 0 | abs 1e-09 | **PASS** | to the printed digits |
| S6.2.Y_0.02 | Sec. 6.2 | y_sep, A = 0.02 | 0.4990 | 0.499 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Y_0.01 | Sec. 6.2 | y_sep, A = 0.01 | 0.4715 | 0.4715 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Y_0.005 | Sec. 6.2 | y_sep, A = 0.005 | 0.4998 | 0.4998 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.2.Y2 | Sec. 6.2 | zero of y - y_sep lies at u_* (largest offset in u) | 1e-5 | 0 | <= 1e-05 | **PASS** |  |
| S6.2.Y3 | Sec. 6.2 | steepness |d y/d u| at the zero (smallest slope) | 1e4 | 25100 | >= 10000 | **PASS** |  |
| S6.3.A_0.08 | Sec. 6.3 | A_* (h = 0.08) | 0.0204360 | 0.020436 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.A_0.04 | Sec. 6.3 | A_* (h = 0.04) | 0.0204280 | 0.020428 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.A_0.02 | Sec. 6.3 | A_* (h = 0.02) | 0.0204260 | 0.020426 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Ar | Sec. 6.3 | Richardson limit of A_* | 0.0204253 | 0.0204253 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Ao | Sec. 6.3 | convergence order of A_* in h | 2 | 1.9961 | abs 0.05 | **PASS** | second order claimed |
| S6.3.D_u6 | Sec. 6.3 | A_* for u1 = 6 (h = 0.04) | 0.022204 | 0.022204 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.D_u8 | Sec. 6.3 | A_* for u1 = 8 (h = 0.04) | 0.021146 | 0.0211459 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.D_u12 | Sec. 6.3 | A_* for u1 = 12 (h = 0.04) | 0.020468 | 0.0204684 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.D_u16 | Sec. 6.3 | A_* for u1 = 16 (h = 0.04) | 0.0204297 | 0.0204297 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.D_u24 | Sec. 6.3 | A_* for u1 = 24 (h = 0.04) | 0.02042799 | 0.020428 | 5e-09 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.D_u32 | Sec. 6.3 | A_* for u1 = 32 (h = 0.04) | 0.02042799 | 0.020428 | 5e-09 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.D2 | Sec. 6.3 | A_*(v1) independent of v1: spread over v1 = 40..100 ("eleven digits") | 1e-11 | 6.22419e-14 | <= 1e-11 | **PASS** |  |
| S6.3.F1 | Sec. 6.3 | flag offset (r_flag/41)^2 for 1e-5 | 6e-14 | 5.94884e-14 | 5e-15 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.F2 | Sec. 6.3 | flag offset for 1e-3 | 6e-10 | 5.94884e-10 | 5e-11 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.G1 | Eq. gamma / abstract | gamma: fit over [1e-10, 1e-9] (h = 0.04) | 0.4997 | 0.49969 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.G2 | Sec. 6.3 | fit over [1e-10, 1e-7] | 0.499 | 0.499031 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.G3 | Sec. 6.3 | fit over [1e-10, 1e-6] | 0.498 | 0.497839 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.G4_0.08 | Eq. gamma | gamma fit over [1e-10, 1e-9] within 0.4997 +- 0.002 (h = 0.08) | [0.4977, 0.5017] | 0.499735 | [0.4977, 0.5017] +- 0 | **PASS** | uncertainty quoted in the text (spread over fit windows) |
| S6.3.G4_0.04 | Eq. gamma | gamma fit over [1e-10, 1e-9] within 0.4997 +- 0.002 (h = 0.04) | [0.4977, 0.5017] | 0.49969 | [0.4977, 0.5017] +- 0 | **PASS** | uncertainty quoted in the text (spread over fit windows) |
| S6.3.G4_0.02 | Eq. gamma | gamma fit over [1e-10, 1e-9] within 0.4997 +- 0.002 (h = 0.02) | [0.4977, 0.5017] | 0.499652 | [0.4977, 0.5017] +- 0 | **PASS** | uncertainty quoted in the text (spread over fit windows) |
| S6.3.P_0.08 | Sec. 6.3 | prefactor r_inf/sqrt(d) at d = 1e-10, h = 0.08 | 40.8 | 40.7715 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.P_0.04 | Sec. 6.3 | prefactor r_inf/sqrt(d) at d = 1e-10, h = 0.04 | 41.2 | 41.2094 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.P_0.02 | Sec. 6.3 | prefactor r_inf/sqrt(d) at d = 1e-10, h = 0.02 | 41.3 | 41.3236 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.L12_lo | Sec. 6.3 | local exponent d ln r/d ln(A_*-A) for A_*-A <= 1.6e-9: minimum over h = 0.08, 0.04, 0.02 | 0.4995 | 0.499491 | 5e-05 (half unit of the last quoted digit) | **PASS** | end of the quoted range 0.4995-0.4999 |
| S6.3.L12_hi | Sec. 6.3 | local exponent d ln r/d ln(A_*-A) for A_*-A <= 1.6e-9: maximum over h = 0.08, 0.04, 0.02 | 0.4998 | 0.499753 | 5e-05 (half unit of the last quoted digit) | **PASS** | end of the quoted range 0.4995-0.4999; text now: 0.4995--0.4999 |
| S6.3.L3_0.08 | Sec. 6.3 | local exponent at 1e-7 (h = 0.08) | 0.496 | 0.496136 | 0.0005 (half unit of the last quoted digit) | **PASS** | central difference (as plotted in Fig. nl(c)); the forward difference between the two points is 0.4955; text now: 0.4955 at 10^-7 |
| S6.3.L4_0.08 | Sec. 6.3 | local exponent at 2.5e-5 (h = 0.08) | 0.43 | 0.430864 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.L5_0.08 | Sec. 6.3 | local exponent at 1e-3 (h = 0.08) | 0.24 | 0.240247 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.L3_0.04 | Sec. 6.3 | local exponent at 1e-7 (h = 0.04) | 0.496 | 0.495997 | 0.0005 (half unit of the last quoted digit) | **PASS** | central difference (as plotted in Fig. nl(c)); the forward difference between the two points is 0.4955; text now: 0.4955 at 10^-7 |
| S6.3.L4_0.04 | Sec. 6.3 | local exponent at 2.5e-5 (h = 0.04) | 0.43 | 0.429671 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.L5_0.04 | Sec. 6.3 | local exponent at 1e-3 (h = 0.04) | 0.24 | 0.239061 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.L3_0.02 | Sec. 6.3 | local exponent at 1e-7 (h = 0.02) | 0.496 | 0.495963 | 0.0005 (half unit of the last quoted digit) | **PASS** | central difference (as plotted in Fig. nl(c)); the forward difference between the two points is 0.4955; text now: 0.4955 at 10^-7 |
| S6.3.L4_0.02 | Sec. 6.3 | local exponent at 2.5e-5 (h = 0.02) | 0.43 | 0.42937 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.L5_0.02 | Sec. 6.3 | local exponent at 1e-3 (h = 0.02) | 0.24 | 0.238758 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.L6 | Sec. 6.3 | local exponent at 1e-10 after the flag-offset correction (h = 0.04) | 0.4999 | 0.499931 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_A_w2_b0.1_k1.5 | Sec. 6.3 | A_* for the family: pulse of width 2 | 0.026673 | 0.0266731 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_A_w1_b0.5_k1.5 | Sec. 6.3 | A_* for the family: B = A/2 | 0.018039 | 0.018039 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_A_w1_b0.1_k2 | Sec. 6.3 | A_* for the family: k = 2 | 0.020385 | 0.0203851 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_lo_w2_b0.1_k1.5 | Sec. 6.3 | local exponent, minimum, family w2_b0.1_k1.5 | 0.499 | 0.499128 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_hi_w2_b0.1_k1.5 | Sec. 6.3 | local exponent, maximum, family w2_b0.1_k1.5 | 0.5 | 0.499862 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_lo_w1_b0.5_k1.5 | Sec. 6.3 | local exponent, minimum, family w1_b0.5_k1.5 | 0.499 | 0.499247 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_hi_w1_b0.5_k1.5 | Sec. 6.3 | local exponent, maximum, family w1_b0.5_k1.5 | 0.5 | 0.499938 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_lo_w1_b0.1_k2 | Sec. 6.3 | local exponent, minimum, family w1_b0.1_k2 | 0.497 | 0.497034 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Fam_hi_w1_b0.1_k2 | Sec. 6.3 | local exponent, maximum, family w1_b0.1_k2 | 0.5 | 0.499672 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.3.Sup_1.0005 | Sec. 6.3 | locus r = 0.05 decreasing with u for A/A_* = 1.0005 | True | 1 | exact | **PASS** |  |
| S6.3.Sup2_1.0005 | Sec. 6.3 | locus tends to a constant v (spread of the last six points) for A/A_* = 1.0005 | 0 | 0 | abs 1e-06 | **PASS** | null ray: constant to the grid |
| S6.3.Sup_1.01 | Sec. 6.3 | locus r = 0.05 decreasing with u for A/A_* = 1.01 | True | 1 | exact | **PASS** |  |
| S6.3.Sup2_1.01 | Sec. 6.3 | locus tends to a constant v (spread of the last six points) for A/A_* = 1.01 | 0 | 0 | abs 1e-06 | **PASS** | null ray: constant to the grid |
| S6.3.Sup_1.05 | Sec. 6.3 | locus r = 0.05 decreasing with u for A/A_* = 1.05 | True | 1 | exact | **PASS** |  |
| S6.3.Sup2_1.05 | Sec. 6.3 | locus tends to a constant v (spread of the last six points) for A/A_* = 1.05 | 0 | 0 | abs 1e-06 | **PASS** | null ray: constant to the grid |
| S6.3.Sup_1.3 | Sec. 6.3 | locus r = 0.05 decreasing with u for A/A_* = 1.3 | True | 1 | exact | **PASS** |  |
| S6.3.Sup2_1.3 | Sec. 6.3 | locus tends to a constant v (spread of the last six points) for A/A_* = 1.3 | 0 | 0 | abs 1e-06 | **PASS** | null ray: constant to the grid |
| S6.3.Sat1 | Sec. 6.3 | r_CH(40) vs r_CH(50) at A_*-A = 1e-10 | 4e-5 | 4.36720e-05 | 5e-06 (half unit of the last quoted digit) | **PASS** | quoted "4e-5": relative difference /r40 - r50//r40 = 4.4e-5; to one digit |
| S6.3.Sat2 | Sec. 6.3 | r_CH(30)/r_CH(40) - 1 at A_*-A = 1e-10 | 0.12 | 0.117706 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K1 | Sec. 6.4 | K(u=2, v=20), h = 0.04 | 25.67 | 25.6652 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K1b | Sec. 6.4 | K(u=2, v=20) (quoted 25.7) | 25.7 | 25.6652 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K2 | Sec. 6.4 | static value of K at (u=2, v=20) | 12.3 | 12.328 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K3 | Sec. 6.4 | K(u=2, v=100), h = 0.04 | 2.5e50 | 2.53138e+50 | 5e+48 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K4 | Sec. 6.4 | change of K(v=100) between h = 0.04 and 0.02 [%] | 0.5 | 0.546652 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K5 | Sec. 6.4 | static K reproduced, relative error at h = 0.04 | 2.0e-4 | 2.02167e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K6 | Sec. 6.4 | first two terms equal to four digits from v = 40: |1 - T1/T2| | 1e-4 | 4.16688e-05 | <= 0.0001 | **PASS** | equal to four digits |
| S6.4.K7 | Sec. 6.4 | K / [2048 pi^2 (phi_u phi_v/W)^2] at v = 98 for all u, A, k: max |ratio - 1| | 1.5e-5 | 4.02259e-06 | <= 1.5e-05 | **PASS** | bound ("1 to 1.5e-5"); computed 4e-6 |
| S6.4.K8 | Sec. 6.4 | phi_u at the horizon (u = 2) | -7.4e-3 | -0.00740758 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K9 | Sec. 6.4 | d ln K/dv at v = 98, k = 3/2 (measured) | 1.54079 | 1.54079 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K9b | Sec. 6.4 | 2 kappa_- - (2k+2)/(v+1) at v = 98, k = 3/2 | 1.54079 | 1.54079 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K10 | Sec. 6.4 | d ln K/dv at v = 98, k = 1 (prediction) | 1.55089 | 1.55089 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K10b | Sec. 6.4 | ... measured | 1.55089 | 1.5509 | abs 2e-05 | **PASS** | the log prints five significant digits (1.5509) |
| S6.4.K11 | Sec. 6.4 | d ln K/dv at v = 98, k = 2 (measured) | 1.53069 | 1.53069 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K12 | Sec. 6.4 | W e^{kappa v} for v = 40 ... 100 | 91.04 | 91.0393 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K12b | Sec. 6.4 | W e^{kappa v} (largest) | 91.04 | 91.0403 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K13 | Sec. 6.4 | sigma_v on the ray (absolute value) | 0.795649 | 0.795649 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K14 | Sec. 6.4 | affine length up to v = 100 (u = 2) | 7.33 | 7.33379 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K15 | Sec. 6.4 | affine length beyond v = 100, W(100)/kappa_- | 3e-33 | 3.19083e-33 | 5e-34 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K16 | Sec. 6.4 | area radius at (u=2, v=100) | 0.80 | 0.801723 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.K17 | Sec. 6.4 | mass-function term / K at v = 100 ("thirteen orders of magnitude") | 1e-12 | 1.64768e-13 | <= 1e-12 | **PASS** | bound; computed 1.6e-13 (12.8 orders) |
| S6.4.K17b | Sec. 6.4 | ... not smaller than 1e-14 | 1e-14 | 1.64768e-13 | >= 1e-14 | **PASS** |  |
| S6.4.LK_B0.03_k1.5 | Sec. 6.4 (lower bound) | ln K >= ln(16 M^2/r^6) at v = 280, ray U = 0.9993, B0.03_k1.5 | 337 | 337 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.LK_B0.03_k0.5 | Sec. 6.4 (lower bound) | ln K >= ln(16 M^2/r^6) at v = 280, ray U = 0.9993, B0.03_k0.5 | 360 | 360.3 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.LK_B0.003_k1.5 | Sec. 6.4 (lower bound) | ln K >= ln(16 M^2/r^6) at v = 280, ray U = 0.9993, B0.003_k1.5 | 323 | 323.5 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.4.LK_B0.003_k0.5 | Sec. 6.4 (lower bound) | ln K >= ln(16 M^2/r^6) at v = 280, ray U = 0.9993, B0.003_k0.5 | 343 | 342.7 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.PD_0.03 | Sec. 6.6 (Mass) | ln M_cc - ln M_ODE at v = 280 (largest over k = 1/2, 3/2, 2, 3), B = 0.03 | 1.4e-6 | 1.39000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** | quoted to two digits (1.39e-6, 2.34e-6) |
| S6.6.PD_0.003 | Sec. 6.6 (Mass) | ln M_cc - ln M_ODE at v = 280 (largest over k = 1/2, 3/2, 2, 3), B = 0.003 | 2.3e-6 | 2.34000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** | quoted to two digits (1.39e-6, 2.34e-6) |
| S6.6.PD_k1.5 | Sec. 6.6 (Mass) | ln M_cc - ln M_ODE at v = 280, B = 0.03, k = 3/2 | 3e-7 | 3.34000e-07 | 5e-08 (half unit of the last quoted digit) | **PASS** | quoted to one digit (3.3e-7) |
| S6.6.E_0.03_0.5_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.03, k = 0.5 | -4.39e-1 | -0.43867 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_0.5_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.03, k = 0.5 | -1.18e-1 | -0.1182 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_0.5_qe | Table ext | q_e, B = 0.03, k = 0.5 | 1.44 | 1.44 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_0.5_rem | Table ext | int_280^inf e dv (est.), B = 0.03, k = 0.5 | 0.74 | 0.744 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_0.5_dJ | Table ext | Delta J/J, B = 0.03, k = 0.5 | 3.3e-2 | 0.0334 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_0.5_dJp | Table ext | Delta J_phi/J_phi, B = 0.03, k = 0.5 | 0.17 | 0.172 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_1.5_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.03, k = 1.5 | -1.58e-2 | -0.015784 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_1.5_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.03, k = 1.5 | -8.3e-4 | -8.25000e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_1.5_qe | Table ext | q_e, B = 0.03, k = 1.5 | 3.4 | 3.39 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_1.5_rem | Table ext | int_280^inf e dv (est.), B = 0.03, k = 1.5 | 7.0e-4 | 6.99000e-04 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_1.5_dJ | Table ext | Delta J/J, B = 0.03, k = 1.5 | 4.5e-5 | 4.48000e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_1.5_dJp | Table ext | Delta J_phi/J_phi, B = 0.03, k = 1.5 | 9.1e-3 | 0.0091 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_2_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.03, k = 2 | -1.05e-2 | -0.010518 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_2_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.03, k = 2 | -1.36e-4 | -1.35600e-04 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_2_qe | Table ext | q_e, B = 0.03, k = 2 | 6.8 | 6.78 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_2_rem | Table ext | int_280^inf e dv (est.), B = 0.03, k = 2 | 2.5e-5 | 2.50000e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_2_dJ | Table ext | Delta J/J, B = 0.03, k = 2 | 2.5e-6 | 2.49000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_2_dJp | Table ext | Delta J_phi/J_phi, B = 0.03, k = 2 | 1.9e-3 | 0.00188 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_3_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.03, k = 3 | -9.40e-3 | -0.0094005 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_3_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.03, k = 3 | -6.9e-5 | -6.93700e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_3_qe | Table ext | q_e, B = 0.03, k = 3 | 11.5 | 11.53 | 0.075 (half unit of the last quoted digit x 1.5) | **PASS** | the text notes that q_e is uncertain for k = 3 (excess within a factor 6 of the sigma_v level spread) |
| S6.6.E_0.03_3_rem | Table ext | int_280^inf e dv (est.), B = 0.03, k = 3 | 1.9e-6 | 1.93000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_3_dJ | Table ext | Delta J/J, B = 0.03, k = 3 | 1.1e-6 | 1.11000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.03_3_dJp | Table ext | Delta J_phi/J_phi, B = 0.03, k = 3 | 1.1e-3 | 0.00106 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_0.5_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.003, k = 0.5 | -4.16e-3 | -0.0041627 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_0.5_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.003, k = 0.5 | -1.12e-3 | -0.001123 | 5e-06 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_0.5_qe | Table ext | q_e, B = 0.003, k = 0.5 | 1.44 | 1.44 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_0.5_rem | Table ext | int_280^inf e dv (est.), B = 0.003, k = 0.5 | 7.1e-3 | 0.00709 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_0.5_dJ | Table ext | Delta J/J, B = 0.003, k = 0.5 | 2.0e-2 | 0.02 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_0.5_dJp | Table ext | Delta J_phi/J_phi, B = 0.003, k = 0.5 | 0.12 | 0.122 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_1.5_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.003, k = 1.5 | -1.46e-4 | -1.45890e-04 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_1.5_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.003, k = 1.5 | -5.9e-6 | -5.88300e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_1.5_qe | Table ext | q_e, B = 0.003, k = 1.5 | 3.4 | 3.37 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_1.5_rem | Table ext | int_280^inf e dv (est.), B = 0.003, k = 1.5 | 6.7e-6 | 6.68000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_1.5_dJ | Table ext | Delta J/J, B = 0.003, k = 1.5 | 3.5e-5 | 3.50000e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_1.5_dJp | Table ext | Delta J_phi/J_phi, B = 0.003, k = 1.5 | 8.8e-3 | 0.00876 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_2_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.003, k = 2 | -9.6e-5 | -9.64440e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_2_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.003, k = 2 | +2.9e-8 | 2.85000e-08 | 5e-10 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_2_qe | Table ext | q_e, B = 0.003, k = 2 | 6.7 | 6.67 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_2_rem | Table ext | int_280^inf e dv (est.), B = 0.003, k = 2 | 2.5e-7 | 2.47000e-07 | 5e-09 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_2_dJ | Table ext | Delta J/J, B = 0.003, k = 2 | 1.8e-6 | 1.80000e-06 | 5e-08 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_2_dJp | Table ext | Delta J_phi/J_phi, B = 0.003, k = 2 | 1.8e-3 | 0.00181 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_3_L100 | Table ext | Lambda(280)-Lambda(100), B = 0.003, k = 3 | -8.6e-5 | -8.60500e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_3_L200 | Table ext | Lambda(280)-Lambda(200), B = 0.003, k = 3 | +1.1e-7 | 1.11200e-07 | 5e-09 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_3_qe | Table ext | q_e, B = 0.003, k = 3 | 11.5 | 11.5 | 0.075 (half unit of the last quoted digit x 1.5) | **PASS** | the text notes that q_e is uncertain for k = 3 (excess within a factor 6 of the sigma_v level spread) |
| S6.6.E_0.003_3_rem | Table ext | int_280^inf e dv (est.), B = 0.003, k = 3 | 1.8e-8 | 1.80000e-08 | 5e-10 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_3_dJ | Table ext | Delta J/J, B = 0.003, k = 3 | 7.6e-7 | 7.55000e-07 | 5e-09 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_0.003_3_dJp | Table ext | Delta J_phi/J_phi, B = 0.003, k = 3 | 1.0e-3 | 0.00101 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_text1 | Sec. 6.6 | k >= 3/2 (B = 0.03): Lambda changes by -0.016, -0.011, -0.009 between v = 100 and 280 (k = 3/2, 2, 3) | 0.016 | 0.015784 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E_text2 | Sec. 6.6 | remainder <= 7e-4 (B = 0.03, k = 3/2) | 7e-4 | 6.99000e-04 | <= 0.000707 | **PASS** |  |
| S6.5.K_5 | Sec. 6.5 | kappa_- for m_N = 5 | 0.796 | 0.795649 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.K_3 | Sec. 6.5 | kappa_- for m_N = 3 | 0.653 | 0.653013 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.K_2 | Sec. 6.5 | kappa_- for m_N = 2 | 0.463 | 0.462565 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.K_1.6 | Sec. 6.5 | kappa_- for m_N = 1.6 | 0.302 | 0.302487 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.K_1.4 | Sec. 6.5 | kappa_- for m_N = 1.4 | 0.164 | 0.163981 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.A_5 | Sec. 6.5 | A_* at h = 0.1 (scaled domain), m_N = 5 | 0.0204 | 0.020442 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.A_3 | Sec. 6.5 | A_* at h = 0.1 (scaled domain), m_N = 3 | 0.0327 | 0.0326933 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.A_2 | Sec. 6.5 | A_* at h = 0.1 (scaled domain), m_N = 2 | 0.0453 | 0.0452685 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.A_1.6 | Sec. 6.5 | A_* at h = 0.1 (scaled domain), m_N = 1.6 | 0.0512 | 0.0512219 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.A_1.4 | Sec. 6.5 | A_* at h = 0.1 (scaled domain), m_N = 1.4 | 0.0497 | 0.0497017 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.G_5 | Sec. 6.5 | peak local exponent, m_N = 5 | 0.4998 | 0.499767 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.G_3 | Sec. 6.5 | peak local exponent, m_N = 3 | 0.4997 | 0.499658 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.G_2 | Sec. 6.5 | peak local exponent, m_N = 2 | 0.4996 | 0.499583 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.G_1.6 | Sec. 6.5 | peak local exponent, m_N = 1.6 | 0.4995 | 0.49955 | 5.5e-05 (half unit of the last quoted digit x 1.1) | **PASS** | computed 0.49955 rounds either way |
| S6.5.G_1.4 | Sec. 6.5 | peak local exponent, m_N = 1.4 | 0.4992 | 0.499202 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.G_flag | Sec. 6.5 | peak at the smallest distance for kappa_- = 0.164 ("still rising") | True | 1 | exact | **PASS** |  |
| S6.5.Q_lo_0.5 | Sec. 6.5 | q(v) at 0.5 x 90/kappa_-: minimum over m_N | 5.132 | 5.13226 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.Q_hi_0.5 | Sec. 6.5 | q(v) at 0.5 x 90/kappa_-: maximum over m_N | 5.140 | 5.13954 | 0.0005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.Q_lo_0.75 | Sec. 6.5 | q(v) at 0.75 x 90/kappa_-: minimum over m_N | 5.0821 | 5.08212 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.Q_hi_0.75 | Sec. 6.5 | q(v) at 0.75 x 90/kappa_-: maximum over m_N | 5.0827 | 5.08272 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.Q_lo_0.95 | Sec. 6.5 | q(v) at 0.95 x 90/kappa_-: minimum over m_N | 5.0634 | 5.06337 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.Q_hi_0.95 | Sec. 6.5 | q(v) at 0.95 x 90/kappa_-: maximum over m_N | 5.0637 | 5.0637 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.L1 | Sec. 6.5 | domain scales as 40/kappa_-: kappa_- u1 (m_N = 1.4) | 40 | 39.9951 | rel 0.001 | **PASS** | u1 = v1 = 40/kappa_- rounded to the grid |
| S6.5.D1 | Sec. 6.5 | A_* for m_N = 1.4, kappa_- u1 = 20 (h = 0.1) | 0.0497017404 | 0.0497017 | 5e-11 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.D2 | Sec. 6.5 | A_* for m_N = 1.4, kappa_- u1 = 40 (h = 0.1) | 0.0497017403 | 0.0497017 | 7.5e-11 (half unit of the last quoted digit x 1.5) | **PASS** | the two values differ in the last quoted digit |
| S6.5.D3 | Sec. 6.5 | |A_*(u1=20) - A_*(u1=40)| | 1e-9 | 1.00000e-10 | <= 1e-09 | **PASS** |  |
| S6.5.F1 | Sec. 6.5 | fixed domain, m_N = 1.4: number of distances listed | 11 | 11 | exact | **PASS** | two of the 13 runs are flagged collapsed |
| S6.5.F2 | Sec. 6.5 | fixed domain, m_N = 1.4: smallest local exponent | -3.4 | -3.417 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.F3 | Sec. 6.5 | fixed domain, m_N = 1.4: largest local exponent | 14.9 | 14.882 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.F4 | Sec. 6.5 | fixed domain, m_N = 1.4: closest to 1/2 (distance from 0.5 at least 0.1) | 0.37 | 0.37 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.F5 | Sec. 6.5 | fixed domain, m_N = 1.4: none within 0.1 of 1/2 | True | True | exact | **PASS** |  |
| S6.5.F6 | Sec. 6.5 | fixed domain, m_N = 1.4: A_* | 0.0503 | 0.0502846 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.5.F7 | Sec. 6.5 | fixed domain, m_N = 5: exponents lie in [0.47, 0.50] at all 13 distances | True | True | exact | **PASS** | text: "0.47-0.50 at all thirteen distances"; the first value is 0.488 and the smallest 0.468 |
| S6.5.F8 | Sec. 6.5 | kappa_- u1 for m_N = 1.4 at u1 = 30 | 4.9 | 4.92 | 0.05 (half unit of the last quoted digit) | **PASS** | arithmetic |
| S6.5.F9 | Sec. 6.5 | kappa_- u1 for m_N = 5 at u1 = 30 | 24 | 23.868 | 0.5 (half unit of the last quoted digit) | **PASS** | arithmetic (23.9) |
| S6.6.Sm1 | Sec. 6.6 (Flux) | PDE/kernel flux ratio without window (s2 = 0) at v = 60 | 0.93 | 0.93181 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.Sm2 | Sec. 6.6 (Flux) | ... at v = 100 | 0.89 | 0.88552 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.Sm3 | Sec. 6.6 (Flux) | change of the ratio for variances 0.25-1 relative to 0.5 at v = 60, 100 (max) | 1.2e-3 | 0.00119 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.Sm4 | Sec. 6.6 (Flux) | ... at v = 200, 290 (max) | 4e-5 | 4.00000e-05 | 5e-06 (half unit of the last quoted digit) | **PASS** | quoted to one digit (4e-5) |
| S6.6.E12b | Sec. 6.6 / summary | constant to 2e-5 for 150 <= v <= 420: max |ratio - 1.00030| | 2e-5 | 1.90000e-05 | 5e-06 (half unit of the last quoted digit) | **PASS** | quoted "+-2e-5" |
| S6.6.E12c | Sec. 6.6 / summary | agreement of flux with the kernel at B = 0.003 to v = 420 (max |ratio - 1|, v >= 60) | 4e-4 | 3.56000e-04 | 5e-05 (half unit of the last quoted digit) | **PASS** | quoted to one digit (3.6e-4) |
| S6.6.E12d | Sec. 6.6 / summary | second Romberg level departs at v = 420 (percent) | 0.8 | 0.8247 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.RM1 | Sec. 6.6 (Mass) / abstract | ray ODE vs extrapolated PDE mass to v = 108, k = 3/2 (B = 0.03) | 6e-5 | 6.10000e-05 | 5e-06 (half unit of the last quoted digit) | **PASS** | quoted to one digit (6.1e-5) |
| S6.6.RM2 | Sec. 6.6 (Mass) / abstract | ... k = 1/2 | 2e-6 | 2.10000e-06 | 5e-07 (half unit of the last quoted digit) | **PASS** | quoted to one digit (2.1e-6) |
| S6.6.QM_1.5 | Sec. 6.6 (Rate) / abstract | q_M = (kappa_-(mu_f) - dlnM/dv)(v+1) at v = 2500, B = 0.003, k = 1.5 | 5.02 | 5.0216 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.QM_0.5 | Sec. 6.6 (Rate) / abstract | q_M = (kappa_-(mu_f) - dlnM/dv)(v+1) at v = 2500, B = 0.003, k = 0.5 | 3.01 | 3.0117 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.Gain | Sec. 6.6 | zero-frequency gain (1 + r_+^2/r_-^2)/2 | 44.30 | 44.3045 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.r_0 | Table semiclassical | r(3000) - r(250) for eps = 0 | -5.3e-11 | -5.26500e-11 | 5e-13 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.M_0 | Table semiclassical | ln|M|(3000) for eps = 0 | 2312.33 | 2312.33 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.s_0 | Table semiclassical | sign of M(3000) for eps = 0 | 1 | 1 | exact | **PASS** |  |
| S6.7.T_1e-15 | Table semiclassical | |T^q_vv| for eps = 1e-15 | 3.0e-19 | 2.98800e-19 | 5e-21 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.v_1e-15 | Table semiclassical | v_flip for eps = 1e-15 | 2670 | 2670 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.r_1e-15 | Table semiclassical | r(3000) - r(250) for eps = 1e-15 | -5.3e-11 | -5.26400e-11 | 5e-13 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.M_1e-15 | Table semiclassical | ln|M|(3000) for eps = 1e-15 | 2312.10 | 2312.1 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.s_1e-15 | Table semiclassical | sign of M(3000) for eps = 1e-15 | -1 | -1 | exact | **PASS** |  |
| S6.7.T_1e-12 | Table semiclassical | |T^q_vv| for eps = 1e-12 | 3.0e-16 | 2.98800e-16 | 5e-18 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.v_1e-12 | Table semiclassical | v_flip for eps = 1e-12 | 679 | 679 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.r_1e-12 | Table semiclassical | r(3000) - r(250) for eps = 1e-12 | -3.9e-11 | -3.89800e-11 | 5e-13 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.M_1e-12 | Table semiclassical | ln|M|(3000) for eps = 1e-12 | 2319.82 | 2319.82 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.s_1e-12 | Table semiclassical | sign of M(3000) for eps = 1e-12 | -1 | -1 | exact | **PASS** |  |
| S6.7.T_1e-10 | Table semiclassical | |T^q_vv| for eps = 1e-10 | 3.0e-14 | 2.98800e-14 | 5e-16 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.v_1e-10 | Table semiclassical | v_flip for eps = 1e-10 | 280 | 280 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.r_1e-10 | Table semiclassical | r(3000) - r(250) for eps = 1e-10 | +1.3e-9 | 1.31900e-09 | 5e-11 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.M_1e-10 | Table semiclassical | ln|M|(3000) for eps = 1e-10 | 2324.42 | 2324.42 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.s_1e-10 | Table semiclassical | sign of M(3000) for eps = 1e-10 | -1 | -1 | exact | **PASS** |  |
| S6.7.T_1e-08 | Table semiclassical | |T^q_vv| for eps = 1e-08 | 3.0e-12 | 2.98800e-12 | 5e-14 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.v_1e-08 | Table semiclassical | v_flip for eps = 1e-08 | 159 | 159 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.r_1e-08 | Table semiclassical | r(3000) - r(250) for eps = 1e-08 | +1.4e-7 | 1.37200e-07 | 5e-09 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.M_1e-08 | Table semiclassical | ln|M|(3000) for eps = 1e-08 | 2329.03 | 2329.03 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.s_1e-08 | Table semiclassical | sign of M(3000) for eps = 1e-08 | -1 | -1 | exact | **PASS** |  |
| S6.7.T_1e-06 | Table semiclassical | |T^q_vv| for eps = 1e-06 | 3.0e-10 | 2.98800e-10 | 5e-12 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.v_1e-06 | Table semiclassical | v_flip for eps = 1e-06 | 103 | 103 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.r_1e-06 | Table semiclassical | r(3000) - r(250) for eps = 1e-06 | +1.4e-5 | 1.37200e-05 | 5e-07 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.M_1e-06 | Table semiclassical | ln|M|(3000) for eps = 1e-06 | 2333.63 | 2333.63 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.s_1e-06 | Table semiclassical | sign of M(3000) for eps = 1e-06 | -1 | -1 | exact | **PASS** |  |
| S6.7.T_0.0001 | Table semiclassical | |T^q_vv| for eps = 0.0001 | 3.0e-8 | 2.97900e-08 | 5e-10 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.v_0.0001 | Table semiclassical | v_flip for eps = 0.0001 | 62 | 62 | 0.5 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.r_0.0001 | Table semiclassical | r(3000) - r(250) for eps = 0.0001 | +1.4e-3 | 0.001371 | 5e-05 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.M_0.0001 | Table semiclassical | ln|M|(3000) for eps = 0.0001 | 2338.24 | 2338.24 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.s_0.0001 | Table semiclassical | sign of M(3000) for eps = 0.0001 | -1 | -1 | exact | **PASS** |  |
| S6.7.FR_1e-10 | Sec. 6.7 | phi_v^2/|T^q_vv| at v_flip, eps = 1e-10 | 0.96 | 0.9595 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.FR_1e-08 | Sec. 6.7 | phi_v^2/|T^q_vv| at v_flip, eps = 1e-08 | 0.91 | 0.9089 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.FR_1e-06 | Sec. 6.7 | phi_v^2/|T^q_vv| at v_flip, eps = 1e-06 | 0.88 | 0.8751 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S6.7.FR_1e-04 | Sec. 6.7 | phi_v^2/|T^q_vv| at v_flip, eps = 1e-04 | 0.44 | 0.4406 | 0.005 (half unit of the last quoted digit) | **PASS** |  |
| S2.Mstar | Sec. 2 | M* = 3 sqrt3 l/4 | 1.299 | 1.29904 | 0.0005 (half unit of the last quoted digit) | **PASS** | arithmetic |
| S6.3.d1 | Sec. 6.3 | smallest distance A_*-A scanned | 1e-10 | 1.00000e-10 | rel 1e-09 | **PASS** | grid of distances 10^-10 ... 10^-3 |
| S6.3.d2 | Sec. 6.3 | largest distance A_*-A scanned | 1e-3 | 0.001 | rel 1e-09 | **PASS** | grid of distances 10^-10 ... 10^-3 |
| S6.6.E_L100_k2 | Sec. 6.6 | Lambda(280) - Lambda(100) for B = 0.03, k = 2 | 0.011 | 0.010518 | 0.0006 (half unit of the last quoted digit x 1.2) | **PASS** | quoted to two digits |
| S6.6.E_L100_k3 | Sec. 6.6 | Lambda(280) - Lambda(100) for B = 0.03, k = 3 | 0.009 | 0.0094005 | 0.0006 (half unit of the last quoted digit x 1.2) | **PASS** | quoted to two digits |
| S6.6.E_Jle | Sec. 6.6 | k >= 3/2: fraction of J accumulated between v = 200 and 280 (max over the six runs) | 5e-5 | 4.48000e-05 | <= 5e-05 | **PASS** |  |
| S6.6.E_Jphile | Sec. 6.6 | k >= 3/2: fraction of J_phi accumulated between v = 200 and 280 (max over the six runs) | 1e-2 | 0.0091 | <= 0.01 | **PASS** |  |
| S6.6.E_L200 | Sec. 6.6 | k >= 3/2: |Lambda(280) - Lambda(200)| (max over the six runs, text: 8e-4) | 1e-3 | 8.25000e-04 | <= 0.001 | **PASS** |  |
| S6.6.E_rem | Sec. 6.6 | k >= 3/2: remainder estimate (max over the six runs, text: <= 7e-4) | 7e-4 | 6.99000e-04 | <= 0.000707 | **PASS** |  |
| S6.6.lnM280 | Sec. 6.6 (Mass) | ln M at v = 280 on the ray U = 0.9993 (B = 0.03, k = 3/2): "M ~ e^170" | 170 | 167.24 | rel 0.03 | **PASS** | order of magnitude statement (167) |
| S6.7.vflip1 | Sec. 6.7 / abstract | v_flip for eps = 1e-15 is before v = 3000 | 3000 | 2670 | <= 3000 | **PASS** |  |
| S6.7.vflip2 | Sec. 6.7 / abstract | v_flip for eps = 1e-6 is inside the PDE window (v_b = 250) | 250 | 103 | <= 250 | **PASS** |  |
| S6.7.vflip3 | Sec. 6.7 | |ln M| keeps growing after the flip at the rate kappa_-: ln|M|(3000) increases with eps by | 4.6 | 4.6 | 0.05 (half unit of the last quoted digit) | **PASS** | consistent with a shift of v_flip only (no change of the exponent) |
| S6.6.E11a | Sec. 6.6 (Flux) | B = 0.03, k = 3/2: flux above the static-hole response at v = 280 [%] | 3.5 | 3.472 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.6.E11b | Sec. 6.6 (Flux) | B = 0.03, k = 1/2: flux above the static-hole response at v = 280 [%] | 3.5 | 3.497 | 0.05 (half unit of the last quoted digit) | **PASS** |  |
| S6.fig1 | Fig. classes | fig_ori_classes.png regenerated (size > 20 kB) | 20000 | 130121 | >= 20000 | **PASS** |  |
| S6.fig2 | Fig. nl | fig_nonlinear.png regenerated (size > 20 kB) | 20000 | 248372 | >= 20000 | **PASS** |  |

