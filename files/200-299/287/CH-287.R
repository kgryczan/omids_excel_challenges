library(tidyverse)
library(readxl)

path = "files/200-299/287/CH-287 Transformation.xlsx"
input = read_excel(path, range = "B2:E6")
test  = read_excel(path, range = "I2:K15")

result = input %>%
  pivot_longer(cols = everything(), names_to = "Date", values_to = "Value", values_drop_na = T) %>%
  mutate(Date = str_sub(Date, 1, 11)) %>%
  separate(Value, into = c("Product", "Value"), sep = "-") %>%
  mutate(Value = as.numeric(Value),
         Date = anytime::anydate(Date) %>% as.POSIXct(format = "%d/%m/%Y", tz = "UTC")) 

all.equal(result, test, check.attributes = F)
