library(tidyverse)
library(readxl)

path <- "400-499/408/CH-408 Number Puzzles - Self Number.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

self_number <- function(n) {
  n + sum(as.integer(strsplit(as.character(n), "")[[1]]))
}
is_self_number <- function(n) {
  n <= 1 || !n %in% purrr::map_int(seq_len(n - 1), self_number)
}
col <- names(input)[1]
result <- input |>
  mutate(is_self_number = purrr::map_lgl(.data[[col]], is_self_number))

all.equal(result$is_self_number, test[[1]])
# Testing output incorrect.
