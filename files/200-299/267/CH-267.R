library(tidyverse)
library(readxl)

path = "files/200-299/267/CH-267 Date Calculation.xlsx"
test  = read_excel(path, range = "B2:B14")

format = "%Y/%m/%d"
eom = ceiling_date(ymd(paste(2025, 1:12, 1, sep = "-")), "month") - 1
last_sunday = eom - days((wday(eom, week_start = 1) %% 7))
last_monday = last_sunday - days(6)
result = data.frame(Dates = paste(format(last_monday, format), format(last_sunday, format), sep = " - "))

result == test 
# May is crossing month boundary, so the last Sunday is in June
