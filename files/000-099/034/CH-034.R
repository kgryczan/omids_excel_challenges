library(tidyverse)
library(readxl)

input = read_excel("files/CH-034 Customer Return Cycle.xlsx", range = "B2:F26")
test  = read_excel("files/CH-034 Customer Return Cycle.xlsx", range = "J2:K6")

result = input %>%
  select(Date, `Customer ID`) %>%
  arrange(`Customer ID`, Date) %>%
  distinct() %>% 
  mutate(lag = lag(Date), .by = `Customer ID`) %>%
  mutate(diff = Date - lag) %>%
  summarise(`Avg Return Cycle` = mean(diff, na.rm = TRUE), .by = `Customer ID`) %>% 
  mutate(`Avg Return Cycle` = as.numeric(`Avg Return Cycle`)) %>%
  select(Customer = `Customer ID`, `Avg Return Cycle`)

identical(result, test)
# [1] TRUE
