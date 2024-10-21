library(tidyverse)
library(readxl)

path = "files/CH-131 Table Transformation.xlsx"
input = read_excel(path, range = "C2:I7")
test  = read_excel(path, range = "K2:N12")

result = bind_rows(input[,1:4], input[,c(1,5:7)]) 

all.equal(result, test)
#> [1] TRUE