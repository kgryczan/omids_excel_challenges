library(tidyverse)
library(readxl)

path = "files/CH-149 Extract From Text.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:D7")

result = input %>%
  mutate(Extracted = str_extract(Text, "(?<=[\\(\\[\\{\\*])(.*?)(?=[\\)\\]\\}\\*])")) 

all.equal(result$Extracted, test$Extracted, check.attributes = FALSE)
#> [1] TRUE