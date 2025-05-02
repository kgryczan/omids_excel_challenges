library(tidyverse)
library(readxl)

path = "files/CH-116 Remove rows and colums.xlsx"
input = read_excel(path, range = "B2:H8") %>%
  column_to_rownames(var = "...1") %>%
  as.matrix()

test  = read_excel(path, range = "J2:M5") %>%
  column_to_rownames(var = "...1") %>%
  as.matrix()

result = input[seq(1, nrow(input), 2), seq(1, ncol(input), 2)]

all.equal(result, test)  
#> [1] TRUE