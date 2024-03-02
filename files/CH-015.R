library(tidyverse)
library(readxl)

input = read_excel("files/CH-015.xlsx", range = "B2:E12")
test  = read_excel("files/CH-015.xlsx", range = "G2:S6")

result = input %>%
  group_by(`Product Code`) %>%
  mutate(nr = row_number()) %>%
  pivot_wider(names_from = nr, 
              values_from = c(`Ship Date`, `Po number`, `Po Quantity`), 
              names_sort = FALSE, 
              names_sep = " ") %>%
  ungroup() %>%
  select(Products = `Product Code`, ends_with("1"), ends_with("2"), ends_with("3"), ends_with("4"))

identical(result, test)
# [1] TRUE
