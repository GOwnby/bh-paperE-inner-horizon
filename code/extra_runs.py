"""Regime II/III numbers quoted in the text of Sec. 4 that are not in make_results.py's tables:
 (a) s=0: advanced time at which M_+ = R^3/(2 l^2) (m passes through +infinity), D0=1e-8, p=4, l0=1, m0=m_inf=5 (run in the regular variable M_+);
 (b) s=1e-3,1e-2,1e-1: advanced time v* at which the run stops at the fold of M(m,r), and M_+(v*) against R^3/(2 l0^2), D0=1e-8.
Run: python3 extra_runs.py   (uses ori_model.py; run_m is copied from make_results.py)."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from ori_model import Cl, run
minf=5.0
c=Cl('h',ell=1.0,m0=minf,s=0.0)
sl=run(c,minf,0.25,4.0,1.0,60,D0=1e-8,q0=1e-4)
def g(v):
    q,M=sl.sol(v); m_=minf-0.25*v**-4.0; R=c.rminus(m_)+q; return M-R**3/2.0
vs=np.linspace(2,59,2000); gs=[g(v) for v in vs]
i=[k for k in range(len(vs)-1) if gs[k]*gs[k+1]<0]
print('(a) s=0: M_+ = R^3/2l^2 at v =',[round(brentq(g,vs[k],vs[k+1]),2) for k in i])
def run_m(cl,D0,q0=1e-4,p=4.0,delta=0.25):
    rm0=cl.rminus(minf); sig=np.sign(cl.dMdm(minf,rm0))
    mm=lambda v:minf-sig*delta*v**(-p); dmm=lambda v:sig*p*delta*v**(-p-1)
    def rhs(v,y):
        q,m=y; m_=mm(v); rm=cl.rminus(m_); drm=-cl.Pm(m_,rm)/cl.Pr(m_,rm)
        fm=cl.f_taylor(m_,rm,q); R=rm+q; fp=cl.P(m,R)/cl.D(m,R)
        return [0.5*fm-drm*dmm(v), cl.dMdm(m_,R)*dmm(v)*fp/(fm*cl.dMdm(m,R))]
    def ev(v,y):
        R=cl.rminus(mm(v))+y[0]; return sig*cl.dMdm(y[1],R)-1e-4*abs(cl.dMdm(mm(v),R))
    ev.terminal=True
    m_=mm(1.0); rm=cl.rminus(m_); M0=cl.M(m_,rm+q0)+D0
    mp=brentq(lambda x:cl.M(x,rm+q0)-M0,m_*0.9,m_*1.1,xtol=1e-300,rtol=1e-15)
    sol=solve_ivp(rhs,[1.0,300],[q0,mp],method='LSODA',rtol=1e-12,atol=1e-300,events=ev,dense_output=True)
    return sol,mm
for s in (1e-3,1e-2,1e-1):
    cl=Cl('h',ell=1.0,m0=minf,s=s); sol,mm=run_m(cl,1e-8); v=sol.t[-1]; q,m=sol.y[:,-1]; R=cl.rminus(mm(v))+q
    print('(b) s=%g: stops at v*=%.2f, M_+=%.3f, R^3/2l0^2=%.3f'%(s,v,cl.M(m,R),R**3/2))
