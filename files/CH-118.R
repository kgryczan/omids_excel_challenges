library(tidyverse)
library(readxl)

path = "files/CH-118 DSO.xlsx"
input1 = read_excel(path, range = "B2:D25")
input2 = read_excel(path, range = "F2:G5")
test  = read_excel(path, range = "H2:H5")

r1 = input1 %>%
  arrange(Customer, desc(Date))

r2 = input2 %>%
  left_join(r1, by = "Customer") %>%
  mutate(days = as.Date("2024/08/31") - as.Date(Date)) %>%
  mutate(cumsum = cumsum(Sales), .by = Customer) %>%
  mutate(balance_cover = ifelse(cumsum <= Balance, Sales, Balance - (cumsum - Sales))) %>%
  filter(balance_cover > 0) %>%
  mutate(weighted_days = days * balance_cover) %>%
  summarise(weighted_days = as.numeric(sum(weighted_days) / sum(balance_cover)), .by = Customer)

all.equal(r2$weighted_days, test$`DSO (day)`, check.attributes = FALSE)
#> [1] TRUE