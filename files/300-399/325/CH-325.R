library(tidyverse)
library(readxl)

path = "300-399/325/CH-325 Date Calculation.xlsx"
input = read_excel(path, range = "B2:C8", col_types = c("text", "numeric"))
test  = read_excel(path, range = "D2:D8") %>%
  mutate(`End Time` = dmy_hms(`End Time`))

result = input %>%
  mutate(`Start Date` = dmy_hms(`Start Date`),
         `End Time` = `Start Date` + ddays(`Duration [h:m:s]`))

result$`End Time` == test$`End Time`
# first date incorrect