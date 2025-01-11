library(tidyverse)
library(readxl)

path = "files/CH-172 Performance  Optimization.xlsx"
input = read_excel(path, range = "R2C2:R250000C3") 
test  = read_excel(path, range = "E2:F7")

tictoc::tic()
result = input %>%
  arrange(`Date Houre`) %>%
  slice_max(Value - lag(Value), n = 5) %>%
  arrange(desc(Value)) 
tictoc::toc()
# 0.01 to 0.05 sec elapsed in few attempts.

all.equal(result, test)
# [1] TRUE