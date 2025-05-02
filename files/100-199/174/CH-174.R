library(tidyverse)
library(readxl)

path = "files/CH-174 Filtering.xlsx"
input = read_excel(path, range = "C2:D25")
test  = read_excel(path, range = "F2:G7")

result = input %>%
  filter(!pmax(lag(Value,1, default = 0) > Value,
             lag(Value,2,default = 0) > Value,
             lead(Value,1, default = 0) > Value,
             lead(Value,2, default = 0) > Value))

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE