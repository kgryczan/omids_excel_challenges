library(purrr)

result = reduce(1:4, ~c(.x, sample(1:10, 1, prob = replace(rep(1,10), tail(.x,1), 2))), .init = sample(1:10, 1))

result
