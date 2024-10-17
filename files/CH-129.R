library(tidyverse)
library(readxl)

path = "files/CH-129 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26") %>% janitor::clean_names()
test  = read_excel(path, range = "G2:I4")


result = input %>%
  mutate(a = cumsum(lag(stock_price, default = 0) > stock_price),
         d = cumsum(lag(stock_price, default = 0) < stock_price)) %>%
  mutate(a_n = ifelse(n() > 2, a, NA), .by = a) %>%
  mutate(d_n = ifelse(n() > 2, d, NA), .by = d) %>%
  mutate(check = case_when(
    !is.na(a_n) & is.na(d_n) ~ a_n,
    !is.na(d_n) & is.na(a_n) ~ d_n,
    !is.na(a_n) & !is.na(d_n) ~ pmin(a_n, d_n),
    TRUE ~ NA_real_
  )) %>%
  mutate(diff = stock_price - lag(stock_price, default = 0)) %>%
  mutate(sign = sign(median(diff)), 
         Group = ifelse(sign == 1, "Upward", "Downward"),
         .by = check) %>%
  summarise(n = n(), .by = c(Group,check)) %>%
  summarise(`AVG Lenght` = mean(n), `Max Length` = max(n), .by = Group)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE