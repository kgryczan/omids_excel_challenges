library(tidyverse)
library(readxl)
library(lubridate)

path = "files/CH-153 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C11")
test  = read_excel(path, range = "G2:H6")

output = input %>%
  mutate(dates = map2(From, To, seq, by = "1 day")) %>%
  unnest(dates) %>%
  distinct(dates) %>%
  group_by(cons = cumsum(c(0, diff(dates)) != 1)) %>%
  summarise(From = min(dates), To = max(dates)) %>%
  ungroup() %>%
  select(-cons)

all.equal(output, test)
#> [1] TRUE