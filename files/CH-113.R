library(tidyverse)
library(readxl)

path = "files/CH-113 Manage Duplicate Values.xlsx"
input = read_excel(path, range = "B2:B15")
test  = read_excel(path, range = "D2:D15")

result <-  input %>%
  mutate(rn = row_number()) %>%
  arrange(`Product ID`) %>%
  mutate(dup = n() > 1,
         a = cumsum(rn - lag(rn, default = first(rn)) != 1),
         .by = `Product ID`) %>%
  mutate(b = row_number(), .by = c(`Product ID`, a)) %>%
  arrange(rn) %>%
  mutate(result = ifelse(dup, paste0(`Product ID`,"-",a, "-", b), `Product ID`)) 


identical(result$result, test$`Product ID`)
#> [1] TRUE