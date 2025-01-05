library(tidyverse)
library(readxl)

path = "files/CH-169 Extract From Text Part 2.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:D7")

result = input %>%
  mutate(result = str_match_all(Text, "(?<=\\{)[^{}]+(?=\\})|(?<=\\[)[^\\]]+(?=\\])|(?<=\\()[^\\)]+(?=\\))|(?<=\\*)[^\\*]+(?=\\*)")) %>%
  mutate(result = map_chr(result, ~paste(., collapse = ", ")))

all.equal(result$result, test$Extracted, check.attributes = FALSE)
#> [1] TRUE