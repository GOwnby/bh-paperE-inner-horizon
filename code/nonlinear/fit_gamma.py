"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Threshold exponent gamma and prefactor of r_inf ~ c (A_* - A)^gamma (Paper E, Sec. 6.4).
Reads threshold_h{0.08,0.04,0.02}.json (written by run_threshold.py) and fits log r_inf against log(A_*-A) over the three windows
[1e-10,1e-9], [1e-10,1e-7], [1e-10,1e-6] of d=A_*-A.  The prefactor quoted in the paper is r_inf/sqrt(d) at d=1e-10.
usage: python3 fit_gamma.py        (instant; writes nothing, redirect to fit_gamma.log)"""
import json, numpy as np
for h in ('0.08', '0.04', '0.02'):
    s = json.load(open('threshold_h%s.json' % h))
    res = [(d, r) for d, r, r4 in s['res'] if r is not None]
    d = np.array([x[0] for x in res]); r = np.array([x[1] for x in res])
    print('h=%s  A*=%.10f  (%d distances)' % (h, s['Astar'], len(d)))
    for lo, hi in ((1e-10, 1e-9), (1e-10, 1e-7), (1e-10, 1e-6)):
        m = (d >= lo * 0.999) & (d <= hi * 1.001)
        g, c = np.polyfit(np.log(d[m]), np.log(r[m]), 1)
        print('  window [%g,%g] (%d points): gamma = %.4f' % (lo, hi, m.sum(), g))
    print('  prefactor r_inf/sqrt(d) at d=1e-10: %.2f' % (r[0] / np.sqrt(d[0])))
