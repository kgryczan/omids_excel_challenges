library(tidyverse)
library(readxl)

path = "files/CH-75 Table Transformation.xlsx"
input = read_xlsx(path, range = "B2:E20")
test  = read_xlsx(path, range = "I2:J5") %>%
  mutate(`AVG Delivery Time` = round(`AVG Delivery Time`, 2))

orders = input %>%
  filter(Quantity > 0)
deliveries = input %>%
  filter(Quantity < 0)

together = orders %>%
  left_join(deliveries, by = c("Order ID" = "Order ID")) %>%
  mutate(Days = as.numeric(Date.y - Date.x)) %>%
  mutate(total_quantity = -sum(Quantity.y), .by = Product.x) %>%
  summarise(`AVG Delivery Time` = round(sum(Days * -Quantity.y) / min(total_quantity),2), 
            .by = Product.x) %>%
  arrange(Product.x) %>%
  rename(Product = Product.x)

identical(together, test)
# [1] TRUE