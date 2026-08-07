library(tidyverse)
library(readxl)

path <- "400-499/454/CH-454 Replacement.xlsx"
input <- read_excel(path, range = "B3:D9")
test <- read_excel(path, range = "F3:H9")

replace_x <- function(product) {
  str_replace_all(product, "XXXX|XX", \(match) {
    if_else(str_length(match) == 4, "XX", "X")
  })
}

result <- input %>%
  mutate(`Product ID` = map_chr(`Product ID`, replace_x)) %>%
  select(all_of(names(test)))

all.equal(result, test)
