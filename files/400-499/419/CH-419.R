library(tidyverse)
library(readxl)

path <- "400-499/419/CH-419 Filter.xlsx"
input <- read_excel(path, range = "B3:C7")
test <- read_excel(path, range = "G3:H5")
colnames(test) = colnames(input)

result = input %>%
  filter(Sales > mean(Sales), .by = Product)

all.equal(result, test)
# [1] TRUE
