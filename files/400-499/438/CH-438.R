library(tidyverse)
library(readxl)

path <- "400-499/438/CH-438 Number Puzzles - Spy Number.xlsx"

is_spy <- function(num) {
  spl <- str_split(as.character(num), "")[[1]] %>% as.numeric()
  sum(spl) == prod(spl)
}

result <- tibble(n = 10000:20000) %>%
  mutate(is_spy = map_lgl(n, is_spy)) %>%
  filter(is_spy) %>%
  head(7)
