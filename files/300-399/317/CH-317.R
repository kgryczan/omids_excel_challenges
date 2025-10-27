library(tidyverse)
library(readxl)

path = "files/300-399/317/CH-317 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "G2:H7")

result = input %>%
  mutate(Group = floor(log2(1:nrow(.))) + 1) %>%
  summarise(`Total Sales` = sum(Sales, na.rm = T), .by = Group)

all.equal(result, test)
# [1] TRUE