library(tidyverse)
library(readxl)

path <- "300-399/354/CH-354 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:C9")
test <- read_excel(path, range = "F3:G9")

result = input %>%
  transmute(
    IDs = ifelse(row_number() == n(), ID, paste0(ID, ",", lead(ID, 1, ))),
    Sales = ifelse(row_number() == n(), Sales, Sales + lead(Sales, 1))
  )

all.equal(result, test)
# [1] TRUE
