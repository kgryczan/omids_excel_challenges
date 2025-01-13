library(tidyverse)
library(readxl)

path = "files/CH-173 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26")
test  = read_excel(path, range = "G2:I26")

result = input %>%
  group_by(month(Date)) %>%
  mutate(Group = paste0(month(Date), "-", pmin(row_number(), rev(row_number())))) %>%
  ungroup() %>%
  select(Date, Quantity, Group)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
