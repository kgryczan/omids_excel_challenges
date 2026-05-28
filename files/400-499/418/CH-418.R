library(tidyverse)
library(readxl)

path <- "400-499/418/CH-418 Number Puzzles - Self Number.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

self_number <- function(n) {
  n + sum(as.integer(strsplit(as.character(n), "")[[1]]))
}
is_self_number <- function(n) {
  n <= 1 || !n %in% map_int(seq_len(n - 1), self_number)
}

result = input %>%
  mutate(is_self_number = map_lgl(Number, is_self_number))
# It has different results.
