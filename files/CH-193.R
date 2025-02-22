library(tidyverse)
library(readxl)

path = "files/CH-193 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C37")
test  = read_excel(path, range = "G2:H4")

result = input %>%
  mutate(Group = ifelse(wday(Date, week_start = 1) >= 6, "Weekend", "Weekday")) %>%
  summarise(`Total Sales` = sum(Sales), .by = Group)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE