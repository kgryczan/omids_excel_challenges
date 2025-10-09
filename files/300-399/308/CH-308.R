library(tidyverse)
library(readxl)

path = "files/300-399/308/CH-308 Table Transformation.xlsx"
input = read_excel(path, range = "B2:B3")
test  = read_excel(path, range = "B6:C29")

result = input %>%
  mutate(all = str_extract_all(Info, "\\d{4}/\\d{1}/\\d{1,2}/\\d{2}")) %>%
  unnest(all) %>%
  select(-Info) %>%
  separate(all, into = c("Year", "Month", "Day", "Sale"), sep = "/", convert = TRUE) %>%
  mutate(Date = as.POSIXct(sprintf("%04d-%02d-%02d", Year, Month, Day), tz = "UTC")) %>%
  select(Date, Sale)

all.equal(result, test, check.attributes = FALSE)
