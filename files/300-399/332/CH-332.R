library(tidyverse)
library(readxl)

path <- "300-399/332/CH-332 Date Calculation.xlsx"
input <- read_excel(path, range = "B2:C8")
test <- read_excel(path, range = "D2:D8") %>%
  mutate(`End Time` = dmy_hms(`End Time`))

result = input %>%
  mutate(`Start Date` = dmy_hms(`Start Date`)) %>%
  mutate(`End Date` = `Start Date` + hours(as.numeric(`Duration [h]`)))

all.equal(result$`End Date`, test$`End Time`)
# First time incorrect in the Excel file, others correct
