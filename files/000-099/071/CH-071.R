library(tidyverse)
library(readxl)

path = "files/CH-071 Extract from Text.xlsx"
input = read_excel(path, range = "B2:B19")
test  = read_excel(path, range = "D2:D11")

email_regex <- "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"

result = input %>%
  mutate(`Email Address` = str_extract(Text, email_regex)) %>%
  na.omit() %>%
  select(`Email Address`)

all.equal(result, test, check.attributes = FALSE)
#  [1] TRUE