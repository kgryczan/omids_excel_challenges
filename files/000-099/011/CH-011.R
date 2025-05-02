library(tidyverse)
library(readxl)

input = read_excel("files/CH-011.xlsx", range = "B2:E16")
test  = read_excel("files/CH-011.xlsx", range = "K2:K6")

result = input %>%
  pivot_longer(cols = everything(), names_to = "columns", values_to = "codes") %>%
  group_by(codes) %>%
  summarise(is_in_col = n_distinct(columns)) %>%
  filter(is_in_col >= 3) %>%
  select(-is_in_col)

identical(result$codes, test$`Item Code`)
# [1] TRUE
