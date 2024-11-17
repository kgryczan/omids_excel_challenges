library(tidyverse)
library(readxl)

path = "files/CH-145 Length of Pattern.xlsx"
input = read_excel(path, range = "B2:D32")
test  = read_excel(path, range = "F2:G5")

result = input %>%
  summarise(result = str_c(Result, collapse = ""), .by = Product) %>%
  mutate(`Largest Length` = map_dbl(result, ~ max(str_length(str_extract_all(.x, "(?:\\+\\+-)+(?:\\+)?")[[1]]), 0))) %>%
  select(Product, `Largest Length`)

all.equal(result, test)
#> [1] TRUE