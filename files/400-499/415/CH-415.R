library(tidyverse)
library(readxl)

path <- "400-499/415/CH-415 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:C23")
test <- read_excel(path, range = "E3:H8")

result = input %>%
  extract(
    COLUMN,
    into = c("COLUMN", "INDEX"),
    regex = "([A-Za-z]+)\\s?(\\d+)",
    convert = TRUE
  ) %>%
  mutate(COLUMN = str_to_upper(COLUMN)) %>%
  pivot_wider(names_from = COLUMN, values_from = VALUE) %>%
  mutate(
    SALES = as.numeric(SALES),
    DATE = janitor::excel_numeric_to_date(as.numeric(DATE)) %>% as.POSIXct()
  ) %>%
  select(-INDEX)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
