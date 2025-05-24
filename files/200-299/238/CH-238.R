library(tidyverse)
library(readxl)

path = "files/200-299/238/CH-238 Consecutive Numbers.xlsx"
input = read_excel(path, range = "B2:B19")
test = read_excel(path, range = "D2:E19")

result = input %>%
  mutate(group = cumsum(Numbers - lag(Numbers, default = first(Numbers)) != 1)) %>%
  mutate(Count = ifelse(n() == 1, "-", as.character(n())), .by = group) %>%
  select(Numbers, Count)

all.equal(result, test) # One row is different
