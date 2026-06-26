library(tidyverse)

input <- data.frame(Number = c(135, 518, 175, 5187, 462, 9474, 4387))
test <- data.frame(is_disarium = c(T, T, T, F, F, F, F))

is_disarium <- function(num) {
  digits <- as.numeric(unlist(strsplit(as.character(num), "")))
  sum_of_powers <- sum(digits^seq_along(digits))
  return(sum_of_powers == num)
}

result <- input %>%
  mutate(is_disarium = map_lgl(Number, is_disarium))

all.equal(result$is_disarium, test$is_disarium)
# True
