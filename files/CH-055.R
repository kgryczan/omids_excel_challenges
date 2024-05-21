library(tidyverse)
library(readxl)

input = read_excel("files/CH-055 Warehouse Management.xlsx", range = "B2:E19")
test  = read_excel("files/CH-055 Warehouse Management.xlsx", range = "H2:K5")

result = input %>%
  mutate(Year = year(Date)) %>%
  summarise(Year = min(Year),
            Quantity = sum(Quantity),
            .by = c("Order No", "Product")) %>%
  select(-`Order No`) %>%
  pivot_wider(names_from  = Year, values_from = Quantity, values_fn = sum) %>%
  mutate(across(everything(), ~ifelse(. == 0, NA, .))) %>%
  arrange(Product)

identical(result, test)
# [1] TRUE