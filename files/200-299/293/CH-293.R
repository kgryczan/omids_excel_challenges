library(tidyverse)
library(readxl)

path = "files/200-299/293/CH-293 Advanced Sorting.xlsx"
input = read_excel(path, range = "B2:D8")
test  = read_excel(path, rsange = "F2:H8")

result = input %>%
  arrange(fct_relevel(Size, "S", "M", "L", "XL", "XXL", "XXXL")) 

all.equal(result, test)
# [1] TRUE