library(tidyverse)
library(readxl)

p <- "400-499/451/CH-451 Column Splitting.xlsx"
data <- read_excel(p, range = "B3:B10")
expected <- read_excel(p, range = "F3:J10")
result <- data %>%
  transmute(parts = map(ID, ~ str_extract_all(.x, "X+|Y+")[[1]])) %>%
  unnest_wider(parts, names_sep = "") %>%
  set_names(names(expected)) %>%
  mutate(across(everything(), ~ replace_na(.x, "")))
expected <- expected %>%
  mutate(across(everything(), ~ replace_na(as.character(.x), "")))

all.equal(result, expected)
# one result incorrect
