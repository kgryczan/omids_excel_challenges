library(tidyverse)
library(readxl)

path = "files/CH-185 Replace consecutive X.xlsx"
input = read_excel(path, range = "C2:D10")
test  = read_excel(path, range = "F2:G10")

result = input %>%
  mutate(ID = str_replace_all(ID, "[Xx]+", "X"))

all.equal(result, test)
#> [1] TRUE