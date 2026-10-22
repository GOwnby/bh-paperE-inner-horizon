"""[Written after the original work; the fixed-domain control that the first version of the paper described was not archived. See PROVENANCE.md.]
Control for run_kappa_scan.py: the threshold exponent with a FIXED domain u1 = v1 = L (default 30) instead of L ~ 40/kappa_-.
usage: python run_kappa_fixedL.py m_N [L] [h]   (writes nothing; prints A* and the local exponent over the same distance grid as run_kappa_scan.py)
Section 'Dependence on kappa_-' of the paper quotes this control: for kappa_- <~ 0.3 the local exponents are spurious (see results_kappa_fixedL.txt)."""
import numpy as np, sys, warnings
warnings.filterwarnings('ignore')
from dn2lib import *
mN=float(sys.argv[1]); L=float(sys.argv[2]) if len(sys.argv)>2 else 30.0; h=float(sys.argv[3]) if len(sys.argv)>3 else 0.1
bg0=Bg(mN); kap=bg0.kap; L=round(L/h)*h; bg=Bg(mN,tmax=L+20)
def col(A,RMIN=1e-5):
    try: u,v,arrs,_=build2(bg,-6,L,0,L,h,h,A,0.1*A)
    except AssertionError: return True,None,None
    run2(bg,arrs,h,h); R=arrs[0]
    return ((~np.isfinite(R))|(R<=RMIN)|(~np.isfinite(arrs[1]))).any(),u,arrs
lo=1e-4; hi=lo
while not col(hi)[0]: lo=hi; hi*=2
for _ in range(50):
    mid=0.5*(lo+hi)
    if col(mid)[0]: hi=mid
    else: lo=mid
As=0.5*(lo+hi)
ds=10**np.linspace(-11,-5,13)*As/0.02; rr=[]
for d in ds:
    c,u,a=col(As-d); rr.append(None if c else float(a[0][-1][-1]))
ok=[x is not None for x in rr]
g=np.gradient(np.log(np.array([x for x in rr if x is not None])),np.log(ds[ok]))
print('m_N=%g kappa_-=%.4f fixed L=%g h=%g: A*=%.6g  local exponents (A*-A = (A*/0.02) 1e-11 ... 1e-5):'%(mN,kap,L,h,As),np.array2string(np.round(g,3),max_line_width=200))
