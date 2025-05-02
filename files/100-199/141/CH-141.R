library(tidyverse)
library(readxl)

path = "files/CH-141 Fill UP and Down.xlsx"
input = read_excel(path, range = "C2:D13")

result = input %>%
  group_by(ID) %>%
  fill(Value, .direction = "downup") 

# As result is not filled with numbers, but highlighted to show which value is proper.
# We need to validate it by eye, but it is correct.