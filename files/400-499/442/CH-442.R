library(tidyverse)
library(readxl)

path <- "400-499/442/CH-442 Matrix Normalization.xlsx"
input <- read_excel(path, range = "C4:F7", col_names = FALSE) %>% as.matrix()
test <- read_excel(path, range = "J4:M7", col_names = FALSE) %>% as.matrix()

result <- input / (max(diag(input)) - min(diag(input)))

all(result == test)
# True
