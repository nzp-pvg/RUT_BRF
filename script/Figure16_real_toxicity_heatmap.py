#!/usr/bin/env python3
"""Figure entrypoint: real_toxicity_heatmap.

The final implementation remains in code_final_only/summarize_real_toxic_data.py; this file is the
single per-figure entrypoint used to regenerate the named main-figure output.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "code_final_only" / "summarize_real_toxic_data.py"
EXPECTED = ROOT / "figure" / "Figure16_real_toxicity_heatmap.pdf"

subprocess.run([sys.executable, str(RUNNER)], cwd=ROOT, check=True)
if not EXPECTED.exists():
    raise FileNotFoundError(f"Expected output was not created: {EXPECTED}")
print(f"Created {EXPECTED}")
