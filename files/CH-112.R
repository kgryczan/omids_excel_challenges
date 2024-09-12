library(tidyverse)
library(readxl)

path = "files/CH-112 Custom Rank.xlsx"

input = read_excel(path, range = "C2:E6")
test  = read_excel(path, range = "J2:K6")

result = input %>%
  mutate(Rank = rank(desc(`2023` - `2022`))) %>%
  arrange(Rank) %>% 
  select(Rank, Product)

identical(result, test)
# [1] TRUE