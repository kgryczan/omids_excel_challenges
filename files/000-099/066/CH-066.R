library(tidyverse)
library(readxl)
library(unpivotr)

input = read_excel("files/CH-066 Merged cells.xlsx", range = "B2:G8", col_names = F)
test  = read_excel("files/CH-066 Merged cells.xlsx", range = "I2:L17")

result = input %>% 
  as_cells() %>%
  behead("up-left", "scenario") %>%
  behead("up", "Year") %>%
  behead("left", "Department") %>%
  select(Department, Year, scenario, dbl, chr) %>%
  mutate(value = case_when(
    !is.na(dbl) ~ dbl,
    !is.na(chr) ~ as.numeric(chr),
    TRUE ~ NA_real_
  ),
  Year = as.numeric(Year)) %>%
  select(-dbl, -chr) %>%
  pivot_wider(names_from = scenario, values_from = value)

identical(result, test)
# [1] TRUE