library(tidyverse)
library(readxl)

path = "files/200-299/252/CH-252 Switching Value.xlsx"
input = read_excel(path, range = "C2:D9")
test  = read_excel(path, range = "F2:G9")

result = input %>%
  mutate(Importance = recode(Importance,
                             "Very low" = 1,
                             "Low" = 2,
                             "Moderate" = 3,
                             "High" = 4,
                             "Very high" = 5))

all.equal(result, test)
#> [1] TRUE