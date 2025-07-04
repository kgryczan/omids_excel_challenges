library(tidyverse)
library(readxl)
library(slider)

path = "files/200-299/259/CH-259 Extract from Text.xlsx"
input = read_excel(path, range = "B2:B3") %>% pull()
test  = read_excel(path, range = "D2:D3") %>% pull()

pattern = "[A-Z][a-z][0-9]-[0-9]{2}[A-Z][a-z]"
chars = str_split(input, "", simplify = TRUE)

windows = slide_chr(
  .x = seq_len(length(chars) - 7),
  .f = ~ str_c(chars[.x:(.x + 7)], collapse = "")
)
matches = windows[str_detect(windows, pattern)] %>%
  str_c(collapse = ", ")

all.equal(matches, test) 
#> [1] TRUE