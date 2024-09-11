library(tidyverse)
library(readxl)

path = "files/CH-111 iNCREASED SALES.xlsx"
input = read_excel(path, range = "B2:D25")
test  = read_excel(path, range = "H2:H6")

result = input %>%
  summarise(sales = sum(Sales), .by = Date) %>%
  filter(sales > lag(sales)) %>%
  select(Dates = Date)

identical(result, test)
# [1] TRUE