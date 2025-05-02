library(tidyverse)
library(readxl)

path = "files/CH-98 Data Cleaning.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:F9")

pattern_date = "(\\d{4}\\/\\d{2}\\/\\d{2})"
pattern_num = "(\\s\\d{1,2}\\s|^\\d{1,2}\\s|\\s\\d{1,2}$)"
pattern_let = "([A-Z]+)"

result = input %>%
  mutate(Description = str_remove_all(Description, ","),
         Date = str_extract(Description, pattern_date) %>% as.POSIXct(., tz = "UTC"),
         Product = str_extract(Description, pattern_let),
         Quantity = str_extract(Description, pattern_num) %>% as.numeric()) %>%
  select(-Description)

all.equal(result, test)
#> [1] TRUE
