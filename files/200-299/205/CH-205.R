library(tidyverse)
library(readxl)

path = "files/CH-205 Missing Char.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:D7")

result = input %>%
  mutate(w_index = row_number()) %>%
  separate_rows(ID, sep = "") %>%
  filter(ID != "") %>%
  mutate(l_index = row_number(), .by = w_index) %>%
  mutate(ID = ifelse(ID == '/', l_index, ID)) %>%
  summarise(ID = paste(ID, collapse = ""), .by = w_index) %>%
  select(-w_index)