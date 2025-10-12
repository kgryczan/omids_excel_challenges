library(tidyverse)
library(readxl)
library(slider)
library(zoo)

path = "files/300-399/309/CH-309 Advanced Filtering.xlsx"
input = read_excel(path, range = "B2:C17")
test  = read_excel(path, range = "G2:H6")

# Solution - classic with lag/lead
result1 = input %>%
  filter(Sales >= lag(Sales) & Sales >= lead(Sales))

# Solution - with zoo::rollapply
result2 = input %>%
  filter(Sales == rollapply(Sales, 3, max, align = "center", fill = NA))

# Solution - with slider::slide_dbl
result3 = input %>%
  filter(Sales == slide_dbl(Sales, ~max(.x), .before = 1, .after = 1))

all.equal(result, test)
# [1] TRUE
all.equal(result2, test)
# [1] TRUE
all.equal(result3, test)
# [1] TRUE