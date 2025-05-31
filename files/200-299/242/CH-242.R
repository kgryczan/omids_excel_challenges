library(tidyverse)
library(readxl)

path = "files/200-299/242/CH-242 Table Transformation.xlsx"
input = read_excel(path, range = "B2:B14")
test = read_excel(path, range = "D2:F7") %>% arrange(Product)

result = tibble(
  Product = input$`Column 1`[seq(1, nrow(input), 2)],
  Price = input$`Column 1`[seq(2, nrow(input), 2)]
) %>%
  separate(Product, into = c("Product", "unit"), sep = " (?=[^ ]+$)") %>%
  separate_rows(Product, sep = ", ") %>%
  mutate(
    unit = trimws(unit),
    Product = trimws(Product),
    Price = as.integer(Price)
  ) %>%
  arrange(Product) %>%
  pivot_wider(names_from = unit, values_from = Price) %>%
  select(Code, Product, Price)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
