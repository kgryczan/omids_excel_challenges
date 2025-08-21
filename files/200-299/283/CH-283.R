library(tidyverse)
library(readxl)

path = "files/200-299/283/CH-283 Advanced Sorting.xlsx"
input = read_excel(path, range = "B2:E9")
test  = read_excel(path, range = "G2:J9")

result = input %>% 
  arrange(desc(pmap_dbl(select(., -`Product ID`), ~max(...))),
          desc(pmap_dbl(select(., -`Product ID`), ~sort(c(...), TRUE)[2])))

all.equal(result, test, check.attributes = FALSE)
# > [1] TRUE