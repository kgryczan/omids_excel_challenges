library(tidyverse)
library(readxl)

path <- "400-499/449/CH-449 Filter.xlsx"
input <- read_excel(path, range = "B3:D10")
test <- read_excel(path, range = "H3:J5")

result <- input %>%
  arrange(Product, Date) %>%
  filter(Sales > (Sales + lag(Sales) + lag(Sales, 2)) / 3, .by = Product)

all.equal(result, test) # TRUE
