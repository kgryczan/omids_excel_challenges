library(tidyverse)
library(readxl)

path = "files/CH-194 Pattern Length.xlsx"
input = read_excel(path, range = "B2:C7")
test  = read_excel(path, range = "G2:H7")

result <- input %>%
  separate_rows(Pattern, sep = " ") %>%
  mutate(cn = consecutive_id(Pattern), .by = Date) %>%
  mutate(n = n(), .by = c(Date, cn)) %>%
  filter(n == max(n), .by = Date) %>%
  unite("Length", Pattern, n, sep = "") %>%
  select(-cn) %>%
  distinct()

all.equal(result, test)
#> [1] TRUE