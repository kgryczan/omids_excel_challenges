library(tidyverse)
library(readxl)

path = "files/CH-222 Table Transformation.xlsx"
input = read_excel(path, range = "B2:B17")
test = read_excel(path, range = "D2:F7")

result = input %>%
  mutate(
    type = case_when(
      str_detect(`Column 1`, "[a-zA-Z]") ~ "Product",
      as.numeric(`Column 1`) > 100 ~ "Date",
      as.numeric(`Column 1`) < 100 ~ "Quantity"
    )
  ) %>%
  mutate(rn = row_number(), .by = type) %>%
  pivot_wider(
    names_from = type,
    values_from = `Column 1`,
    values_fill = list(`Column 1` = NA)
  ) %>%
  select(-rn) %>%
  mutate(
    Date = as.Date(as.numeric(Date), origin = "1899-12-30") %>% as.POSIXct(),
    Quantity = as.numeric(Quantity)
  )

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
