#!/usr/bin/env python3
"""verify.py -- reproduce and check every number of Paper E ("Inner-horizon stability of the Hayward metric").

Normally started through ./verify.sh (which builds the C kernels first):
    bash verify.sh            # quick (default): all cheap generators + analysis of the shipped data of the long jobs
    bash verify.sh --full     # quick + the hours-long regeneration jobs (in a scratch copy, verification/regen/)
    python3 verify.py --list  # list jobs and checks
    python3 verify.py --only text_numbers,e15 --no-checks     # run single jobs

What it does
  1. runs the jobs of JOBS in a SCRATCH COPY of code/ (verification/regen_quick/code; each job = one or more script runs; stdout/stderr go to
     verification/logs/<job>.log). The shipped result files, which are the author's original outputs, are never overwritten: the regenerated
     file is compared with the shipped one (table 'Regenerated output against the shipped version' in REPORT.md) and the checks read the
     regenerated file where a job ran and the shipped file where it did not,
  2. evaluates CHECKS: every number quoted in main.tex that can be computed here, with the paper value, the tolerance and the reason,
  3. writes verification/REPORT.md and verification/checks.json, prints a PASS/FAIL table and a last line  RESULT <repo>: PASSED n/n checks (quick).
Jobs whose Python modules are missing (scipy, sympy) are SKIPPED (printed), the checks that depend on them are SKIPPED too.
Exit status: 0 if no check failed, 1 otherwise.  Nothing outside this directory is read or written (the shipped files of code/ are only read); no network.
"""
import sys
sys.dont_write_bytecode = True
import argparse, concurrent.futures as cf, datetime, importlib.util, json, math, os, platform, re, shutil, subprocess, sys, threading, time
from decimal import Decimal

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = 'bh-paperE-inner-horizon'
CODE = os.path.join(ROOT, 'code')
VER = os.path.join(ROOT, 'verification')
QS = os.path.join(VER, 'regen_quick', 'code')     # scratch copy in which the quick jobs run
PY = sys.executable
LOCK = threading.Lock()


def have(mod):
    try:
        return importlib.util.find_spec(mod) is not None
    except Exception:
        return False


def modver(mod):
    try:
        m = __import__(mod)
        return getattr(m, '__version__', '?')
    except Exception:
        return 'not installed'


# ======================================================================================================== jobs
class Job:
    """runs: list of dict(argv=[script, args...], out=None|file (stdout is written there when rc == 0, relative to cwd), env={})
    where: 'code' (quick, in the scratch copy verification/regen_quick/code) or 'ws' (full, in the scratch copy verification/regen/code)."""

    def __init__(self, id, cwd, runs, needs=(), after=(), outputs=(), est='', desc='', where='code', clib=(), join='', head='', tail=''):
        self.id, self.cwd, self.runs, self.needs, self.after = id, cwd, runs, tuple(needs), tuple(after)
        self.outputs, self.est, self.desc, self.where, self.clib = list(outputs), est, desc, where, tuple(clib)
        self.join, self.head, self.tail = join, head, tail      # layout of a concatenated result file
        self.status = 'PENDING'
        self.wall = self.cpu = 0.0
        self.note = ''
        self.drift = {}


def R1(*argv, out=None, env=None):
    return dict(argv=list(argv), out=out, env=env or {})


G3 = ['gen3_B0.03_k0.5_v300', 'gen3_B0.03_k1.5_v300', 'gen3_B0.03_k2_v300', 'gen3_B0.03_k3_v300',
      'gen3_B0.003_k0.5_v300', 'gen3_B0.003_k1.5_v300', 'gen3_B0.003_k2_v300', 'gen3_B0.003_k3_v300']
LIBS = ('nonlinear/libdouble_null.so', 'eh_init/libdouble_null.so', 'eh_init/libstream.so', 'eh_init/libstream2.so')


