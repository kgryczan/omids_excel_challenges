library(tidyverse)
library(readxl)

path = "files/CH-216 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:F7")

result = input %>%
  extract(ID, into = c("Prefix", "Root", "Suffix"),
          regex = "^([A-Z]{2})(.*)([A-Za-z0-9]{1})$")

all.equal(result, test)
#> [1] TRUE