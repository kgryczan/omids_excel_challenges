library(tidyverse)
library(readxl)

path = "files/CH-161 Custom Index Column.xlsx"
input = read_excel(path, range = "B2:C11")
test  = read_excel(path, range = "E2:H6")

result = input %>%
  mutate(rn = row_number(), .by = Product) %>%
  pivot_wider(names_from = Product, values_from = Date) %>%
  select(-rn)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE