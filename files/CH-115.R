library(tidyverse)
library(readxl)

path = "files/CH-115 Multi Replacement.xlsx"
input = read_excel(path, range = "B2:E9")
test  = read_excel(path, range = "G2:J9")

result = input %>%
  mutate(across(c(`Product ID`, `Customer ID`), ~str_replace(., "0{3}|q", "-")))

identical(result, test)
#> [1] TRUE