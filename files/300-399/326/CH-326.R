library(tidyverse)
library(readxl)
library(glue)

path = "300-399/326/CH-326 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:E11")
test  = read_excel(path, range = "I2:J5")

result = input %>%
  mutate(
    min_char = pmin(From, To),
    max_char = pmax(From, To)) %>%
  mutate(Group = glue("{min_char}{max_char} or {max_char}{min_char}")) %>%
  summarise(`Total Sales` = sum(Sales), .by = Group)

all.equal(result$`Total Sales`, test$`Total Sales`)
# Values in provided solution not correct. 
# group names are different, because of my choice