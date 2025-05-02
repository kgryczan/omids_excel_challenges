library(tidyverse)
library(readxl)

path = "files/CH-158 Filter the last transaction in mounth.xlsx"
input = read_excel(path, range = "B2:D14")
test  = read_excel(path, range = "F2:H6")

result = input %>% 
  group_by(`Product ID`, month = month(Date)) %>%
  filter(Date == max(Date)) %>%
  ungroup() %>%
  select(-month)

all.equal(result, test)
# [1] TRUE