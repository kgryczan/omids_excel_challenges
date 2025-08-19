library(tidyverse)
library(readxl)

path = "files/200-299/282/CH-282 Advanced Filtering.xlsx"
input = read_excel(path, range = "C2:E9") %>% as.matrix()
test  = read_excel(path, range = "G2:G12") %>% pull() %>% sort()

output = matrix(0, nrow = nrow(input), ncol = ncol(input))
for (i in 1:nrow(input)) {
  for (j in 1:ncol(input)) {
    if (sum(input[i, ] == input[i, j]) == 1 && sum(input[, j] == input[i, j]) == 1) {
      output[i, j] = 1
    }
  }
}
result = input[output == 1] %>% sort() %>% unique()

all(result == test)
# [1] TRUE