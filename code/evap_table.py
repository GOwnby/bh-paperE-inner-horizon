"""Table of Lambda=int kappa_-/P dM and u=int dM/P in the variable ln(M-M*), plus asymptotes (Paper E, Sec. 5)."""
import io, contextlib, json, numpy as np
from scipy.integrate import quad
with contextlib.redirect_stdout(io.StringIO()):
    import evap_coupling as E
Ms=E.Ms
def I(fun,Mf,Mi):
    g=lambda x: fun(Ms+np.exp(x))*np.exp(x)
    xs=np.linspace(np.log(Mf-Ms),np.log(Mi-Ms),60)
    return sum(quad(g,xs[i],xs[i+1],epsabs=0,epsrel=1e-11,limit=200)[0] for i in range(len(xs)-1))
rows=[]
for Mi in (5.0,20.0,1e3):
    for d in (1e-1,1e-2,1e-3,1e-4,1e-5,1e-6):
        Mf=Ms*(1+d); u=I(lambda M:1/E.P(M),Mf,Mi); L=I(lambda M:E.kappas2(M)[0]/E.P(M),Mf,Mi)
        rows.append((Mi,d,u,L,L/Mi**3)); print("%8g %8g %12.4e %12.4e %9.1f"%rows[-1])
json.dump(rows,open('evap_table.json','w'))
for d in (1e-4,1e-6,1e-8): print("Lambda*sqrt(eps_f)",d,I(lambda M:E.kappas2(M)[0]/E.P(M),Ms*(1+d),2.0)*np.sqrt(d))
