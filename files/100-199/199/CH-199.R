library(tidyverse)
library(readxl)

path = "files/CH-199 Combining the columns.xlsx"
input = read_excel(path, range = "B2:E7")
test  = read_excel(path, range = "H2:H7")

result = input %>%
  mutate(result = pmap_chr(
    list(`First Name`, `Middle Name`, `Last Name`, Pattern),
    function(a, b, c, ord_str) {
      order <- as.integer(str_split(ord_str, ",", simplify = TRUE))
      paste(c(a, b, c)[order], collapse = " ")
    }
  )) %>%
  select(result)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE