library(tidyverse)
library(readxl)

path = "files/CH-148 Filter Dates.xlsx"
input = read_excel(path, range = "C2:E17")
test  = read_excel(path, range = "G2:I11")

result = input %>%
  mutate(
    first = Date == min(Date, na.rm = TRUE),
    last  = Date == max(Date, na.rm = TRUE),
    middle = Date == Date[ceiling(length(Date)/2)],
    .by = Customer
  ) %>%
  filter(first | last | middle) %>%
  select(Date, Customer, Qty)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE