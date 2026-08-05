library(tidyverse)
library(readxl)

path <- "400-499/453/CH-453 Number Puzzles - Disarium Number.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "D3:D10")

is_disarium <- function(number) {
  digits <- str_split_1(as.character(number), "")
  sum(as.integer(digits) ^ seq_along(digits)) == number
}

result <- tibble(`Disarium Number` = (100:9999) %>%
  keep(is_disarium) %>%
  head(nrow(input)))

all.equal(result, test)
