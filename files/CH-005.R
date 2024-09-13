library(tidyverse)
library(readxl)

path = "files/CH-005.xlsx"
input = read_excel(path, range = "B2:D21")
test  = read_excel(path, range = "I2:L6") %>% as.matrix() 
# replace NA with 0
test[is.na(test)] = 0

result = input %>%
  mutate(value = 1) %>%
  select(-Quantity) %>%
  pivot_wider(names_from = Product, values_from = value, values_fill = list(value = 0)) %>%
  select(-c(`Invoice Num`))

prod = as.matrix(result)
prod_t = as.matrix(result) %>% t()
cooc = prod_t %*% prod

diag(cooc) = 0
rownames(cooc) = rownames(test) = colnames(test) = colnames(cooc) = colnames(result) 

identical(cooc, test)
# [1] TRUE