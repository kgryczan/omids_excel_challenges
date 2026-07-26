library(tidyverse)
library(readxl)

path <- "400-499/448/CH-448 Number Puzzles - Spy Number.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

is_spy <- function(number) {
  digits <- as.integer(str_split(as.character(number), "", simplify = TRUE))
  sum(digits) == prod(digits)
}

nearest_spy <- function(number) {
  for (distance in seq_len(number) - 1) {
    candidates <- c(number - distance, number + distance)
    hits <- candidates[candidates > 0 & map_lgl(candidates, is_spy)]
    if (length(hits)) return(hits[[1]])
  }
}

result <- input %>%
  mutate(nearest_spy = map_dbl(Number, nearest_spy)) %>%
  rename("Nearest Spy Number" = nearest_spy)

all.equal(result[["Nearest Spy Number"]], test[["Nearest Spy Number"]])
# Wrong answer provides
