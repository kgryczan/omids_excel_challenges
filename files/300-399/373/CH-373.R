library(tidyverse)
library(readxl)

path <- "300-399/373/CH-373 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:E11")
test <- read_excel(path, range = "H3:I8")

lower <- 600
upper <- 1200

result = input %>%
  mutate(
    s = `Total Sales`,
    small = s < lower,
    start = !lag(small, default = FALSE),
    grp = cumsum(start)
  ) %>%
  summarise(`Total Sales` = sum(s), .by = grp) %>%
  mutate(IDs = paste("Group", row_number())) %>%
  select(IDs, `Total Sales`)

all.equal(result, test)
#> [1] TRUE
