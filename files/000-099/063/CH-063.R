library(tidyverse)
library(readxl)
library(rebus)

input = read_excel("files/CH-063 Custom splitter.xlsx", range = "B2:B15")
test  = read_excel("files/CH-063 Custom splitter.xlsx", range = "D2:F15")

pattern = capture(digit(4) %R% "/" %R% digit(1,2) %R% "/" %R% digit(1,2)) %R%
  capture(alpha(1,2)) %R% capture(digit(1,2))


result = input %>%
  extract(col = "Info", into = c("Date", "Product", "Quantity"), pattern) %>%
  mutate(Quantity = as.numeric(Quantity))

identical(result, test)
# [1] TRUE