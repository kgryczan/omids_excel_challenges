library(tidyverse)
library(readxl)

path <- "300-399/363/CH-363 Matrix Calculation.xlsx"
input <- read_excel(path, range = "C4:G7", col_names = FALSE) %>% as.matrix()
test1 <- read_excel(path, range = "J4:L4", col_names = FALSE) %>% as.matrix()
test2 <- read_excel(path, range = "O4:S4", col_names = FALSE) %>% as.matrix()
test3 <- read_excel(path, range = "W4:W7", col_names = FALSE) %>% as.matrix()

par = 16

find_subvectors_sum_to_par <- function(mat, target_sum) {
  results <- list()

  for (i in 1:nrow(mat)) {
    for (j in 1:ncol(mat)) {
      for (k in j:ncol(mat)) {
        subvector <- mat[i, j:k]
        if (sum(subvector) == target_sum) {
          results <- append(results, list(matrix(subvector, nrow = 1)))
        }
      }
    }
  }

  for (j in 1:ncol(mat)) {
    for (i in 1:nrow(mat)) {
      for (k in i:nrow(mat)) {
        subvector <- mat[i:k, j]
        if (sum(subvector) == target_sum) {
          results <- append(results, list(matrix(subvector, ncol = 1)))
        }
      }
    }
  }

  return(results)
}

result <- find_subvectors_sum_to_par(input, par)

all(result[[1]] == test1)
all(result[[2]] == test2)
all(result[[3]] == test3)
