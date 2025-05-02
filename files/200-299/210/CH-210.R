library(tidyverse)
library(readxl)

path = "files/CH-210Removing a character.xlsx"
input = read_excel(path, range = "B2:B6")
test  = read_excel(path, range = "D2:E6")

result = input %>%
  mutate(rn = row_number()) %>%
  separate_rows(Text, sep = "") %>%
  filter(Text != "") %>%
  mutate(counter = row_number(), .by = Text) %>%
  mutate(rem = ifelse(counter > 1, "Removed chars", "Revised Text")) %>%
  select(-counter) %>%
  pivot_wider(names_from = rem, values_from = Text, values_fn = list(Text = toString)) 
