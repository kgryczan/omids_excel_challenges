library(tidyverse)
library(readxl)

path = "files/CH-221 Combining the columns.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "E2:E7")

result = input %>%
  mutate(Text = str_remove_all(Text, "[a-z]"))

all.equal(result, test)
#> [1] TRUE
