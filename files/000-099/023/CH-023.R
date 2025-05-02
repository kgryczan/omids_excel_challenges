library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-023 Advance Weighted AVG.xlsx", range = "B2:E18")
input2 = read_excel("files/CH-023 Advance Weighted AVG.xlsx", range = "G2:J5")
test   = read_excel("files/CH-023 Advance Weighted AVG.xlsx", range = "L2:M5")

prod = input2 %>%
  pivot_longer(cols = -Month, names_to = "Machine Code", values_to = "value") 

result = input1 %>%
  group_by(Month, `Machine Code`) %>%
  summarise(Avg = mean(`Weight (KG/Meter)`)) %>%
  left_join(prod, by = c("Machine Code", "Month")) %>%
  ungroup() %>%
  group_by(Month) %>%
  summarise(`AVG weight (Kg/Meter)` = sum(Avg * value) / sum(value)) %>%
  mutate(`AVG weight (Kg/Meter)` = round(`AVG weight (Kg/Meter)`, 2)) %>%
  ungroup()

identical(result, test)
# [1] TRUE
