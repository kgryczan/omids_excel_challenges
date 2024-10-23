library(tidyverse)
library(readxl)

path = "files/CH-132 Merge.xlsx"
input = read_excel(path, range = "B2:C7")
input2 = read_excel(path, range = "H2:H8")
test  = read_excel(path, range = "I2:I8") %>% arrange(desc(Value))

result = input %>%
  cross_join(input2) %>%
  filter(str_detect(Code, `Sub code`)) %>%
  select(Value) %>%
  arrange(desc(Value))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE