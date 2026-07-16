library(tidyverse)
library(readxl)

path <- "400-499/443/CH-443 Number Puzzles - Disarium Number.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

is_disarium <- function(n) {
  digits <- as.integer(strsplit(as.character(n), "")[[1]])
  n == sum(digits^seq_along(digits))
}

canditates <- 0:1e6 %>%
  keep(is_disarium)
result <- input %>%
  crossing(canditates) %>%
  summarize(
    result = case_when(
      any(canditates == Number) ~ max(canditates[canditates < Number]),
      .default = canditates[which.min(abs(canditates - Number))]
    ),
    .by = Number
  )
# different results
