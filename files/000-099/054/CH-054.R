library(tidyverse)
library(readxl)
library(padr)

input = read_excel("files/CH-054 Missing Values.xlsx", range = "B2:D21")
test  = read_excel("files/CH-054 Missing Values.xlsx", range = "H2:J38")

result = input %>%
  group_by(Project) %>%
  mutate(Date = floor_date(Date, "month")) %>%
  pad() %>%
  fill(`Actual Progress`, .direction = "down") %>%
  mutate(Date = Date + months(1) - days(1)) 

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE