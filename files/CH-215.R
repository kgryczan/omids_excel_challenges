library(tidyverse)
library(readxl)

path = "files/CH-215 Missing Char.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:D7")

result = input %>%
  mutate(rn = row_number()) %>%
  separate_rows(ID, sep =  "") %>%
  filter(ID != "") %>%
  mutate(is_letter = str_detect(ID, "[a-zA-Z]")) %>%
  mutate(rn2 = row_number(), .by = c(rn, is_letter)) %>%
  mutate(final = ifelse(is_letter, ID, rn2)) %>%
  summarise(ID = paste(final, collapse = ""), .by = rn)

all.equal(result$ID, test$ID)
#> [1] TRUE