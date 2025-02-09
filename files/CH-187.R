library(tidyverse)
library(readxl)

path = "files/CH-187 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "G2:H7")

result = input %>%
  mutate(diff = difftime(lead(Date), Date, units = "days") %>% as.numeric()) %>%
  mutate(Group = cumsum(lag(diff, default = 0) > 1) + 1) %>%
  summarise(`Total Sales` = sum(Sales, na.rm = T), .by = Group)

all.equal(result, test)
#> [1] TRUE