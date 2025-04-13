library(tidyverse)
library(readxl)

path = "files/CH-218 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:E7")

result = input %>%
  mutate(
    Uppercase = map_chr(str_extract_all(ID, "[A-Z]+"), ~ paste(.x, collapse = "")),
    Lowercase = map_chr(str_extract_all(ID, "[a-z]+"), ~ paste(.x, collapse = "")))