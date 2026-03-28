library(tidyverse)
library(readxl)

path <- "300-399/388/CH-388 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:C24", col_types = "text")
test <- read_excel(path, range = "E3:H9")

result = input %>%
  mutate(
    Date = if_else(`Col1` == "Date", `Col 2`, NA_character_),
    Customer = if_else(`Col1` == "Customer", `Col 2`, NA_character_)
  ) %>%
  fill(Date, Customer, .direction = "down") %>%
  filter(`Col1` %in% c("Product", "Sale")) %>%
  mutate(grp = cumsum(`Col1` == "Product")) %>%
  pivot_wider(
    names_from = `Col1`,
    values_from = `Col 2`
  ) %>%
  select(Date, Customer, Product, Sale) %>%
  mutate(Sale = as.numeric(Sale))

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
