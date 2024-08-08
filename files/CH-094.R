library(tidyverse)
library(readxl)

path = "files/CH-094 Two Column Text.xlsx"
input = read_excel(path, range = "B2:C13")
test  = read_excel(path, range = "H2:J9")

result = input %>%
  mutate(column = ifelse(row_number() %% 2 == 0, 2, 1),
         row = ceiling(row_number() / 2), 
         .by = Group) %>%
  pivot_wider(names_from = column, values_from = Text, names_glue = "Column {column}") %>%
  select(-row)

all.equal(result, test) 
#> [1] TRUE 