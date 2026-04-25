library(tidyverse)
library(readxl)

path <- "400-499/401/CH-401 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "F3:H8") %>%
  replace(is.na(.), "")

split_id <- function(x) {
  n <- nchar(x)
  q <- n %/% 3
  r <- n %% 3
  l <- q + c(r > 0, r > 1, 0)
  k <- cumsum(l)
  c(
    ID1 = substr(x, 1, k[1]),
    ID2 = substr(x, k[1] + 1, k[2]),
    ID3 = substr(x, k[2] + 1, n)
  )
}

result <- input %>% transmute(parts = map(ID, split_id)) %>% unnest_wider(parts)
all.equal(result, test)
# One additional letter in first column.
