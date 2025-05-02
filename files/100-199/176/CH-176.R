library(tidyverse)
library(readxl)

path = "files/CH-176 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C27")
test  = read_excel(path, range = "F2:G7")

result = input %>%
  mutate(Group = rep(1:ceiling(nrow(input)/5), each = 5)) %>%
  summarise(Quantity = sum(Quantity), .by = Group)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE