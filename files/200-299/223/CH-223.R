library(tidyverse)
library(readxl)
library(hms)

path = "files/CH-223 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:D16")
test = read_excel(path, range = "H2:I9")

result = input %>%
  mutate(Date = day(Date), Time = hms::as_hms(Time)) %>%
  mutate(Date = ifelse(Time > hms::as_hms("12:00:00"), Date + 1, Date)) %>%
  summarise(Sales = sum(Sales), .by = Date) %>%
  mutate(Day = row_number()) %>%
  select(Day, Sales)

all.equal(result, test, check.attributes = FALSE)
##> [1] TRUE
