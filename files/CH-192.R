library(tidyverse)
library(readxl)

path = "files/CH-192 Table Transformation.xlsx"
input = read_excel(path, range = "B2:D12")
test  = read_excel(path, range = "B15:D18")

result = input %>%
  mutate(sign = sign(Quantity)) %>%
  mutate(group = ceiling(cumsum(sign != lag(sign, default = 0))/2), .by = Product) %>%
  summarise(Quantity = sum(Quantity), 
            Date = min(Date),
            .by = c(Product,group)) %>%
  filter(Quantity != 0) %>%
  select(Date, Product, Quantity)

all.equal(result, test)
#> [1] TRUE