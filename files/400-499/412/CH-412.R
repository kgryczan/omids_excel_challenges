library(tidyverse)
library(readxl)

path <- "400-499/412/CH-412 Matrix Normalization.xlsx"
input <- read_excel(path, range = "C4:F7", col_names = FALSE) %>% as.matrix()
test <- read_excel(path, range = "J4:M7", col_names = FALSE) %>% as.matrix()

result <- t(t(input) - diag(input))

all.equal(result, test)
# [1] TRUE
