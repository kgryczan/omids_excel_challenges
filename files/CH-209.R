library(tidyverse)
library(readxl)

path = "files/CH-209 Combining the columns.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "E2:E7")

result = input %>% 
  mutate(rn = row_number()) %>%
  separate_rows(Text, sep = " ") %>%
  mutate(Text = str_sub(Text, 1, 1)) %>%
  summarise(Text = paste(Text, collapse = ""), .by = rn) %>%
  select(-rn)

all.equal(result, test)
#> [1] TRUE