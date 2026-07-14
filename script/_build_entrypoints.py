from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "code_by_figure_v1"


FIGURES = {
    1: ("transcriptomic_baseline", "R", "run_analysis.R", "Figure1_volcano_panels.pdf"),
    2: ("consensus_and_target_network", "R", "run_analysis.R", "Figure2_consensus_heatmap_gse43292.pdf"),
    3: ("compound_gene_network", "R", "run_analysis.R", "Figure3_compound_gene_network.pdf"),
    4: ("benefit_risk_prioritization", "R", "run_analysis.R", "Figure4_compound_scores.pdf"),
    5: ("go_enrichment", "R", "run_analysis.R", "Figure5_enrichment.pdf"),
    6: ("external_validation", "R", "run_analysis.R", "Figure6_external_validation.pdf"),
    7: ("compact_signature", "R", "run_analysis.R", "Figure7_signature_model.pdf"),
    8: ("pathway_cell_context", "R", "run_analysis.R", "Figure8_pathway_cellscape.pdf"),
    9: ("model_benchmark", "R", "run_analysis.R", "Figure9_benchmark_models.pdf"),
    10: ("benchmark_roc_overlay", "R", "run_analysis.R", "Figure10_benchmark_roc_overlay.pdf"),
    11: ("qpcr_reference_genes", "R", "run_qpcr_analysis.R", "Figure11_reference_gene_stability.pdf"),
    12: ("qpcr_gene_panels", "R", "run_qpcr_analysis.R", "Figure12_qpcr_gene_panels.pdf"),
    13: ("qpcr_heatmap", "R", "run_qpcr_analysis.R", "Figure13_qpcr_heatmap.pdf"),
    14: ("qpcr_blood_scores", "R", "run_qpcr_analysis.R", "Figure14_qpcr_blood_scores.pdf"),
    15: ("candidate_prioritization", "PY", "run_pharmaceuticals_enhancement.py", "Figure15_candidate_prioritization.pdf"),
    16: ("real_toxicity_heatmap", "PY", "summarize_real_toxic_data.py", "Figure16_real_toxicity_heatmap.pdf"),
    17: ("real_candidate_priority", "PY", "summarize_real_toxic_data.py", "Figure17_real_candidate_priority_summary.pdf"),
    18: ("rutaecarpine_mmp9_md", "PY", "postprocess_rutaecarpine_mmp9_md.py", "Figure18_rutaecarpine_mmp9_md_docking_overlay.png"),
    19: ("framework_transferability_and_strategy", "R", "run_framework_priority_analysis.R", "Figure19_framework_transferability_auc_heatmap.png"),
    20: ("ranking_robustness", "R", "run_framework_priority_analysis.R", "Figure20_ranking_robustness_weight_heatmap.png"),
}


def py_entry(name: str, runner: str, output: str) -> str:
    return f'''#!/usr/bin/env python3
"""Figure entrypoint: {name}.

The final implementation remains in code_final_only/{runner}; this file is the
single per-figure entrypoint used to regenerate the named main-figure output.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "code_final_only" / "{runner}"
EXPECTED = ROOT / "figure" / "{output}"

subprocess.run([sys.executable, str(RUNNER)], cwd=ROOT, check=True)
if not EXPECTED.exists():
    raise FileNotFoundError(f"Expected output was not created: {{EXPECTED}}")
print(f"Created {{EXPECTED}}")
'''


def r_entry(name: str, runner: str, output: str) -> str:
    return f'''#!/usr/bin/env Rscript
# Figure entrypoint: {name}.
# The shared final implementation remains in code_final_only/{runner}.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- normalizePath(sub("^--file=", "", file_arg[[1]]), winslash = "/")
root <- dirname(dirname(script_path))
runner <- file.path(root, "code_final_only", "{runner}")
expected <- file.path(root, "figure", "{output}")

status <- system2("Rscript", c(runner), stdout = "", stderr = "")
if (!identical(status, 0L) || !file.exists(expected)) {{
  stop("Expected output was not created: ", expected)
}}
cat("Created ", expected, "\\n", sep = "")
'''


def main() -> None:
    for number, (name, language, runner, output) in FIGURES.items():
        prefix = f"Figure{number:02d}_{name}"
        suffix = ".py" if language == "PY" else ".R"
        content = py_entry(name, runner, output) if language == "PY" else r_entry(name, runner, output)
        (OUT / f"{prefix}{suffix}").write_text(content, encoding="utf-8")

    (OUT / "MANIFEST.csv").write_text(
        "figure,entrypoint,language,shared_runner,expected_output\n"
        + "\n".join(
            f"Figure{number:02d},Figure{number:02d}_{name}{'.py' if language == 'PY' else '.R'},{language},{runner},{output}"
            for number, (name, language, runner, output) in FIGURES.items()
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
