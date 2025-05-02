library(tidyverse)
library(readxl)
library(janitor)

path = "files/CH-147 Table Transformation.xlsx"
input = read_excel(path, range = "C2:C27", col_types = "text")
test  = read_excel(path, range = "E2:G12") %>%
  mutate(Date = as.Date(Date, format = "%Y-%m-%d"))


result = input %>%
  mutate(Date = str_extract(`Column 1`, "\\d{5}")) %>%
  fill(Date, .direction = "down") %>%
  filter(`Column 1` != Date) %>%
  mutate(clmn = rep(c("Product", "Quantity"), length.out = n()),
         group = cumsum(clmn == "Product")) %>%
  pivot_wider(names_from = clmn, values_from = `Column 1`) %>%
  select(-group) %>%
  mutate(Quantity = as.numeric(Quantity),
         Date = excel_numeric_to_date(as.numeric(Date)))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE