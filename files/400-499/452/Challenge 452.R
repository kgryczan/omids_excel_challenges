library(tidyverse)
library(readxl)

p <- "400-499/452/CH-452 Matrix Normalization.xlsx"
matrix <- read_excel(
  p,
  sheet = "Sheet1",
  range = "C4:F7",
  col_names = FALSE
) %>%
  as.matrix()
expected <- read_excel(
  p,
  sheet = "Sheet1",
  range = "J4:M7",
  col_names = FALSE
) %>%
  as.matrix()

result <- matrix %>%
  apply(1, sort) %>%
  t() %>%
  apply(2, sort)

print(isTRUE(all.equal(unname(result), unname(expected))))
