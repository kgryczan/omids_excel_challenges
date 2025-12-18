library(tidyverse)
library(readxl)

path <- "300-399/343/CH-343 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:C12")
test <- read_excel(path, range = "F3:G7")

result = input %>%
  mutate(ID = str_sub(ID, 1, 2)) %>%
  summarise(Sales = sum(Sales), .by = ID)

all.equal(result, test)
# [1] TRUE
