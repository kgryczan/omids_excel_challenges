library(tidyverse)
library(readxl)

path = "files/200-299/239/CH-239 Extract from Text.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:D11")

result = input %>%
  mutate(
    `Product ID` = str_extract_all(Text, "[a-zA-Z]{2}[0-9]{1}-[0-9]{2}")
  ) %>%
  unnest(`Product ID`) %>%
  select(-Text)

all.equal(result, test)
# [1] TRUE
