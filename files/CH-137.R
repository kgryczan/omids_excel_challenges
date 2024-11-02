library(tidyverse)
library(readxl)
library(janitor)

path = "files/CH-137 Table Transformation.xlsx"
input = read_excel(path, range = "C2:D17")
test  = read_excel(path, range = "F2:H12") %>% mutate(Date = as.Date(Date))

result = input %>%
  mutate(Date = ifelse(is.na(`Column 2`), as.numeric(`Column 1`), NA)) %>%
  fill(Date) %>%
  na.omit() %>%
  transmute(Date = excel_numeric_to_date(Date), Product = `Column 1`, Quantity = `Column 2`)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
