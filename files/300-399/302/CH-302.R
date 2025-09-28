library(tidyverse)
library(readxl)

path = "files/300-399/302/CH-302 Remove Duplicate Values.xlsx"
input = read_excel(path, range = "B2:E11")
test  = read_excel(path, range = "G2:J8")

result = input %>%
  mutate(all_sorted = paste(sort(c_across(starts_with("Value"))), collapse = ","), .by = ID) %>%
  distinct(all_sorted, .keep_all = TRUE) %>%
  select(-all_sorted)

all.equal(result, test)
# [1] TRUE