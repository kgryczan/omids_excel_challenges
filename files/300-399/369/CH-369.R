library(tidyverse)
library(readxl)

path <- "300-399/369/CH-369 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:E10")
test <- read_excel(path, range = "H3:I5")

result = input %>%
  mutate(rn = row_number()) %>%
  mutate(
    group = case_when(
      row_number() < ceiling(n() / 2) ~ "Group 1",
      row_number() > ceiling(n() / 2) ~ "Group 2",
      TRUE ~ "Middle"
    )
  ) %>%
  group_by(group) %>%
  summarise(sum_value = sum(`Total Sales`, na.rm = TRUE)) %>%
  pivot_wider(names_from = group, values_from = sum_value) %>%
  mutate(
    `Group 1` = `Group 1` + if_else(`Group 1` < `Group 2`, Middle, 0),
    `Group 2` = `Group 2` + if_else(`Group 2` <= `Group 1`, Middle, 0)
  ) %>%
  select(`Group 1`, `Group 2`) %>%
  pivot_longer(everything(), names_to = "IDs", values_to = "Sales")

all.equal(result, test)
## [1] TRUE
