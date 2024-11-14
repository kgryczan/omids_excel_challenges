library(tidyverse)
library(readxl)

path = "files/CH-143 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26")
test  = read_excel(path, range = "G2:H6")

result = input %>%
  mutate(wday = floor_date(Date, unit = "week", week_start = 5)) %>%
  mutate(Group = cumsum(c(1, diff(wday) != 0))) %>%
  summarize(`Total Sales` = sum(Sales), .by = Group)

all.equal(result, test)
#> [1] TRUE
