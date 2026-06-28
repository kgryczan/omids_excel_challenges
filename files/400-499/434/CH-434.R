library(tidyverse)
library(readxl)

path <- "400-499/434/CH-434 Replacement.xlsx"
input <- read_excel(path, range = "B3:D9")
test <- read_excel(path, range = "F3:H9")

result <- input %>%
  mutate(
    `Product ID` = str_replace_all(
      `Product ID`,
      "(?<!R)[[:punct:]]|[[:punct:]](?!S)",
      "-"
    )
  )

all.equal(result, test)
# TRUE
