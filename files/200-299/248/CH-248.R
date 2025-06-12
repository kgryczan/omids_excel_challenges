library(tidyverse)
library(readxl)

path = "files/200-299/248/CH-248 Time Difference.xlsx"
input = read_excel(path, range = "B2:D15")
test = read_excel(path, range = "G2:H5")

result = input %>%
  arrange(`User ID`) %>%
  mutate(Consecutive = lag(`User ID`) == `User ID` & lag(Action) == Action) %>%
  filter(Consecutive != T | is.na(Consecutive)) %>%
  select(-Consecutive) %>%
  mutate(run = cumsum(Action == "Login")) %>%
  pivot_wider(names_from = Action, values_from = Time) %>%
  mutate(Duration = as.numeric(difftime(Logout, Login, units = "hours"))) %>%
  summarise(`Time (Hour)` = floor(sum(Duration, na.rm = TRUE)), .by = `User ID`)

all.equal(result, test)
# [1] TRUE
