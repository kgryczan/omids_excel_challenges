library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-044 Combine Tables.xlsx", range = "C3:F6")
input2 = read_excel("files/CH-044 Combine Tables.xlsx", range = "C9:G12")
input3 = read_excel("files/CH-044 Combine Tables.xlsx", range = "C15:F18")

test   = read_excel("files/CH-044 Combine Tables.xlsx", range = "J2:O6")

result = map_dfr(list(input1, input2, input3), ~.x %>% pivot_longer(cols = -1)) %>%
  pivot_wider(names_from = name, values_from = value, values_fn = sum, values_fill = 0) %>%
  select(colnames(test))

identical(result, test)
# [1] TRUE
