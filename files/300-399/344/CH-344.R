library(tidyverse)
library(readxl)

path <- "300-399/344/CH-344  Matrix Calculation.xlsx"
input1 <- read_excel(path, range = "B4:F8", col_names = FALSE) %>% as.matrix()
input2 <- read_excel(path, range = "B14:F18", col_names = FALSE) %>% as.matrix()
test1 <- read_excel(path, range = "H4", col_names = FALSE) %>% pull()
test2 <- read_excel(path, range = "H14", col_names = FALSE) %>% pull()

is_symmetric <- function(mat) {
  all(mat == t(mat))
}
max_sym1 <- max(which(map_lgl(1:min(dim(input1)), function(x) {
  is_symmetric(input1[1:x, 1:x])
})))
max_sym2 <- max(which(map_lgl(1:min(dim(input2)), function(x) {
  is_symmetric(input2[1:x, 1:x])
})))

all.equal(test1, max_sym1) # True
all.equal(test2, max_sym2) # True