def quick_jobs():
    J = []
    A = J.append
    # ---- symbolic (sympy only)
    A(Job('symbolic', '.', [R1('symbolic_checks.py', out='symbolic_checks.log')], needs=['sympy'], outputs=['symbolic_checks.log'], est='5 s',
          desc='sympy: closure identities, field equations dn1-dn3 (all Einstein components), conservation law, ray equations, Kretschmann decomposition, constants'))
    # ---- numpy/scipy only, instant
    A(Job('text_numbers', '.', [R1('text_numbers.py', out='text_numbers.log')], needs=['scipy'], outputs=['text_numbers.json', 'text_numbers.log'], est='5 s',
          desc='regime I/III numbers of Sec. 4, 10 M_sun numbers of Sec. 5, transfer-function gain'))
    A(Job('fold_integrator_scan', '.', [R1('fold_integrator_scan.py', 'all', out='fold_integrator_scan.log')], needs=['scipy'], outputs=['fold_integrator_scan.log'],
          est='3 min', desc='integrator dependence of the D0 = 1e-12 rows of Table fold (LSODA rtol sweep, DOP853, Radau, RK45)'))
    A(Job('make_results', '.', [R1('make_results.py')], needs=['scipy', 'matplotlib'], outputs=['results.json', '../fig_ori_classes.png'], est='1 min',
          desc='Tables validation and fold, Fig. classes (results.json)'))
    A(Job('extra_runs', '.', [R1('extra_runs.py', out='results_extra_runs.txt')], needs=['scipy'], outputs=['results_extra_runs.txt'], est='15 s',
          desc='passage through m = infinity (v = 36.6) and the small-s fold runs'))
    A(Job('evap_table', '.', [R1('evap_table.py')], needs=['scipy'], outputs=['evap_table.json'], est='1 min', desc='Table evap and the M_i = 2 l values of Sec. 5'))
    A(Job('evap_alpha', '.', [R1('evap_alpha.py', out='evap_alpha.log')], needs=['scipy'], outputs=['evap_alpha.log'], est='15 s', desc='alpha = 1.513e-4 and 2 sqrt2/(3 alpha) = 6233'))
    # ---- nonlinear double-null test (needs the C kernel)
    N = 'nonlinear'
    A(Job('nl_validation', N, [R1('run_validation.py')], needs=['scipy'], clib=LIBS[:1], outputs=['validation_nonlinear.json'], est='1 min', desc='static error and Raychaudhuri residual vs h'))
    A(Job('nl_rates', N, [R1('run_rates.py', out='rates.log')], needs=['scipy'], clib=LIBS[:1], outputs=['rates_nonlinear.json', 'rates.log'], est='2 min', desc='d ln|M|/dv: PDE against the Ori model (Table nlrate)'))
    A(Job('nl_curvature', N, [R1('run_curvature.py', out='curv.log')], needs=['scipy'], clib=LIBS[:1], outputs=['curvature_nonlinear.json', 'curv.log'], est='1 min', desc='Kretschmann scalar on the Cauchy horizon (K = 25.7 at v = 20)'))
    A(Job('nl_sign_mech', N, [R1('sign_mech.py', out='sign_mech.log')], needs=['scipy'], clib=LIBS[:1], outputs=['sign_mech.log'], est='10 s', desc='sign of M and of r_u at v = 100'))
    A(Job('nl_sign_ustar', N, [R1('sign_ustar.py', out='sign_ustar.log')], needs=['scipy'], clib=LIBS[:1], outputs=['sign_ustar.log'], est='1 min', desc='u_*(v): the zero of r_u is fixed by v = 30'))
    A(Job('nl_sign_separatrix', N, [R1('sign_separatrix.py', out='sign_separatrix.log')], needs=['scipy'], clib=LIBS[:1], outputs=['sign_separatrix.log'], est='1 min', desc='separatrix of the linear ray equation'))
    A(Job('nl_threshold_h0.08', N, [R1('run_threshold.py', '0.08', out='thr_0.08.log')], needs=['scipy'], clib=LIBS[:1], outputs=['threshold_h0.08.json', 'thr_0.08.log'], est='3 min',
          desc='A_* by bisection and r_inf(A_*-A), h = 0.08 (h = 0.04, 0.02 are in --full; their stored files are analysed)'))
    kf_head = ('# run_kappa_fixedL.py output (fixed domain u1 = v1 = 30, h = 0.1), Paper E Sec. 6.5 control.\n'
               '# Regenerated by verify.py with scipy %s.   python3 run_kappa_fixedL.py 5   (about 2 min)   |   python3 run_kappa_fixedL.py 1.4   (about 1 min)\n' % modver('scipy'))
    A(Job('nl_kappa_fixedL', N, [R1('run_kappa_fixedL.py', '5', out='results_kappa_fixedL.txt'), R1('run_kappa_fixedL.py', '1.4', out='results_kappa_fixedL.txt')], needs=['scipy'], clib=LIBS[:1],
          outputs=['results_kappa_fixedL.txt'], est='3 min', desc='fixed-domain control of the kappa_- scan', head=kf_head,
          tail='# (m_N=1.4: 11 of the 13 distances are listed, two runs were flagged as collapsed and are dropped by the script; A* = 0.0503 at this domain against 0.0497 with the scaled domain.)\n'))
    A(Job('nl_domain_mN1.4', N, [R1('domain_mN1.4.py', out='domain_mN1.4.log')], needs=['scipy'], clib=LIBS[:1], outputs=['domain_mN1.4.log'], est='3 min', desc='A_* for m_N = 1.4, kappa_- u1 = 20 and 40'))
    A(Job('nl_saturation', N, [R1('check_saturation.py', out='check_saturation.log')], needs=['scipy'], clib=LIBS[:1], after=['nl_threshold_h0.08'], outputs=['check_saturation.json', 'check_saturation.log'], est='1 min',
          desc='r_CH(u) saturation at A_*-A = 1e-10 (r_CH(40) vs r_CH(50), r_CH(30) vs r_CH(40))'))
    A(Job('nl_fit_gamma', N, [R1('fit_gamma.py', out='fit_gamma.log')], needs=['numpy'], after=['nl_threshold_h0.08'], outputs=['fit_gamma.log'], est='1 s', desc='threshold exponent and prefactors from threshold_h*.json'))
    A(Job('nl_figure', N, [R1('make_fig_nonlinear.py')], needs=['scipy', 'matplotlib'], clib=LIBS[:1], after=['nl_threshold_h0.08'], outputs=['../../fig_nonlinear.png'], est='1 min', desc='Fig. nl'))
    A(Job('nl_analyze_stored', N, [R1('analyze_stored.py')], needs=['numpy'],
          after=['nl_validation', 'nl_rates', 'nl_curvature', 'nl_sign_mech', 'nl_sign_ustar', 'nl_sign_separatrix', 'nl_threshold_h0.08'],
          outputs=['analyze_stored.json', 'analyze_stored.log'], est='1 s', desc='re-derives the numbers of Sec. 6.1-6.5 from the stored outputs of all (also the long) nonlinear runs'))
    # ---- event-horizon-regular part (Paper G method; the pieces Paper E quotes)
    E = 'eh_init'
    A(Job('eh_field_equations', E, [R1('check_field_equations.py', out='results_check_field_equations.txt')], needs=['numpy'], outputs=['results_check_field_equations.txt'], est='5 s',
          desc='finite-difference Riemann tensor: G_ab - 8 pi T_ab = 0, Kretschmann decomposition'))
    A(Job('eh_conserv', E, [R1('conserv_num.py')], needs=['numpy'], est='2 s', desc='nabla_a T^a_b for the monopole stress tensor (Eq. consT)'))
    A(Job('eh_kernel_smoothing', E, [R1('kernel_smoothing_test.py', out='results_kernel_smoothing.txt')], needs=['scipy'], outputs=['results_kernel_smoothing.txt'], est='1 min',
          desc='sensitivity of the PDE/kernel flux ratio to the Gaussian window'))
    A(Job('eh_e12', E, [R1('e12_ratio.py', out='results_e12_ratio.txt')], needs=['scipy'], outputs=['results_e12_ratio.txt'], est='15 s', desc='PDE/kernel flux ratio to v = 420'))
    A(Job('eh_e11_ratio', E, [R1('e11_ratio.py', out='results_e11_ratio.txt')], needs=['scipy'], outputs=['results_e11_ratio.txt'], est='20 s', desc='PDE/kernel flux ratio vs v (3.5% above the static-hole response at B = 0.03)'))
    A(Job('eh_e15', E, [R1('e15_extend.py', g + '.json', out='results_e15_extend.txt') for g in G3], join='\n', needs=['scipy'], outputs=['results_e15_extend.txt'], est='5 min',
          desc='Table ext: extendibility indicators from the eight five-grid runs'))
    A(Job('eh_e13', E, [R1('e13_all.py', g + '.json', '2') for g in G3], needs=['scipy'], est='6 min', desc='constraint-projected mass, ln K >= ... (ray U = 0.9993)'))
    A(Job('eh_ray_mass', E, [R1('ray_mass.py', 'gen2_B%s_k%s_A0_U1_w0.3_v300.json' % (b, k), out='results_ray_mass_B%s_k%s.txt' % (b, k)) for b in ('0.03', '0.003') for k in ('0.5', '1.5')],
          needs=['scipy'], outputs=['results_ray_mass_B0.03_k0.5.txt', 'results_ray_mass_B0.03_k1.5.txt', 'results_ray_mass_B0.003_k0.5.txt', 'results_ray_mass_B0.003_k1.5.txt'], est='3 min',
          desc='exact ray integration of M against the extrapolated PDE mass (6e-5, 2e-6 to v = 108)'))
    A(Job('eh_ray_extend', E, [R1('ray_extend.py', 'gen3_B0.003_k%s_v300.json' % k, out='results_ray_extend_ext_def_B0.003_k%s.txt' % k) for k in ('0.5', '1.5')],
          needs=['scipy'], outputs=['results_ray_extend_ext_def_B0.003_k0.5.txt', 'results_ray_extend_ext_def_B0.003_k1.5.txt'], est='3 min',
          desc='kernel-driven extension to v = 3000: q_M(2500) = 5.02 (k = 3/2) and 3.01 (k = 1/2)'))
    A(Job('eh_e8_semiclassical', E, [R1('e8_semiclassical.py', 'gen3_B0.003_k1.5_v300.json', out='results_e8_semiclassical.txt')], needs=['scipy'],
          outputs=['results_e8_semiclassical.txt', 'results_e8_semiclassical.json'], est='10 min', desc='anomaly term along the ray: v_flip, r(3000)-r(250), ln|M|(3000)'))
    A(Job('eh_e8_flip_ratio', E, [R1('e8_flip_ratio.py', 'gen3_B0.003_k1.5_v300.json', out='results_e8_flip_ratio.txt')], needs=['scipy'], outputs=['results_e8_flip_ratio.txt'], est='10 min',
          desc='phi_v^2/|T^q_vv| at v_flip'))
    return J


