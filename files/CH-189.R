library(tidyverse)
library(readxl)

path = "CH-189 Combining the columns.xlsx"
input = read_excel(path, range = "B2:E7")
test  = read_excel(path, range = "H2:H7")

result = input %>%
  mutate(Pattern = trimws(Pattern)) %>%
  separate_rows(Pattern, sep = "") %>%
  mutate(repl = case_when(
    Pattern == "F" ~ `First Name`,
    Pattern == "L" ~ `Last Name`,
    Pattern == "M" ~ `Middle Name`,
    TRUE ~ Pattern
  )) %>%
  summarise(`Custom Format` = paste(repl, collapse = ""), .by = `First Name`)

