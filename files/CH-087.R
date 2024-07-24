library(tidyverse)
library(readxl)
library(fuzzyjoin)

path = "files/CH-087 Price List.xlsx"
input1 = read_excel(path, range = "B2:D9")
input2 = read_excel(path, range = "G2:I11")
test = read_excel(path, range = "J2:J11")

result = input2  %>%
  fuzzy_left_join(input1, by = c("Product" = "Product", "Date" = "From Date"),
                  match_fun = list(`==`, `>=`)) %>%
  filter(`From Date` == max(`From Date`), .by = c("Product.x", "Date"))

identical(result$Price, test$Price)
# [1] TRUE