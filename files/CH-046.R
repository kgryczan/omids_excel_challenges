library(tidyverse)
library(readxl)

input = read_excel("files/CH-046 Numbers Cleaning.xlsx", range = "B2:B16")
test  = read_excel("files/CH-046 Numbers Cleaning.xlsx", range = "J2:J7")

result = input %>%
  arrange(`Product ID`) %>%
  mutate(group = cumsum(`Product ID` - lag(`Product ID`, default = 0) > 1)) %>%
  summarise(`Product ID` = if_else(max(`Product ID`) == min(`Product ID`), 
                                   as.character(max(`Product ID`)), 
                                   paste(min(`Product ID`), str_sub(max(`Product ID`),3,4), sep = "-")), .by = group) %>%
  select(`Product ID`)

identical(result, test)
# [1] TRUE
