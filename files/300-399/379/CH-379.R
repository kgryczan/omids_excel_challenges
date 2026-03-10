library(tidyverse)
library(readxl)

path <- "300-399/379/CH-379 Filter.xlsx"
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
# GH9087 and PQ1357 dont meet condition of "either or",
# but met if there would be "normal or" == "one or the other or both".
