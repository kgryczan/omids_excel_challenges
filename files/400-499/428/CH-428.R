library(tidyverse)
library(readxl)

path <- "400-499/428/CH-428 Number Puzzles - Self Number.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

digit_sum <- function(x) {
  x |>
    as.character() |>
    str_split("") |>
    map_int(\(digits) sum(as.integer(digits)))
}

closest_self_numbers <- function(x) {
  limit <- max(x) + 9 * nchar(max(x))
  n <- seq_len(limit)

  self_numbers <- setdiff(n, n + digit_sum(n))
  pos <- findInterval(x, self_numbers)

  tibble(
    closest_down = self_numbers[pmax(pos, 1)],
    closest_up = self_numbers[pmin(pos + 1, length(self_numbers))]
  )
}

result <- input |>
  bind_cols(closest_self_numbers(input$Number))

# some of numbers are not matching.
