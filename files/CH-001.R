library(tidyverse)
library(readxl)

path = "files/CH-001.xlsx"
input = read_excel(path, range = "B2:E9")
test  = read_excel(path, range = "K2:N13")

result = input %>%
  pivot_longer(-Date, names_to = "Product", values_to = "Value") %>%
  drop_na() %>%
  arrange(Product, Date) %>%
  mutate(date_1 = lag(Date, 1, default = as.Date("2024-01-01")),
         diff = Value - lag(Value, 1, default = 0),
         .by = Product) %>%
  separate(Product, into = c("Product", "Type"), sep = " ") %>%
  select(From = date_1, To = Date, Product = Type, diff) %>%
  arrange(From, Product)
  
all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE