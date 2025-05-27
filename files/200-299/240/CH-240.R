library(tidyverse)
library(readxl)

input <- read_excel("files/200-299/240/CH-240  Clean Up Excel Formulas.xlsx", range = "B2:C7")

format_excel_formula_clean <- function(formula) {
  chars <- strsplit(formula, "")[[1]]
  indent <- 0
  formatted <- character()
  for (ch in chars) {
    formatted <- c(formatted, switch(
      ch,
      "(" = { indent <- indent + 1; paste0("(\n", strrep("  ", indent)) },
      ")" = { indent <- indent - 1; paste0("\n", strrep("  ", indent), ")") },
      "," = paste0(",\n", strrep("  ", indent)),
      ch
    ))
  }
  paste(formatted, collapse = "")
}

input %>%
  mutate(broken = map_chr(`Formula (Unformatted)`, format_excel_formula_clean)) %>%
  pull(broken) %>%
  walk(~cat(.x, "\n\n"))
