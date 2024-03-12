library(tidyverse)
library(readxl)

input = read_excel("files/CH-020 Transform Higherarchey format.xlsx", range = "B2:C18")
test  = read_excel("files/CH-020 Transform Higherarchey format.xlsx", range = "E2:H10")

result = input %>%
  mutate(level = str_length(Code), 
         first_digit = str_sub(Code, 1,1)) %>%
  pivot_wider(names_from = level, values_from = Description) %>%
  group_by(first_digit) %>%
  fill(everything(), .direction = "down")  %>%
  ungroup() %>%
  filter(str_length(Code) == 3) %>%
  select(Code, `Lvel 1` = `1`, `Lvel 2` = `2`, `Lvel 3` = `3`)

identical(result, test)
# [1] TRUE
