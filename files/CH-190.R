library(tidyverse)
library(readxl)

path = "files/CH-190 Convert Text to number.xlsx"
input = read_excel(path, range = "B2:B5")
test  = read_excel(path, range = "D2:D5")

library(reticulate)
w2n = import("word2number")$w2n

result = input %>%
  mutate(Output = map_dbl(Date, ~w2n$word_to_num(.x))) %>%
  select(Output)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE