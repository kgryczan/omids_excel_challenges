library(tidyverse)
library(readxl)

input = read_excel("files/CH-021 Transformation.xlsx", range = "B2:E11")
test  = read_excel("files/CH-021 Transformation.xlsx", range = "G2:H8")

result = input %>%
  select(`Machinary code`, Product_1 = 2, Product_2 = 3, Product_3 = 4) %>%
  pivot_longer(cols = -`Machinary code`, names_to = "Product", values_to = "Value") %>%
  na.omit() %>%
  arrange(Product) %>%
  group_by(Value) %>%
  summarise(Machine = paste0(`Machinary code`, collapse = " ,")) %>%
  select(`Product Code`= Value, `Machinary Code` = Machine)

identical(result, test)
# [1] TRUE
