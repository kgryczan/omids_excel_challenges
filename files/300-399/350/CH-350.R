library(tidyverse)
library(readxl)
library(charcuterie)

path <- "300-399/350/CH-350 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F6")

check_pattern <- function(text) {
  chars <- unique(charcuterie::chars(text))
  patterns <- combn(chars, 2, simplify = TRUE, FUN = function(p) {
    str_c(p[1], ".*", p[2], ".*", p[1], ".*", p[2])
  })
  any(str_detect(text, patterns))
}

result = input %>%
  filter(map_lgl(ID, check_pattern))
