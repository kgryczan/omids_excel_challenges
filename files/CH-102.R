library(tidyverse)
library(readxl)

path = "files/CH-102 Compare Rows.xlsx"
input = read_excel(path, range = "B2:C26")
test  = read_excel(path, range = "G2:G14")

result = input %>%
  filter(Sales - lag(Sales) > 0) %>%
  select(Dates = Date)

identical(result, test)
# [1] TRUE

# Second approach (no comparison gte or lte)

result = input %>%
  filter(sign(Sales - lag(Sales)) == 1) %>%
  select(Dates = Date)
# [1] TRUE
