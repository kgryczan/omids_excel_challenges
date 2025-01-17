library(tidyverse)
library(readxl)

path = "files/CH-175 Remove consecutive X.xlsx"
input = read_excel(path, range = "C2:D10")
test  = read_excel(path, range = "G2:G10") %>%
  replace(is.na(.), "")

result = input %>%
  mutate(ID = str_remove_all(ID, "[xX]{2,}")) %>%
  select(ID)

all.equal(result, test, check.attributes = FALSE)
