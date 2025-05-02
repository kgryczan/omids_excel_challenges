library(tidyverse)
library(readxl)

path = "files/CH-114 Merge.xlsx"
input1 = read_excel(path, range = "B2:C9")
input2 = read_excel(path, range = "B13:C18")
test  = read_excel(path, range = "H2:J9")

r1 = input1 %>%
  separate_rows(`Product ID`, sep = ",") %>%
  inner_join(input2, by = c("Product ID" = "product id")) %>%
  summarise(price = first(price) %>% as.character(), .by = Date) 
r2 = input1 %>%
  left_join(r1, by = "Date") %>%
  replace_na(list(price = "-"))

identical(r2, test)
#> [1] TRUE