library(tidyverse)
library(readxl)

path = "files/CH-008.xlsx"
input = read_excel(path, range = "B2:E19")
test  = read_excel(path, range = "I2:L4")

result = input %>%
  arrange(Product, Date) %>%
  mutate(rn = row_number(), .by = Product) %>%
  complete(Date = seq(min(Date), max(Date), by = "day"),
           Product = c("A", "B", "C")) %>%
  mutate(sign = ifelse(Type == "Reduce", -1, 1),
         Month = month(Date),
         Quantity = Quantity * sign) %>%
  replace_na(list(Quantity = 0)) %>%
  ungroup() %>%
  arrange(Product, Date) %>%
  fill(rn, .direction = "down") %>%
  mutate(cumsum = cumsum(Quantity), .by = Product) %>%
  summarise(days = n_distinct(Date), .by = c(Product, rn, Month, cumsum)) %>%
  summarise(weighted_value = sum(cumsum * days)/sum(days), .by = c(Product, Month)) %>%
  pivot_wider(names_from = Product, values_from = weighted_value) 
         