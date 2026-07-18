library(tidyverse)
library(readxl)

path <- "400-499/444/CH-444 Replacement.xlsx"
input <- read_excel(path, range = "B3:D9")
test <- read_excel(path, range = "F3:H9")

replace_x <- function(id) {
  str_replace_all(id, "(?<!Y)X(?!Y)", "Y")
}

result <- input %>%
  mutate(`Product ID` = map_chr(`Product ID`, replace_x))

all.equal(result, test)
# True
