library(tidyverse)
library(readxl)

path = "files/CH-100 Manage Duplicate Values.xlsx"
input = read_excel(path, range = "B2:B15")
test  = read_excel(path, range = "D2:D15")

result = input %>%
  mutate(row = row_number(), 
         n = n(), 
         .by = `Product ID`) %>%
  mutate(letter = ifelse(n > 1, LETTERS[row], "")) %>%
  select(`Product ID`, letter) %>%
  unite("Product ID", `Product ID`, letter, sep = "")

identical(result, test)
#> [1] TRUE