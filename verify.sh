#!/usr/bin/env bash
# verify.sh [--quick|--full] [--jobs N]
#   --quick (default): builds the C kernels, runs every cheap generator of the paper, analyses the shipped data of the long runs and compares
#                      ~600 numbers with the numbers quoted in main.tex (about 15 min on two cores; see verification/REPORT.md for measured times).
#   --full           : additionally re-runs the hours-long jobs (five-grid PDE runs, threshold scans, ...) in a scratch copy verification/regen/ (several hours).
# Needs Python >= 3.10 with numpy >= 2, scipy >= 1.11, sympy, mpmath, matplotlib, and gcc + make. Works on Linux, WSL and macOS; no network access.
# Choose the interpreter with  PYTHON=/path/to/python3 bash verify.sh.   The last line printed is  RESULT <repo>: PASSED n/n checks (quick|full).
set -u
cd "$(dirname "$0")" || exit 2
PYTHON="${PYTHON:-python3}"
if ! command -v "$PYTHON" >/dev/null 2>&1; then echo "verify.sh: $PYTHON not found (set PYTHON=...)" >&2; exit 2; fi
if ! "$PYTHON" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then echo "verify.sh: Python >= 3.10 is required" >&2; exit 2; fi
if ! "$PYTHON" -c 'import numpy' 2>/dev/null; then echo "verify.sh: numpy is not installed (pip install -r requirements.txt)" >&2; exit 2; fi
CC="${CC:-gcc}"
if command -v make >/dev/null 2>&1 && command -v "$CC" >/dev/null 2>&1; then
    make -C code -s CC="$CC" all || echo "verify.sh: WARNING: building the C kernels failed; the jobs that need them will be SKIPPED" >&2
else
    echo "verify.sh: make or $CC not found; the C kernels are not built, the jobs that need them will be SKIPPED" >&2
fi
export PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg
exec "$PYTHON" -B verify.py "$@"
