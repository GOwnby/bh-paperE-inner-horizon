"""[Written after the original work; derived from the original e8_semiclassical.py (same inputs and ray integration). See PROVENANCE.md.]
Ratio phi_v^2 / |T^q_vv| at v_flip for the rows of the table of e8_semiclassical.py (Paper E, Sec. 6.8): at the flip the classical source phi_v^2
and the anomaly term hbar kappa_-^2/(192 pi^2 r^2) are comparable but not equal (the definition of v_flip in the text is an estimate).
Same inputs and ray integration as e8_semiclassical.py.   usage: python3 e8_flip_ratio.py gen3_B0.003_k1.5_v300.json [eps ...]
(default eps = 1e-10 1e-8 1e-6 1e-4; about 1-2 min in total)  -> results_e8_flip_ratio.txt"""
import json,sys,os,numpy as np
from scipy.interpolate import CubicSpline
import raylib as R, raylib_sc as RS, analyze, kernel_lib as KL
fn=sys.argv[1]; epss=[float(x) for x in sys.argv[2:]] or [1e-10,1e-8,1e-6,1e-4]
v0=60.; vb=250.; V=3000.; n=2
D=json.load(open(fn)); hs=sorted(D['data'],key=float,reverse=True); vq=np.array(D['vq']); k=D['k']; B=D['B']; km=D['km']
def fld(name):
    arr=[]
    for h in hs:
        d=D['data'][h]; arr.append(np.array(d['rs'][n])*np.exp(-np.array(d['sg'][n])) if name=='Y' else np.array(d[name][n]))
    return analyze.extrap(arr)[-1][0]
F={nm:fld(nm) for nm in ('r','rv','Y','M','sV','PV')}; r,rv,Y=F['r'],F['rv'],F['Y']
ib=int(vb-vq[0]); sVb=np.abs(F['sV']); ex=sVb-km
mm=(vq>=150)&(vq<=vb)&(ex>0); q=-np.polyfit(np.log(vq[mm]),np.log(ex[mm]),1)[0] if mm.sum()>5 else 1.0
vk=np.arange(vb,V+1,1.0); Pk=np.array([KL.phi_v(v,k,B) for v in vk]); ratio=F['PV'][ib]/Pk[0]
Pall=CubicSpline(np.concatenate([vq[:ib+1],vk[1:]]),np.concatenate([F['PV'][:ib+1],ratio*Pk[1:]]))
spl=CubicSpline(vq,F['sV'])
def sV(v): return float(spl(v)) if v<=vb else -(km+ex[ib]*(vb/v)**q)
i0=int(v0-vq[0])
print('%s: k=%g B=%g kappa_-(mu_f)=%.6f'%(fn,k,B,km)); print('eps=hbar/l^2   v_flip   phi_v^2/|T^q_vv| at v_flip   (T^q = eps kappa_-^2/(192 pi^2 r^2), r = r(v_flip))')
for eps in epss:
    sol=RS.integrate_sc(v0,V,r[i0],-rv[i0],np.log(-Y[i0]),sV,Pall,eps)
    vv=np.arange(v0,V,1.0); rho=np.array([sol.sol(x)[1] for x in vv]); neg=np.where(rho<0)[0]
    vf=vv[neg[0]]; rf=sol.sol(vf)[0]
    print('%8.0e   %6.1f   %.4f'%(eps,vf,Pall(vf)**2/(eps*km**2/(192*np.pi**2*rf**2))),flush=True)
