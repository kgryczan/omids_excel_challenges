library(tidyverse)
library(readxl)

path = "files/CH-196 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B8")
test  = read_excel(path, range = "D2:E8")

result = input %>%
  mutate(`ID.1` = str_remove_all(ID, "[0-9]"),
         `ID.2` = str_remove_all(ID, "[A-Z]") %>% as.numeric()) %>%
  select(-ID)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE