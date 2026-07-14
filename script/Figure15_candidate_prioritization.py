#!/usr/bin/env python3
"""Figure entrypoint: candidate_prioritization.

The final implementation remains in code_final_only/run_pharmaceuticals_enhancement.py; this file is the
single per-figure entrypoint used to regenerate the named main-figure output.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "code_final_only" / "run_pharmaceuticals_enhancement.py"
EXPECTED = ROOT / "figure" / "Figure15_candidate_prioritization.pdf"

subprocess.run([sys.executable, str(RUNNER)], cwd=ROOT, check=True)
if not EXPECTED.exists():
    raise FileNotFoundError(f"Expected output was not created: {EXPECTED}")
print(f"Created {EXPECTED}")
