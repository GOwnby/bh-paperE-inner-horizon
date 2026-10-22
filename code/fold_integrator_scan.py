"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Integrator sensitivity of the D0 = 1e-12 rows of Table fold (Paper E, Sec. 4 and Reproducibility section).
The seed D0 = 1e-12 is of the order of the absolute accuracy of the state variable m (~5e-12 at rtol 1e-12), so the advanced time v* at which the fold is
reached depends slightly on the integrator; the rows D0 = 1e-6 and 1e-9 do not.  This script lists v* for LSODA at rtol 1e-10 ... 1e-13 (scipy clamps rtol to
>= 2.2e-14 and LSODA then refuses with 'excess accuracy'), and for DOP853, Radau and RK45 at rtol 1e-12, 1e-13.   usage: python3 fold_integrator_scan.py [lsoda|all]
-> fold_integrator_scan.log (via verify.sh)"""
import sys, warnings, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from ori_model import Cl
warnings.filterwarnings('ignore')
minf = 5.0
def vstar(cl, D0, rtol, method, q0=1e-4, p=4.0, delta=0.25):
    rm0 = cl.rminus(minf); sig = np.sign(cl.dMdm(minf, rm0))
    mm = lambda v: minf - sig * delta * v**(-p); dmm = lambda v: sig * p * delta * v**(-p - 1)
    def rhs(v, y):
        q, m = y; m_ = mm(v); rm = cl.rminus(m_); drm = -cl.Pm(m_, rm) / cl.Pr(m_, rm)
        fm = cl.f_taylor(m_, rm, q); R = rm + q; fp = cl.P(m, R) / cl.D(m, R)
        return [0.5 * fm - drm * dmm(v), cl.dMdm(m_, R) * dmm(v) * fp / (fm * cl.dMdm(m, R))]
    def ev(v, y):
        R = cl.rminus(mm(v)) + y[0]; return sig * cl.dMdm(y[1], R) - 1e-4 * abs(cl.dMdm(mm(v), R))
    ev.terminal = True
    m_ = mm(1.0); rm = cl.rminus(m_); M0 = cl.M(m_, rm + q0) + D0
    mp = brentq(lambda x: cl.M(x, rm + q0) - M0, m_ * 0.9, m_ * 1.1, xtol=1e-300, rtol=1e-15)
    sol = solve_ivp(rhs, [1.0, 300], [q0, mp], method=method, rtol=rtol, atol=1e-300, events=ev)
    return float(sol.t[-1])
which = sys.argv[1] if len(sys.argv) > 1 else 'lsoda'
cases = [('LSODA', rt) for rt in (1e-10, 1e-11, 1e-12, 1e-13, 3e-14)]
if which == 'all':
    cases += [(m, rt) for m in ('DOP853', 'Radau', 'RK45') for rt in (1e-12, 1e-13)]
print('integrator rtol        s=1: v*(D0=1e-6, 1e-9, 1e-12)        s=2: v*(D0=1e-6, 1e-9, 1e-12)')
for meth, rt in cases:
    row = []
    for s in (1.0, 2.0):
        cl = Cl('h', ell=1.0, m0=minf, s=s)
        row.append('(%s)' % ', '.join('%.3f' % vstar(cl, D0, rt, meth) for D0 in ((1e-6, 1e-9, 1e-12) if meth == 'LSODA' else (1e-12,))))
    print('%-7s %-7g %s   %s' % (meth, rt, row[0], row[1]), flush=True)
rt = 2e-14
cl = Cl('h', ell=1.0, m0=minf, s=1.0)
print('LSODA rtol=%g (below the scipy floor 2.22e-14): v* = %.3f  (integration refused: excess accuracy requested)' % (rt, vstar(cl, 1e-12, rt, 'LSODA')))
