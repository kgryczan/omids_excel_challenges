library(tidyverse)
library(readxl)

path = "files/CH-004.xlsx"
input = read_excel(path, range = "B2:C17")
test  = read_excel(path, range = "G2:H5")

result = input %>%
  group_by(Person) %>%
  complete(`Mission Date` = seq.Date(min(as.Date(`Mission Date`)), max(as.Date(`Mission Date`)), by = "day")) %>%
  ungroup() %>%
  mutate(wday = wday(`Mission Date`, label = TRUE, locale = "en"),
         is_weekend = wday %in% c("Sat", "Sun")) %>%
  full_join(input %>% mutate(n = 1), by = c("Person", "Mission Date")) %>%
  mutate(n = ifelse(lag(wday) == "Fri" & lag(n) == 1, 1, n), 
         n = ifelse(lag(wday) == "Sat" & lag(n) == 1, 1, n)) %>%
  mutate(cons = consecutive_id(n == 1), .by = Person) %>%
  replace_na(list(n = 0)) %>%
  mutate(cum1 = cumsum(n), .by = c(Person, cons)) %>%
  summarise(cum = sum(cum1), .by = Person)
