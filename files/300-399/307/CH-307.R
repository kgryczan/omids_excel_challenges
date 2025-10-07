library(tidyverse)
library(readxl)

path = "files/300-399/307/CH-307 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "G2:H4")

result = input %>%
  mutate(Group = (row_number() - 1) %% 2 + 1) %>%
  summarise(`Total Sales` = sum(Sales), .by = Group) 

all.equal(result, test)
# [1] TRUE