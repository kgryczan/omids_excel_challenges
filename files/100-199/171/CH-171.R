library(tidyverse)
library(readxl)

path = "files/CH-171 Table Transformation.xlsx"
input = read_excel(path, range = "C2:C148")
test = read_excel(path, range = "E2:H8") %>%
  mutate(across(c(From, To), ~ str_replace(., "availabe", "available")))

r1 = input %>% filter(row_number() %% 2 == 1)
r2 = input %>% filter(row_number() %% 2 == 0) %>% rename(Value = Name)

result = cbind(r1, r2) %>%
  filter(Name %in% c('From', 'To', 'Status') | Value == "Process") %>%
  mutate(group = ifelse(Value == "Process", Name, NA)) %>%
  fill(group) %>%
  filter(group != Name) %>%
  pivot_wider(names_from = Name, values_from = Value)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE