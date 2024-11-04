library(tidyverse)
library(readxl)

path = "files/CH-138 Periodic Sales Summary.xlsx"
input = read_excel(path, range = "C2:E27")
test  = read_excel(path, range = "G2:J6")

result = input %>%
  mutate(Month = month(Date),
         day = day(Date), 
         decade_days = paste0("P",ifelse(ceiling(day / 10) == 4, 3, ceiling(day/10)))) %>%
  summarise(`Total Qty` = sum(Qty, na.rm = TRUE), .by = c(decade_days, Month)) %>%
  pivot_wider(names_from = decade_days, values_from = `Total Qty`, values_fill = 0) %>%
  select(Month, P1, P2, P3)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE