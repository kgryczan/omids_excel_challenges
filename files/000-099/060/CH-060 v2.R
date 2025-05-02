library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-060 Match payments.xlsx", range = "B2:D14")
input2 = read_excel("files/CH-060 Match payments.xlsx", range = "F2:H7")
test   = read_excel("files/CH-060 Match payments.xlsx", range = "K2:P14")


rec = input1 %>%
  mutate(ID = factor(ID, levels = paste0("C", 1:12), ordered = TRUE)) %>%
  uncount(Cost, .remove = FALSE) %>%
  mutate(Cost = 1, rn = row_number())

pay = input2 %>%
  mutate(ID = factor(ID, levels = paste0("P", 1:5), ordered = TRUE)) %>%
  uncount(Payment, .remove = FALSE) %>%
  mutate(Payment = 1, rn = row_number())

all = full_join(rec, pay, by = "rn") %>%
  summarise(Value = sum(Payment), .by = c("ID.x", "ID.y")) %>%
  pivot_wider(names_from = "ID.y", values_from = "Value") %>%
  select(-"NA") %>%
  mutate(across(everything(), as.character))
