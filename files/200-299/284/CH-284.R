library(tidyverse)
library(readxl)
library(janitor)

path = "files/200-299/284/CH-284 Transformation.xlsx"
input = read_excel(path, range = "B2:E10")
test  = read_excel(path, range = "I2:J18")

result = input %>% 
  mutate(row = row_number() %% 2,
         nr = (row_number() + 1) %/% 2) %>%
  pivot_longer(-c(row, nr), names_to = "col") %>%
  pivot_wider(names_from = row, values_from = value) %>%
  select(Date = `1`, Value = `0`) %>%
  mutate(Date = excel_numeric_to_date(Date) %>% as.POSIXct()) 

all.equal(result, test, check.attributes = FALSE)
# > [1] TRUE