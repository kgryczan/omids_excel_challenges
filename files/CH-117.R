library(tidyverse)
library(readxl)

path = "files/CH-117 Add Index Column.xlsx"
input = read_excel(path, range = "B2:C13")
test  = read_excel(path, range = "E2:G13")

result = input %>%
  mutate(index = row_number(), .by = Stock)

all.equal(result, test)
#> [1] TRUE