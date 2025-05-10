library(tidyverse)
library(readxl)

path = "files/200-299/231/CH-231 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:F7")

result = input %>%
  extract(
    ID,
    into = c("Before Symbol", "Symbol", "After Symbol"),
    regex = "([[:alnum:]]+)([^[:alnum:]]+)([[:alnum:]]+)",
    remove = TRUE
  )

all.equal(result, test)
#> [1] TRUE
