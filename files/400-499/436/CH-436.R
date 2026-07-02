library(tidyverse)
library(readxl)

path <- "400-499/436/CH-436 Number Series.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10", col_types = "numeric")

pell_index <- function(n) {
  p <- c(0, 1)
  while (tail(p, 1) < n) {
    p <- c(p, 2 * p[length(p)] + p[length(p) - 1])
  }
  i <- which(p == n) - 1
  if (length(i)) as.numeric(i) else NA_real_
}

result <- input %>%
  mutate(n = map_dbl(`Pell Number`, pell_index))

all.equal(result$n, test$n)
# True
