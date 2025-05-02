library(tidyverse)
library(readxl)

path = "files/CH-127 Add Index Column.xlsx"
input = read_excel(path, range = "B2:C13")
test  = read_excel(path, range = "E2:G13")

compute_index <- function(price_vector) {
  idx <- rep(1, length(price_vector))
  for (i in 2:length(price_vector)) {
    if (price_vector[i] > price_vector[i - 1]) {
      idx[i] <- idx[i - 1] + 1
    } else {
      idx[i] <- 1
    }
  }
  return(idx)
}

result <- input %>%
  group_by(Stock) %>%
  mutate(index = compute_index(Price))

all.equal(result$index, test$index, check.attributes = FALSE)
#> [1] TRUE