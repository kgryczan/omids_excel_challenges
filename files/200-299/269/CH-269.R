library(tidyverse)
library(readxl)

path = "files/200-299/269/CH-269 Text Cleaning.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:D9")

result = input %>%
  mutate(ID = str_replace_all(str_remove_all(ID, "-"), "(.)(?=.)", "\\1-"))

all.equal(result$ID, test$`ID 1`, check.attributes = FALSE)
# > [1] TRUE