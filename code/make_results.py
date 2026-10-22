"""[Modified relative to the original only in the output path of the figure (../fig_ori_classes.png; original: ./fig_ori_classes.png). See PROVENANCE.md.]
Generates all numbers and figures of Paper E. Run: python3 make_results.py  (needs ori_model.py in the same folder)."""
import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from ori_model import Cl, run
out={}
# ---------- (1) RN validation ----------
cl=Cl('rn',Q=0.8); minf,delta,p=1.0,0.05,4.0
rm=cl.rminus(minf); rp=minf+np.sqrt(minf**2-.64); kap=(rp-rm)/(2*rm**2)
rn_sol=run(cl,minf,delta,p,1.0,60,D0=1e-6); sol=rn_sol
def slope(sol,v,h=1e-3): return (np.log(abs(sol.sol(v+h)[1]))-np.log(abs(sol.sol(v-h)[1])))/(2*h)
out['RN']={'kappa':kap,'p':p,'rows':[(v,slope(sol,v),(kap-slope(sol,v))*v) for v in (20,30,40,50,60)]}
vs_=np.linspace(30,60,31); dl_=np.array([slope(sol,v) for v in vs_]); A_=np.vstack([np.ones_like(vs_),1/vs_,1/vs_**2]).T; cf=np.linalg.lstsq(A_,dl_,rcond=None)[0]
out['RN']['fit']={'kappa_fit':float(cf[0]),'c1':float(cf[1])}
vv=np.linspace(2,60,300); rn_M=np.array([sol.sol(v)[1] for v in vv])
# ---------- (2) Hayward-type closures ----------
minf=5.0; res={}
def kappam(cl):
    rm=cl.rminus(minf); return -0.5*cl.Pr(minf,rm)/cl.D(minf,rm)
curves={}
for s,pp in [(-1.0,4.0),(-0.5,4.0),(0.0,4.0),(0.0,3.0),(0.0,6.0)]:  # s=-1,-1/2 run to v=600
    c=Cl('h',ell=1.0,m0=minf,s=s); k=kappam(c)
    sl=run(c,minf,0.25,pp,1.0,600,D0=1e-8,q0=1e-4)
    rows=[(v,float(slope(sl,v)),float(v*slope(sl,v))) for v in (100,200,400,600)]
    res[f's={s:g},p={pp:g}']={'kappa_minus':k,'rows':rows}
    curves[(s,pp)]=(np.linspace(2,600,500),np.array([sl.sol(v)[1] for v in np.linspace(2,600,500)]))
out['Hayward']=res
# saturation coefficient for s=0 : M_sat = kappa R^4 /(6 l^2 |Rdot|)
c=Cl('h',ell=1.0,m0=minf,s=0.0); sl=run(c,minf,0.25,4.0,1.0,600,D0=1e-8,q0=1e-4)
chk=[]
for v in (200,400,600):
    q,M=sl.sol(v); m_=minf-0.25*v**-4; rm=c.rminus(m_); R=rm+q; Rd=0.5*c.f_taylor(m_,rm,q)
    chk.append((v,float(M),float(kappam(c)*R**4/(6*abs(Rd))),float(M/(kappam(c)*R**4/(6*abs(Rd))))))
out['saturation_s0']=chk
# ---------- (3) s>0 : breakdown at the fold ----------
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
brk={}
for s in (1.0,2.0):
    c=Cl('h',ell=1.0,m0=minf,s=s); rows=[]
    for D0 in (1e-6,1e-9,1e-12):
        sol,mm=run_m(c,D0); v=sol.t[-1]; q,m=sol.y[:,-1]; R=c.rminus(mm(v))+q
        rows.append((D0,float(v),float(c.M(m,R)),float(R/2)))
    # analytic fold value M_max(R): s=1 -> sqrt(m0 R^3/(8 l^2))
    brk[f's={s:g}']={'rows':rows}
    if s==1.0: brk['s=1']['analytic_Mmax_at_last_R']=float(np.sqrt(minf*(rows[-1][3]*2)**3/8))
out['fold_breakdown']=brk
json.dump(out,open('results.json','w'),indent=1)
# ---------- figure 1 ----------
fig,ax=plt.subplots(1,3,figsize=(13,3.8))
ax[0].plot(vv[vv>5],[(slope(rn_sol,v)) for v in vv[vv>5]],'k'); ax[0].axhline(kap,ls='--',c='C3',label=r'$\kappa_-$ (exact)')
ax[0].set_xlabel('$v$'); ax[0].set_ylabel(r'$d\ln M_+/dv$'); ax[0].set_title('(a) Reissner–Nordström'); ax[0].legend()
for key,lab,col in [((-1.0,4.0),'$s=-1$','C0'),((-0.5,4.0),'$s=-1/2$','C2'),((0.0,4.0),'$s=0$','C1')]:
    v,M=curves[key]; ax[1].semilogy(v,M,col,label=lab)
ax[1].set_xlabel('$v$'); ax[1].set_ylabel('$M_+$'); ax[1].set_title('(b) closure index $s$ ($p=4$)'); ax[1].legend()
for pp,col in [(3.0,'C4'),(4.0,'C1'),(6.0,'C5')]:
    v,M=curves[(0.0,pp)]; ax[2].loglog(v[v>20],M[v>20],col,label=f'$p={pp:g}$: slope $p+1={pp+1:g}$')
ax[2].set_xticks([30,100,300,600]); ax[2].set_xticklabels(['30','100','300','600']); ax[2].minorticks_off(); ax[2].set_xlabel('$v$'); ax[2].set_ylabel('$M_+$'); ax[2].set_title('(c) $s=0$: late power law'); ax[2].legend(fontsize=8)
plt.tight_layout(); plt.savefig('../fig_ori_classes.png',dpi=160)
print(json.dumps(out,indent=1)[:3500])
