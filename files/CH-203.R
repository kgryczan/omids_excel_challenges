library(tidyverse)
library(readxl)

path = "files/CH-203 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C63")
test  = read_excel(path, range = "G2:H5")

result = input %>%
  complete(Date = seq.Date(min(as.Date(Date)), max(as.Date(Date)), by = "1 day")) %>%
  replace_na(list(Sales = 0)) %>%
  mutate(wday = wday(Date, label = TRUE, locale = "en"),
         Group = month(Date, label = TRUE, abbr = TRUE, locale = "en")) %>%
  filter(!wday %in% c("Sat", "Sun") & Sales == 0) %>%
  summarise(`No missing dates` = n(), .by = Group)

all.equal(result$`No missing dates`, test$`No missing dates`, check.attributes = FALSE)
#> [1] TRUE