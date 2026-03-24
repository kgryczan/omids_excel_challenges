library(tidyverse)
library(readxl)

path <- "300-399/386/CH-386 Index.xlsx"
input <- read_excel(path, range = "B3:E11")
test <- read_excel(path, range = "G3:K11")

result <- input |>
  mutate(
    Index = if_else(row_number() == 1, "*", NA_character_),
    .by = c("Customer", "Product")
  )

all.equal(result, test)
## [1] TRUE
