"""NOTE: the quad() calls in the lower part of this script fail for eps_f <~ 1e-6. For the tables in Paper E use evap_table.py (integration in ln(M-M*))."""
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
Ms=3*np.sqrt(3)/4   # M* in units of l (G=c=1, l=1)
def roots(M):
    # f=0:  r^3-2Mr^2+2M l^2=0
    c=np.roots([1,-2*M,0,2*M]); c=np.sort(c[np.isreal(c)].real); c=c[c>0]
    return c[0],c[-1]
def kap(M,r): # |f'|/2 with f=1-2Mr^2/(r^3+2M)
    h=1e-6*r
    f=lambda x:1-2*M*x*x/(x**3+2*M)
    return abs(f(r+h)-f(r-h))/(4*h)
def kappas(M):
    rm,rp=roots(M); return kap(M,rm),kap(M,rp),rm,rp
# analytic derivative for accuracy
def kappas2(M):
    rm,rp=roots(M)
    D=lambda r:r**3+2*M
    fp=lambda r:-(4*M*r*D(r)-2*M*r*r*3*r*r)/D(r)**2
    return abs(fp(rm))/2,abs(fp(rp))/2,rm,rp
def P(M):   # Paper A: P ~ A kappa_+^4, normalised to Hawking P_S=1/(15360 pi M^2) (Planck units hbar=1)
    km,kp,rm,rp=kappas2(M); A=4*np.pi*rp**2
    return A*kp**4/(960*np.pi**2)
print("checks: kappa_- (M=1e3)=%.6f  (1/l); kappa_+*4M=%.6f"%(kappas2(1e3)[0],kappas2(1e3)[1]*4e3))
print("P/P_S at M=1e3: %.6f"%(P(1e3)*15360*np.pi*1e6))
# near-M*: eps=(M-M*)/M*,  kappa ~ sqrt(eps) ?
for e in [1e-2,1e-4,1e-6]:
    M=Ms*(1+e); km,kp,*_=kappas2(M); print("eps=%g kappa-/sqrt(eps)=%.4f kappa+/sqrt(eps)=%.4f  P/eps^2=%.4e"%(e,km/np.sqrt(e),kp/np.sqrt(e),P(M)/e**2))
print("\nIntegrated inner-horizon exponent Lambda=int kappa_- du  and evaporation time u (Planck units), from M_i down to M_f")
print("%10s %10s %14s %14s %12s"%("M_i/l","M_f/M*","u_evap","Lambda","Lambda/(M_i^3/l)"))
for Mi in [2.0,5.0,20.0,1e3]:
    for d in [1e-1,1e-2,1e-4]:
        Mf=Ms*(1+d)
        if Mf>=Mi: continue
        g=lambda lnM:np.exp(lnM)*1.0
        u=quad(lambda M:1/P(M),Mf,Mi,limit=400,epsabs=0,epsrel=1e-9)[0]
        L=quad(lambda M:kappas2(M)[0]/P(M),Mf,Mi,limit=400,epsabs=0,epsrel=1e-9)[0]
        print("%10.3g %10.4g %14.5e %14.5e %12.3f"%(Mi,1+d,u,L,L/Mi**3))
# sqrt scaling:  Lambda(eps_f) - ... ~ c / sqrt(eps_f)  (since eps ~1/u, kappa~sqrt(eps)): check slope in eps_f^{-1/2}
print("\nnear-M* check: Lambda(eps_f) vs eps_f^{-1/2}")
Mi=2.0; prev=None
for d in [1e-3,1e-4,1e-5,1e-6,1e-7]:
    Mf=Ms*(1+d)
    L=quad(lambda M:kappas2(M)[0]/P(M),Mf,Mi,limit=800,epsabs=0,epsrel=1e-9)[0]
    u=quad(lambda M:1/P(M),Mf,Mi,limit=800,epsabs=0,epsrel=1e-9)[0]
    print("eps_f=%g  Lambda=%.5e  u=%.5e   Lambda*sqrt(eps_f)=%.4f  u*eps_f=%.4f  Lambda/sqrt(u)=%.4f"%(d,L,u,L*np.sqrt(d),u*d,L/np.sqrt(u)))
# astrophysical: 10 Msun, l = l_Planck
Mpl=2.176434e-8; Msun=1.98841e30; Mi=10*Msun/Mpl
print("\n10 Msun, l=l_P: M/l=%.3e  Lambda ~ M^3/(3*C*l)*... with kappa_-=1/l: Lambda=%.3e e-folds ; u_evap=%.3e t_P"%(Mi,15360*np.pi*Mi**3/3,15360*np.pi*Mi**3/3))
