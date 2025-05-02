library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-060 Match payments.xlsx", range = "B2:D14")
input2 = read_excel("files/CH-060 Match payments.xlsx", range = "F2:H7")
test   = read_excel("files/CH-060 Match payments.xlsx", range = "K2:P14")
names(test)[1] = "ID"

receipts = input1 %>%
  mutate(rec_cum = cumsum(Cost),
         prev_rec_cum = lag(rec_cum, default = 0))

payments = input2 %>%
  mutate(pay_cum = cumsum(Payment),
         prev_pay_cum = lag(pay_cum, default = 0))

matched = receipts %>%
  left_join(payments, by = join_by(overlaps(prev_rec_cum, rec_cum, prev_pay_cum, pay_cum, bounds = "()")))

matched = matched %>%
  mutate(match = pmin(rec_cum, pay_cum),
         match = c(first(match), diff(match))) %>%
  group_by(ID.x) %>%
  mutate(match = ifelse(prev_rec_cum < pay_cum, match, 0)) %>%
  ungroup() %>%
  fill(Date.y)

result = matched %>%
  select(ID.x, ID.y, match) %>%
  mutate(match = as.character(match)) %>%
  pivot_wider(id_cols = ID.x, names_from = ID.y, values_from = match) %>%
  rename(ID = ID.x) %>%
  select(-`NA`) %>%
  mutate(check = if_else(reduce(across(2:6, ~is.na(.x)), `&`), "No", "Yes")) %>%
  rowwise() %>%
  mutate(across(2:6, ~if_else(check == "No", "NP", .))) %>%
  ungroup() %>%
  select(-check)

identical(result, test)
# [1] TRUE