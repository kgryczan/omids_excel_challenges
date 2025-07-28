library(tidyverse)
library(readxl)

path = "files/200-299/271/CH-271 Randomly Reorder rows.xlsx"
input = read_excel(path, range = "B2:E9")

result = input[sample(nrow(input)),]
