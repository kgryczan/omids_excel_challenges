library(tidyverse)
library(readxl)
library(janitor)

path <- "300-399/357/CH-357 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:F13")
test <- read_excel(path, range = "H3:L8")
test$Date = as.Date(test$Date, origin = "1899-12-30")

res = input %>%
  mutate(Group = cumsum(Column1 == "Date")) %>%
  nest_by(Group) %>%
  mutate(data = list(row_to_names(data, row_number = 1))) %>%
  unnest() %>%
  mutate(
    Date = excel_numeric_to_date(round(as.numeric(Date), 0)),
    across(-Date, as.numeric)
  ) %>%
  ungroup() %>%
  select(Date, A, B, C, D)

all.equal(res, test)
# [1] TRUE
