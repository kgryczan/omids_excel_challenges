library(tidyverse)
library(readxl)

path = "files/CH-227 Data Normalization Min-Max.xlsx"
input = read_excel(path, range = "B2:G8")
test = read_excel(path, range = "J2:O8")

result = input %>%
  mutate(across(where(is.numeric), ~ (. - min(.)) / (max(.) - min(.))))

all.equal(result, test)
#> [1] TRUE
