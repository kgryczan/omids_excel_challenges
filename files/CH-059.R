library(tidyverse)
library(readxl)

input = read_excel("files/CH-059 Merge Columns.xlsx", range = "B2:J12")
test  = read_excel("files/CH-059 Merge Columns.xlsx", range = "L2:P12")

result = input %>%
  pivot_longer(cols = -c(1), names_to = "time", values_to = "value") %>%
  mutate(time = str_sub(time, 1,4) %>% paste0(., "00")) %>%
  pivot_wider(names_from = time, values_from = value, values_fn = sum) 

identical(result, test)
# [1] TRUE