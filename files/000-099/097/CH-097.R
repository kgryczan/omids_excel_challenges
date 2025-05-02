library(tidyverse)
library(readxl)
library(zoo)

path = "files/CH-097 Linear Interpolation.xlsx"
input = read_excel(path, range = "B2:E5")
test = read_excel(path, range = "H2:K15")

years = tibble(Year = 2010:2022)

df = years %>%
  left_join(input, by = c("Year" = "Year")) %>%
  mutate(across(c("A", "B", "C"), ~ na.approx(.x, na.rm = FALSE))) %>%
  mutate(across(
    c("A", "B", "C"),
    ~ case_when(
      row_number() == 1 ~ 2 * lead(.x) - lead(lead(.x)),
      row_number() == n() ~ 2 * lag(.x) - lag(lag(.x)),
      TRUE ~ .x
    )
  )) %>%
  mutate(across(c("A", "B", "C"), round, 0))

identical(df, test) # TRUE