def full_jobs():
    """Long regeneration jobs, run in the scratch copy verification/regen/code (shipped data are never overwritten).  Commands are rebuilt from the
    metadata stored in the shipped JSON files."""
    J = []
    A = J.append
    N, E = 'nonlinear', 'eh_init'
    for h, est in (('0.04', '2 min CPU (measured)'), ('0.02', '~10 min CPU')):
        A(Job('full_threshold_h' + h, N, [R1('run_threshold.py', h, out='thr_%s.log' % h)], needs=['scipy'], clib=LIBS[:1], where='ws', outputs=['threshold_h%s.json' % h], est=est,
              desc='A_* and r_inf(A_*-A), h = %s' % h))
    A(Job('full_domain', N, [R1('run_domain.py', out='dom.log')], needs=['scipy'], clib=LIBS[:1], where='ws', outputs=['domain_nonlinear.json'], est='25 min (original run)', desc='A_* vs u1, r_CH(u) profiles'))
    A(Job('full_supercritical', N, [R1('run_supercritical.py')], needs=['scipy'], clib=LIBS[:1], where='ws', outputs=['supercritical_nonlinear.json'], est='10 min (original run)', desc='locus r = 0.05 above threshold'))
    A(Job('full_universality', N, [R1('run_universality.py', out='univ.log')], needs=['scipy'], clib=LIBS[:1], where='ws', outputs=['universality_nonlinear.json'], est='40 min (original run)', desc='tails k = 1 ... 5/2 and other data families'))
    A(Job('full_checks', N, [R1('run_checks.py', out='checks.log')], needs=['scipy'], clib=LIBS[:1], where='ws', outputs=['checks_nonlinear.json'], est='30 min (original run)', desc='A_*(v1), saturation in v, near-threshold rates, u_*'))
    for mN, est in (('5', '10 min (original run)'), ('3', '10 min (original run)'), ('2', '15 min (original run)'), ('1.6', '25 min (original run)'), ('1.4', '40 min (original run)')):
        A(Job('full_kscan_mN' + mN, N, [R1('run_kappa_scan.py', mN, out='kscan_%s.log' % ('%.1f' % float(mN)))], needs=['scipy'], clib=LIBS[:1], where='ws', outputs=['kscan_mN%s.json' % mN], est=est, desc='kappa_- scan, m_N = %s' % mN))
    A(Job('full_sign_scan', N, [R1('sign_scan.py', out='sign_scan.log')], needs=['scipy'], clib=LIBS[:1], where='ws', outputs=['sign_scan.log'], est='60 min (original run)', desc='17 (A, B, h) runs for the sign mechanism'))
    meta = {  # name -> (B, k, A, U0, w, v1, grids)
        'gen3_B0.03_k1.5_v110': ('0.03', '1.5', '0', '1', '0.3', '110', ['0.05', '0.025', '0.0125', '0.00625'], '2 min CPU (measured)'),
        'gen3_B0.003_k1.5_v450': ('0.003', '1.5', '0', '1', '0.3', '450', ['0.05', '0.025', '0.0125', '0.00625'], '~20 min CPU'),
    }
    for g in G3:
        m = re.match(r'gen3_B([\d.]+)_k([\d.]+)_v300', g)
        meta[g] = (m.group(1), m.group(2), '0', '1', '0.3', '300', ['0.05', '0.025', '0.0125', '0.00625', '0.003125'], '53 min CPU (measured)')
    for g, (B, k, Aa, U0, w, v1, hs, est) in meta.items():
        A(Job('full_' + g, E, [R1('gen3.py', B, k, Aa, U0, w, v1, *hs)], needs=['scipy'], clib=LIBS[2:], where='ws', outputs=[g + '.json'], est=est, desc='five-grid event-horizon-regular run (%s)' % g))
    # analysis of the regenerated data (same scripts as in the quick run)
    gens = ['full_' + g for g in G3] + ['full_gen3_B0.003_k1.5_v450']
    A(Job('full_eh_e15', E, [R1('e15_extend.py', g + '.json', out='results_e15_extend.txt') for g in G3], join='\n', needs=['scipy'], where='ws', after=gens, outputs=['results_e15_extend.txt'], est='20 s CPU', desc='Table ext from the regenerated runs'))
    A(Job('full_eh_e13', E, [R1('e13_all.py', g + '.json', '2') for g in G3], needs=['scipy'], where='ws', after=gens, est='1 min CPU', desc='projected mass and ln K from the regenerated runs'))
    A(Job('full_eh_e12', E, [R1('e12_ratio.py', out='results_e12_ratio.txt')], needs=['scipy'], where='ws', after=gens, outputs=['results_e12_ratio.txt'], est='15 s', desc='flux ratio to v = 420 from the regenerated v1 = 450 run'))
    A(Job('full_eh_flip', E, [R1('e8_flip_ratio.py', 'gen3_B0.003_k1.5_v300.json', out='results_e8_flip_ratio.txt')], needs=['scipy'], where='ws', after=gens, outputs=['results_e8_flip_ratio.txt'], est='1 min CPU', desc='flip ratios from the regenerated run'))
    A(Job('full_eh_ray_extend', E, [R1('ray_extend.py', 'gen3_B0.003_k%s_v300.json' % k, out='results_ray_extend_ext_def_B0.003_k%s.txt' % k) for k in ('0.5', '1.5')], needs=['scipy'], where='ws', after=gens,
          outputs=['results_ray_extend_ext_def_B0.003_k0.5.txt', 'results_ray_extend_ext_def_B0.003_k1.5.txt'], est='2.5 min CPU', desc='q_M(2500) from the regenerated runs'))
    A(Job('full_nl_analyze_stored', N, [R1('analyze_stored.py')], needs=['numpy'], where='ws', after=[j.id for j in J if j.id.startswith('full_') and j.cwd == N], outputs=['analyze_stored.json'], est='1 s',
          desc='Sec. 6.1-6.5 numbers from the regenerated nonlinear data'))
    return J


