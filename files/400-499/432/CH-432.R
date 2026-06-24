library(tidyverse)
library(readxl)
library(matricks)

path <- "400-499/432/CH-432 Matrix Normalization.xlsx"
input <- read_excel(path, range = "C4:F7", col_name = FALSE) %>% as.matrix()
test <- read_excel(path, range = "J4:M7", col_name = FALSE) %>% as.matrix()

result <- sweep(input, 2, rev(antidiag(input)), "-")

all.equal(result, test)
