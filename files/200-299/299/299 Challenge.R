library(tidyverse)
library(readxl)

path = "files/200-299/299/CH-299 Advanced Filtering.xlsx"
input = read_excel(path, range = "B2:C17")
test  = read_excel(path, range = "G2:H8")

result = input %>%
  filter(Sales > lag(Sales, 1, default = first(Sales)))
        
all.equal(result, test)
# [1] TRUE