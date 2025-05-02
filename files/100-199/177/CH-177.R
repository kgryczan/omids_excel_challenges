library(tidyverse)
library(readxl)

path = "files/CH-177 Table Transformation.xlsx"
input = read_excel(path, range = "C2:C24")
test  = read_excel(path, range = "E2:G12")

result = input %>%
  mutate(col = case_when(
    str_detect(`Column 1`, "[0-9]{5}") ~ 1,
    str_detect(`Column 1`, "[A-Z]{1}") ~ 2,
    TRUE ~ 3)) %>%
  mutate(Date = ifelse(col == 1, `Column 1`, NA)) %>%
  fill(Date, .direction = "down") %>%
  mutate(Quantity = ifelse(col == 3, `Column 1`, NA)) %>%
  fill(Quantity, .direction = "up") %>%
  filter(col == 2) %>%
  select(Date, Product=`Column 1`, Quantity) %>%
  mutate(Date = janitor::excel_numeric_to_date(as.numeric(Date)) %>% as.POSIXct(),
         Quantity = as.numeric(Quantity))

all.equal(result, test, check.attributes = FALSE)         
#> [1] TRUE