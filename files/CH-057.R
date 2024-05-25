library(tidyverse)
library(readxl)

input = read_excel("files/CH-057 Fuzzy Numbers Calculation.xlsx", range = "B2:C15")
test  = read_excel("files/CH-057 Fuzzy Numbers Calculation.xlsx", range = "G2:H15")

result = input %>%
  separate(A, into = c("A1", "A2", "A3"), sep = ",", convert = TRUE) %>%
  separate(B, into = c("B1", "B2", "B3"), sep = ",", convert = TRUE) %>%
  mutate(
    A = pmap(list(A1, A2, A3), c),
    B = pmap(list(B1, B2, B3), c),
    `A+B` = map2_chr(A, B, ~ paste(.x + .y, collapse = ",")),
    `A-B` = map2_chr(A, map(B, rev), ~ paste(.x - .y, collapse = ","))
  ) %>%
  select(`A+B`, `A-B`)

identical(result, test)
# [1] TRUE