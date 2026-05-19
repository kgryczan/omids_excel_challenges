library(tidyverse)
library(readxl)

path <- "400-499/414/CH-414 Replacement.xlsx"
input <- read_excel(path, range = "B3:D9")
test <- read_excel(path, range = "F3:H9")

result = input %>%
  mutate(
    `Product ID` = str_replace_all(`Product ID`, "X(\\d)", "X-\\1")
  )

all.equal(result, test)
#> [1] TRUE
