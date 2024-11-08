library(tidyverse)
library(readxl)
library(slider)

path = "files/CH-140 Golden Period.xlsx"
input = read_excel(path, range = "B2:D26")
test  = read_excel(path, range = "F2:H5")

result = input %>%
  summarise(Qty = sum(Qty), .by = c(Date, Customer)) %>%
  group_by(Customer) %>%
  complete(Date = seq.Date(min(as.Date(Date)), as.Date("2024/11/01"), by = "1 day")) %>%
  left_join(input)  %>%
  replace_na(list(Qty = 0)) %>%
  group_by(Customer) %>%
  mutate(rolling_sum = slide_dbl(Qty, sum, .before = 9, .complete = TRUE)) %>%
  filter(rolling_sum == max(rolling_sum, na.rm = T)) %>%
  filter(Date == max(Date, na.rm = T)) %>% 
  mutate(min_date = Date - days(9)) %>%
  select(Customer, min_date, Date, `Total Qty` = rolling_sum) %>%
  mutate(min_date = format(min_date, "%y-%m-%d"), Date = format(Date, "%y-%m-%d")) %>%
  unite("Period", min_date, Date, sep = " to ")

all.equal(result, test, check.attributes = F)
#> [1] TRUE
