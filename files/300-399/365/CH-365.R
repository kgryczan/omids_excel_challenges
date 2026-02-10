library(tidyverse)
library(readxl)

path <- "300-399/365/CH-365 Matrix Calculation.xlsx"
input <- read_excel(path, range = "C4:G7", col_names = FALSE) %>%
  as.matrix()
test <- read_excel(path, range = "K4:O7", col_names = FALSE) %>%
  as.matrix()

add_surrounding = function(mat) {
  result <- matrix(0, nrow = nrow(mat), ncol = ncol(mat))
  for (i in 1:nrow(mat)) {
    for (j in 1:ncol(mat)) {
      rows <- max(1, i - 1):min(nrow(mat), i + 1)
      cols <- max(1, j - 1):min(ncol(mat), j + 1)
      result[i, j] <- sum(mat[rows, cols]) - mat[i, j]
    }
  }
  return(result)
}
result = add_surrounding(input)
all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
