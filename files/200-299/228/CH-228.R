library(tidyverse)
library(readxl)

path = "files/200-299/228/CH-228 Table Transformation.xlsx"
input = read_excel(path, range = "B2:H5")
test = read_excel(path, range = "F8:H26")

result = input %>%
  pivot_longer(cols = -Product, names_to = "Date", values_to = "Price") %>%
  replace_na(list(Price = 0)) %>%
  mutate(Date = str_extract(Date, "\\d{1,2}/\\d{2}/\\d{4}") %>% dmy()) %>%
  mutate(Price = cumsum(Price), .by = Product) %>%
  select(Date, Product, Price)
