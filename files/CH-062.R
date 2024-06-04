library(tidyverse)
library(readxl)
library(zoo)
library(padr)

input = read_excel("files/CH-062 Missing Values.xlsx", range = "B2:D21")
test  = read_excel("files/CH-062 Missing Values.xlsx", range = "H2:J38")

result = input %>%
  mutate(Date = Date + days(1)) %>%
  group_by(Project) %>%
  pad() %>%
  mutate(`Actual Progress` = na.approx(`Actual Progress`)) %>%
  ungroup() %>%
  mutate(Date = Date - days(1))

all.equal(test,result)
#> [1] TRUE