library(tidyverse)
library(readxl)

path = "files/200-299/263/CH-263 UnGrouping.xlsx"
input = read_excel(path, range = "B2:C5")
test  = read_excel(path, range = "G2:H17")

result = input %>%
  separate_wider_delim(Group, "-", names = c("From", "To")) %>%
  mutate(Date = map2(From, To, ~seq(as.Date(.x), as.Date(.y), by = "day"))) %>%
  unnest(Date) %>%
  mutate(n_days = n_distinct(Date),
         Sales = `Total Sales` / n_days,
         Date = as.POSIXct(Date), .by = From) %>%
  select(Date, Sales)

all.equal(result, test, check.attributes = FALSE)
# > [1] TRUE