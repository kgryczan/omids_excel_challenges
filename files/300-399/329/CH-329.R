library(tidyverse)
library(readxl)
library(lubridate)

path <- "300-399/329/CH-329 Date Calculation.xlsx"
input <- read_excel(path, range = "B2:C8")
test  <- read_excel(path, range = "D2:D8") %>%
  mutate(`End Time` = dmy_hms(`End Time`))

result <- input %>%
  mutate(
    `Start Date` = dmy_hms(`Start Date`)
  ) %>%
  separate(`Duration [d.h:m:s]`, into = c("dh", "m", "s"), sep = ":", extra = "merge") %>%
  separate(dh, into = c("d", "h"), sep = "\\.", convert = TRUE) %>%
  mutate(across(c(d, h, m, s), as.numeric)) %>%
  mutate(
    calculated_end_date = `Start Date` +
      days(d) + hours(h) + minutes(m) + seconds(s)
  )

result$calculated_end_date == test$`End Time`
# [1] FALSE  TRUE  TRUE  TRUE  TRUE  TRUE
