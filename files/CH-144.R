library(tidyverse)
library(readxl)

path = "files/CH-144 First transaction in each month.xlsx"
input = read_excel(path, range = "C2:E27")
test  = read_excel(path, range = "G2:I6")

result = input %>%
  mutate(month = month(Date)) %>%
  filter(row_number() == 1, .by = month) %>%
  select(-month)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE