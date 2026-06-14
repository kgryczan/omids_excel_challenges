library(tidyverse)
library(readxl)

path <- "400-499/427/CH-427 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:F14")
test <- read_excel(path, range = "H3:I8")

result = input %>%
  mutate(
    PRODUCTS = pmap_chr(
      list(`PRODUCT 1`, `PRODUCT 2`, `PRODUCT 3`),
      ~ paste(sort(c(...)), collapse = "-")
    )
  ) %>%
  summarise(`TOTA; QUANTITY` = sum(QUANTITY), .by = PRODUCTS)

# Result almost ideal. One set is not sorted in provided answer data.
