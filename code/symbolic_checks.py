"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Computer-algebra (sympy) verification of every analytic statement of Paper E that the text calls derived, "checked" or "exact".

Run:  python3 symbolic_checks.py            (about 1-3 min; needs sympy >= 1.12)   -> symbolic_checks.log (via verify.sh)
Each identity is printed as a line  'CHECK <id>: OK|FAIL  <text>';  the exit status is non-zero if one of them fails.

Part A  (Sections 2-4, Ori model and closure family):  Eq. (Gfamily), the Moebius closure, the fold values M_max, the identity
        'linear drive = kappa_-', the Dray-'t Hooft-Redmount reduction, the extremal tuning of the bi-Proca family, kappa_+- near M*.
Part B  (Section 5, evaporation clock):  normalisation of P, Lambda = 5120 pi M^3/l, Lambda ~ 2 sqrt(2)/(3 alpha) eps_f^(-1/2).
Part C  (Section 6, double-null system):  the field equations (dn1)-(dn3) and the constraints from the full 4D Einstein tensor
        of ds^2 = -W du dv + r^2 dOmega^2 with scalar + NED-monopole source;  the divergence formula (consT);
        the ray equations (ray) and mu_v (muv);  the Kretschmann decomposition against the full Riemann contraction;
        K = 2048 pi^2 (phi_u phi_v/W)^2 = 128 pi^2 [(grad phi)^2]^2 and C^2 = K/6;  monotonicity of r_u/W;  the anomaly-term factors.
