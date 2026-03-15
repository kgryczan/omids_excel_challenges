library(tidyverse)
library(readxl)

path <- "300-399/382/CH-382 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F9")

is_valid = function(s) {
  nums = str_extract_all(s, "[1-9]")[[1]] %>% as.numeric()
  num_prod = prod(nums)
  return(num_prod %% 4 == 0 || num_prod %% 3 == 0)
}

result = input %>%
  filter(map_lgl(ID, is_valid))
# PQ1347 which is filtered out shouldn't be because product is 105 which is divisible by 3.
