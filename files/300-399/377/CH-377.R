library(tidyverse)
library(readxl)

path <- "300-399/377/CH-377 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F8")

digit_sum <- function(x, pattern) {
  x |>
    str_extract_all(pattern) |>
    map_dbl(~ sum(as.numeric(.x), na.rm = TRUE))
}

result <- input |>
  mutate(
    even_sum = digit_sum(ID, "[02468]"),
    odd_sum = digit_sum(ID, "[13579]")
  ) |>
  filter(xor(even_sum < 10, odd_sum > 10))

all.equal(result$ID, test$ID)
# ST2467 doesn't match conditions.
