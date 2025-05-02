library(tidyverse)
library(readxl)

path = "files/CH-108 AVG Cooperation time.xlsx"
input = read_excel(path, range = 'B2:E12')
test  = read_excel(path, range = 'J2:K4')

result = input %>%
  filter(`Leave date` == "-") %>%
  mutate(cooperation = interval(ymd(`Employee Date`), ymd("2024/08/16")) / months(1)) %>%
  summarise(avg_cooperation = mean(cooperation), .by = Level)

result
# Level      avg_cooperation
# <chr>                <dbl>
# 1 Expert              56.5
# 2 Managerial          56.6