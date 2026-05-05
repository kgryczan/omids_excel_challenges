library(tidyverse)
library(readxl)

path <- "400-499/407/CH-407 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:D12")
test <- read_excel(path, range = "G3:H6")

result = input %>%
  mutate(ROW = paste0(pmin(FROM, TO), "-", pmax(FROM, TO))) %>%
  summarise(`TOTA; QUANTITY` = sum(QUANTITY, na.rm = TRUE), .by = ROW)

all.equal(result, test)
# [1] TRUE
