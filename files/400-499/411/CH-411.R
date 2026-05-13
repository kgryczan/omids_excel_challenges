library(tidyverse)
library(readxl)

path <- "400-499/411/CH-411 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B9")
test <- read_excel(path, range = "F3:H9")

split_mod <- \(x, n = 3) {
  if (is.na(x)) {
    return(rep(NA_character_, n))
  }
  chars <- str_split_1(x, "")
  idx <- seq_along(chars)
  map_chr(
    seq_len(n),
    \(i) str_c(chars[idx >= i & ((idx - i) %% n == 0)], collapse = "")
  )
}

result <- input |>
  mutate(parts = map(ID, split_mod)) |>
  unnest_wider(parts, names_sep = "") |>
  rename(ID1 = parts1, ID2 = parts2, ID3 = parts3) |>
  select(-ID) |>
  mutate(across(everything(), ~ na_if(.x, "")))

all.equal(result, test)
#> [1] TRUE
