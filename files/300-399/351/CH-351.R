library(tidyverse)
library(readxl)

path <- "300-399/351/CH-351 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F6")

result = input %>%
  filter(str_detect(ID, "M.*N.*M.*"))

all.equal(result, test)
# [1] TRUE