# ======================================================================================================== job execution
def run_job(job, root, logdir, py_extra=()):
    """returns (rc, wall, cpu). Writes logdir/<id>.log; refreshes the stdout result files."""
    t0 = time.time()
    cpu = 0.0
    cwd = os.path.join(root, job.cwd)
    sections, rc_all = [], 0
    outs = []
    for k, run in enumerate(job.runs):
        argv = [PY, '-B'] + run['argv']
        env = dict(os.environ)
        env.update({'PYTHONDONTWRITEBYTECODE': '1', 'MPLBACKEND': 'Agg', 'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1'})
        env.update(run['env'])
        import tempfile
        with tempfile.TemporaryFile() as fo, tempfile.TemporaryFile() as fe:
            p = subprocess.Popen(argv, cwd=cwd, stdout=fo, stderr=fe, env=env)
            _, status, ru = os.wait4(p.pid, 0)
            rc = os.waitstatus_to_exitcode(status)
            fo.seek(0); fe.seek(0)
            so, se = fo.read().decode('utf-8', 'replace'), fe.read().decode('utf-8', 'replace')
        cpu += ru.ru_utime + ru.ru_stime
        sections.append('### RUN %d  (cwd %s)  %s\n### rc=%d  cpu=%.1fs\n----- stdout -----\n%s\n----- stderr -----\n%s\n' % (k, job.cwd, ' '.join(run['argv']), rc, ru.ru_utime + ru.ru_stime, so, se))
        outs.append((run, rc, so))
        if rc != 0:
            rc_all = rc
    wall = time.time() - t0
    # result files: written only when every run succeeded; several runs with the same target are concatenated (job.join between them)
    if rc_all == 0:
        targets = {}
        for run, rc, so in outs:
            if run['out']:
                targets.setdefault(run['out'], []).append(so)
        for fn, parts in targets.items():
            _atomic_write(os.path.join(cwd, fn), job.head + job.join.join(parts) + job.tail)
    os.makedirs(logdir, exist_ok=True)
    hdr = 'job %s  (%s)\nstarted %s\nwall %.1f s   cpu %.1f s   rc %d\n\n' % (job.id, job.desc, datetime.datetime.fromtimestamp(t0).strftime('%Y-%m-%d %H:%M:%S'), wall, cpu, rc_all)
    _atomic_write(os.path.join(logdir, job.id + '.log'), hdr + '\n'.join(sections))
    return rc_all, wall, cpu


