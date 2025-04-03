library(tidyverse)
library(readxl)

path = "files/CH-213 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C18")
test  = read_excel(path, range = "G2:H5")

result = count(input, cut(Temperature, c(-Inf, 10, 24, Inf), c("Cold", "Mild", "Hot"))) %>%
  select(Group = 1, `No Days` = 2) %>%
  mutate(Group = as.character(Group))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE