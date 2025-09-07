library(tidyverse)
library(readxl)

path = "files/200-299/292/CH-292 Advanced Filtering.xlsx"
input = read_excel(path, range = "B2:E9")
test  = read_excel(path, range = "G2:G6")

result = input %>%
  rowwise() %>%
  filter(n_distinct(c_across(-ID)) == ncol(across(-ID))) %>%
  ungroup() %>%
  select(ID)
  
all.equal(result$ID, test$`Selected IDs`) # TRUE
