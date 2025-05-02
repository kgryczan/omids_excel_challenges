library(tidyverse)
library(readxl)

input = read_excel("files/CH-029 Identifying Customers Staple Products.xlsx", range = "B2:E36")
test  = read_excel("files/CH-029 Identifying Customers Staple Products.xlsx", range = "I2:J6")

result = input %>%
  summarise(total_quantity = sum(Quantity), .by = c("Customer ID", "Product")) %>%
  group_by(`Customer ID`) %>%
  mutate(rank = rank(-total_quantity),
         lowest_rank = min(rank)) %>%
  filter(rank == lowest_rank) %>%
  summarise(`Most Purchased PRODUCT` = paste0(sort(Product), collapse = ","))

identical(result$`Most Purchased PRODUCT`, test$`Most Purchased PRODUCT`)
# [1] TRUE
