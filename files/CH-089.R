library(tidyverse)
library(readxl)
library(unpivotr)

path = "files/CH-089 Transformation.xlsx"
input = read_excel(path, range = "B2:G10", col_names = F)
test = read_excel(path, range = "I2:K20")

result = as_cells(input) %>%
  behead("up-left", "Product") %>%
  mutate(col_mod = col %% 2)

list_r = map(0:1, ~result %>% filter(col_mod == .x) %>% select(chr, Product))

r1 = list_r[[1]]
r2 = list_r[[2]]

r3 = cbind(r2, r1) %>%
  set_names(c("Date", "Product", "Quantity", "Product2")) %>%
  as_tibble() %>%
  mutate(Quantity = suppressWarnings(as.numeric(Quantity))) %>%
  filter(!is.na(Quantity)) %>%
  select(-Product2) %>%
  mutate(Date = as.POSIXct(as.Date(as.numeric(Date), origin = "1899-12-30")))

identical(r3, test)
#> [1] TRUE
