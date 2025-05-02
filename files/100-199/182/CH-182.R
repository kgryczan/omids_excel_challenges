library(tidyverse)
library(readxl)

path = "files/CH-182 Indexing Blank cells.xlsx"
input = read_excel(path, range = "B2:D14", col_types = "text")
test  = read_excel(path, range = "F2:H14")

result = input %>%
  mutate(rn = row_number()) %>%
  pivot_longer(cols = -rn, names_to = "col", values_to = "value") %>%
  arrange(rn, col) %>%
  mutate(value = ifelse(is.na(value), paste0("B", cumsum(is.na(value))), value)) %>%
  pivot_wider(names_from = col, values_from = value) %>%
  select(-rn)

all.equal(result, test)
#> [1] TRUE