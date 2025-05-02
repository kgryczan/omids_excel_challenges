library(tidyverse)
library(readxl)

input = read_excel("files/CH-0010.xlsx", range = "B2:D17")
test  = read_excel("files/CH-0010.xlsx", range = "G2:H7")

result = input %>%
  mutate(requirements = case_when(
    Material == "A" ~ 1,
    Material == "B" ~ 2,
    Material == "C" ~ 3
  ), product_available = Inventory%/%requirements) %>%
  group_by(Date) %>%
  mutate(min_available = min(product_available), 
         usage = min_available*requirements) %>%
  summarise(usage = sum(usage),
            inventory = sum(Inventory),
            Efficiency_rate = usage/inventory)

identical(result$Efficiency_rate, test$`Efficeincy Rate`)
# [1] TRUE

