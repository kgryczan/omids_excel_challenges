library(tidyverse)
library(readxl)

path = "files/200-299/251/CH-251 Table Transformation.xlsx"
input = read_excel(path, range = "B3:D16", col_names = F) %>% as.matrix()
test = read_excel(path, range = "F2:H9")

result = input %>%
  t() %>%
  matrix(ncol = 1) %>%
  trimws() %>%
  as.data.frame() %>%
  mutate(group = cumsum(str_length(V1) == 5)) %>%
  slice_head(n = 3, by = group) %>%
  mutate(l = row_number(), .by = group) %>%
  mutate(
    l = case_when(
      l == 1 ~ "Date",
      l == 2 ~ "Product",
      l == 3 ~ "Quantity"
    )
  ) %>%
  pivot_wider(names_from = l, values_from = V1) %>%
  mutate(
    Date = janitor::excel_numeric_to_date(as.numeric(Date)) %>% as.POSIXct(),
    Quantity = as.numeric(Quantity)
  ) %>%
  select(-group)

all.equal(test, result, check.attributes = FALSE) # TRUE
