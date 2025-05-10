library(tidyverse)
library(readxl)

path = "files/200-299/232/CH-232 Table Transformation.xlsx"
input = read_excel(path, range = "B2:B18")
test = read_excel(path, range = "D2:F6") %>%
  arrange(Price)

result = input %>%
  mutate(col = row_number() %% 2, row = (row_number() + 1) %/% 2) %>%
  pivot_wider(names_from = col, values_from = `Column 1`) %>%
  separate(
    `1`,
    into = c("Product", "Measure"),
    sep = "\\s",
    extra = "merge"
  ) %>%
  select(-row) %>%
  pivot_wider(names_from = Measure, values_from = `0`) %>%
  select(Code, Product, Price) %>%
  mutate(Price = as.numeric(Price), Code = as.numeric(Code)) %>%
  arrange(Price)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
