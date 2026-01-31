library(tidyverse)
library(readxl)

path <- "300-399/360/CH-360 Matrix Calculation.xlsx"
input <- read_excel(path, range = "C4:H9", col_names = FALSE) %>% as.matrix()
test1 <- read_excel(path, range = "K4:M6", col_names = FALSE) %>% as.matrix()
test2 <- read_excel(path, range = "P4:R6", col_names = FALSE) %>% as.matrix()
test3 <- read_excel(path, range = "U4:W6", col_names = FALSE) %>% as.matrix()

find_sym_submatrices <- function(mat, n) {
  r <- list()
  sz <- nrow(mat) - n + 1
  for (i in 1:sz) {
    for (j in 1:sz) {
      s <- mat[i:(i + n - 1), j:(j + n - 1)]
      if (all(s == t(s))) r[[length(r) + 1]] <- list(pos = c(i, j), mat = s)
    }
  }
  return(r)
}

res = find_sym_submatrices(input, 3)
all(res[[1]]$mat == test1) # TRUE
all(res[[4]]$mat == test2) # TRUE
all(res[[3]]$mat == test3) # TRUE

# one extra find
res[[2]]$mat

#      ...3 ...4 ...5
# [1,]    1    4    8
# [2,]    4    7    7
# [3,]    8    7    3
