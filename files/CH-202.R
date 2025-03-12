library(tidyverse)
library(readxl)

path = "files/CH-202 Table Transformation.xlsx"
input = read_excel(path, range = "B2:B18")
test  = read_excel(path, range = "D2:F11")

result = input %>%
  mutate(Date = if_else(str_detect(`Column 1`, "^\\d+$") & as.numeric(`Column 1`) > 40000,
                        as_date(as.numeric(`Column 1`), origin = "1899-12-30"),
                        NA_Date_) %>% as.POSIXct()) %>%
  fill(Date) %>%
  filter(nchar(`Column 1`) != 5) %>%
  mutate(col = if_else(str_detect(`Column 1`, "^\\d+$"),"Quantity","Product")) %>%
  mutate(change = ifelse(lag(col) == "Product" & col == "Quantity", 0, 1), .by = Date) %>%
  group_by(Date) %>%
  mutate(row = cumsum(change)) %>%
  ungroup() %>%
  select(-change) %>%
  pivot_wider(names_from = col, values_from = `Column 1`) %>%
  select(-row) %>%
  mutate(Quantity = as.numeric(Quantity))


all.equal(result, test)
#> [1] TRUE