def _atomic_write(path, text):
    tmp = path + '.tmp_verify'
    with open(tmp, 'w', newline='\n') as f:
        f.write(text)
    os.replace(tmp, path)


def snapshot(job, root):
    snap = {}
    for o in job.outputs:
        p = os.path.normpath(os.path.join(root, job.cwd, o))
        if os.path.isfile(p) and not p.endswith(('.png', '.npz')):
            with open(p, 'rb') as f:
                snap[o] = f.read()
    return snap


_FL = re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?')


def numeric_drift(old, new):
    """maximum relative difference of the numbers of two text/JSON files with the same layout.  The scale below which a pair is ignored is
    1e-9 times the largest |number| ON THE SAME LINE (not in the whole file, which hid all small entries of files that also contain huge numbers);
    pairs that are both exactly 0 are equal.  Informational: it is reported, not thresholded."""
    la, lb = old.decode('utf-8', 'replace').split('\n'), new.decode('utf-8', 'replace').split('\n')
    a = [[float(x) for x in _FL.findall(l)] for l in la]
    b = [[float(x) for x in _FL.findall(l)] for l in lb]
    na, nb = [x for x in a if x], [x for x in b if x]
    if len(na) != len(nb) or any(len(x) != len(y) for x, y in zip(na, nb)):
        return None
    worst = 0.0
    for xs, ys in zip(na, nb):
        scale = max(max(abs(x) for x in xs), max(abs(y) for y in ys), 1e-300)
        for x, y in zip(xs, ys):
            m = max(abs(x), abs(y))
            if m < 1e-9 * scale or m == 0:
                continue
            worst = max(worst, abs(x - y) / m)
    return worst


def schedule(jobs, root_of, logdir_of, nworkers, only=None, log=print):
    """runs the jobs respecting 'after' dependencies; returns nothing (job.status etc. are set)."""
    byid = {j.id: j for j in jobs}
    pending = [j for j in jobs if (only is None or j.id in only)]
    done = set()
    running = {}
    ex = cf.ThreadPoolExecutor(max_workers=nworkers)

    def ready(j):
        return all((d in done) or (d not in byid) or (only is not None and d not in only) or byid[d].status in ('SKIPPED',) for d in j.after)

    def work(j):
        root = root_of(j)
        snap = snapshot(j, root)
        rc, wall, cpu = run_job(j, root, logdir_of(j))
        j.wall, j.cpu = wall, cpu
        j.status = 'OK' if rc == 0 else 'FAILED'
        if rc != 0:
            j.note = 'rc=%d (see %s)' % (rc, os.path.relpath(os.path.join(logdir_of(j), j.id + '.log'), ROOT))
        for o, old in snap.items():
            p = os.path.normpath(os.path.join(root, j.cwd, o))
            if os.path.isfile(p):
                with open(p, 'rb') as f:
                    new = f.read()
                d = numeric_drift(old, new) if old != new else 0.0
                j.drift[o] = d
        return j

    while pending or running:
        started = False
        for j in list(pending):
            miss = [m for m in j.needs if not have(m)]
            clib = [c for c in j.clib if not os.path.isfile(os.path.join(root_of(j), c))]
            if miss or clib:
                j.status = 'SKIPPED'
                j.note = ('python module(s) not installed: ' + ', '.join(miss)) if miss else ('C library missing: ' + ', '.join(clib) + ' (gcc/make?)')
                if j.outputs and miss:
                    j.note += '; the stored output (%s) is used by the checks' % ', '.join(j.outputs[:2])
                log('  SKIPPED %-22s %s' % (j.id, j.note))
                os.makedirs(logdir_of(j), exist_ok=True)
                _atomic_write(os.path.join(logdir_of(j), j.id + '.log'), 'job %s  (%s)\nSKIPPED in this run: %s\n(no script was executed; the shipped result file(s) %s were read by the checks)\n' % (j.id, j.desc, j.note, ', '.join(j.outputs) or '-'))
                pending.remove(j)
                done.add(j.id)
                continue
            if len(running) < nworkers and ready(j):
                log('  start   %-22s (est. %s) %s' % (j.id, j.est, j.desc))
                running[ex.submit(work, j)] = j
                pending.remove(j)
                started = True
        if running:
            fin, _ = cf.wait(list(running), timeout=1.0, return_when=cf.FIRST_COMPLETED)
            for f in fin:
                j = running.pop(f)
                try:
                    f.result()
                except Exception as e:      # noqa
                    j.status = 'FAILED'
                    j.note = 'exception: %r' % (e,)
                done.add(j.id)
                log('  %-7s %-22s wall %7.1f s  cpu %7.1f s %s' % (j.status, j.id, j.wall, j.cpu, ('  ' + j.note) if j.note else ''))
        elif pending and not started:
            for j in pending:       # unsatisfiable dependency
                j.status = 'FAILED'
                j.note = 'dependency never ran'
            break
    ex.shutdown()