"""
import sys, itertools, time
import sympy as sp

FAILED = []
T0 = time.time()


def check(cid, text, ok):
    ok = bool(ok)
    print('CHECK %s: %s  %s' % (cid, 'OK' if ok else 'FAIL', text), flush=True)
    if not ok:
        FAILED.append(cid)


def zero(expr):
    """exact test of an expression for identical vanishing"""
    e = sp.simplify(sp.together(expr))
    return e == 0


print('sympy', sp.__version__)

# =====================================================================================================================
# Part A: Ori model, closure family
# =====================================================================================================================
m, m0, r, l0, s, a0 = sp.symbols('m m0 r ell0 s a0', positive=True)
a = 2 * l0**2 * m0 * (m / m0)**(1 + s)                                  # Eq. (family)
M = m * r**3 / (r**3 + a)                                                # Eq. (closure) with a(m)
Gdef = sp.diff(M, r)                                                     # (dM/dr)_m
check('A1', '(dM/dr)_m = 3 M a /[r (r^3 + a)]', zero(Gdef - 3 * M * a / (r * (r**3 + a))))
Gfam = 6 * l0**2 * M**2 / r**4 * (m / m0)**s                             # Eq. (Gfamily)
check('A2', 'G = (dM/dr)_m = 6 l0^2 M^2 (m/m0)^s / r^4  (Eq. Gfamily)', zero(Gdef - Gfam))

# s = 0 (Moebius closure, fixed ell):  a = 2 l^2 m
l = sp.symbols('ell', positive=True)
Mm = m * r**3 / (r**3 + 2 * l**2 * m)
check('A3', 'Moebius closure: dM/dm = r^6/(r^3+2 l^2 m)^2 > 0', zero(sp.diff(Mm, m) - r**6 / (r**3 + 2 * l**2 * m)**2))
Msym = sp.symbols('Msym', positive=True)
msol = sp.solve(sp.Eq(Msym, Mm), m)
check('A4', 'Moebius inverse m = M r^3/(r^3 - 2 l^2 M)', len(msol) == 1 and zero(msol[0] - Msym * r**3 / (r**3 - 2 * l**2 * Msym)))
check('A5', 'm -> infinity at the finite mass M = r^3/(2 l^2); pole at m = -r^3/(2 l^2)',
      sp.limit(Mm, m, sp.oo) == r**3 / (2 * l**2) and sp.simplify(sp.denom(sp.together(Mm)).subs(m, -r**3 / (2 * l**2))) == 0)
G0 = sp.diff(Mm, r).subs(m, Msym * r**3 / (r**3 - 2 * l**2 * Msym))
check('A6', 'G = 6 l^2 M^2 / r^4 for s = 0 (n = 2)', zero(G0 - 6 * l**2 * Msym**2 / r**4))

# regime I
# s = -1: a = const = 2 l0^2 m0 ; G = (3M/r) a/(r^3+a)
a_c = 2 * l0**2 * m0
Mc = m * r**3 / (r**3 + a_c)
Gc = sp.diff(Mc, r)
check('A7', 's = -1: G = (3 M/r) a/(r^3+a)', zero(Gc - 3 * Mc / r * a_c / (r**3 + a_c)))
# -1<s<0 : a >> r^3 => (m/m0)^s -> r^3/(2 l0^2 M)  => G -> 3M/r  (algebra on Eq. Gfamily)
Msy = sp.symbols('Msy', positive=True)
check('A8', '-1<s<0 at large M: (m/m0)^s = r^3/(2 l0^2 M) in Eq. (Gfamily) gives G = 3M/r',
      zero(6 * l0**2 * Msy**2 / r**4 * (r**3 / (2 * l0**2 * Msy)) - 3 * Msy / r))

# fold of the closure (regime III)
dMdm = sp.diff(M, m)
check('A9', 'dM/dm = r^3 (r^3 - s a(m)) / (r^3 + a)^2 (sign change at a = r^3/s)', zero(dMdm - r**3 * (r**3 - s * a) / (r**3 + a)**2))
for sv, label in ((1, 'A10'), (2, 'A11')):
    Ms = M.subs(s, sv)
    crit = sp.solve(sp.Eq(sp.diff(Ms, m), 0), m)
    crit = [c for c in crit if c.is_positive or c.is_real is not False]
    Mmax = [sp.simplify(Ms.subs(m, c)) for c in crit]
    if sv == 1:
        target = sp.sqrt(m0 * r**3 / (8 * l0**2))
    else:
        target = sp.Rational(2, 3) * (m0**2 * r**3 / (4 * l0**2))**sp.Rational(1, 3)
    good = any(zero(sp.simplify(mm_ - target)) or zero(sp.simplify(mm_**6 - target**6)) for mm_ in Mmax)
    check(label, 'fold value M_max(r) for s = %d equals %s' % (sv, 'sqrt(m0 r^3/(8 l0^2))' if sv == 1 else '(2/3)(m0^2 r^3/(4 l0^2))^(1/3)'), good)

# the linear drive equals kappa_-:  dM/dm / (R |dr_-/dm|) = |1/2 - M_r|/R = kappa_-  for ANY closure M(m, r)
Mm_s = sp.Symbol('M_m', positive=True)          # dM/dm at the inner horizon
Mr_s = sp.Symbol('M_r', real=True)              # dM/dr at the inner horizon
Rh = sp.Symbol('R', positive=True)
drm = sp.Symbol('drm', real=True)               # dr_-/dm
# horizon condition  M(m, r_-(m)) = r_-(m)/2, differentiated along the horizon:  M_m + M_r r_-' = r_-'/2
sol_drm = sp.solve(sp.Eq(Mm_s + Mr_s * drm, drm / 2), drm)
check('A12', 'any closure: dr_-/dm = 2 M_m/(1 - 2 M_r), so M_m/(R |dr_-/dm|) = |1 - 2 M_r|/(2R) = |f\'(r_-)|/2 = kappa_- (linear drive of Eq. Mode)',
      len(sol_drm) == 1 and zero(sol_drm[0] - 2 * Mm_s / (1 - 2 * Mr_s))
      and zero(Mm_s / (Rh * sp.Abs(sol_drm[0])) - sp.Abs(1 - 2 * Mr_s) / (2 * Rh)))

# Dray - 't Hooft - Redmount reduction:  f_a f_d = f_c f_b with f_b = f_a - 2 dM_-/R, f_d = f_c - 2 dM_+/R
fa, fc, dMm, dMp, Rs = sp.symbols('f_a f_c dM_m dM_p R')
sol = sp.solve(sp.Eq(fa * (fc - 2 * dMp / Rs), fc * (fa - 2 * dMm / Rs)), dMp)
check('A13', 'DTR: f_a f_d = f_c f_b with infinitesimal shell gives dM_+/f_+ = dM_-/f_-', len(sol) == 1 and zero(sol[0] / fc - dMm / fa))

# kappa_+- of the fixed-ell Hayward metric near M* and at large mass
Mq, rr, eps = sp.symbols('M r epsilon', positive=True)
P = rr**3 - 2 * Mq * rr**2 + 2 * l**2 * Mq                              # horizon polynomial (f = P/(r^3 + 2 l^2 M))
fH = P / (rr**3 + 2 * l**2 * Mq)
Mstar = 3 * sp.sqrt(3) * l / 4
rdbl = 4 * Mstar / 3
check('A14', 'at M* = 3 sqrt(3) l/4 the horizon polynomial has the double root r = 4M*/3 = sqrt(3) l (no other M has one)',
      zero(P.subs({Mq: Mstar, rr: rdbl})) and zero(sp.diff(P, rr).subs({Mq: Mstar, rr: rdbl}))
      and sp.solve(sp.Eq(P.subs(rr, 4 * Mq / 3), 0), Mq) == [3 * sp.sqrt(3) * l / 4])
Prr = sp.diff(P, rr, 2).subs({Mq: Mstar, rr: rdbl})
PM = sp.diff(P, Mq).subs({Mq: Mstar, rr: rdbl})
delta2 = sp.simplify(-2 * PM * Mstar / Prr)                              # root splitting delta^2 = -2 P_M M* eps / P_rr  (coefficient of eps)
den = (rdbl**3 + 2 * l**2 * Mstar)                                       # r^3 + 2 l^2 M at the double root
kap_coeff = sp.simplify(sp.sqrt(delta2) * Prr / (2 * den))               # kappa = |P_r|/(2 den), P_r = P_rr delta (same for both roots)
check('A15', 'kappa_+- -> (sqrt(2)/3) sqrt(eps)/l near M* (both horizons), eps = (M-M*)/M*: root splitting delta = sqrt(2) l sqrt(eps)', zero(kap_coeff - sp.sqrt(2) / (3 * l)) and zero(delta2 - 2 * l**2))
check('A16', 'numerical value (sqrt 2)/3 = 0.4714', abs(float(sp.sqrt(2) / 3) - 0.4714) < 1e-4)
# large mass: kappa_- -> 1/l, kappa_+ -> 1/(4 m)
x = sp.symbols('x', positive=True)
Mbig = sp.symbols('Mbig', positive=True)
fbig = lambda rv: 1 - 2 * Mbig * rv**2 / (rv**3 + 2 * l**2 * Mbig)
# r_- ~ l sqrt(2/ ...) : P=0 -> r^3 - 2 M r^2 + 2 l^2 M ; for M -> infinity: r_- = l sqrt(1) ... derive: r_-^2 = l^2 (1 + O(l/M)) ; kappa_- = |f'(r_-)|/2
rm_series = sp.symbols('rm_s', positive=True)
Pfun = lambda rv: rv**3 - 2 * Mbig * rv**2 + 2 * l**2 * Mbig
Mn, ln_ = 1000, 1
_roots = sorted([x for x in sp.Poly(Pfun(rr).subs({Mbig: Mn, l: ln_}), rr).nroots(n=30) if x.is_real and x > 0])
rm_num, rp_num = _roots[0], _roots[-1]
fprime = sp.diff(fH, rr).subs({Mq: Mn, l: ln_})
kmn = abs(fprime.subs(rr, rm_num)) / 2
kpn = abs(fprime.subs(rr, rp_num)) / 2
check('A17', 'm = 10^3 l: kappa_- l = %.4f (-> 1), kappa_+ 4m = %.7f (-> 1)  [text: 0.9990, 0.9999995]' % (float(kmn), float(kpn * 4 * Mn)),
      abs(float(kmn) - 0.9990) < 5e-5 and abs(float(kpn * 4 * Mn) - 0.9999995) < 5e-7)

# extremal tuning of the bi-Proca family: q_a = 16 M^3/(27 l^2): single degenerate horizon at r = 4M/3, kappa = 0
qa = 16 * Mq**3 / (27 * l**2)
Pq = rr**3 - 2 * Mq * rr**2 + 2 * qa * l**2
check('A18', 'q_a = 16 M^3/(27 l^2): r^3 - 2 M r^2 + 2 q_a l^2 = (r - 4M/3)^2 (r + 2M/3): degenerate horizon r = 4M/3, kappa = 0',
      zero(Pq - (rr - 4 * Mq / 3)**2 * (rr + 2 * Mq / 3)) and zero(sp.diff(Pq, rr).subs(rr, 4 * Mq / 3)))

# =====================================================================================================================
# Part B: evaporation clock
# =====================================================================================================================
Ms_, ell_ = sp.symbols('M ell', positive=True)
kp = 1 / (4 * Ms_)
Ahor = 4 * sp.pi * (2 * Ms_)**2
Pev = Ahor * kp**4 / (960 * sp.pi**2)
check('B1', 'P = A kappa_+^4/(960 pi^2) -> 1/(15360 pi M^2) for M >> l (A = 16 pi M^2, kappa_+ = 1/4M)', zero(Pev - 1 / (15360 * sp.pi * Ms_**2)))
Lam = sp.integrate((1 / ell_) * 15360 * sp.pi * Ms_**2, Ms_)
check('B2', 'Lambda = int kappa_-/P dM = 5120 pi M^3/l for M >> l (kappa_- = 1/l)', zero(Lam - 5120 * sp.pi * Ms_**3 / ell_))
check('B3', '5120 pi = 1.6085e4', abs(float(5120 * sp.pi) - 1.6085e4) < 1)
u_, al = sp.symbols('u alpha', positive=True)
Lnear = sp.integrate(sp.sqrt(2) / 3 * (1 / (al * u_))**sp.Rational(1, 2), (u_, 0, u_))
epsf = 1 / (al * u_)
check('B4', 'kappa_- = (sqrt2/3) sqrt(eps), eps = 1/(alpha u): Lambda = int kappa_- du = (2 sqrt2/(3 alpha)) eps_f^(-1/2)',
      zero(Lnear - 2 * sp.sqrt(2) / (3 * al) * epsf**sp.Rational(-1, 2)))
check('B5', '2 sqrt(2)/(3 alpha) at alpha = 1.5126e-4 is 6233 (text: 6233)', abs(float(2 * sp.sqrt(2) / (3 * sp.Rational('1.5126e-4'))) - 6233.0) < 1.5)

# =====================================================================================================================
# Part C: double-null system
# =====================================================================================================================
u, v, th, ph = sp.symbols('u v theta varphi', real=True)
X = [u, v, th, ph]
rf = sp.Function('r')(u, v)
sf = sp.Function('sigma')(u, v)
pf = sp.Function('phi')(u, v)
W = sp.exp(sf)
g = sp.zeros(4, 4)
g[0, 1] = g[1, 0] = -W / 2
g[2, 2] = rf**2
g[3, 3] = rf**2 * sp.sin(th)**2
gi = g.inv()


def christoffel(g, gi):
    G = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    for a_, b_, c_ in itertools.product(range(4), repeat=3):
        G[a_][b_][c_] = sp.simplify(sum(gi[a_, d_] * (sp.diff(g[d_, b_], X[c_]) + sp.diff(g[d_, c_], X[b_]) - sp.diff(g[b_, c_], X[d_])) for d_ in range(4)) / 2)
    return G


Gam = christoffel(g, gi)
Riem = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]       # R^a_{bcd}
for a_, b_, c_, d_ in itertools.product(range(4), repeat=4):
    if c_ >= d_:
        continue
    val = sp.diff(Gam[a_][b_][d_], X[c_]) - sp.diff(Gam[a_][b_][c_], X[d_]) + sum(Gam[a_][c_][e_] * Gam[e_][b_][d_] - Gam[a_][d_][e_] * Gam[e_][b_][c_] for e_ in range(4))
    val = sp.simplify(val)
    Riem[a_][b_][c_][d_] = val
    Riem[a_][b_][d_][c_] = -val
Ric = sp.zeros(4, 4)
for b_, d_ in itertools.product(range(4), repeat=2):
    Ric[b_, d_] = sp.simplify(sum(Riem[a_][b_][a_][d_] for a_ in range(4)))
Rsc = sp.simplify(sum(gi[a_, b_] * Ric[a_, b_] for a_ in range(4) for b_ in range(4)))
Gein = (Ric - g * Rsc / 2).applyfunc(sp.simplify)
print('  [4D curvature computed in %.0f s]' % (time.time() - T0), flush=True)

# --- jets: replace derivatives of r, sigma, phi by symbols -----------------------------------------------------------
def jet_symbols(expr):
    reps = {}
    ders = sorted([d for d in expr.atoms(sp.Derivative)], key=lambda d: -sum(c for _, c in d.variable_count))
    for d in ders:
        base = d.expr.func.__name__
        name = {'r': 'r', 'sigma': 's', 'phi': 'p'}[base] + ''.join(str(vv) for vv, c in d.variable_count for _ in range(c))
        reps[d] = sp.Symbol(name)
    expr = expr.subs(reps)
    expr = expr.subs({rf: sp.Symbol('r0', positive=True), sf: sp.Symbol('s0', real=True), pf: sp.Symbol('p0', real=True)})
    return expr


ru, rv, ruu, rvv, ruv = sp.symbols('ru rv ruu rvv ruv')
r0 = sp.Symbol('r0', positive=True)
s0 = sp.Symbol('s0', real=True)
su, sv, suu, svv, suv = sp.symbols('su sv suu svv suv')
pu, pv, puu, pvv, puv = sp.symbols('pu pv puu pvv puv')
MNp, MNpp = sp.symbols('MNp MNpp')                                         # M_N'(r), M_N''(r) at the point
Wv = sp.exp(s0)

# NED monopole + scalar stress tensor
rho_ = MNp / (4 * sp.pi * r0**2)
drho = MNpp / (4 * sp.pi * r0**2) - 2 * MNp / (4 * sp.pi * r0**3)          # d rho/dr
pt_ = -rho_ - r0 * drho / 2
dphi = [pu, pv, 0, 0]
gJ = g.applyfunc(jet_symbols)
giJ = gi.applyfunc(jet_symbols)
dphi_sq = sum(giJ[a_, b_] * dphi[a_] * dphi[b_] for a_ in range(4) for b_ in range(4))
Tscal = sp.Matrix(4, 4, lambda a_, b_: dphi[a_] * dphi[b_] - gJ[a_, b_] * dphi_sq / 2)
Tmix = sp.diag(-rho_, -rho_, pt_, pt_)                                      # T^a_b of the monopole
Tned = (gJ * Tmix)
Ttot = Tscal + Tned
EqJ = (Gein.applyfunc(jet_symbols) - 8 * sp.pi * Ttot)

# the equations to be imposed (dn1, dn2, constraints, dn3)
dn1 = -ru * rv / r0 - Wv / (4 * r0) * (1 - 2 * MNp)
dn2 = -2 * dn1 / r0 - 8 * sp.pi * pu * pv + Wv * MNpp / (2 * r0)
cons_u = su * ru - 4 * sp.pi * r0 * pu**2                                    # r_uu
cons_v = sv * rv - 4 * sp.pi * r0 * pv**2                                    # r_vv
sub_eq = {ruv: dn1, suv: dn2, ruu: cons_u, rvv: cons_v}
names = {(0, 0): 'uu', (1, 1): 'vv', (0, 1): 'uv', (2, 2): 'thth'}
allok = True
for (i, j), nm in names.items():
    e = EqJ[i, j].subs(sub_eq)
    ok = zero(e)
    allok &= ok
    print('   G_%s - 8 pi T_%s after imposing dn1, dn2 and the constraints: %s' % (nm, nm, 'identically 0' if ok else str(sp.simplify(e))[:200]))
    # sensitivity: without the equation the component must NOT vanish
check('C1', 'Einstein equations G_ab = 8 pi T_ab (scalar + NED monopole with p_t = -rho - r rho\'/2) for ds^2=-W du dv+r^2 dOmega^2 are equivalent to Eqs. (dn1), (dn2) and the two constraints (all components uu, vv, uv, thth, exact)', allok)
nz = lambda e: sp.simplify(e) != 0
e_unperturbed = [nz(EqJ[0, 1].subs({ruu: cons_u, rvv: cons_v})),            # dn1 omitted: G_uv - 8 pi T_uv != 0
                 nz(EqJ[2, 2].subs({ruu: cons_u, rvv: cons_v, ruv: dn1})),    # dn2 omitted: G_thth - 8 pi T_thth != 0
                 nz(EqJ[0, 0]), nz(EqJ[1, 1])]                                # u- and v-constraints omitted: G_uu, G_vv != 0
check('C2', 'the check can fail: omitting dn1, dn2 or a constraint leaves G_uv, G_thth, G_uu, G_vv - 8 pi T non-zero', all(e_unperturbed))
# scalar equation
GamJ = [[[jet_symbols(sp.sympify(Gam[a_][b_][c_])) for c_ in range(4)] for b_ in range(4)] for a_ in range(4)]
box = 0
dd = {(0, 0): puu, (1, 1): pvv, (0, 1): puv, (1, 0): puv}
for a_ in range(4):
    for b_ in range(4):
        term = dd.get((a_, b_), 0) - sum(GamJ[c_][a_][b_] * dphi[c_] for c_ in range(2))
        box += giJ[a_, b_] * term
dn3 = -(ru * pv + rv * pu) / r0
check('C3', 'Box phi = 0 is Eq. (dn3): phi_uv = -(r_u phi_v + r_v phi_u)/r', zero(box.subs(puv, dn3)))
# Misner-Sharp mass
Mms = r0 / 2 * (1 + 4 * ru * rv / Wv)
grr = sum(giJ[a_, b_] * (ru if a_ == 0 else rv if a_ == 1 else 0) * (ru if b_ == 0 else rv if b_ == 1 else 0) for a_ in range(4) for b_ in range(4))
check('C4', 'Misner-Sharp mass: 1 - 2M/r = g^ab r_a r_b with M = (r/2)(1 + 4 r_u r_v/W)', zero(1 - 2 * Mms / r0 - grr))

# --- Kretschmann scalar: full contraction vs decomposition ------------------------------------------------------------------
Rlow = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
for a_, b_, c_, d_ in itertools.product(range(4), repeat=4):
    Rlow[a_][b_][c_][d_] = sum(g[a_, e_] * Riem[e_][b_][c_][d_] for e_ in range(4))
Kfull = 0
for a_, b_, c_, d_ in itertools.product(range(4), repeat=4):
    if Rlow[a_][b_][c_][d_] == 0:
        continue
    up = sum(gi[b_, bb] * gi[c_, cc] * gi[d_, dd_] * Riem[a_][bb][cc][dd_] for bb in range(4) for cc in range(4) for dd_ in range(4) if gi[b_, bb] != 0 and gi[c_, cc] != 0 and gi[d_, dd_] != 0)
    Kfull += Rlow[a_][b_][c_][d_] * up
KfullJ = jet_symbols(Kfull)
# decomposition
R2 = 4 * sp.exp(-s0) * suv
Huu, Hvv, Huv = ruu - su * ru, rvv - sv * rv, ruv
HH = (8 / Wv**2) * (Huu * Hvv + Huv**2)
Kdec = R2**2 + 8 * HH / r0**2 + 4 * (2 * Mms / r0)**2 / r0**4
check('C5', 'Kretschmann scalar: full R_abcd R^abcd = R2^2 + 8 H_AB H^AB/r^2 + 4 (2M/r)^2/r^4, R2 = 4 e^{-sigma} sigma_uv, H_AB = nabla_A nabla_B r (exact, generic jets)',
      zero(KfullJ - Kdec))
HABup = sum(giJ[a_, c_] * giJ[b_, d_] * [[Huu, Huv], [Huv, Hvv]][a_][b_] * [[Huu, Huv], [Huv, Hvv]][c_][d_] for a_ in range(2) for b_ in range(2) for c_ in range(2) for d_ in range(2))
check('C6', 'H_AB H^AB = (8/W^2)(H_uu H_vv + H_uv^2) with g^{uv} = -2/W', zero(HABup - HH))

# --- divergence formula (consT) ----------------------------------------------------------------------------------------------
rhof = sp.Function('rho')(u, v)
ptf = sp.Function('p_t')(u, v)
Tm = sp.diag(-rhof, -rhof, ptf, ptf)
div = []
for b_ in range(4):
    val = sum(sp.diff(Tm[a_, b_], X[a_]) for a_ in range(4))
    val += sum(Gam[a_][a_][c_] * Tm[c_, b_] for a_ in range(4) for c_ in range(4))
    val -= sum(Gam[c_][a_][b_] * Tm[a_, c_] for a_ in range(4) for c_ in range(4))
    div.append(sp.simplify(val))
pred_u = -sp.diff(rhof, u) - 2 * sp.diff(rf, u) * (rhof + ptf) / rf
pred_v = -sp.diff(rhof, v) - 2 * sp.diff(rf, v) * (rhof + ptf) / rf
check('C7', 'nabla_a T^a_u = -rho_u - 2 r_u (rho + p_t)/r and nabla_a T^a_v = -rho_v - 2 r_v (rho + p_t)/r (Eq. consT; theta, phi components vanish)',
      zero(div[0] - pred_u) and zero(div[1] - pred_v) and zero(div[2]) and zero(div[3]))
# consequence: rho_u r_v = rho_v r_u  <=>  d rho ^ d r = 0, and then p_t = -rho - r rho'/2 is the static relation
ru_, rv_, rhou, rhov, rr_, pp_, rh_ = sp.symbols('ru_ rv_ rho_u rho_v rr_ pp_ rh_')
eq_u = -rhou - 2 * ru_ * (rh_ + pp_) / rr_
eq_v = -rhov - 2 * rv_ * (rh_ + pp_) / rr_
check('C8', 'both components vanish => r_v rho_u - r_u rho_v = 0 (d rho ^ d r = 0): rho = rho(r) where dr != 0', zero(rv_ * eq_u - ru_ * eq_v - (-rv_ * rhou + ru_ * rhov)))
rhoR = sp.Function('rhoR')
rsym = sp.Symbol('rsym', positive=True)
# rho = rho(r): rho_u = rho' r_u : eq_u = 0 -> p_t = -rho - r rho'/2
pt_sol = sp.solve(sp.Eq(eq_u.subs(rhou, sp.Symbol('drho') * ru_), 0), pp_)
check('C9', "with rho = rho(r): p_t = -rho - r rho'/2 (static relation)", len(pt_sol) == 1 and zero(pt_sol[0] - (-rh_ - rr_ * sp.Symbol('drho') / 2)))

# --- ray equations (ray), mu_v (muv), monotonicity of r_u/W ------------------------------------------------------------------
y = -rf.diff(u) / W
Sfun = (1 - 2 * MNp) / (4 * r0)
yv = sp.diff(y, v)
# substitute r_uv by dn1 (jets), then compare to y(rho/r - sigma_v) + S with rho = -r_v
yvJ = jet_symbols(yv).subs(ruv, dn1)
yJ = -ru / Wv
rhoJ = -rv
rhs_y = yJ * (rhoJ / r0 - sv) + Sfun
check('C10', 'ray equation (ln y)\' = rho/r - sigma_v + S(r)/y with y = -r_u/W, rho = -r_v, S = (1-2M_N\')/(4r)', zero(yvJ - rhs_y))
check('C11', 'ray equation rho\' = sigma_v rho + 4 pi r phi_v^2 (v-Raychaudhuri r_vv - sigma_v r_v + 4 pi r phi_v^2 = 0)',
      zero(-cons_v - (sv * rhoJ + 4 * sp.pi * r0 * pv**2)))
# M along the ray and mu_v
Mf_ = rf / 2 * (1 + 4 * sp.diff(rf, u) * sp.diff(rf, v) / W)
MNf = sp.Function('MN')
Mv = sp.diff(Mf_, v)
MvJ = jet_symbols(Mv).subs({ruv: dn1, rvv: cons_v})
muv_expr = MvJ - MNp * rv                                                     # mu = M - M_N(r): mu_v = M_v - M_N'(r) r_v
check('C12', 'mu_v = -8 pi r^2 (r_u/W) phi_v^2 = 8 pi r^2 y phi_v^2 (Eq. muv) from dn1 and the v-constraint', zero(muv_expr + 8 * sp.pi * r0**2 * ru / Wv * pv**2))
mon = sp.diff(-sp.diff(rf, u) / W * (-1), u)                                  # d_u (r_u/W)
monJ = jet_symbols(sp.diff(sp.diff(rf, u) / W, u)).subs(ruu, cons_u)
check('C13', 'u-Raychaudhuri gives d_u(r_u/W) = -4 pi r phi_u^2/W <= 0 (r_u/W non-increasing in u at fixed v)', zero(monJ + 4 * sp.pi * r0 * pu**2 / Wv))

# --- Kretschmann for the late-time asymptotics -----------------------------------------------------------------------------------
Y = sp.Symbol('Y')                                                            # Y = phi_u phi_v / W
# r_u r_v/W and M negligible, r_uv ~ 0:  sigma_uv/W -> -8 pi Y ; H_uu H_vv = 16 pi^2 r^2 phi_u^2 phi_v^2
R2sq = 16 * (-8 * sp.pi * Y)**2
HHterm = 8 * (8 / 1) * (16 * sp.pi**2 * r0**2 * Y**2) / r0**2                  # 8 H_AB H^AB / r^2 with H_uv -> 0, in units W = 1 => (phi_u phi_v/W)^2
check('C14', 'K -> R2^2 + 8 H_AB H^AB/r^2 = 1024 pi^2 Y^2 + 1024 pi^2 Y^2 = 2048 pi^2 (phi_u phi_v/W)^2 (Eq. Kscalar)', zero(R2sq + HHterm - 2048 * sp.pi**2 * Y**2))
gradphi2 = -4 * Y                                                             # (grad phi)^2 = 2 g^{uv} phi_u phi_v = -4 phi_u phi_v / W
check('C15', '2048 pi^2 Y^2 = 128 pi^2 [(grad phi)^2]^2', zero(2048 * sp.pi**2 * Y**2 - 128 * sp.pi**2 * gradphi2**2))
X2 = gradphi2**2
Kv = 128 * sp.pi**2 * X2
Rab2 = 64 * sp.pi**2 * X2                                                     # R_ab R^ab, R_ab = 8 pi d_a phi d_b phi
Rs2 = (8 * sp.pi * gradphi2)**2                                               # R^2
check('C16', 'Weyl invariant: C^2 = K - 2 R_ab R^ab + R^2/3 = K/6 for R_ab = 8 pi d_a phi d_b phi', zero((Kv - 2 * Rab2 + Rs2 / 3) - Kv / 6))
kap_, k_, vv_ = sp.symbols('kappa k v', positive=True)
dlnK = sp.diff(sp.log(sp.exp(-2 * (-kap_) * vv_) * (vv_ + 1)**(-(2 * k_ + 2))), vv_)
check('C17', 'd ln K/dv = 2 kappa_- - (2k+2)/(v+1) for W ~ e^{-kappa v}, phi_v ~ (1+v)^(-k-1) (K ~ W^-2 phi_v^2 => e^{2 kappa v} (1+v)^{-2k-2})',
      zero(dlnK - (2 * kap_ - (2 * k_ + 2) / (vv_ + 1))))
# lower bound K >= 16 M^2/r^6: mass term is 4 (2M/r)^2/r^4 = 16 M^2/r^6
check('C18', 'mass term 4 (2M/r)^2/r^4 = 16 M^2/r^6; with the other two terms squares (non-negative) K >= 16 M^2/r^6', zero(4 * (2 * Msym / rr)**2 / rr**4 - 16 * Msym**2 / rr**6))

# --- ray: metric in the regular coordinate; anomaly term --------------------------------------------------------------------------------
Vc = -sp.exp(-kap_ * vv_)
check('C19', 'V = -exp(-kappa v): dV/dv = kappa e^{-kappa v}, hence W_sV = W e^{kappa v}/kappa', zero(sp.diff(Vc, vv_) - kap_ * sp.exp(-kap_ * vv_)))
hb, rr0, sg_v, sg_vv = sp.symbols('hbar r sigma_v sigma_vv', positive=True)
Tq = -(hb / (48 * sp.pi)) * (sg_v**2 - 2 * sg_vv) / (4 * sp.pi * rr0**2)
check('C20', 'T^q_vv = -hbar (sigma_v^2 - 2 sigma_vv)/(192 pi^2 r^2) is the 1+1 anomaly term -hbar(...)/(48 pi) divided by 4 pi r^2', zero(Tq + hb * (sg_v**2 - 2 * sg_vv) / (192 * sp.pi**2 * rr0**2)))
check('C21', 'sigma_v = -kappa, sigma_vv = 0: T^q_vv = -hbar kappa^2/(192 pi^2 r^2); v_flip: phi_v^2 = eps kappa^2/(192 pi^2 r^2)', zero(Tq.subs({sg_v: -kap_, sg_vv: 0}) + hb * kap_**2 / (192 * sp.pi**2 * rr0**2)))

# --- coordinate relations of Sec. kscan / data: static interior sigma_v at the Cauchy horizon ------------------------------------
# kappa_-(static) of the NED/Hayward interior with m_N = 5, a_N = 10:  kappa_- = -f'(r_-)/2 = 0.795649, r_- = 1.057475, r_+ = 9.897927, kappa_+ = 0.048969
mN, aN = sp.Integer(5), sp.Integer(10)
fN = 1 - 2 * mN * rr**2 / (rr**3 + aN)
def horizons(mNs, aNs):
    rts = sorted([x for x in sp.Poly(rr**3 - 2 * mNs * rr**2 + aNs, rr).nroots(n=30) if x.is_real and x > 0])
    return rts[0], rts[-1]
rmN, rpN = horizons(mN, aN)
fp = sp.diff(fN, rr)
kmN = abs(fp.subs(rr, rmN)) / 2
kpN = abs(fp.subs(rr, rpN)) / 2
check('C22', 'm_N=5, a_N=10: r_- = %.6f, r_+ = %.6f, kappa_- = %.6f, kappa_+ = %.6f (text: 1.057475, 9.897927, 0.795649, 0.048969)' % (rmN, rpN, kmN, kpN),
      abs(rmN - 1.057475) < 5e-7 and abs(rpN - 9.897927) < 5e-7 and abs(kmN - 0.795649) < 5e-7 and abs(kpN - 0.048969) < 5e-7)
for mNv, kref in ((3, 0.653), (2, 0.463), (1.6, 0.302), (1.4, 0.164)):
    mNs = sp.nsimplify(mNv); aNs = 2 * mNs
    rm_, _ = horizons(mNs, aNs)
    kk = abs(sp.diff(1 - 2 * mNs * rr**2 / (rr**3 + aNs), rr).subs(rr, rm_)) / 2
    check('C23_mN%g' % mNv, 'kappa_- for m_N = %g (a_N = 2 m_N) is %.3f (text %.3f)' % (mNv, kk, kref), abs(kk - kref) < 6e-4)

print('  [total %.0f s]' % (time.time() - T0))
if FAILED:
    print('SYMBOLIC CHECKS FAILED: ' + ', '.join(FAILED))
    sys.exit(1)
print('ALL SYMBOLIC CHECKS PASSED')
