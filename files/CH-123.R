library(tidyverse)
library(readxl)

path = "files/CH-123 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26")
test  = read_excel(path, range = "G2:H5")


result = input %>%
  mutate(Group = (row_number() - 1) %/% 10 + 1) %>%
  summarise(`Total Sales` = sum(Sales),
            .by = Group)

all.equal(result, test)
#> [1] TRUE