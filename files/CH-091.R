library(tidyverse)
library(readxl)

path = "files/CH-091 Extract from table.xlsx"
input = read_excel(path, range = "B2:E6")
test  = read_excel(path, range = "G2:L9") %>%
  arrange(desc(Department), Name) %>%
  mutate(Name = ifelse(Name == "Mije", "Mike", Name))


result = input %>%
  pivot_longer(cols = -c(1), names_to = "Department", values_to = "Name") %>%
  mutate(Value = '✔',
         `Branch NO` = paste0("Branch ", `Branch NO`),
         Name = ifelse(Name == "Daniel", "David", Name)) %>%
  pivot_wider( names_from = "Branch NO", values_from = "Value") %>%
  arrange(desc(Department), Name) %>%
  select(Name, Department, everything())

all.equal(result, test)
# [1] TRUE