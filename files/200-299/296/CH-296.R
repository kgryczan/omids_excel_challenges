library(tidyverse)
library(readxl)

path = "files/200-299/296/CH-296 Transformation.xlsx"
input = read_excel(path, range = "B2:E18")
test  = read_excel(path, range = "I2:K26") %>% arrange(Date, Product)

result = stack(input[c(1:4)]) %>%
  mutate(date = ifelse(str_detect(values, "\\d{5,5}"), values, NA)) %>%
  fill(date) %>%
  mutate(product = ifelse(str_detect(values, "[A-Z]"), values, NA)) %>%
  group_by(date) %>%
  fill(product) %>%
  ungroup() %>%
  filter(values != product & values != date) %>%
  mutate(date = as.Date(as.numeric(date), origin = "1899-12-30") %>% as.POSIXct(),
         values = as.numeric(values)) %>%
  select(Date = date, Product = product, Result = values) %>% 
  arrange(Date, Product)

all.equal(result, test, check.attributes = FALSE)
# TRUE