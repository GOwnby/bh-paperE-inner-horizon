"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Saturation of the Cauchy-horizon radius in u (Paper E, Sec. 6.3): at A_* - A = 1e-10 (h = 0.04, domain u in [-6,50], v in [0,50], B = A/10)
r_CH(u=40) agrees with r_CH(u=50) to 4e-5 while r_CH(u=30) is still 12 % larger than r_CH(40);  r_inf := r(u=40, v=50).
usage: python3 check_saturation.py   (~30 s; needs threshold_h0.04.json) -> check_saturation.log"""
import json, warnings, numpy as np
warnings.filterwarnings('ignore')
from dn2lib import *
bg = Bg(); h = 0.04
As = json.load(open('threshold_h0.04.json'))['Astar']
out = {}
for d in (1e-10, 1e-7):
    A = As - d
    u, v, arrs, _ = build2(bg, -6, 50, 0, 50, h, h, A, 0.1 * A); run2(bg, arrs, h, h)
    R = arrs[0][-1]
    r = lambda uu: float(R[int(round((uu + 6) / h))])
    out['d=%g' % d] = {'r30': r(30), 'r40': r(40), 'r50': r(50), 'r30/r40-1': r(30) / r(40) - 1, '|r40-r50|': abs(r(40) - r(50))}
    print('A*-A=%g: r_CH(30)=%.6f r_CH(40)=%.6f r_CH(50)=%.6f  r30/r40-1=%.4f  |r40-r50|=%.2e' % (d, r(30), r(40), r(50), r(30) / r(40) - 1, abs(r(40) - r(50))))
json.dump(out, open('check_saturation.json', 'w'), indent=1)
