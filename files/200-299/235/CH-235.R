library(tidyverse)
library(readxl)

path = "files/200-299/235/CH-235 Filtering & Removing.xlsx"
input = read_excel(path, range = "B2:F7")
test = read_excel(path, range = "H2:H6")

result = input %>%
  pivot_longer(-1, values_to = "Value") %>%
  summarise(nums = toString(sort(Value, decreasing = TRUE)), .by = ID) %>%
  distinct(nums, .keep_all = TRUE) %>%
  select(ID)

all.equal(result, test)
#> [1] TRUE
