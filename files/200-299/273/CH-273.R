library(tidyverse)
library(readxl)

path = "files/200-299/273/CH-273 Advanced Sorting.xlsx"
input = read_excel(path, range = "B2:E9")
test  = read_excel(path, range = "G2:J9")

result = input %>%
  rowwise() %>%
  mutate(highest_value = max(c_across(starts_with("2"))),
         max_col = names(.)[which.max(c_across(starts_with("2")))+1]) %>%
  arrange(desc(highest_value), desc(max_col)) %>%
  select(-c(highest_value, max_col)) 

all.equal(result, test, check.attributes = FALSE) 
# > [1] TRUE