library(tidyverse)
library(readxl)

path = "files/200-299/246/CH-246 Table Transformation.xlsx"
input = read_excel(path, range = "B2:H6")
test = read_excel(path, range = "B10:E14")

result = input %>%
  select_if(~ any(str_detect(., "\\*")))

all.equal(result, test)
#> [1] TRUE
