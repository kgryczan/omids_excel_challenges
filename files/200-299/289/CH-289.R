library(tidyverse)
library(readxl)

path = "files/200-299/289/CH-289 Aggregation.xlsx"
input = read_excel(path, range = "B3:E9", col_names = FALSE) %>% as.matrix()
test  = read_excel(path, range = "G3:J9", col_names = FALSE) %>% as.matrix()

get_neighbour <- function(df, r, c) {
  r_rng <- max(1, r-1):min(nrow(df), r+1)
  c_rng <- max(1, c-1):min(ncol(df), c+1)
  vals  <- df[r_rng, c_rng, drop = FALSE]
  vals[match(r, r_rng), match(c, c_rng)] <- NA_real_
  mean(vals, na.rm = TRUE)
}

output <- matrix(
  purrr::map2_dbl(
    rep(1:nrow(input), times = ncol(input)),
    rep(1:ncol(input), each = nrow(input)),
    ~ get_neighbour(input, .x, .y)
  ),
  nrow = nrow(input),
  ncol = ncol(input)
)

all(output==test) # TRUE
