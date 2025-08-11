library(tidyverse)
library(readxl)
library(charcuterie)

path = "files/200-299/278/CH-278 Pattern Recognition.xlsx"
input = read_excel(path, range = "B2:C7")
test  = read_excel(path, range = "D2:D7")

result = input %>%
  mutate(`Pattern Length` = map_int(Pattern, \(x) length(rle(strsplit(x, "")[[1]])$lengths) - 1))

all.equal(result$`Pattern Length`, test$`Pattern Length`) 
# > [1] TRUE