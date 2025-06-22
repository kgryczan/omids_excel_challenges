library(tidyverse)
library(readxl)

path = "files/200-299/253/CH-253 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26")
test  = read_excel(path, range = "G2:H6")

result = input %>%
  arrange(Date) %>%
  mutate(Group = cumsum(c(T, diff(Date)/68400 >= 2))) %>%
  summarise(`Total Sales` = sum(Sales, na.rm = T), .by = Group) 

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE