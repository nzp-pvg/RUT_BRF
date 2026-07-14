#!/usr/bin/env Rscript
# Figure entrypoint: framework_transferability_and_strategy.
# The shared final implementation remains in code_final_only/run_framework_priority_analysis.R.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- normalizePath(sub("^--file=", "", file_arg[[1]]), winslash = "/")
root <- dirname(dirname(script_path))
runner <- file.path(root, "code_final_only", "run_framework_priority_analysis.R")
expected <- file.path(root, "figure", "Figure19_framework_transferability_auc_heatmap.png")

status <- system2("Rscript", c(runner), stdout = "", stderr = "")
if (!identical(status, 0L) || !file.exists(expected)) {
  stop("Expected output was not created: ", expected)
}
cat("Created ", expected, "\n", sep = "")
