library(tidyverse)
library(readxl)

input = read_excel("files/CH-049 Assignment Problem Part 1.xlsx", range = "C2:F6") 
step2 = read_excel("files/CH-049 Assignment Problem Part 1.xlsx", range = "P2:S6")

result = input %>%
  rowwise() %>%
  mutate(across(everything(), ~ . - min(c_across(everything())))) %>%
  ungroup() %>%
  mutate(across(everything(), ~ . - min(.)))

identical(result, step2)
#  [1] TRUE