#!/usr/bin/env python3
"""Figure entrypoint: rutaecarpine_mmp9_md.

The final implementation remains in code_final_only/postprocess_rutaecarpine_mmp9_md.py; this file is the
single per-figure entrypoint used to regenerate the named main-figure output.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "code_final_only" / "postprocess_rutaecarpine_mmp9_md.py"
EXPECTED = ROOT / "figure" / "Figure18_rutaecarpine_mmp9_md_docking_overlay.png"

subprocess.run([sys.executable, str(RUNNER)], cwd=ROOT, check=True)
if not EXPECTED.exists():
    raise FileNotFoundError(f"Expected output was not created: {EXPECTED}")
print(f"Created {EXPECTED}")
