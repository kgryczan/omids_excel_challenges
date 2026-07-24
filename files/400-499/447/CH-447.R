library(tidyverse)
library(readxl)

path <- "400-499/447/CH-447 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:D15")
test <- read_excel(path, range = "F3:H10")

result <- input %>%
  mutate(
    products = str_split(Products, ","),
    products = map_chr(products, \(x) str_c(sort(x), collapse = ","))
  ) %>%
  mutate(
    cons = cumsum(products != lag(products, default = first(products)))
  ) %>%
  summarise(
    PRODUCTS = first(products),
    `TOTAL QUANTITY` = sum(Quantity, na.rm = T),
    DATES = ifelse(
      n() == 1,
      as.character(first(Date)),
      paste0(min(Date), "-", max(Date))
    ),
    .by = c(products, cons)
  ) %>%
  select(-c(products, cons))

# Different results
