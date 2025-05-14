library(tidyverse)
library(readxl)

path = "files/200-299/233/CH-233 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:B102")
test = read_excel(path, range = "F2:G11")

compute_range_table = function(x) {
  x = sort(as.numeric(unlist(x)))
  n = length(x)

  map_dfr(seq(10, 90, by = 10), function(pct) {
    k = ceiling(pct / 100 * n)
    diffs = x[k:n] - x[1:(n - k + 1)]
    i = which.min(diffs)
    tibble(
      `%` = pct / 100,
      Range = paste0(x[i], "-", x[i + k - 1])
    )
  })
}

result = compute_range_table(input)

all.equal(result, test)
#> [1] TRUE
