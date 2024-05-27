library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-058 Stepped Tax.xlsx", range = "B2:D7")
input2 = read_excel("files/CH-058 Stepped Tax.xlsx", range = "F2:G7")
test   = read_excel("files/CH-058 Stepped Tax.xlsx", range = "H2:H7")

input1$To = ifelse(input1$To == "Over", Inf, input1$To) %>% as.numeric()

result = input1 %>% 
  mutate(key = 1) %>%
  full_join(input2 %>% mutate(key = 1), by = "key") %>%
  select(-key) %>%
  filter(From <= To) %>%
  mutate(income_over_threshold = Income - From,
         income_in_threshold = ifelse(Income >= From & Income <= To  , T, F)) %>%
  filter(income_over_threshold >= 0) %>%
  arrange(`Person ID`) %>%
  mutate(tax = ifelse(income_in_threshold, 
                      income_over_threshold * `Tax Rate`,
                      (To - From) * `Tax Rate`)) %>%
  summarise(Tax = sum(tax), .by = c(`Person ID`, Income)) %>%
  select(Tax)

all(round(result$Tax, 1) == round(test$Tax, 1))
# TRUE