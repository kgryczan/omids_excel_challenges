library(tidyverse)
library(readxl)

path = "files/CH-186 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B8")
test  = read_excel(path, range = "D2:E8") %>%
  mutate_all(~replace_na(., ""))

result = input %>%
  mutate(ID.1 = str_remove_all(ID, "[^aeiouAEIOU]"),
         ID.2 = str_remove_all(ID, "[aeiouAEIOU]")) %>%
  select(-ID)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE         