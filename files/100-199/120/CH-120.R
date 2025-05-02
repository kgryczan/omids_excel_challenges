library(tidyverse)
library(readxl)

path = "files/CH-120 payments Durations.xlsx"
input1 = read_excel(path, range = "B2:D14")
input2 = read_excel(path, range = "F2:H7")
test  = read_excel(path, range = "K2:L14")
test = test %>%
  mutate(Duration = ifelse(is.na(as.numeric(Duration)), Duration, as.character(round(as.numeric(Duration), 0))))


rec = input1 %>%
  mutate(ID = factor(ID, levels = paste0("C", 1:12), ordered = TRUE)) %>%
  uncount(Cost, .remove = FALSE) %>%
  mutate(Cost = 1, rn = row_number())

pay = input2 %>%
  mutate(ID = factor(ID, levels = paste0("P", 1:5), ordered = TRUE)) %>%
  uncount(Payment, .remove = FALSE) %>%
  mutate(Payment = 1, rn = row_number())

all = full_join(rec, pay, by = "rn") %>%
  mutate(pay_time = Date.y - Date.x) %>%
  summarise(amount = sum(Cost), .by = c(ID.x, ID.y, pay_time)) %>%
  summarise(mean_time = as.character(round(sum(pay_time * amount) / sum(amount)),0), .by = ID.x) %>%
  replace_na(list(mean_time = "NP")) %>%
  mutate(ID.x = as.character(ID.x))

all.equal(test, all, check.attributes = FALSE)
#> [1] TRUE
