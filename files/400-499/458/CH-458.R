library(tidyverse)
library(charcuterie)

# First spy numbers over 1000.
is_spy <- function(number) {
  digs <- as.numeric(chars(as.character(number)))
  return(sum(digs) == prod(digs))
}
result <- 1000:10000 %>%
  keep(is_spy) %>%
  head(7)
