library(tidyverse)
library(readxl)

path <- "400-499/429/CH-429 Filter.xlsx"
input <- read_excel(path, range = "B3:D8")
test <- read_excel(path, range = "H3:J7")

result = input %>%
  slice_max(order_by = Sales, n = 2, by = Customer)

all.equal(result, test)
# [1] TRUE
