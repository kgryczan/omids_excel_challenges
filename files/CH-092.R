library(tidyverse)
library(readxl)

path = "files/CH - 92 Missing value.xlsx"
input = read_excel(path, range = "C2:F12", col_names = F) %>% as.matrix()
test  = read_excel(path, range = "K2:N12", col_names = F) %>% as.matrix()

replace_values = function(x) {
  for (i in 1:nrow(x)) {
    for (j in 1:ncol(x)) {
      if (x[i,j] == "D") {
        x[i,j] = x[i + 1,j]
      } else if (x[i,j] == "U") {
        x[i,j] = x[i - 1,j]
      } else if (x[i,j] == "R") {
        x[i,j] = x[i,j + 1]
      } else if (x[i,j] == "L") {
        x[i,j] = x[i,j - 1]
      }
    }
  }
  return(x)
}

result = replace_values(input)
all.equal(result, test) # TRUE
