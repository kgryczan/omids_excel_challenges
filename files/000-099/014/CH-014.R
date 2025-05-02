library(tidyverse)
library(readxl)

input = read_excel("files/CH-014.xlsx", range = "B2:D133")
test  = read_excel("files/CH-014.xlsx", range = "K2:K5")

result = input %>%
  mutate(month = month(Date)) %>%
  group_by(Product) %>%
  summarise(nm = n_distinct(month)) %>%
  filter(nm == 12) %>%
  ungroup() %>%
  select(Products = Product)

identical(result, test)
# [1] TRUE
