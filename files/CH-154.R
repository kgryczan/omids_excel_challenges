library(tidyverse)
library(readxl)

path = "files/CH-154 Custom Index Column.xlsx"
input = read_excel(path, range = "B2:C13")
test  = read_excel(path, range = "E2:G13")

result = input %>%
  mutate(index = cumsum(c(0, diff(Date)) != 1)) 

all.equal(result$index, test$index)
#> [1] TRUE          