"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Re-derives, from the stored outputs of the double-null runs, the numbers of Section 6 of Paper E that come from long jobs
(threshold scans, domain scans, universality, kappa scan, rates, checks, supercritical locus), without re-running them.
Reads (all shipped in this directory): validation_nonlinear.json rates_nonlinear.json checks_nonlinear.json threshold_h*.json domain_nonlinear.json
universality_nonlinear.json supercritical_nonlinear.json kscan_mN*.json curvature_nonlinear.json sign_scan.log sign_ustar.log sign_separatrix.log
kscan/fixed-domain outputs.   usage: python3 analyze_stored.py     (~1 s)   -> analyze_stored.json, analyze_stored.log
The long jobs that regenerate the input files are listed in ../../verify.py (--full)."""
import json, re, os, glob, numpy as np

R = {}          # name -> value, every entry is checked against the manuscript by ../../verify.py
L = open('analyze_stored.log', 'w')


def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    L.write(s + '\n')


def J(f):
    return json.load(open(f))


# ---------------------------------------------------------------------------------------------------- validation (Sec. 6.1)
V = J('validation_nonlinear.json')
for h, e in V['static']:
    R['val.static_err_h%g' % h] = e
R['val.static_order_min'] = min(V['static_orders'])
R['val.static_order_max'] = max(V['static_orders'])
for row in V['constraint']:
    h = row[0]
    R['val.rayu_v0_20_h%g' % h] = row[1]
    R['val.rayu_v20_40_h%g' % h] = row[2]
    R['val.rayu_v40_60_h%g' % h] = row[3]
R['val.rayu_order_min'] = min(min(r) for r in V['constraint_orders'])
R['val.rayu_order_max'] = max(max(r) for r in V['constraint_orders'])
C = J('checks_nonlinear.json')
for hh, a, b in C['constraint_v']:
    R['val.rayv_v0_20_h%g' % hh] = a
    R['val.rayv_v20_58_h%g' % hh] = b
say('validation:', {k: v for k, v in R.items() if k.startswith('val.')})

# ---------------------------------------------------------------------------------------------------- growth rates (Sec. 6.2, Table nlrate)
RT = J('rates_nonlinear.json')
kap = RT['kappa_minus']
R['rates.kappa_minus'] = kap
R['rates.rm'] = RT['rm']
ori = RT['ori']
R['rates.ori_v79_delta1e-3'] = ori['delta=0.001']["v'=80"]
R['rates.ori_v79_delta1e-2'] = ori['delta=0.01']["v'=80"]
R['rates.ori_v98_delta1e-3'] = ori['delta=0.001']["v'=99"]
R['rates.ori_v98_delta1e-2'] = ori['delta=0.01']["v'=99"]
R['rates.lead_v79'] = kap - 5 / 80.
R['rates.lead_v98'] = kap - 5 / 99.
vals79, vals98, vals79_main, sv = [], [], [], []
dev79_main = []
small = {}
for key, runs in RT['pde'].items():
    for u, x in runs.items():
        vals79.append(x['rate@79']); vals98.append(x['rate@98']); sv.append(x['sigma_v(v=100)'])
        if not key.startswith('A=0.0005'):
            vals79_main.append(x['rate@79'])
            dev79_main.append(abs(x['rate@79'] - ori['delta=0.01']["v'=80"]))
        else:
            small[u] = x['rate@79'] - 0.732038
R['rates.pde_v79_min'] = min(vals79)
R['rates.pde_v79_max'] = max(vals79)
R['rates.pde_v98'] = vals98[0]
R['rates.pde_v98_spread'] = max(vals98) - min(vals98)
R['rates.pde_ori_maxdiff_v79_all_but_smallest'] = max(dev79_main)
R['rates.pde_ori_maxdiff_v98_all'] = max(abs(x - ori['delta=0.01']["v'=99"]) for x in vals98)
R['rates.smallest_A_dev_u-3'] = small['u=-3']
R['rates.smallest_A_dev_u2'] = small['u=2']
R['rates.smallest_A_dev_u0'] = small['u=0']
R['rates.dev79_others_max_vs_0.732038'] = max(abs(x - 0.732038) for x in vals79_main)
R['rates.sigma_v_all'] = float(np.mean(sv))
R['rates.sigma_v_all_spread'] = float(max(sv) - min(sv))
R['rates.v59_u0_A0.02_h0.04'] = RT['pde']['A=0.02,B=0.002,h=0.04']['u=0']['rate@59']
R['rates.v59_u-3_A0.005'] = RT['pde']['A=0.005,B=0.001,h=0.02']['u=-3']['rate@59']
R['rates.v59_u-3_A0.02_h0.04'] = RT['pde']['A=0.02,B=0.002,h=0.04']['u=-3']['rate@59']
R['rates.v59_u-3_A0.02_h0.02'] = RT['pde']['A=0.02,B=0.002,h=0.02']['u=-3']['rate@59']
R['rates.ori_next_term_v79'] = (R['rates.lead_v79'] - R['rates.ori_v79_delta1e-2'])         # ( = 7.1/(v+1)^2 )
R['rates.ori_next_term_v79_coeff'] = (R['rates.lead_v79'] - R['rates.ori_v79_delta1e-2']) * 80 ** 2 * -1
R['rates.ori_next_term_v98_coeff'] = (R['rates.lead_v98'] - R['rates.ori_v98_delta1e-2']) * 99 ** 2 * -1
say('rates:', {k: v for k, v in R.items() if k.startswith('rates.')})
# 'near' (checks): rates at u=30, 40 and A*-A = 1e-10
nr = C['near']['A*-A=1e-10']['rates']
R['near.rate79_u30'] = nr['u=30']['rate@79']
R['near.rate98_u30'] = nr['u=30']['rate@98']
R['near.rate79_u40'] = nr['u=40']['rate@79']
R['near.rate98_u40'] = nr['u=40']['rate@98']
R['near.sat_weak_u4'] = C['near']['weak A=0.02,B=0.002']['|r(100)-r(50)|/r']['u=4']
R['near.sat_weak_u40'] = C['near']['weak A=0.02,B=0.002']['|r(100)-r(50)|/r']['u=40']
R['near.sat_1e-10_u4'] = C['near']['A*-A=1e-10']['|r(100)-r(50)|/r']['u=4']
R['near.sat_1e-10_u40'] = C['near']['A*-A=1e-10']['|r(100)-r(50)|/r']['u=40']
R['near.sat_max'] = max(max(v['|r(100)-r(50)|/r'].values()) for v in C['near'].values())
R['near.sign_change_u'] = C['sign_change_u(A=0.02,B=0.002,v=100)'][0]
say('near-threshold checks:', {k: v for k, v in R.items() if k.startswith('near.')})

# ---------------------------------------------------------------------------------------------------- tails (Sec. 6.2): q = (kappa - rate)(v+1) -> 2k+2
U = J('universality_nonlinear.json')
for qd in U['q']:
    k = qd['k']
    for v0, rate, q in qd['rates']:
        R['univ.q_k%g_v%d' % (k, v0)] = q
        R['univ.rate_k%g_v%d' % (k, v0)] = rate

# ---------------------------------------------------------------------------------------------------- threshold (Sec. 6.3)
Ast = {}
fits = {}
for h in ('0.08', '0.04', '0.02'):
    s = J('threshold_h%s.json' % h)
    Ast[h] = s['Astar']
    R['thr.Astar_h%s' % h] = s['Astar']
    res = [(d, r) for d, r, r4 in s['res'] if r is not None]
    d = np.array([x[0] for x in res]); r = np.array([x[1] for x in res])
    R['thr.n_distances_h%s' % h] = len(d)
    for lo, hi in ((1e-10, 1e-9), (1e-10, 1e-7), (1e-10, 1e-6)):
        m = (d >= lo * 0.999) & (d <= hi * 1.001)
        g = np.polyfit(np.log(d[m]), np.log(r[m]), 1)[0]
        R['thr.gamma_h%s_[%g,%g]' % (h, lo, hi)] = float(g)
    R['thr.prefactor_h%s' % h] = float(r[0] / np.sqrt(d[0]))
    ge = np.gradient(np.log(r), np.log(d))
    R['thr.localexp_h%s_min_le1.6e-9' % h] = float(ge[d <= 1.6e-9 * 1.001].min())
    R['thr.localexp_h%s_max_le1.6e-9' % h] = float(ge[d <= 1.6e-9 * 1.001].max())
    R['thr.localexp_h%s_at1e-7' % h] = float(np.interp(np.log(1e-7), np.log(d), ge))
    R['thr.localexp_h%s_at2.5e-5' % h] = float(np.interp(np.log(2.5e-5), np.log(d), ge))
    R['thr.localexp_h%s_at1e-3' % h] = float(np.interp(np.log(1e-3), np.log(d), ge))
    R['thr.d_min_h%s' % h] = float(d.min())
    R['thr.d_max_h%s' % h] = float(d.max())
    fits[h] = (d, r)
# exponent at 1e-10 after correcting for the flag offset: A* (true) = A*_flag + (r_flag/41)^2   (r_inf = 41 sqrt(A*_true - A))
d, r = fits['0.04']
off = (1e-5 / 41.0) ** 2
dd = d + off
ge2 = np.gradient(np.log(r), np.log(dd))
R['thr.localexp_h0.04_at1e-10_flagcorrected'] = float(ge2[0])
R['thr.flag_offset_1e-5'] = off
R['thr.flag_offset_1e-3'] = (1e-3 / 41.0) ** 2
# Richardson in h^2 for A*
a1, a2, a3 = Ast['0.08'], Ast['0.04'], Ast['0.02']
R['thr.Astar_richardson'] = (4 * a3 - a2) / 3.
R['thr.Astar_richardson_from_0.08_0.04'] = (4 * a2 - a1) / 3.
R['thr.Astar_order'] = float(np.log2((a1 - a2) / (a2 - a3)))
say('threshold:', {k: v for k, v in R.items() if k.startswith('thr.')})

# domain (A*(u1)), v1-independence
D = J('domain_nonlinear.json')
for u1, a in D['Astar_vs_u1']:
    R['dom.Astar_u1_%d' % u1] = a
R['dom.Astar_u1_32_vs_24'] = abs(D['Astar_vs_u1'][-1][1] - D['Astar_vs_u1'][-2][1])
v1 = C['Astar_vs_v1(u1=8)']
vals = list(v1.values())
R['dom.Astar_v1_independence_max_spread'] = max(vals) - min(vals)
R['dom.Astar_v1_independence_value'] = vals[0]
for key, p in D['profile'].items():
    u = np.array(p['u']); rr = np.array(p['r'])
    R['dom.rCH_%s_u30_over_u40' % key] = float(rr[list(u).index(30.0)] / rr[list(u).index(40.0)])
    R['dom.rCH_%s_u48_minus_u40' % key] = float(abs(rr[list(u).index(48.0)] - rr[list(u).index(40.0)]))
    R['dom.rCH_%s_decreasing_beyond_u-2' % key] = bool(np.all(np.diff(rr[u >= -2]) <= 1e-12))
R['dom.rCH_max_at_u'] = float(np.array(D['profile']['d=1e-07']['u'])[int(np.argmax(D['profile']['d=1e-07']['r']))])
say('domain:', {k: v for k, v in R.items() if k.startswith('dom.')})

# other data families (Sec. 6.3)
for gd in U['gamma']:
    key = 'w%g_b%g_k%g' % (gd['width'], gd['ratio'], gd['k'])
    R['fam.Astar_' + key] = gd['Astar']
    le = np.array(gd['local_exponent'])
    R['fam.localexp_min_' + key] = float(le.min())
    R['fam.localexp_max_' + key] = float(le.max())

# supercritical locus (Sec. 6.3): r = 0.05 locus v_s(u): decreasing for moderate u, constant (null) at large u
S = J('supercritical_nonlinear.json')
for fac, rows in S.items():
    for row in rows:
        if row['r_s'] != 0.05:
            continue
        cv = [(a, b) for a, b in row['curve'] if b is not None]
        us = np.array([a for a, b in cv]); vs = np.array([b for a, b in cv])
        R['sup.%s.decreasing' % fac] = bool(np.all(np.diff(vs) <= 1e-9))
        R['sup.%s.last6_spread' % fac] = float(vs[-6:].max() - vs[-6:].min())
        R['sup.%s.n_points' % fac] = len(cv)
say('supercritical:', {k: v for k, v in R.items() if k.startswith('sup.')})

# kappa scan (Sec. 6.5)
for mN in (5, 3, 2, 1.6, 1.4):
    k = J('kscan_mN%g.json' % mN)
    R['kscan.kappa_mN%g' % mN] = k['kappa']
    R['kscan.Astar_mN%g' % mN] = k['Astar']
    R['kscan.peak_exponent_mN%g' % mN] = max(k['local_gamma'])
    R['kscan.peak_at_smallest_distance_mN%g' % mN] = bool(int(np.argmax(k['local_gamma'])) == 0)
    for (v0, rate, q), fr in zip(k['rates'], (0.5, 0.75, 0.95)):
        R['kscan.q_mN%g_f%g' % (mN, fr)] = q
        R['kscan.rate_over_kappa_mN%g_f%g' % (mN, fr)] = rate / k['kappa']
    R['kscan.L_kappa_mN%g' % mN] = k['L'] * k['kappa']
for fr in (0.5, 0.75, 0.95):
    qs = [R['kscan.q_mN%g_f%g' % (mN, fr)] for mN in (5, 3, 2, 1.6, 1.4)]
    R['kscan.q_min_f%g' % fr] = min(qs)
    R['kscan.q_max_f%g' % fr] = max(qs)
say('kscan:', {k: v for k, v in R.items() if k.startswith('kscan.')})

# ---------------------------------------------------------------------------------------------------- sign mechanism logs (Sec. 6.2)
rows = []
for line in open('sign_scan.log'):
    m = re.match(r'\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(\[.*?\])\s+(\[.*?\])\s+\((\d+),(\d+)\)\s+([\d.]+)\s+.*?along u / max\|r_u/W\| = ([\d.e+-]+)', line)
    if m:
        rows.append(dict(A=float(m.group(1)), B=float(m.group(2)), h=float(m.group(3)), ustar_ru=eval(m.group(4)), ustar_M=eval(m.group(5)),
                         n_ru=int(m.group(6)), n_M=int(m.group(7)), frac=float(m.group(8)), mono=float(m.group(9))))
R['sign.n_runs'] = len(rows)
R['sign.n_one_change_same_u'] = sum(1 for r_ in rows if r_['n_ru'] == 1 and r_['n_M'] == 1 and r_['ustar_ru'] == r_['ustar_M'])
R['sign.min_fraction'] = min(r_['frac'] for r_ in rows)
good = [r_ for r_ in rows if not (r_['A'] == 0.0005 and r_['h'] >= 0.02)]
R['sign.n_good'] = len(good)
R['sign.mono_max_good'] = max(r_['mono'] for r_ in rows if r_['A'] != 0.0005)
for r_ in rows:
    if r_['A'] == 0.0005:
        R['sign.mono_smallest_h%g' % r_['h']] = r_['mono']
        R['sign.nchanges_smallest_h%g' % r_['h']] = r_['n_ru']
R['sign.ustar_smallest_h0.01'] = [r_ for r_ in rows if r_['A'] == 0.0005 and r_['h'] == 0.01][0]['ustar_ru'][0]


def us(A, B, h):
    return [r_ for r_ in rows if r_['A'] == A and r_['B'] == B and r_['h'] == h][0]['ustar_ru'][0]


for A_ in (0.005, 0.01, 0.02, 0.0204):
    R['sign.ustar_A%g_B0.002_h0.04' % A_] = us(A_, 0.002, 0.04)
for B_ in (0.0005, 0.002, 0.01, 0.02):
    R['sign.ustar_A0.02_B%g_h0.04' % B_] = us(0.02, B_, 0.04)
for h_ in (0.08, 0.04, 0.02, 0.01):
    R['sign.ustar_A0.02_B0.002_h%g' % h_] = us(0.02, 0.002, h_)
R['sign.ustar_min'] = min(r_['ustar_ru'][0] for r_ in good)
R['sign.ustar_max'] = max(r_['ustar_ru'][0] for r_ in good)
txt = open('sign_ustar.log').read()
blocks = re.split(r'\nA=', '\n' + txt)[1:]
for b, tag in zip(blocks, ('A0.02', 'A0.01', 'A0.005')):
    vals = [float(m.group(1)) for m in re.finditer(r'^\s+(?:30|40|60|80|100)\s+(-?[\d.]+)\s', b, re.M)]
    R['sign.ustar_v30to100_%s' % tag] = vals[0]
    R['sign.ustar_v30to100_spread_%s' % tag] = max(vals) - min(vals)
sep = open('sign_separatrix.log').read()
ys = re.findall(r'y_sep=([\d.]+)', sep)
R['sign.ysep_A0.02'] = float(ys[0]); R['sign.ysep_A0.01'] = float(ys[3]); R['sign.ysep_A0.005'] = float(ys[6])
R['sign.separatrix_offsets_max'] = max(abs(float(x)) for x in re.findall(r'u_\*-u = ([+-][\d.]+)', sep))
R['sign.separatrix_min_slope'] = min(float(x) for x in re.findall(r'slope d\(y-y_sep\)/du=([\d.e+-]+)', sep))
sm = open('sign_mech.log').read()
R['sign.mech_M_change_u'] = float(re.search(r'M\(v=100\) sign changes at u = \[(-?[\d.]+)\]', sm).group(1))
R['sign.mech_ru_change_u'] = float(re.search(r'r_u\(v=100\) sign changes at u = \[(-?[\d.]+)\]', sm).group(1))
R['sign.mech_rCH_max_u'] = float(re.search(r'max of r\(u,v=100\) at u=(-?[\d.]+)', sm).group(1))
ru100 = [(float(a), float(b), float(c)) for a, b, c in re.findall(r'u=\s*(-?[\d.]+)\s+M\(100\)=[+-][\d.e+]+\s+r_u\(100\)=([+-][\d.e-]+)\s+r_u\(50\)=([+-][\d.e-]+)', sm)]
R['sign.mech_ru_v50_eq_v100'] = max(abs(b - c) / abs(b) for a, b, c in ru100)
say('sign mechanism:', {k: v for k, v in R.items() if k.startswith('sign.')})

# ---------------------------------------------------------------------------------------------------- curvature (Sec. 6.4), from curvature_nonlinear.json
CV = J('curvature_nonlinear.json')
R['curv.static_rel_err_h0.04_max'] = max(CV['static_rel_err'][1][1])
R['curv.static_rel_err_h0.04_first'] = CV['static_rel_err'][1][1][0]
for hh, v in CV['static_K_u2_v20']:
    R['curv.static_K_u2_v20_h%g' % hh] = v
for hh in ('0.04', '0.02'):
    for row in CV['K'][hh]['rows']:
        R['curv.K_h%s_v%d' % (hh, row['v'])] = row['K']
        if row['v'] >= 40:
            R['curv.ratio_h%s_v%d' % (hh, row['v'])] = row['K/(phi_u phi_v/W)^2'] / CV['2048pi^2']
            R['curv.T1_over_T2_h%s_v%d' % (hh, row['v'])] = row['T1'] / row['T2']
            R['curv.T3_over_K_h%s_v%d' % (hh, row['v'])] = row['T3'] / row['K']
        if row['v'] == 100:
            R['curv.phi_u_h%s_v100' % hh] = row['phi_u']
R['curv.K_h0.04_over_h0.02_v100'] = CV['K']['0.04']['rows'][-1]['K'] / CV['K']['0.02']['rows'][-1]['K'] - 1
R['curv.dlnK_v98_k1.5'] = CV['K']['0.04']['dlnK/dv']['98']
R['curv.dlnK_pred_v98_k1.5'] = CV['K']['0.04']['2kappa-5/(v+1)']['98']
other = CV['K_other']
R['curv.ratio_max_dev_all'] = max(abs(x['ratio'] - 1) for row in other for x in row['u'].values())
for row in other:
    R['curv.dlnK_v98_k%g_A%g' % (row['k'], row['A'])] = row['u']['2']['dlnK/dv@98']
    R['curv.dlnK_pred_v98_k%g_A%g' % (row['k'], row['A'])] = row['u']['2']['2kappa-(2k+2)/(v+1)']
R['curv.affine_total_to_v100'] = CV['affine']['affine_length_to_v100']
R['curv.affine_beyond_v100'] = CV['affine']['W(100)/kappa']
R['curv.W_exp_kappa_v_min'] = min(CV['affine']['W*exp(kappa v) at v=40,70,100'])
R['curv.W_exp_kappa_v_max'] = max(CV['affine']['W*exp(kappa v) at v=40,70,100'])
R['curv.r_v100_u2'] = CV['affine']['r(v=100)']
R['curv.sigma_v_v100'] = CV['affine']['sigma_v(v=100)']
say('curvature:', {k: v for k, v in R.items() if k.startswith('curv.')})

# ---------------------------------------------------------------------------------------------------- numbers that are plain arithmetic in the text
R['arith.kappa_pred_v98_k1'] = 2 * kap - 4 / 99.
R['arith.flag_offset_1e-5_over_41'] = (1e-5 / 41.0) ** 2

json.dump(R, open('analyze_stored.json', 'w'), indent=1, sort_keys=True, default=lambda o: bool(o) if isinstance(o, (np.bool_,)) else float(o))
say('wrote analyze_stored.json with %d entries' % len(R))
L.close()
