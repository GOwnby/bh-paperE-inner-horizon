"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Near-M* constants of the evaporation clock (Paper E, Sec. 5): the coefficient alpha in P(M) ~ alpha (M-M*)^2 ... and the constant 2*sqrt(2)/(3 alpha)
that multiplies eps_f^{-1/2} in Lambda = int kappa_- dM/P.   With eps=(M-M*)/M*:  P/eps^2 -> c0, alpha = c0/M*, and kappa_- ~ sqrt(2 eps)/ ... (printed).
usage: python3 evap_alpha.py      (instant)   -> evap_alpha.log"""
import io, contextlib, numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import evap_coupling as E
Ms = E.Ms
eps = np.array([1e-4, 1e-5, 1e-6, 1e-7, 1e-8])
c = np.array([E.P(Ms * (1 + e)) / e**2 for e in eps])
kk = np.array([E.kappas2(Ms * (1 + e))[0] / np.sqrt(e) for e in eps])
for e, ci, ki in zip(eps, c, kk): print('eps=%8.1e  P/eps^2 = %.6e   kappa_-/sqrt(eps) = %.6f' % (e, ci, ki))
# Richardson in sqrt(eps): c(eps) = c0 (1 + b sqrt(eps) + ...); fit the two smallest eps
x = np.sqrt(eps[-2:]); c0 = (c[-1] * x[0] - c[-2] * x[1]) / (x[0] - x[1])
alpha = c0 / Ms
print('c0 = lim P/eps^2 = %.5e   alpha = c0/M* = %.4e   2 sqrt(2)/(3 alpha) = %.1f' % (c0, alpha, 2 * np.sqrt(2) / (3 * alpha)))
