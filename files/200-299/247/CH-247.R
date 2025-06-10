library(tidyverse)
library(readxl)

path = "files/200-299/247/CH-247 Date Calculation.xlsx"
test = read_excel(path, range = "B2:B14") %>%
  mutate(Dates = as.Date(Dates))

result = data.frame(
  date = seq(as.Date("2025-01-01"), as.Date("2025-12-01"), by = "month")
) %>%
  mutate(
    Dates = map(date, ~ date + (8 - wday(date, week_start = 1)) %% 7),
    .by = "date"
  ) %>%
  select(Dates) %>%
  unnest(Dates)

all.equal(test$Dates, result$Dates)
# [1] TRUE
