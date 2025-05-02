library(tidyverse)
library(readxl)

path = "files/CH-079 Remove Blank Columns.xlsx"
input = read_excel(path, range = "B2:I6")
test  = read_excel(path, range = "K2:N6")

result = input %>%
  select(-where(~all(is.na(.))))

identical(result, test)
# [1] TRUE