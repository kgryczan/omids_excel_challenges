library(tidyverse)
library(readxl)

input = read_excel("files/CH-038 Duration Since Last Visit.xlsx", range = "B2:C26")
test  = read_excel("files/CH-038 Duration Since Last Visit.xlsx", range = "G2:H6")

dates = seq(as.Date("2024-01-01"), as.Date("2024-04-01"), by = "month") %>%
  as_tibble() %>%
  mutate(end_of_month = value + months(1) - days(1)) %>%
  select(end_of_month) 

ends = expand_grid(Date = dates$end_of_month, `Agent ID` = unique(input$`Agent ID`)) %>%
  mutate(type = "end")

result = input %>%
  mutate(type = "visit") %>%
  bind_rows(ends) %>%
  arrange(`Agent ID`, Date) %>%
  group_by(`Agent ID`) %>%
  mutate(last_visit = if_else(type == "visit", as.Date(as.POSIXct(Date)), NA)) %>%
  fill(last_visit, .direction = "down") %>%
  mutate(month = month(Date)) %>%
  filter(type == "end") %>%
  mutate(datediff = difftime(Date, last_visit, units = "days") %>% as.numeric()) %>%
  ungroup() %>%
  summarise(mean = mean(datediff, na.rm = TRUE), .by = "month")

identical(result$mean, test$`AVG Duration from Last Visit`)
# [1] TRUE
