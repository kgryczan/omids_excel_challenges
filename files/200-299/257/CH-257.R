library(tidyverse)
library(readxl)

path = "files/200-299/257/CH-257 Date Calculation.xlsx"
test  = read_excel(path, range = "B2:B14") %>% 
  mutate(Dates = as.Date(Dates))

eom = ceiling_date(ymd(paste(2025, 1:12, 1, sep = "-")), "month") - 1
last_mondays = eom - days((wday(eom) - 2) %% 7) 

all.equal(last_mondays, test$Dates, check.attributes = FALSE)
#> [1] TRUE