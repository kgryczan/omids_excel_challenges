library(tidyverse)
library(readxl)
library(data.table)


path = "files/CH-124 Merge.xlsx"
input = read_excel(path, range = "B2:C7") %>% as.data.table()
input2  = read_excel(path, range = "H2:H9") %>% as.data.table()
test = read_excel(path, range = "I2:I9")  %>% as.data.table()

result = input[input2, on = "Date", roll = "nearest"]

all.equal(result$price, test$Price, check.attributes = FALSE)
#> [1] TRUE