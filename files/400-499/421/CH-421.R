library(tidyverse)
library(readxl)

path <- "400-499/421/CH-421 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B9")
test <- read_excel(path, range = "F3:J9")

result = input %>%
  transmute(
    out = map(ID, \(x) {
      chars <- unique(str_split_1(x, ""))
      str_c(chars, ":", str_count(x, fixed(chars)))
    })
  ) %>%
  unnest_wider(out, names_sep = "") %>%
  rename_with(\(x) str_replace(x, "^out", "ID"))

all.equal(result, test)
# [1] TRUE
