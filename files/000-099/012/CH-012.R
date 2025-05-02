library(tidyverse)
library(readxl)

input = read_excel("files/CH-012.xlsx", range = "B3:G8", col_names = F)
test  = read_excel("files/CH-012.xlsx", range = "O3:T8", col_names = F)

result = input %>%
  mutate(across(everything(), ~ .x / sum(.x)))

# some cells in test were not correct to compare.

result %>% mutate(across(everything(), ~ round(.x * 100, 0)))

# # A tibble: 6 × 6
# ...1  ...2  ...3  ...4  ...5  ...6
# <dbl> <dbl> <dbl> <dbl> <dbl> <dbl>
#   1    13    29     4    27    22    20
#   2    29     8    21    29     4    23
#   3    21    27    34    11    10    22
#   4    26     4    22    17    19    19
#   5     4    20    11    14    21     9
#   6     7    12     8     3    23     6                 