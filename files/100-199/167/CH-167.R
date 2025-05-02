library(tidyverse)
library(readxl)

path = "files/CH-167 Table Transformation.xlsx"
input = read_excel(path, range = "C2:C27")
test  = read_excel(path, range = "E2:G12")

result = tibble(raw = input$`Column 1`) %>%
  mutate(
    type = case_when(
      str_detect(raw, "^\\d{5}$") ~ "date",
      str_detect(raw, "^[A-Za-z]+$") ~ "letter",
      str_detect(raw, "^\\d+$") ~ "digit",
      TRUE ~ "unknown"
    ),
    group = cumsum(type == "date")
  ) %>%
  pivot_wider(names_from = type, values_from = raw, values_fn = list(raw = list)) %>%
  unnest(cols = c(date, letter, digit)) %>%
  select(Date = date, Product = letter, Quantity = digit) %>%
  mutate(Date = as.POSIXct(as.Date(as.numeric(Date), origin = "1899-12-30")),
         Quantity = as.numeric(Quantity))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE