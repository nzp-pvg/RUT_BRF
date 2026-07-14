#!/usr/bin/env Rscript
# Figure entrypoint: qpcr_blood_scores.
# The shared final implementation remains in code_final_only/run_qpcr_analysis.R.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- normalizePath(sub("^--file=", "", file_arg[[1]]), winslash = "/")
root <- dirname(dirname(script_path))
runner <- file.path(root, "code_final_only", "run_qpcr_analysis.R")
expected <- file.path(root, "figure", "Figure14_qpcr_blood_scores.pdf")

status <- system2("Rscript", c(runner), stdout = "", stderr = "")
if (!identical(status, 0L) || !file.exists(expected)) {
  stop("Expected output was not created: ", expected)
}
cat("Created ", expected, "\n", sep = "")
