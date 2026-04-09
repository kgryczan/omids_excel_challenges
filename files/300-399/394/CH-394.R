library(tidyverse)
library(readxl)

path <- "300-399/394/CH-394 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F7")

result = input %>%
  filter(str_detect(ID, "[A-Z]{2}[1-6]{3,4}|[A-Z]{2}[7-9]{3,4}"))

all.equal(result$ID, test$ID)
# [1] TRUE
