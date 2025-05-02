library(tidyverse)
library(readxl)

path = "files/CH-164 Extract from Text.xlsx"
input = read_excel(path, range = "B2:C7")
test  = read_excel(path, range = "E2:F7")

maxDepth = function(S) {
  get_chars = function(str) {
    tibble(pos = 1:nchar(str), char = strsplit(str, "")[[1]])
  }
  
  check = if_else(str_detect(S, "^[{]+[0-9,]+[}]+$"), -1, 0)
  df = get_chars(S)
  
  df = df %>%
    mutate(count = ifelse(char == "{", 1, ifelse(char == "}", -1, 0)),
           cum_sum = cumsum(count))
  
  max_depth = max(df$cum_sum) + check
  
  return(max_depth)
}

result = input %>%
  mutate(Depth = map_dbl(Value, maxDepth))

all.equal(result$Depth, test$Depth)
#> [1] TRUE