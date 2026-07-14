#!/usr/bin/env Rscript
# Figure entrypoint: benchmark_roc_overlay.
# The shared final implementation remains in code_final_only/run_analysis.R.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- normalizePath(sub("^--file=", "", file_arg[[1]]), winslash = "/")
root <- dirname(dirname(script_path))
runner <- file.path(root, "code_final_only", "run_analysis.R")
expected <- file.path(root, "figure", "Figure10_benchmark_roc_overlay.pdf")

status <- system2("Rscript", c(runner), stdout = "", stderr = "")
if (!identical(status, 0L) || !file.exists(expected)) {
  stop("Expected output was not created: ", expected)
}
cat("Created ", expected, "\n", sep = "")
