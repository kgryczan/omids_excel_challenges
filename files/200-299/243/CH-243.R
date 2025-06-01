library(tidyverse)
library(readxl)

path = "files/200-299/243/CH-243 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C16")
test = read_excel(path, range = "F2:G7")

result = input %>%
  count(
    `Age Group` = cut(
      Age,
      c(0, 30, 40, 50, 60, Inf),
      right = FALSE,
      labels = c("<30", "[30-40)", "[40-50)", "[50-60)", ">60")
    ),
    name = "Count"
  ) %>%
  complete(`Age Group`, fill = list(Count = 0)) %>%
  mutate(`Age Group` = as.character(`Age Group`))

all.equal(result, test)
# [1] TRUE
