library(tidyverse)
library(readxl)
library(memoise)

path <- "400-499/403/CH-403 Number Puzzles - Happy Numbers.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

is_happy <- function(x) {
  step <- function(n) sum((as.integer(strsplit(as.character(n), "")[[1]]))^2)
  detect_index(
    accumulate(rep(NA, 100), ~ step(ifelse(.y == 1, x, .x)), .init = x),
    ~ .x == 1
  ) >
    0
}

result = input %>%
  mutate(is_happy = map_lgl(Number, is_happy))
