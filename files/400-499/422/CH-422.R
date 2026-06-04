library(tidyverse)
library(readxl)
library(matricks)

path <- "400-499/422/CH-422 Matrix Normalization.xlsx"
input <- read_excel(path, range = "C4:F7", col_names = FALSE) %>%
  as.matrix()
test <- read_excel(path, range = "J4:M7", col_names = FALSE) %>%
  as.matrix()

result = input - antidiag(input)
all.equal(result, test)
#> [1] TRUE
