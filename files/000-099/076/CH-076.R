library(tidyverse)
library(readxl)

path = "files/CH-076 Reverse Stepped Tax.xlsx"

input1 = read_xlsx(path, range = "B2:D7")
input2 = read_xlsx(path, range = "F2:G7")
test   = read_xlsx(path, range = "F2:H7")

in1 = input1 %>%
  mutate(To = ifelse(To == "Over", Inf, as.numeric(To))) %>%
  mutate(max_tax = round(cumsum((To - From) * `Tax Rate`),0))

in2 = input2 %>%
  crossing(in1) %>%
  mutate(tax_in_max_thr = Tax - lag(max_tax), .by = `Person ID`) %>%
  filter(tax_in_max_thr > 0) %>%
  filter(tax_in_max_thr == min(tax_in_max_thr), .by = `Person ID`) %>%
  mutate(income = From + tax_in_max_thr / `Tax Rate`)

diff = test$Income - in2$income
# [1] -1.000000 -1.421053  1.076923 -1.052632 -2.567568
# discrepancies caused by rounding errors
