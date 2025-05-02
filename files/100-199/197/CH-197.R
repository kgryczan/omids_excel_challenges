library(tidyverse)
library(readxl)

path = "files/CH-197 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "G2:H7")

result = input %>%
  mutate(Date = as.Date(Date, format = "%Y-%m-%d")) %>%
  complete(Date = seq.Date(min(Date), max(Date), by = "day")) %>%
  replace_na(list(Sales = 0)) %>%
  mutate(group_ends = ifelse(Sales == 0, cumsum(Sales == 0) %% 2, NA)) %>%
  group_by(group_ends) %>%
  mutate(Group = cumsum(group_ends == 0)) %>%
  ungroup() %>%
  mutate(Group = ifelse(Group == 0, NA, Group)) %>%
  fill(Group, .direction = "up") %>%
  mutate(Group = ifelse(is.na(Group), max(Group, na.rm = TRUE) + 1, Group)) %>%
  summarise(`Total Sales` = sum(Sales, na.rm = TRUE), .by = Group)

# # A tibble: 6 × 2
# Group `Total Sales`
# <dbl>         <dbl>
# 1     1           137
# 2     2            27
# 3     3            89
# 4     4            51
# 5     5            53
# 6     6            23