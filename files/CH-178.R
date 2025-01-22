library(tidyverse)
library(readxl)

path = "files/CH-178 Prime Factors.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "F2:G7")


find_prime_factors <- function(n) {
  factors <- c()
  for (divisor in 2:n) {
    while (n %% divisor == 0) {
      factors <- c(factors, divisor)
      n <- n / divisor
    }
  }
  str_c(factors, collapse = "*")
}

result = input %>%
  mutate(prime_factors = map_chr(Numbers, find_prime_factors)) 

all.equal(result$prime_factors, test$`Result 1`)
# [1] TRUE