library(tidyverse)
library(readxl)

path = "files/CH-184 Table Transformation.xlsx"
input = read_excel(path, range = "C2:C17", col_types = "text")
test  = read_excel(path, range = "E2:G12" , col_types = "text")

result = input %>%
  mutate(Date = ifelse(!str_detect(`Column 1`, ","), `Column 1`, NA)) %>%
  fill(Date, .direction  = "down") %>%
  filter(Date != `Column 1`) %>%
  separate(`Column 1`, into = c("Product", "Quantity"), sep = ", ") %>%
  relocate(Date, .before = Product)

all.equal(result, test)
#> [1] TRUE