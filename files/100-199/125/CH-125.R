library(tidyverse)
library(readxl)

path = "files/CH-125 Pad middle.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:D9")

innix_pad = function(string) {
  letters = str_extract(string, "[A-Z]+")
  numbers = str_extract(string, "[0-9]+")
  pad_num = 6  - nchar(letters)
  return(paste0(letters, str_pad(numbers, pad_num, side = "left", pad = "0")))
}

result = input %>%
  mutate(ID = map_chr(ID, innix_pad))
all.equal(result, test)
#> [1] TRUE