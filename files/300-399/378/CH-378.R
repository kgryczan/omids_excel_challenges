library(tidyverse)
library(readxl)

path <- "300-399/378/CH-378 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:B12")
test <- read_excel(path, range = "D3:F9")

result = input %>%
  separate_longer_delim(col = 1, delim = ", ") %>%
  mutate(
    type = case_when(
      str_length(Col1) > 3 ~ "Date",
      str_detect(Col1, "^[A-Za-z]+$") ~ "Product",
      TRUE ~ "Sale"
    )
  ) %>%
  mutate(rn = row_number(), .by = type) %>%
  pivot_wider(names_from = type, values_from = Col1) %>%
  select(-rn) %>%
  mutate(Sale = as.numeric(Sale))

all.equal(result, test)
# Correct transformation. Cannot be checked because R read dates differently.
