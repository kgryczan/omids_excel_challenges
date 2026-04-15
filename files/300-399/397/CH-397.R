library(tidyverse)
library(readxl)

path <- "300-399/397/CH-397 Index.xlsx"
input <- read_excel(path, range = "B3:F23")
test <- read_excel(path, range = "G3:G23")

r = input %>%
  group_by(Customer) %>%
  mutate(cons = consecutive_id(Product)) %>%
  group_by(Customer, cons) %>%
  mutate(
    count = n(),
    Mark = ifelse(count >= 2, "*", NA_character_)
  ) %>%
  ungroup()

all.equal(r$Mark, test$Mark)
# [1] TRUE
