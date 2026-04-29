library(tidyverse)
library(readxl)

path <- "400-499/404/CH-404 Replacement.xlsx"
input <- read_excel(path, range = "B3:D9")
test <- read_excel(path, range = "F3:H9")

result <- input |>
  mutate(
    `Product ID` = str_replace(
      `Product ID`,
      "^((?:[^X]*X){2}[^X]*)X",
      "\\1-"
    )
  )

all.equal(result, test)
# Fourth string in testing data incorrect.
