library(tidyverse)
library(readxl)

path = "files/300-399/320/CH-320 Text Cleaning.xlsx"
input = read_excel(path, range = "B1:B7")
test  = read_excel(path, range = "C1:C7")

result = input %>%
  transmute(`Result ID` = parse_number(`Question ID`))

all.equal(result, test)
# [1] TRUE