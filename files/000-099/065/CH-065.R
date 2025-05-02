library(tidyverse)
library(readxl)

input = read_excel("files/CH-065 Transformation.xlsx", range = "B2:D6")
test  = read_excel("files/CH-065 Transformation.xlsx", range = "F2:G12")

result = input %>%
  mutate(seq = map2(From, TO, ~seq.POSIXt(.x, .y, by = "day")),
         len = map(seq, ~length(.x)),
         `AVG Cost` = map2_dbl(len, Cost, ~ .y / .x)) %>%
  select(-c(From, TO, len, Cost)) %>%
  unnest(cols = c(seq)) %>%
  select(Date = seq, `AVG Cost`)

identical(result, test)
# [1] TRUE