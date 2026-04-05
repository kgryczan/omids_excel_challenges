library(tidyverse)
library(readxl)

path <- "300-399/392/CH-392 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:C27")
test <- read_excel(path, range = "E3:H9")

result = input %>%
  mutate(group = cumsum(Col1 == "Date")) %>%
  pivot_wider(names_from = Col1, values_from = `Col 2`) %>%
  select(-group) %>%
  mutate(Sale = as.numeric(Sale))

all.equal(result, test)
## [1] TRUE
