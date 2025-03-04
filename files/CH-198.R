library(tidyverse)
library(readxl)

path = "files/CH-198 Matrix Calculation.xlsx"
input1 = read_excel(path, range = "C3:D4", col_names = FALSE) %>% as.matrix()
input2 = read_excel(path, range = "C6:E8", col_names = FALSE) %>% as.matrix()
input3 = read_excel(path, range = "C10:G14", col_names = FALSE) %>% as.matrix()
test1  = read_excel(path, range = "J3:K4")
test2  = read_excel(path, range = "J6:L7")
test3  = read_excel(path, range = "J10:N11")

process <- function(mat) {
  map_dfc(seq_len(nrow(mat)), ~{
    colname <- paste0("Z", .x)
    tibble(!!colname := sum(mat[.x, ]) + sum(mat[, .x]))
  })
}

output1 = process(input1)
all(output1 == test1) # TRUE

output2 = process(input2)
all(output2 == test2) # TRUE

output3 = process(input3)
all(output3 == test3) # TRUE

