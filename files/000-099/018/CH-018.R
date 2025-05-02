library(tidyverse)
library(readxl)
library(padr)

input = read_excel("files/CH-018 Sales Calendar Extraction.xlsx", range = "B2:C121")
test_month = 2
test = read_excel("files/CH-018 Sales Calendar Extraction.xlsx", range = "I2:O7")

result = input %>%
  pad() %>% #fill dataseries with missing dates
mutate(month = month(Date),
       wday = wday(Date, abbr = TRUE, label = TRUE, locale = "English"),
       week = week(Date)) %>%
  group_by(month) %>%
  mutate(monthly_av = mean(Quantity[!is.na(Quantity)], na.rm = TRUE) %>%
           round(0)) %>%
  ungroup() %>%
  filter(month == test_month) %>%
  mutate(Quantity_check = case_when(Quantity <= monthly_av ~ "L",
                                    Quantity > monthly_av ~ "U",
                                    .default = "-")) %>%
  select(wday, week, Quantity_check) %>%
  pivot_wider(names_from = wday, values_from = Quantity_check, 
              values_fill = list(Quantity_check = NA)) %>%
  select(Su= Sun, Mo = Mon, Tu = Tue, We = Wed, Th = Thu, Fr = Fri,Sa = Sat)

all.equal(test, result)
# [1] TRUE