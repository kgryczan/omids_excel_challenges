library(tidyverse)
library(readxl)
library(reshape2)

path = "files/CH-088 Subtotal Calculation.xlsx"
input = read_excel(path, range = "B2:E18")
test  = read_excel(path, range = "I2:M23")

result = input %>%
  pivot_longer(cols = -c(1, 2), names_to = "Region", values_to = "value") %>%
  dcast(Product + Season ~ Region, 
                     value.var = "value", 
                     fun.aggregate = sum, 
                     margins = c("Product", "Season")) %>%
  mutate(`Total Regions` = rowSums(.[, -c(1, 2)], na.rm = TRUE)) %>%
  as_tibble()

all.equal(result[,3:5], test[,3:5], check.attributes = FALSE)
# [1] TRUE - result the same, didn't change total labels
