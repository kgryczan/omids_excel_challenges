library(tidyverse)
library(readxl)
library(MESS)

path = "files/CH-002.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "H2:J19")

result = input %>%
  mutate(Group = cumsumbinning(Cost, 120))

all.equal(result$Group, test$Group, check.attributes = FALSE)
#> [1] TRUE