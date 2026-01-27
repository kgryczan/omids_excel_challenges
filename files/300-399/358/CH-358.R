library(tidyverse)
library(readxl)
library(janitor)

path <- "300-399/358/CH-358 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:E17")
test <- read_excel(path, range = "G3:K8") %>%
  mutate(Date = as.Date(Date, origin = "1899-12-30"))

result = input |>
  mutate(across(1, ~ replace_na(.x, "Date"))) %>%
  mutate(Group = cumsum(Column1 == "Date")) %>%
  nest_by(Group) %>%
  mutate(data = list(data |> select(where(~ !all(is.na(.x)))))) %>%
  mutate(data = list(row_to_names(data, row_number = 1))) %>%
  mutate(
    data = list(
      data |> pivot_longer(-Date, names_to = "Variable", values_to = "Value")
    )
  ) %>%
  unnest(data) %>%
  ungroup() %>%
  mutate(
    Date = excel_numeric_to_date(round(as.numeric(Date), 0)),
    Value = as.numeric(Value)
  ) %>%
  summarise(Value = sum(Value, na.rm = T), .by = c(Date, Variable)) %>%
  pivot_wider(names_from = Variable, values_from = Value, values_fn = sum)

all.equal(result, test)
# [1] TRUE
