library(tidyverse)
library(readxl)

input = read_excel("files/CH-025 ABC analysis.xlsx", range = "B2:D14")
test  = read_excel("files/CH-025 ABC analysis.xlsx", range = "L2:M14")

result = input %>%
  mutate(avg_spend_value = `AVG Inventory (unit)` * `Value per unit ($)`) %>%
  arrange(desc(avg_spend_value)) %>%
  mutate(total_spend = sum(avg_spend_value),
         cum_spend = cumsum(avg_spend_value),
         cum_percent = cum_spend / total_spend * 100,
         Class = case_when(
           cum_percent <= 80 & row_number() <= n() * 0.2 ~ "A",
           cum_percent <= 95 & row_number() <= n() * 0.5 ~ "B",
           TRUE ~ "C"
         )) %>%
  select(Product = `Item Code`, Class)

