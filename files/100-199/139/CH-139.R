library(tidyverse)
library(readxl)

path = "files/CH-139 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26") %>% janitor::clean_names()
test  = read_excel(path, range = "G2:H4")


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
  mutate(perc_diff_dod = diff / lag(stock_price, default = 0)) %>%
  mutate(first_value = first(stock_price),
         cumsum_per_check = cumsum(lead(diff,1)),
         ratio = cumsum_per_check / first_value ,
         .by = check) %>%
  mutate_at(vars(perc_diff_dod, ratio), ~replace(., is.infinite(.), 0)) %>%
  summarise(Increase = pmax(max(perc_diff_dod, na.rm = T), max(ratio, na.rm = T)),
            Decrease = pmin(min(perc_diff_dod, na.rm = T), min(ratio, na.rm = T))) %>%
  pivot_longer(cols = everything(),  names_to = "Group", values_to = "Percent")
            
all.equal(result, test, check.attributes = F)
# [1] TRUE