# ======================================================================================================== checks
class Ctx:
    """access to the generated/stored files, relative to a code tree (CODE for quick checks, the scratch copy for the full variants)"""

    def __init__(self, root, logdir):
        self.root, self.logdir = root, logdir
        self._c = {}

    def p(self, rel):
        return os.path.join(self.root, rel)

    def text(self, rel):
        if rel not in self._c:
            with open(self.p(rel), errors='replace') as f:
                self._c[rel] = f.read()
        return self._c[rel]

    def json(self, rel):
        key = 'json:' + rel
        if key not in self._c:
            with open(self.p(rel)) as f:
                self._c[key] = json.load(f)
        return self._c[key]

    def A(self, key):
        return self.json('nonlinear/analyze_stored.json')[key]

    def TN(self, key):
        return self.json('text_numbers.json')[key]

    def runout(self, job, k=0):
        """stdout of the k-th run of a job (from its log)"""
        t = open(os.path.join(self.logdir, job + '.log'), errors='replace').read()
        secs = re.split(r'^### RUN (\d+) ', t, flags=re.M)
        for i in range(1, len(secs), 2):
            if int(secs[i]) == k:
                body = secs[i + 1]
                return body.split('----- stdout -----\n', 1)[1].split('----- stderr -----', 1)[0]
        raise KeyError('run %d of %s' % (k, job))

    def rx(self, text, pattern, group=1, nth=0):
        m = list(re.finditer(pattern, text, re.M))
        if len(m) <= nth:
            raise KeyError('pattern %r not found (%d matches)' % (pattern, len(m)))
        return float(m[nth].group(group))


class Check:
    def __init__(self, id, where, paper, get, kind='digits', tol=None, reason='', src=(), full=False, old=None, quantity=''):
        self.id, self.where, self.paper, self.get, self.kind, self.tol, self.reason = id, where, paper, get, kind, tol, reason
        self.src, self.full, self.old, self.quantity = tuple(src), full, old, quantity
        self.status, self.value, self.msg, self.extra = 'PENDING', None, '', ''


def _digits(s):
    d = Decimal(str(s))
    return float(d), float(Decimal(1).scaleb(d.as_tuple().exponent))


def evaluate(ch, val):
    """returns (ok, tol_text)"""
    k, p, t = ch.kind, ch.paper, ch.tol
    if k == 'digits':
        pv, unit = _digits(p)
        slack = t if t else 1.0          # tol = multiple of the half unit of the last quoted digit
        return abs(val - pv) <= 0.5 * unit * slack * (1 + 1e-9) + 1e-300, '%g (half unit of the last quoted digit%s)' % (0.5 * unit * slack, '' if slack == 1 else ' x %g' % slack)
    if k == 'rel':
        pv = float(p)
        return abs(val - pv) <= t * abs(pv), 'rel %g' % t
    if k == 'abs':
        pv = float(p)
        return abs(val - pv) <= t, 'abs %g' % t
    if k == 'le':
        pv = float(p)
        return val <= pv * (1 + (t or 0)), '<= %g' % (pv * (1 + (t or 0)))
    if k == 'ge':
        pv = float(p)
        return val >= pv * (1 - (t or 0)), '>= %g' % (pv * (1 - (t or 0)))
    if k == 'range':
        lo, hi = p
        e = t or 0.0
        return lo - e <= val <= hi + e, '[%g, %g] +- %g' % (lo, hi, e)
    if k == 'bool':
        return bool(val) == (p if isinstance(p, bool) else str(p) == 'True'), 'exact'
    if k == 'eq':
        try:
            return float(val) == float(p), 'exact'
        except (TypeError, ValueError):
            return str(val) == str(p), 'exact'
    raise ValueError(k)


def run_checks(checks, ctx_for, jobs_by_id, selected_full):
    out = []
    for ch in checks:
        if ch.full and not selected_full:
            continue
        ctx = ctx_for(ch)
        notes = []
        for sj in ch.src:
            st = jobs_by_id[sj].status if sj in jobs_by_id else 'PENDING'
            if st == 'SKIPPED':
                notes.append('stored output used (job %s skipped: %s)' % (sj, jobs_by_id[sj].note))
            elif st == 'FAILED':
                notes.append('job %s FAILED, stored output used' % sj)
        ch.extra = '; '.join(sorted(set(notes)))
        try:
            val = ch.get(ctx)
        except FileNotFoundError as e:
            ch.status, ch.msg = ('SKIPPED', 'file missing: %s' % e.filename) if ch.src else ('FAIL', 'file missing: %s' % e.filename)
            out.append(ch)
            continue
        except Exception as e:      # noqa
            ch.status, ch.msg = 'FAIL', 'could not evaluate: %r' % (e,)
            out.append(ch)
            continue
        ch.value = val
        try:
            ok, tt = evaluate(ch, val)
        except Exception as e:      # noqa
            ok, tt = False, 'error %r' % (e,)
        ch.status = 'PASS' if ok else 'FAIL'
        ch.msg = tt
        out.append(ch)
    return out


