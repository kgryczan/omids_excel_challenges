library(tidyverse)
library(readxl)

path = "files/200-299/237/CH-237 Table Transformation.xlsx"
input = read_excel(path, range = "B2:E10")
test = read_excel(path, range = "H2:O6")

result = input %>%
  mutate(rn = row_number(), .by = Doc) %>%
  pivot_wider(
    names_from = rn,
    values_from = c(Code, Num),
    names_sep = "",
    names_vary = "slowest"
  )

all.equal(result, test)
#> [1] TRUE
