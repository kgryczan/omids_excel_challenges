library(tidyverse)
library(readxl)

path = "files/CH-224 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:E7")

result = input %>%
  separate(
    col = "ID",
    into = c("ID1", "ID2", "ID3", "ID4"),
    sep = "-",
    extra = "merge"
  ) %>%
  unite(col = "ID.1", ID1, ID2, sep = "-", na.rm = TRUE) %>%
  unite(col = "ID.2", ID3, ID4, sep = "-", na.rm = TRUE)

all.equal(result, test)
# [1] TRUE
