library(tidyverse)
library(readxl)

path = "files/CH-212 Remove duplicate.xlsx"
input = read_excel(path, range = "B2:E16")
test  = read_excel(path, range = "G2:G11") %>% arrange(`Item Code`)


value_counts = input %>%
  pivot_longer(cols = everything(), names_to = "Column Title", values_to = "Value") %>%
  summarise(n = n_distinct(`Column Title`), .by  = Value) %>%
  filter(n == 1) %>%
  select(-n) %>%
  arrange(Value)

all.equal(test$`Item Code`, value_counts$Value, check.attributes = FALSE)
#> [1] TRUE