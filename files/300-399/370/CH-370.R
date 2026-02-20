library(tidyverse)
library(readxl)

path <- "300-399/370/CH-370 Matrix Calculation.xlsx"
mat <- read_excel(path, range = "C4:G7", col_names = FALSE) %>%
  as.matrix()

find_submatrices <- function(mat, target) {
  n_rows <- nrow(mat)
  n_cols <- ncol(mat)
  submatrices <- list()

  for (start_row in 1:n_rows) {
    for (start_col in 1:n_cols) {
      for (end_row in start_row:n_rows) {
        for (end_col in start_col:n_cols) {
          submatrix <- mat[start_row:end_row, start_col:end_col]
          if (sum(submatrix) == target) {
            submatrices <- append(submatrices, list(submatrix))
          }
        }
      }
    }
  }

  return(submatrices)
}
target_sum <- 16
result <- find_submatrices(mat, target_sum)
print(result)
