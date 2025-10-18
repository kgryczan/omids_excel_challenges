library(tidyverse)
library(readxl)

path = "files/300-399/312/CH-312 Remove Duplicate Values.xlsx"
input = read_excel(path, range = "B2:E11")
test  = read_excel(path, range = "G2:J7")

result = input %>%
  rowwise() %>%
  mutate(set = list(sort(unique(c_across(-ID))))) %>%
  ungroup() %>%
  distinct(set, .keep_all = TRUE) %>%
  select(-set)

all.equal(result, test)
# [1] TRUE