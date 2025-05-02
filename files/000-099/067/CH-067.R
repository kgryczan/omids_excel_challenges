library(tidyverse)
library(readxl)

input = read_excel("files/CH-067 Index Selections.xlsx", range = "B2:H17")
test  = read_excel("files/CH-067 Index Selections.xlsx", range = "J2:J7")

result = input %>%
  rowwise() %>%
  filter(sum(c_across(2:7) <= 7, na.rm = TRUE) >= 2) %>%
  ungroup() %>%
  select(`Selected Indexes` = 1)
  
identical(result, test)
#> [1] TRUE