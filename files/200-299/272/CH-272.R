library(tidyverse)
library(readxl)

path = "files/200-299/272/CH-272 Find Value.xlsx"
input = read_excel(path, range = "B2:D9") 
test  = read_excel(path, range = "F2:F13") %>% pull() %>% sort()

result = map2(
  row(input), col(input),
  ~ {
    val = input[[.y]][.x]
    is_unique_row = sum(input[.x, ] == val) == 1
    is_unique_col = sum(input[[.y]] == val) == 1
    if (is_unique_row && is_unique_col) val else NULL
  }
) %>%
  compact() %>%
  unlist() %>%
  sort()

all.equal(result, test)
# [1] TRUE