def fmt(v):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, (int,)):
        return str(v)
    if isinstance(v, float):
        if v == 0:
            return '0'
        if 1e-3 <= abs(v) < 1e5:
            return '%.6g' % v
        return '%.5e' % v
    return str(v)


# the check table lives in a second file to keep this one readable
sys.path.insert(0, os.path.join(ROOT, 'verification'))


def load_checks():
    import expected
    return expected.build(Check)


# ======================================================================================================== report
def write_report(args, jobs, checks, mode, tstart, wall_total):
    lines = []
    A = lines.append
    npass = sum(c.status == 'PASS' for c in checks)
    nfail = sum(c.status == 'FAIL' for c in checks)
    nskip = sum(c.status == 'SKIPPED' for c in checks)
    ntot = npass + nfail
    A('# Verification report -- Paper E (%s)' % REPO)
    A('')
    A('Mode: **%s**.  Result: **%d / %d checks passed**%s%s.' % (mode, npass, ntot, (', %d FAILED' % nfail) if nfail else '', (', %d SKIPPED (missing Python modules, see below)' % nskip) if nskip else ''))
    A('')
    A('## Environment')
    A('')
    try:
        gcc = subprocess.run([os.environ.get('CC', 'gcc'), '--version'], capture_output=True, text=True).stdout.splitlines()[0]
    except Exception:
        gcc = 'not found'
    A('| item | value |')
    A('|---|---|')
    A('| date | %s |' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    A('| platform | %s |' % platform.platform())
    A('| python | %s |' % sys.version.split()[0])
    for m in ('numpy', 'scipy', 'sympy', 'mpmath', 'matplotlib'):
        A('| %s | %s |' % (m, modver(m)))
    A('| gcc | %s |' % gcc)
    A('| cpus | %s |' % os.cpu_count())
    A('| total wall time | %.0f s (%.1f min) |' % (wall_total, wall_total / 60))
    A('')
    A('## Jobs')
    A('')
    A('| job | status | wall [s] | cpu [s] | what | log |')
    A('|---|---|---:|---:|---|---|')
    for j in jobs:
        if j.status == 'PENDING':
            continue
        A('| `%s` | %s | %.1f | %.1f | %s%s | `verification/logs%s/%s.log` |' % (j.id, j.status, j.wall, j.cpu, j.desc, (' -- ' + j.note) if j.note else '', '_full' if j.where == 'ws' else '', j.id))
    A('')
    drifts = [(j, o, d) for j in jobs for o, d in j.drift.items()]
    if drifts:
        A('## Regenerated output (scratch copy) against the SHIPPED version (the author\'s original output, never overwritten)')
        A('')
        A('Maximum relative difference of the numbers in the file (a number is ignored only if it is below 1e-9 of the largest number on its own line); `None` = layout changed (e.g. timing lines of the original log).  0 = bit-identical.  Informational; differences at the 1e-6 level in near-threshold scans are platform noise (see PROVENANCE.md).')
        A('')
        A('| job | file | max rel. difference |')
        A('|---|---|---:|')
        for j, o, d in drifts:
            A('| `%s` | `%s` | %s |' % (j.id, o, 'None' if d is None else ('%.1e' % d if d else '0')))
        A('')
    A('## Checks (paper value against computed value)')
    A('')
    A('`digits` tolerance = half a unit of the last digit quoted in the paper; other tolerances and their reasons are given in the table. `where` = section of `main.tex`.')
    A('A note `text now: ...` marks a number whose current wording in `main.tex` differs from the value tested here (proposed correction, see the final report).')
    A('')
    A('| id | where | quantity | paper | computed | tolerance | status | note |')
    A('|---|---|---|---|---|---|---|---|')
    for c in checks:
        pv = c.paper if isinstance(c.paper, str) else (('[%g, %g]' % c.paper) if isinstance(c.paper, tuple) else str(c.paper))
        note = c.reason
        if c.old:
            note = (note + '; ' if note else '') + 'text now: ' + c.old
        if c.status in ('SKIPPED', 'FAIL') and c.msg:
            note = (note + '; ' if note else '') + c.msg
        if c.extra:
            note = (note + '; ' if note else '') + c.extra
        A('| %s | %s | %s | %s | %s | %s | **%s** | %s |' % (c.id, c.where, c.quantity, pv, fmt(c.value) if c.value is not None else '--', c.msg if c.status == 'PASS' else '', c.status, note.replace('|', '/')))
    A('')
    return '\n'.join(lines) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--quick', action='store_true', help='default')
    g.add_argument('--full', action='store_true', help='also run the long regeneration jobs in verification/regen/')
    ap.add_argument('--jobs', type=int, default=0, help='parallel jobs (default min(2, cpus))')
    ap.add_argument('--only', default='', help='comma-separated job ids (no check evaluation unless --checks)')
    ap.add_argument('--no-checks', action='store_true')
    ap.add_argument('--checks-only', action='store_true', help='do not run jobs, evaluate the checks on the files present')
    ap.add_argument('--list', action='store_true')
    args = ap.parse_args()
    full = args.full
    mode = 'full' if full else 'quick'
    nworkers = args.jobs or max(1, min(2, os.cpu_count() or 1))
    qjobs = quick_jobs()
    fjobs = full_jobs() if full else []
    if args.list:
        for j in qjobs + full_jobs():
            print('%-26s %-5s est %-7s needs %-18s %s' % (j.id, 'ws' if j.where == 'ws' else 'code', j.est, ','.join(j.needs), j.desc))
        checks = load_checks()
        print('%d checks' % len(checks))
        return 0
    tstart = time.time()
    os.makedirs(os.path.join(VER, 'logs'), exist_ok=True)
    WS = os.path.join(VER, 'regen', 'code')
    only = set(x for x in args.only.split(',') if x) or None
    say = lambda s: (print(s, flush=True))
    say('verify.py (%s) in %s' % (mode, ROOT))
    say('python %s, numpy %s, scipy %s, sympy %s, mpmath %s, matplotlib %s' % (sys.version.split()[0], modver('numpy'), modver('scipy'), modver('sympy'), modver('mpmath'), modver('matplotlib')))
    jobs = qjobs + fjobs
    if not args.checks_only:
        say('-- quick jobs (%d workers)' % nworkers)
        if not only or not os.path.isdir(QS):
            say('-- preparing the scratch copy %s (the shipped files are not modified)' % os.path.relpath(QS, ROOT))
            prepare_ws(QS)
        schedule(qjobs, lambda j: QS, lambda j: os.path.join(VER, 'logs'), nworkers, only, log=say)
        if full:
            say('-- full: preparing the scratch copy %s' % os.path.relpath(WS, ROOT))
            prepare_ws(WS)
            say('-- full jobs (%d workers); expected durations are listed in the table below' % nworkers)
            schedule(fjobs, lambda j: WS, lambda j: os.path.join(VER, 'logs_full'), nworkers, only, log=say)
        if not only:
            _atomic_write(os.path.join(VER, 'jobs.json'), json.dumps(dict(mode=mode, wall=time.time() - tstart, jobs=[dict(id=j.id, status=j.status, wall=j.wall, cpu=j.cpu, note=j.note, drift=j.drift) for j in jobs]), indent=1))
    else:
        # --checks-only: take the job table (status, times, drift) of the last real run
        prev = {}
        try:
            with open(os.path.join(VER, 'jobs.json')) as f:
                prev = json.load(f)
        except Exception:
            pass
        pj = {d['id']: d for d in prev.get('jobs', [])}
        for j in jobs:
            d = pj.get(j.id)
            if d:
                j.status, j.wall, j.cpu, j.note, j.drift = d['status'], d['wall'], d['cpu'], d['note'], d['drift']
            else:
                j.status = 'OK'
        tstart = time.time() - prev.get('wall', 0.0)
    # ---- checks
    checks = []
    if not args.no_checks and not only:
        allchecks = load_checks()
        byid = {j.id: j for j in jobs}
        ctx_q = Ctx(QS if os.path.isdir(QS) else CODE, os.path.join(VER, 'logs'))
        ctx_f = Ctx(WS, os.path.join(VER, 'logs_full'))
        checks = run_checks(allchecks, lambda c: ctx_f if c.full else ctx_q, byid, full)
    wall = time.time() - tstart
    npass = sum(c.status == 'PASS' for c in checks)
    nfail = sum(c.status == 'FAIL' for c in checks)
    nskip = sum(c.status == 'SKIPPED' for c in checks)
    jfail = [j for j in jobs if j.status == 'FAILED']
    if checks or args.checks_only:
        report = write_report(args, jobs, checks, mode, tstart, wall)
        _atomic_write(os.path.join(VER, 'REPORT.md'), report)
        _atomic_write(os.path.join(VER, 'checks.json'), json.dumps([dict(id=c.id, where=c.where, quantity=c.quantity, paper=c.paper, computed=c.value, kind=c.kind, tolerance=c.msg if c.status == 'PASS' else None,
                                                                         reason=c.reason, status=c.status, text_now=c.old) for c in checks], indent=1, default=str))
        say('')
        say('%-6s %-8s %-52s %-14s %-14s %s' % ('status', 'id', 'quantity', 'paper', 'computed', 'where'))
        for c in checks:
            if c.status == 'FAIL':
                say('FAIL   %-9s %-52s paper %-14s computed %-14s %s %s' % (c.id, c.quantity[:52], str(c.paper)[:14], fmt(c.value)[:14] if c.value is not None else '--', c.where, c.msg))
        sk = [c for c in checks if c.status == 'SKIPPED']
        if sk:
            say('SKIPPED %d checks (file missing or job not run), e.g. %s' % (len(sk), ', '.join(c.id for c in sk[:6])))
        say('')
        say('checks: %d passed, %d failed, %d skipped; jobs failed: %d; wall %.0f s.  Report: verification/REPORT.md' % (npass, nfail, nskip, len(jfail), wall))
    ntot = npass + nfail
    status = 'PASSED' if (nfail == 0 and not jfail and ntot > 0) else 'FAILED'
    extra = ''
    if nskip:
        extra = '; %d further checks SKIPPED (missing Python modules)' % nskip
    if jfail:
        extra += '; jobs failed: ' + ','.join(j.id for j in jfail)
    say('RESULT %s: %s %d/%d checks (%s%s)' % (REPO, status, npass, ntot, mode, extra))
    return 0 if status == 'PASSED' else 1


def prepare_ws(ws):
    """scratch copy of code/ (sources, data and the built libraries) for the quick jobs (verification/regen_quick/) and the full jobs (verification/regen/); regenerated every time"""
    if os.path.isdir(ws):
        shutil.rmtree(ws)
    ig = shutil.ignore_patterns('__pycache__', '*.pyc', '*.tmp_verify')
    shutil.copytree(CODE, ws, ignore=ig)


if __name__ == '__main__':
    sys.exit(main())
