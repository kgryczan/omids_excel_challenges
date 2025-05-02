library(tidyverse)
library(readxl)

input = read_excel("files/CH-041 Transformation.xlsx", range = "B2:E11")
test  = read_excel("files/CH-041 Transformation.xlsx", range = "G2:H21")

result = input %>%
  select(`Machinary Code` = 1, Col1 = 2, Col2 = 3, Col3 = 4) %>%
  pivot_longer(cols = -c(1), names_to = "col", values_to = "Product Code", values_drop_na = TRUE) %>%
  arrange(str_extract(`Product Code`, "\\d+"), col) %>%
  select(-col)

identical(result, test)
# [1] TRUE
