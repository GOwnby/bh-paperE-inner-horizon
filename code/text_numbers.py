"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Numerical statements of the text of Paper E that are not produced by another script (all instant):
 (1) Sec. 4, regime I: G/(3M/R) - 1 at M = 1e50 for s = -1/2 and G/(3M/R) for s = -1; m_+ needed for M = 6e5 at s = -0.01 (about 1e600);
 (2) Sec. 4, regime III: the fold values m_*, M_max/(R^3/2l^2) for s = 1e-3, 1e-2, 1e-1 (R = r_-(m_inf = 5)) and the analytic M_max for s = 1, 2;
 (3) Sec. 5: M_i/l and Lambda for a 10 solar-mass hole with l = l_P, the timescales 2 ln(r_g/l)/kappa_- (180 l) and 3 ln(r_g/l)/kappa_- (270 l);
 (4) Sec. 6.7: zero-frequency gain (1 + r_+^2/r_-^2)/2 = 44.30 of the interior transfer function for m_N = 5.
usage: python3 text_numbers.py  -> text_numbers.log, text_numbers.json (via verify.sh)"""
import json
import numpy as np
from ori_model import Cl
T = {}
print('# (1) regime I')
minf = 5.0
c = Cl('h', ell=1.0, m0=minf, s=-0.5); R = c.rminus(minf)
dev = abs(c.G(1e50, R) / (3 * 1e50 / R) - 1)
T['regI.dev_G_s-0.5_M1e50'] = dev
print('s=-0.5: |G/(3M/R) - 1| at M=1e50, R=r_-=%.6f: %.3e   (exact deviation ~ R^3/a(m) = %.1e; the printed value is the double-precision tolerance of the log-space inversion of the closure)' % (R, dev, R**3 / c.a(c.mofM(1e50, R))))
c = Cl('h', ell=1.0, m0=minf, s=-1.0); R = c.rminus(minf)
T['regI.G_ratio_s-1_rel'] = abs(c.G(1e50, R) / (3 * 1e50 / R) / (c.a(1.0) / (R**3 + c.a(1.0))) - 1)
print('s=-1: G/(3M/R) = %.6f = a/(R^3+a) = %.6f (linear in M with this factor); relative difference %.1e' % (c.G(1e50, R) / (3 * 1e50 / R), c.a(1.0) / (R**3 + c.a(1.0)), T['regI.G_ratio_s-1_rel']))
R = Cl('h', ell=1.0, m0=minf, s=-0.01).rminus(minf)
T['regI.log10_m_plus_s-0.01'] = np.log10(minf) + np.log10(2 * 6e5 / R**3) / 0.01
print('s=-0.01: log10(m_+) needed for M=6e5: %.1f' % T['regI.log10_m_plus_s-0.01'])
print('# (2) regime III')
R = Cl('h', ell=1.0, m0=minf, s=0.0).rminus(minf); R32 = R**3 / 2
print('R = r_-(5) = %.6f, R^3/(2 l^2) = %.6f' % (R, R32))
T['III.R32'] = R32
for s_ in (1e-3, 1e-2, 1e-1):
    c = Cl('h', ell=1.0, m0=minf, s=s_)
    ms = minf * (R**3 / (s_ * 2 * minf))**(1 / (1 + s_)); Mmax = c.M(ms, R)       # fold: a(m_*) = R^3/s
    T['III.mstar_s%g' % s_] = ms; T['III.Mmax_over_R32_s%g' % s_] = Mmax / R32
    print('s=%g: m_*=%.1f  M_max=%.4f  M_max/(R^3/2l^2)=%.3f' % (s_, ms, Mmax, Mmax / R32))
T['III.s_min_fold_at_minf'] = R**3 / (2 * minf)
print('threshold index s > R^3/a(m_inf) = %.4f' % T['III.s_min_fold_at_minf'])
for s_, f in ((1, lambda R: np.sqrt(minf * R**3 / 8.0)), (2, lambda R: 2 / 3 * (minf**2 * R**3 / 4.0)**(1 / 3))):
    c = Cl('h', ell=1.0, m0=minf, s=float(s_))
    ms = np.logspace(-1, 3, 400001); Mv = np.array([c.M(m, R) for m in ms[::200]]); i = int(np.argmax(Mv)) * 200
    ms2 = np.linspace(ms[max(i - 400, 0)], ms[min(i + 400, len(ms) - 1)], 20001); Mv2 = np.array([c.M(m, R) for m in ms2])
    T['III.Mmax_num_s%d' % s_] = float(Mv2.max()); T['III.Mmax_analytic_s%d' % s_] = float(f(R))
    print('s=%d at R=r_-(5): numerical max_m M = %.6f, analytic %.6f' % (s_, Mv2.max(), f(R)))
print('# (3) evaporation clock')
Mpl = 2.176434e-8; Msun = 1.98841e30           # kg (CODATA 2018 Planck mass; IAU nominal solar mass)
Mi = 10 * Msun / Mpl
Lam = 5120 * np.pi * Mi**3
rg = 2 * Mi
T['evap.Mi_over_l'] = Mi; T['evap.Lambda_10Msun'] = Lam
T['evap.t_2ln_rg'] = 2 * np.log(rg); T['evap.t_3ln_rg'] = 3 * np.log(rg)
print('M_i/l = %.4e   Lambda = 5120 pi M_i^3 = %.4e' % (Mi, Lam))
print('2 ln(r_g/l) = %.1f ;  3 ln(r_g/l) = %.1f   (e-folding time 1/kappa_- = l)' % (2 * np.log(rg), 3 * np.log(rg)))
print('# (4) interior transfer function, m_N = 5')
import scipy.optimize as so
f_ = lambda r: 1 - 2 * 5.0 * r**2 / (r**3 + 10.0)           # f = 1 - 2 M_N(r)/r, M_N = m_N r^3/(r^3 + a_N)
rm_ = so.brentq(f_, 0.5, 2.0, xtol=1e-14); rp_ = so.brentq(f_, 5.0, 12.0, xtol=1e-14)
T['EH.gain0'] = (1 + (rp_ / rm_)**2) / 2
print('r_-=%.6f r_+=%.6f  (1+(r_+/r_-)^2)/2 = %.2f' % (rm_, rp_, T['EH.gain0']))
json.dump({k: float(v) for k, v in T.items()}, open('text_numbers.json', 'w'), indent=1)
