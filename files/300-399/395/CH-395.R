library(tidyverse)
library(readxl)

path <- "300-399/395/CH-395  Replacement.xlsx"
input <- read_excel(path, range = "B3:E10")
test <- read_excel(path, range = "G3:J10")

result = input %>%
  mutate(`Total Sales` = `Total Sales` * (1 - 0.1 * (`Customer ID` == "C-12")))

all.equal(result['Total Sales'], test['Total Sales'])
# [1] TRUE
