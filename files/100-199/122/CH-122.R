library(tidyverse)
library(readxl)

path = "files/CH-122 Table Transformation.xlsx"
input = read_excel(path, range = "C2:E27")
test  = read_excel(path, range = "G2:J17") %>%
  mutate(Date = format(Date, "%d/%m/%Y"))

block_size = 5

result = input %>%
  mutate(row_id = row_number(),
         block_id = (row_id - 1) %/% block_size + 1) %>%
  summarise(
    date = Date[2],
    region = Date[1],
    fruits = list(Description[3:block_size]),
    values = list(Qty[3:block_size]),
    .by = block_id
  ) %>%
  unnest(c(fruits, values)) %>%
  arrange(date, block_id, desc(values)) %>%
  select(-block_id)

names(result) = names(test)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE