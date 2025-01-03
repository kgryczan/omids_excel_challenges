library(tidyverse)
library(readxl)

path = "files/CH-168 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26")
test  = read_excel(path, range = "G2:I26")

result = input %>%
  mutate(group = cumsum(cummin(`Stock price`) != lag(cummin(`Stock price`), default = first(cummin(`Stock price`)))) + 1)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE