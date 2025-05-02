library(tidyverse)
library(readxl)

input = read_excel("files/CH-043 Sort Table columns .xlsx", range = "B2:G9")
test  = read_excel("files/CH-043 Sort Table columns .xlsx", range = "J2:O9")

result =   input %>% select(Regions, names(sort(colSums(select(., -Regions)), decreasing = TRUE)))

identical(result, test)
# [1] TRUE