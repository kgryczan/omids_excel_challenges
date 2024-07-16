library(tidyverse)
library(readxl)

path = "files/CH-083 Custom splitter 3.xlsx"
input = read_excel(path, range = "B2:B3")
test = read_excel(path, range = "D5:F27")

result = input %>%
  separate_rows(Info, sep = ";") %>%
  separate(Info, into = c("Date","Product","Quantity"), sep = ", ") %>%
  mutate(Quantity = as.numeric(Quantity))

identical(result, test)
#> [1] TRUE