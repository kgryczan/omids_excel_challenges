library(tidyverse)
library(readxl)

path = "files/CH-217 Table Transformation.xlsx"
input = read_excel(path, range = "B2:C17")
test  = read_excel(path, range = "E2:G11") %>% arrange(Date, Product, Quantity)

result = input %>%
  mutate(Product = ifelse(is.na(`Column 2`), `Column 1`, NA) %>% str_extract(".{1}$")) %>%
  fill(Product) %>%
  mutate(`Column 2` = ifelse(str_detect(`Column 2`, "^[0-9]+$"), `Column 2`, NA)) %>%
  na.omit() %>%
  select(Date = `Column 1`, Product, Quantity = `Column 2`) %>%
  mutate(Date = as.Date(as.numeric(Date), origin = "1899-12-30") %>% as.POSIXct(),
         Quantity = as.numeric(Quantity)) %>%
  arrange(Date, Product, Quantity)

all.equal(result, test, check.attributes = FALSE) 
#> True