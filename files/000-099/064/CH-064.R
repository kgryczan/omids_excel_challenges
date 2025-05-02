library(tidyverse)
library(readxl)

input = read_excel("files/CH-064 Text Cleaning.xlsx", range = "B2:B9")
test  = read_excel("files/CH-064 Text Cleaning.xlsx", range = "D2:F14")
test$Date = as.character(as.Date(test$Date))

result = input %>%
  mutate(date = str_split_fixed(Description, ", ", 2),
         Date = date[,1],
         Product = date[,2]) %>%
  select(Date, Product) %>%
  separate_longer_delim(Product, delim = ", ") %>%
  separate(Product, into = c("Product", "Quantity"), sep = " ") %>%
  mutate(Quantity = as.numeric(Quantity),
         Date = str_replace_all(Date, "/", "-")) %>%
  replace_na(list(Quantity = 1))

identical(result, test)
# [1] TRUE