library(tidyverse)
library(readxl)

input = read_excel("files/CH-019 Suduku in Excel.xlsx", range = "B3:G8",
                   col_names = FALSE) %>% 
  mutate_all(as.numeric)
test  = read_excel("files/CH-019 Suduku in Excel.xlsx", range = "O3:T8",
                   col_names = FALSE) 

row_na = apply(input, 1, function(x) sum(is.na(x)))
row_na = which(row_na == 1)
for (r in 1:length(row_na)) {
  input[row_na[r], which(is.na(input[row_na[r],]))] = 21 - sum(input[row_na[r],], na.rm = TRUE)
}
col_na = apply(input, 2, function(x) sum(is.na(x)))
col_na = which(col_na == 1)
for (c in 1:length(col_na)) {
  input[which(is.na(input[,col_na[c]])), col_na[c]] = 21 - sum(input[,col_na[c]], na.rm = TRUE)
}
row_na = apply(input, 1, function(x) sum(is.na(x)))
row_na = which(row_na == 1)
for (r in 1:length(row_na)) {
  input[row_na[r], which(is.na(input[row_na[r],]))] = 21 - sum(input[row_na[r],], na.rm = TRUE)
}
col_na = apply(input, 2, function(x) sum(is.na(x)))
col_na = which(col_na == 1)
for (c in 1:length(col_na)) {
  input[which(is.na(input[,col_na[c]])), col_na[c]] = 21 - sum(input[,col_na[c]], na.rm = TRUE)
}

missing = which(is.na(input), arr.ind = TRUE)
col_of_missing = missing[,2] %>% unique()
row_of_missing = missing[,1] %>% unique()

first_row = setdiff(1:6, input[row_of_missing[1],])
second_row = setdiff(1:6, input[row_of_missing[2],]) 

first_col = input[, col_of_missing[1]] %>% na.omit() %>% pull() %>% setdiff(1:6,.)
second_col = input[, col_of_missing[2]] %>% na.omit() %>% pull() %>% setdiff(1:6,.)

input[row_of_missing[1], col_of_missing[1]] <- intersect(first_row, first_col) 
input[row_of_missing[2], col_of_missing[2]] <- intersect(second_row, second_col)

row_na = apply(input, 1, function(x) sum(is.na(x)))
row_na = which(row_na == 1)
for (r in 1:length(row_na)) {
  input[row_na[r], which(is.na(input[row_na[r],]))] = 21 - sum(input[row_na[r],], na.rm = TRUE)
}

identical(input, test)
# [1] TRUE

