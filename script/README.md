# Figure-organized entrypoints

This folder provides one regeneration entrypoint per main figure. The original final implementations remain unchanged in `../code_final_only`; each entrypoint calls the appropriate final runner, uses the project root as its working directory, and verifies that the expected figure file was created.

## Entry points

- `Figure01`-`Figure10`: use `run_analysis.R`. This shared analysis pipeline regenerates the transcriptomic figures and their supporting result tables in one run; the per-figure files verify their own expected output afterward.
- `Figure11`-`Figure14`: use `run_qpcr_analysis.R` for the blood qPCR figures.
- `Figure15`: use `run_pharmaceuticals_enhancement.py` for candidate prioritization, docking, and ADMET-linked outputs.
- `Figure16`-`Figure17`: use `summarize_real_toxic_data.py` for the downloaded ADMETlab/ProTox toxicity figures.
- `Figure18`: use `postprocess_rutaecarpine_mmp9_md.py` for the existing rutaecarpine-MMP9 MD/docking overlay output. The MD trajectory and topology must already exist.
- `Figure19`-`Figure20`: use `run_framework_priority_analysis.R` for transferability, strategy ranking, and risk-weight robustness.

## Important reproducibility note

The entrypoint organization is intentionally separate from the implementation bundle. Figures sharing a runner share the same upstream analysis and are not reimplemented as duplicated code. This avoids diverging copies of the same statistical workflow while giving each main figure a single user-facing command.

Run an entrypoint from the project root, for example:

```bash
Rscript code_by_figure_v1/Figure11_qpcr_reference_genes.R
python code_by_figure_v1/Figure15_candidate_prioritization.py
```

The expected output mapping is recorded in `MANIFEST.csv`.
