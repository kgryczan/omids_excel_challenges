library(tidyverse)
library(readxl)

path = "files/CH-072 Fibonacci sequence .xlsx"
test = read_excel(path,  range = "B1:B19") %>% pull()


fibonacci <- function(n) {
  if (n == 1) {
    return(c(0))
  } else if (n == 2) {
    return(c(0, 1))
  } else {
    fib_sequence <- accumulate(3:n, .init = c(0, 1), ~ c(.x, .x[length(.x)] + .x[length(.x) - 1]))
    return(unlist(fib_sequence[n - 1]))
  }
}
identical(fibonacci(18), test) 
# [1] TRUE

fibonacci1 <- function(n) {
  fib_sequence <- numeric(n)
  fib_sequence[1] <- 0
  if (n > 1) {
    fib_sequence[2] <- 1
  }
  if (n > 2) {
    map(3:n, ~ {
      fib_sequence[.x] <<- fib_sequence[.x - 1] + fib_sequence[.x - 2]
    })
  }
  return(fib_sequence)
}
identical(fibonacci1(18), test)
# [1] TRUE