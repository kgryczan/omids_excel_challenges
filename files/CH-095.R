library(tidyverse)
library(readxl)

path = "files/CH-095 Last Inventory.xlsx"
input = read_excel(path, range = "B2:G7")
test  = read_excel(path, range = "I2:J7")


result = input %>%
  rowwise() %>%
  mutate(`Last Inventory` = last(na.omit(c_across(-Product)))) %>%
  ungroup() %>%
  select(c(1,7))

identical(result, test)         
# [1] TRUE