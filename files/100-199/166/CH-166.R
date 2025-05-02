library(tidyverse)
library(readxl)

path = "files/CH-166 Time Zone.xlsx"
input = read_excel(path, range = "B2:D12")
test  = read_excel(path, range = "F2:I12")

result = input %>%
  separate(`Date Time`, into = c("Day", "Month", "Year", "Hour", "Minute"), sep = " |:|/", convert = TRUE) %>%
  mutate(Day = Day + if_else(Hour >= 24, 1, 0),
         Hour = Hour %% 24) %>%
  mutate(`Date Time` = make_datetime(year = Year, month = Month, day = Day, hour = Hour, min = Minute),  .keep = "unused") %>%
  mutate(`GMT From` = str_remove(`GMT From`, "GMT") %>% as.numeric(),
         `GMT To` = str_remove(`GMT To`, "GMT") %>% as.numeric()) %>%
  mutate(`New Date Time` = `Date Time` + hours(`GMT To` - `GMT From`)) %>%
  select(`New Date Time`) %>%
  mutate(`New Date Time` = format(`New Date Time`, "%d/%m/%Y %H:%M"))
  

all.equal(result$`New Date Time`, test$`New Date Time`, check.attributes = FALSE)
# False, one discrepancy on 5th row.