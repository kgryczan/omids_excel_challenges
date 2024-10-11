library(tidyverse)
library(readxl)

path = "files/CH-126 Transformation.xlsx"
input = read_excel(path, range = "B2:C8")
test  = read_excel(path, range = "E2:G20") %>%
  mutate(Dates = as.Date(Dates))

result = input %>%
  separate_wider_delim(Dates, delim = ", ", names = c("Registeration", "Evaluation", "Approved")) %>%
  pivot_longer(cols = -`Order IDS`, names_to = "Group", values_to = "Dates") %>%
  mutate(Dates = as.Date(Dates)) %>%
  arrange(`Order IDS`, Dates)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
