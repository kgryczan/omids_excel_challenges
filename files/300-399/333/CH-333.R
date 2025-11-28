library(tidyverse)
library(readxl)

path <- "300-399/333/CH-333 Pattern Combinations.xlsx"
input <- read_excel(path, range = "B2:D8")
test <- read_excel(path, range = "F2:F8")

roll_column <- function(column, steps) {
  n <- length(column)
  c(tail(column, n - steps %% n), head(column, steps %% n))
}

result = input %>%
  mutate(
    `Column 1` = `Column 1`,
    `Column 2` = roll_column(`Column 2`, 1),
    `Column 3` = roll_column(`Column 3`, 2)
  ) %>%
  unite("Combinations", `Column 1`:`Column 3`, sep = "")

all.equal(result, test)
# [1] TRUE
