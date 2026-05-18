library(tidyverse)
library(readxl)

path <- "400-499/413/CH-413 Number Puzzles - Happy Number.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

is_happy <- function(n) {
  seen <- integer()
  while (n != 1 && !n %in% seen) {
    seen <- c(seen, n)
    digits <- as.integer(strsplit(as.character(n), "")[[1]])
    n <- sum(digits^2)
  }
  n == 1
}

find_nearest_happy <- function(n) {
  if (is_happy(n)) {
    return(n)
  }

  d <- 1
  repeat {
    lower <- n - d
    upper <- n + d
    if (lower > 0 && is_happy(lower)) {
      return(lower)
    }
    if (is_happy(upper)) {
      return(upper)
    }
    d <- d + 1
  }
}

result = input |>
  mutate(next_happy = map_dbl(Number, find_nearest_happy))
# all results are happy. wrong expected values
