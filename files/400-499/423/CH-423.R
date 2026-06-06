library(tidyverse)
library(readxl)
library(memoise)

path <- "400-499/423/CH-423 Number Puzzles - Happy Number.xlsx"
test <- read_excel(path, range = "C3:C10")

digit_square_sum <- function(n) {
  sum(as.integer(str_split_1(as.character(n), ""))^2)
}
reduce_to_digit <- function(n) {
  if (n < 10) n else Recall(digit_square_sum(n))
}

df = tibble(result = 1:1000 + 1e6) %>%
  mutate(reduced = map_dbl(result, reduce_to_digit)) %>%
  filter(reduced %in% c(1, 7)) %>%
  head(7)
