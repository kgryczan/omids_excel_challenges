library(tidyverse)
library(readxl)

path = "files/200-299/291/CH-291 Randomly Reorder Columns.xlsx"
input = read_excel(path, range = "B2:E9")

result = input %>%
  select(sample(everything()))
