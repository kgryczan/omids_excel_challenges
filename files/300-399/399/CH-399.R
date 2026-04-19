library(tidyverse)
library(readxl)

path <- "300-399/399/CH-399 Table Transformation.xlsx"
input <- read_excel(path, range = "B4:B9", col_names = "input")
test <- read_excel(path, range = "D3:G9")

result = input %>%
  pivot_longer(everything()) %>%
  pull(value) %>%
  discard(is.na) %>%
  map(~ read_delim(I(.x), delim = "\t", show_col_types = FALSE)) %>%
  list_rbind()

all.equal(result, test)
# [1] TRUE
