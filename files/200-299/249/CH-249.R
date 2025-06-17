library(tidyverse)
library(readxl)

path = "files/200-299/249/CH-249 Extract from Text.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:D6")

pattern = "[A-Z]{1}[a-z]{1}[0-9]{1}-[0-9]{2}"

result = input %>%
  mutate(`Product ID` = str_extract(Text, pattern)) %>%
  na.omit() %>%
  select(`Product ID`)

all.equal(result, test, check.attributes = FALSE)
# @ [1] TRUE
