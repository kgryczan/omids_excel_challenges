library(tidyverse)
library(readxl)

path = "files/200-299/266/CH-266 Extract from Text.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:E7")

find_pattern_python_style = function(s) {
  1:(str_length(s) %/% 2) %>%
    map_chr(~ str_sub(s, 1, .x)) %>%
    detect(~ {
      unit_len = str_length(.x)
      repeat_count = str_length(s) %/% unit_len
      repeated = str_dup(.x, repeat_count)
      str_sub(s, 1, unit_len * repeat_count) == repeated
    }, .default = s)
}

result = input %>%
  mutate(Pattern = map_chr(Text, find_pattern_python_style))

all.equal(result$Pattern, test$Pattern) 
# > [1] TRUE