library(tidyverse)
library(readxl)

path = "files/CH-96 Top Products.xlsx"
input = read_excel(path, range = "B2:D20")
test  = read_excel(path, range = "I2:K11")

result = input %>%
  mutate(Month = month(Date)) %>%
  summarise(Quantity = sum(Quantity), .by = c(Product, Month)) %>%
  mutate(Rank = dense_rank(desc(Quantity)), .by = Month) %>%
  mutate(Product = ifelse(Rank < 3, Product, "Other")) %>%
  arrange(Month, Rank) %>%
  summarise(Quantity = sum(Quantity), .by = c(Product, Month)) %>%
  mutate(`% of Month sales` = Quantity / sum(Quantity), .by = Month) %>%
  select(Month, Product, `% of Month sales`)

identical(result, test)
# [1] TRUE