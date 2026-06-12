library(tidyverse)
library(readxl)

path <- "400-499/426/CH-426 Number Series.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

get_nth_term <- function(n) {
  if (n < 2) {
    return(n)
  }
  a <- 0
  b <- 1
  for (i in 2:n) {
    tmp <- b
    b <- 2 * b + a
    a <- tmp
  }
  b
}
result = input %>%
  mutate(`Pell Number` = map_dbl(n, get_nth_term))

all.equal(result$`Pell Number`, test$`Pell  Number`)
# [1] TRUE
