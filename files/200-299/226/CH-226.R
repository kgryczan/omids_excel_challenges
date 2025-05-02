library(tidyverse)
library(readxl)

path = "files/CH-226 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:F7")

result = input %>% separate(ID, into = c("ID1", "ID2", "ID3"), sep = "(?<=[A-Za-z])(?=[A-Za-z])")
