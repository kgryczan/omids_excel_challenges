library(tidyverse)
library(readxl)

path <- "300-399/341/CH-341 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F6")

result = input %>%
  filter(str_detect(ID, "N.*M"))

all.equal(result$ID, test$ID)
# [1] TRUE
