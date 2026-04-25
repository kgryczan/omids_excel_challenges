library(tidyverse)
library(readxl)

path <- "400-499/402/CH-402 Matrix Normalization.xlsx"
input <- read_excel(path, range = "C4:F7", col_names = FALSE) %>% as.matrix()
test <- read_excel(path, range = "J4:M7", col_names = FALSE) %>% as.matrix()

normalized_input <- sweep(input, 1, diag(input), "-")
all.equal(normalized_input, test)
#> [1] TRUE
