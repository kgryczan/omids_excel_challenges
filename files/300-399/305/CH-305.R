library(tidyverse)
library(readxl)

path = "files/300-399/305/CH-305 Advanced Calculation.xlsx"
input = read_excel(path, range = "B2:D19")
test  = read_excel(path, range = "H2:I5") 

result = input %>%
  summarise(Index = diff(range(Sales)/mean(Sales[!Sales %in% range(Sales)])), .by = Product)

all.equal(result, test)
# wrong answer for product A