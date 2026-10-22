"""[Written after the original work; no counterpart in the author's archive (Zenodo v1.0.1). See PROVENANCE.md.]
Sensitivity of the interior linear-response kernel to the Gaussian smoothing of the Fourier inversion (Paper E, Sec. 6.8 / Paper G).
kernel_analytic.py and kernel_lib.py use K(tau) = (1/pi) Re sum_w exp(-i w tau) T(w) exp(-w^2 s2/2) dw with s2 = 0.5, a numerical choice that
suppresses the Gibbs oscillation of the truncated inversion (the cut-off is w = 6); it makes the kernel slightly acausal.  Here s2 = 0, 0.25, 0.5, 1
are compared through the ratio (PDE flux phi_v on U~1)/(kernel flux) for B=0.003, k=3/2 at v = 60, 100, 200, 290.
Needs gen_B0.003_k1.5_A0_U1_w0.3_v300.json (shipped).  usage: python3 kernel_smoothing_test.py   (about 10 s) -> results_kernel_smoothing.txt"""
import json, numpy as np, analyze, warnings, transfer_vec as TV
warnings.filterwarnings('ignore')
kp = TV.kp; R1 = 0.64423
dw = 0.004; ws = np.arange(dw/2, 6.0, dw); T, _ = TV.Tvec(ws, ds=0.002)
tau = np.arange(-12, 160.5, 0.5); ph = np.exp(-1j*np.outer(tau, ws)); Bp = 0.003
L = json.load(open('gen_B0.003_k1.5_A0_U1_w0.3_v300.json')); hl = sorted(L['data'], key=float, reverse=True); vl = np.array(L['vq'])
P = analyze.extrap([np.array(L['data'][h]['PV'][2]) for h in hl])[-1][0]
print('ratio PDE/kernel for the smoothing variance s2 (s2 = 0.5 is the value used in kernel_lib.py)')
for s2 in (0.0, 0.25, 0.5, 1.0):
    Kt = (1/np.pi)*np.real((ph*(T*np.exp(-ws**2*s2/2))).sum(1))*dw
    m = (tau >= 60) & (tau <= 120); y = Kt[m]*np.exp(kp*tau[m])/R1 - 1; X = np.vstack([np.exp(-kp*tau[m]), np.exp(-2*kp*tau[m])]).T
    (a, b), *_ = np.linalg.lstsq(X, y, rcond=None)
    def Kf(t_):
        t_ = np.asarray(t_, float); out = np.interp(t_, tau, Kt, left=0.0); tail = R1*np.exp(-kp*t_)*(1+a*np.exp(-kp*t_)+b*np.exp(-2*kp*t_)); return np.where(t_ > 120, tail, out)
    def pred(v, k=1.5):
        vp = np.concatenate([np.linspace(0, min(v, 60), 24001), np.linspace(min(v, 60), v+12, 100001)[1:]])
        return np.trapezoid(Kf(v-vp)*(-k*Bp*(1+vp)**(-k-1)), vp)
    print('s2 = %4.2f   v = 60, 100, 200, 290:' % s2, ['%.5f' % (P[int(v-vl[0])]/pred(v)) for v in (60, 100, 200, 290)], flush=True)
