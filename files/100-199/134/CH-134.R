library(tidyverse)
library(readxl)

path = "files/CH-134 Final Week of the Month.xlsx"
input = read_excel(path, range = "C2:E27")
test  = read_excel(path, range = "G2:I5")

result = input %>%
  mutate(day = day(Date),
         month_end = ceiling_date(Date, "month") - days(1)) %>%
  filter(day >= day(month_end) - 6) %>%
  select(-day, -month_end)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE