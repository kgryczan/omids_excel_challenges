library(tidyverse)
library(readxl)

path <- "400-499/406/CH-406 Number Series.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")
options(scipen = 999)

fibonacci <- local({
  cache <- c(`0` = 0, `1` = 1)
  f <- function(n) {
    k <- as.character(n)
    if (!is.na(cache[k])) {
      return(cache[k])
    }
    cache[k] <<- f(n - 1) + f(n - 2)
  }
  f
})

result = input %>%
  mutate(`Fibonacci Number` = map_dbl(n, fibonacci))

all.equal(result$`Fibonacci Number`, test$`Fibonacci Number`)
# [1] TRUE
