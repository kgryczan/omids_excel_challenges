library(tidyverse)
library(readxl)

path <- "400-499/416/CH-416 Number Series.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

fib_cache <- new.env(parent = emptyenv())

find_fib <- function(n) {
  key <- as.character(n)
  if (exists(key, envir = fib_cache, inherits = FALSE)) {
    return(get(key, envir = fib_cache, inherits = FALSE))
  }
  a <- 0
  b <- 1
  i <- 1

  while (b < n) {
    temp <- b
    b <- a + b
    a <- temp
    i <- i + 1
  }

  if (b == n) {
    value <- as.character(i)
  } else {
    value <- 'N/A'
  }

  assign(key, value, envir = fib_cache)
  value
}

result = input %>%
  mutate(n = map_chr(`Fibonacci Number`, find_fib))

all.equal(result$n, test$n)
# [1] TRUE
