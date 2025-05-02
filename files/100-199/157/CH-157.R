library(tidyverse)
library(readxl)

path = "files/CH-157 Table Transformation.xlsx"
input = read_excel(path, range = "C2:C17", col_types = "text")
test  = read_excel(path, range = "E2:G12")

result = input %>%
  as.matrix() %>%
  matrix(., ncol = 3, byrow = TRUE) %>%
  as.data.frame() %>%
  separate_rows(V2:V3, sep = ",") %>%
  mutate(V1 = as.Date(as.integer(V1), origin = "1899-12-30") %>% as.POSIXct(), 
         V3 = as.integer(V3)) %>%
  set_names(c("Date", "Product", "Quantity")) 


all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE