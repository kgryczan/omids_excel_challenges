library(tidyverse)
library(readxl)

path = "files/CH-191Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:F7")

result = input %>% 
  extract(ID, into = c("Part 1", "Separator", "Part 2"), "([A-Za-z0-9]+)([^A-Za-z0-9])(.*)")
all.equal(result, test, check.attributes = FALSE)
# [1] TRUE