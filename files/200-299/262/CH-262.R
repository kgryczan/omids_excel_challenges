library(tidyverse)
library(readxl)
library(jsonlite)

path = "files/200-299/262/CH-262 JSON Structures.xlsx"
input = read_excel(path, range = "B2:C5")
test  = read_excel(path, range = "E2:G8")

result = input %>%
  mutate(
    sales = map(Data, ~ fromJSON(.x)$sales %>% as_tibble())
  ) %>% 
  unnest(cols = sales) %>%
  select(ID, Region = region, Value = val)

all.equal(result, test)
#> [1] TRUE