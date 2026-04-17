library(tidyverse)
library(readxl)

path <- "300-399/398/CH-398  Replacement.xlsx"
input <- read_excel(path, range = "B3:E10")
test <- read_excel(path, range = "G3:J10")

result = input |>
  mutate(`Product ID` = lead(`Product ID`, default = first(`Product ID`)))

all.equal(result$`Product ID`, test$`Product ID`)
# [1] TRUE
