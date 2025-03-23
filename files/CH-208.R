library(tidyverse)
library(readxl)

path = "files/CH-208 Matrix Calculation.xlsx"
input1 = read_excel(path, range = "C3:D4", col_names = FALSE) %>% as.matrix()
input2 = read_excel(path, range = "C6:E8", col_names = FALSE) %>% as.matrix()
input3 = read_excel(path, range = "C10:G14", col_names = FALSE) %>% as.matrix()
test1  = read_excel(path, range = "K3", col_names = FALSE) %>% pull()
test2  = read_excel(path, range = "K6", col_names = FALSE) %>% pull()
test3  = read_excel(path, range = "K10", col_names = FALSE) %>% pull()

result1 = sum(diag(input1))
result2 = sum(diag(input2))
result3 = sum(diag(input3))

all.equal(result1, test1) # TRUE
all.equal(result2, test2) # TRUE
all.equal(result3, test3) # TRUE