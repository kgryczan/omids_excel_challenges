library(tidyverse)
library(readxl)

path = "files/CH-103 Custom Average.xlsx"
input = read_excel(path, range = "B2:D21")
test = read_excel(path, range = "I2:J6")

today = as.POSIXct(as.Date("2024-08-20"))

result = input %>%
  mutate(del_time = as.numeric(`Delivery Date` - `Order Date`),
         adj_del_time = ifelse(is.na(`Delivery Date`), today - `Order Date`, del_time)) %>%
  mutate(avg_del_time = mean(del_time, na.rm = T), .by = `Product ID`) %>%
  filter(!is.na(del_time) | adj_del_time >= avg_del_time) %>%
  summarise(`Avg delivery time` = mean(adj_del_time, na.rm = T), .by = `Product ID`) %>%
  arrange(`Product ID`)

identical(result$`Avg delivery time`, test$`Avg delivery time`)
#> [1] TRUE