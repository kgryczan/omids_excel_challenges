library(tidyverse)
library(readxl)

path <- "400-499/425/CH-425 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:E6")
test <- read_excel(path, range = "G3:J11")

result = input %>%
  pivot_longer(cols = c(-1), names_to = "CUSTOMER", values_to = "value") %>%
  na.omit() %>%
  separate_longer_delim(value, delim = ",") %>%
  separate_wider_delim(value, delim = ':', names = c("PRODUCT", "SALES")) %>%
  mutate(SALES = as.numeric(SALES)) %>%
  rename(DATE = "Date")

all.equal(result, test)
# [1] TRUE
