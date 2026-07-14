# 🧬 *Evodiae Fructus* – CVD Reproducibility Hub

This repository provides a reproducible analysis workflow for integrating *Evodiae Fructus* compound–target evidence with human carotid atherosclerosis transcriptomics and cardiovascular safety signals. It is organized for traceability, parameter transparency, and figure-level reruns.

![Research stage](https://img.shields.io/badge/research-submission--ready-005493)
![Analysis](https://img.shields.io/badge/analysis-multi--omics%20%7C%20in%20silico-712238)
![Main figures](https://img.shields.io/badge/main%20figures-20-F5BD4D)
![License](https://img.shields.io/badge/license-to%20be%20specified-lightgrey)

> 🫀 **Core question:** Which *Evodiae Fructus* constituents show the most coherent benefit–risk evidence for carotid atherosclerosis, and how stable is that evidence across independent human cohorts?

---

## 🎯 What you can reproduce here

- ✅ Discovery and external validation of plaque-associated transcriptomic signals
- ✅ ChEMBL-supported human compound–target extraction and target filtering
- ✅ Benefit/risk module construction using plaque biology and a curated cardiovascular safety panel
- ✅ External module-score validation in plaque progression and macrophage-vulnerability cohorts
- ✅ Compact LASSO signature and seven-model benchmark comparison
- ✅ Pathway ssGSEA and marker-based bulk cell-context scoring
- ✅ Peripheral-blood qPCR normalization, group comparison, and composite-score analysis
- ✅ Candidate-level ADMET/ProTox safety comparison and prioritization
- ✅ Support-level molecular docking and exploratory molecular-dynamics analysis
- ✅ LINCS L1000 transcriptome-reversal prioritization and mechanism-class summarization
- ✅ Regeneration of the 20 main figures through figure-level entrypoints

⚠️ Docking, molecular dynamics, ADMET, ProTox, and LINCS results are **computational or support-level evidence**. They are not experimental binding measurements, measured toxicity, clinical efficacy, or direct drug-repositioning validation.

---

## 🚀 Quick start

### 1. Environment

R workflows use packages declared in the scripts, including:

```text
limma, GEOquery, GSVA, clusterProfiler, glmnet, pROC, patchwork,
data.table, dplyr, tidyr, ggplot2, igraph, randomForest, e1071
```

Python workflows use:

```text
numpy, pandas, matplotlib, scipy, RDKit, Biopython, Pillow
```

Structural workflows may additionally require AutoDock Vina, Meeko, OpenMM, MDTraj, ParmEd, and PyMOL.

### 2. Recommended entrypoints

Run commands from the project root:

```bash
# Main transcriptomic figures and core result tables
Rscript code_by_figure_v1/Figure01_transcriptomic_baseline.R

# Peripheral-blood qPCR figures
Rscript code_by_figure_v1/Figure11_qpcr_reference_genes.R

# Candidate prioritization and docking-linked outputs
python code_by_figure_v1/Figure15_candidate_prioritization.py

# Ranking robustness and framework transferability
Rscript code_by_figure_v1/Figure20_ranking_robustness.R
```

The complete figure-to-runner mapping is recorded in [`code_by_figure_v1/MANIFEST.csv`](code_by_figure_v1/MANIFEST.csv). Figures that share a statistical pipeline intentionally share one underlying final runner to avoid duplicated and diverging analysis code.

---

## 🧬 Data and cohorts

| Data layer | Dataset or source | Role |
|---|---|---|
| Discovery plaque transcriptomics | `GSE43292` | Paired intact tissue and atheroma plaque; discovery analysis |
| Plaque progression validation | `GSE28829` | Early versus advanced carotid plaque |
| Plaque vulnerability context | `GSE41571` | Stable versus ruptured plaque macrophages |
| Additional public resource | `GSE100927` | Retained public transcriptomic resource where applicable |
| Human target evidence | ChEMBL | Compound-specific human single-protein activity evidence |
| Perturbational signatures | LINCS L1000 / Enrichr | Transcriptome-reversal prioritization |
| Safety prediction | ADMETlab 3.0 / ProTox 3.0 | Computational developability and toxicity context |
| Blood validation | 36 qPCR samples | `CTL n=12`, `CAD n=12`, `AMI n=12` |

Public transcriptomic inputs are cached under `data/raw/`. Processed tables and analysis summaries are stored under `res/`.

---

## 🧹 Core preprocessing and analysis rules

### Transcriptomic processing

- Probe-level expression is collapsed to gene symbols using platform-specific annotation.
- Discovery analysis uses paired modeling for `GSE43292`.
- External datasets use cohort-specific group comparisons.
- Discovery-associated genes are defined using adjusted `P < 0.05` and `|logFC| > 0.5`.
- External support is recorded by directional concordance rather than by reusing discovery labels.

### Benefit–risk integration

- Benefit genes are herb targets overlapping plaque-associated genes.
- Risk genes are herb targets overlapping the curated cardiovascular safety panel.
- Module-level benefit, risk, and net scores are calculated from row-standardized expression.
- The primary interpretable summary is the module-derived `net score`.

### Model benchmark

The benchmark compares:

- Module-derived `net score`
- Discovery-trained three-gene LASSO signature
- Ridge regression
- Elastic net
- Eight-gene LASSO
- Linear SVM
- Random forest

Model performance is reported with cohort-specific AUROC values and external transfer comparisons.

### qPCR normalization

- `TBP` and `HPRT1` are used as dual reference genes.
- Technical replicates are averaged.
- The two `TP53` assay blocks are collapsed to a target-level estimate.
- Expression is summarized using `log2(2^-ddCt)` relative to the CTL mean.
- Group comparisons include ANOVA, Kruskal–Wallis testing, and Benjamini–Hochberg-adjusted pairwise testing.

---

## 🗂️ Repository layout

```text
data/
├── raw/                         # GEO matrices and ChEMBL target cache
└── meta/                        # Compound metadata and safety-panel definitions

res/
├── tables/                      # DEG, module, model, pathway, and ranking tables
├── qPCR/tables/                 # Sample-level qPCR data and statistics
├── pharma/tables/               # ADMET, docking, and candidate-priority tables
├── toxic/tables/                # Downloaded-file-supported toxicity tables
└── lincs/                       # LINCS signatures, hits, and mechanism summaries

dock/                            # Receptors, ligand poses, docking logs, and summaries
figure/                          # Main figures and retained historical versions
code_final_only/                 # Curated final implementation bundle
code_by_figure_v1/               # One main-figure entrypoint per Figure 1–20
supplementary_material_v1/       # Supplementary figures, tables, legends, and manifest
manuscript/                      # Draft manuscript, figure legends, and submission files
```

---

## 🎨 Figure-level regeneration

Each file in `code_by_figure_v1/` is a user-facing entrypoint for one main figure:

| Figures | Shared final runner |
|---|---|
| Figure 1–10 | `code_final_only/run_analysis.R` |
| Figure 11–14 | `code_final_only/run_qpcr_analysis.R` |
| Figure 15 | `code_final_only/run_pharmaceuticals_enhancement.py` |
| Figure 16–17 | `code_final_only/summarize_real_toxic_data.py` |
| Figure 18 | `code_final_only/postprocess_rutaecarpine_mmp9_md.py` |
| Figure 19–20 | `code_final_only/run_framework_priority_analysis.R` |

The entrypoint verifies that the expected output file is created. Heavy workflows, particularly the MD and docking analyses, require the corresponding intermediate structures, trajectories, and external software to be available.

---

## 📦 Supplementary material

The current upload package is in [`supplementary_material_v1/`](supplementary_material_v1/):

- 🖼️ Supplementary Figures 1–5
- 📊 Supplementary Table 6
- 📝 Figure and table legends
- 📋 Upload manifest

The manuscript currently defines additional supplementary tables that should be added to the upload package if required by the target journal.

---

## ♻️ Reproducibility and interpretation boundaries

The results should be interpreted alongside the following limitations:

- public cohorts are heterogeneous in tissue context, phenotype definition, and sample size;
- `GSE41571` is a small macrophage-focused vulnerability dataset;
- the cardiovascular safety panel is curated rather than genome-wide;
- the blood qPCR layer contains 36 samples and reflects peripheral blood rather than plaque tissue;
- docking is a fixed-configuration structural-support analysis rather than a binding assay;
- the available MD result is exploratory and should not be treated as publication-grade long-timescale validation;
- LINCS mechanism classes are library- and annotation-dependent.

Historical figure versions and intermediate outputs are retained where available to preserve traceability and comparison across revisions.

---

## 📖 Citation and license

If you use this repository, please cite the associated manuscript once the final publication reference is available.

The repository currently does not specify a software license. Please contact the authors before reuse or redistribution until a license is added.
