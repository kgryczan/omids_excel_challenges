monte_carlo_simulation <- function(n) {
  sum(ifelse(runif(n) < 1/6, 6, -1.3))
}

monte_carlo_simulation(100)