library(tidyverse)
library(readxl)

path = "files/200-299/274/CH-274 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C18")
test  = read_excel(path, range = "G2:I18")

result = input %>%
  mutate(Group = cumsum(c(1, diff(Date) > 2)))

all.equal(result$Group, test$Group) 
# [1] TRUE