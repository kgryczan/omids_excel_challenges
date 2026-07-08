library(tidyverse)
library(readxl)

path <- "400-499/439/CH-439 Filter.xlsx"
input <- read_excel(path, range = "B3:D8")
test <- read_excel(path, range = "H3:J5")

result <- input %>%
  filter(Sales > lag(Sales))

all.equal(result, test)
# True
