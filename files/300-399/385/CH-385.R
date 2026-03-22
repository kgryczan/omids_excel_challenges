library(tidyverse)
library(readxl)

path <- "300-399/385/CH-385 Replacement.xlsx"
input <- read_excel(path, range = "B3:E10")
test <- read_excel(path, range = "G3:J10")

result <- input |>
  mutate(
    `Customer ID` = if_else(
      Date >= as.POSIXct("2024-08-14"),
      str_replace(`Customer ID`, "X", "C"),
      `Customer ID`
    )
  )

all.equal(result, test)
## [1] TRUE
