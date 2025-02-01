library(tidyverse)
library(readxl)
library(anytime)

path = "files/CH-183 Match the Dates.xlsx"
input = read_excel(path, range = "C2:C29")
test  = read_excel(path, range = "I2:I14")

result = input %>%
  mutate(date = anytime(Date),
         dateymd = ymd(Date),
         result = coalesce(date, dateymd)) %>%
  select(result) %>%
  distinct()

all.equal(anydate(result$result), anydate(test$Date))
# [1] TRUE