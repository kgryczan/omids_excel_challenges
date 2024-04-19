library(tidyverse)
library(readxl)

input = read_excel("files/CH-039 Transformation.xlsx", range = 'B2:E10', col_names = F)
test  = read_excel("files/CH-039 Transformation.xlsx", range = 'G1:G22')


result = input %>%
  pivot_longer(everything(), names_to = NULL) %>%
  arrange(value) %>%
  na.omit() %>%
  distinct()

identical(result$value, test$`Result - Unique Code`)
# [1] TRUE
