library(tidyverse)
library(readxl)

path <- "300-399/393/CH-393 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:E8")
test <- read_excel(path, range = "G3:J9")

result = input %>%
  t() %>%
  as.data.frame() %>%
  janitor::row_to_names(row_number = 1) %>%
  pivot_longer(
    cols = -c(Customer, Product),
    names_to = "Date",
    values_to = "Sale"
  ) %>%
  na.omit() %>%
  arrange(Date) %>%
  mutate(Sale = as.numeric(Sale)) %>%
  select(Date, Customer, Product, Sale)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
