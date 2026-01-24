library(tidyverse)
library(readxl)
library(janitor)

path <- "300-399/356/CH-356 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:B18")
test <- read_excel(path, range = "D3:F8") %>%
  mutate(Date = as.Date(Date, origin = "1899-12-30"))

Date <- input %>%
  filter(str_length(Name) > 3) %>%
  mutate(Date = excel_numeric_to_date(as.numeric(Name))) %>%
  select(Date)
Product <- input %>%
  filter(str_detect(Name, "[A-Za-z]")) %>%
  rename(Product = Name)
Sale <- input %>%
  filter(str_detect(Name, "^[0-9]{1,2}$")) %>%
  mutate(Sale = as.numeric(Name)) %>%
  select(Sale)

final <- bind_cols(Date, Product, Sale)
all_equal(final, test)
# [1] TRUE
