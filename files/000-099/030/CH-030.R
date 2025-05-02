library(tidyverse)
library(readxl)

input = read_excel("files/CH-30-Risk Analysis.xlsx", range = "C3:H8")
test  = read_excel("files/CH-30-Risk Analysis.xlsx", range = "K2:l7")

classify_risk <- function(L, C) {
  if (L < 7 & C < 7 & (L + C) < 7) {
    "Very Low"
  } else if (L < 9 & C < 9 & (L + C) < 9) {
    "Low"
  } else if (L < 11 & C < 11 & (L + C) < 11) {
    "Moderate"
  } else if (L < 13 & C < 13 & (L + C) < 13) {
    "High"
  } else {
    "Very High"
  }
}


result = input %>%
  select(Lh = 1, everything()) %>%
  pivot_longer(-Lh, names_to = "Cons", values_to = "count") %>%
  mutate(Cons = as.numeric(Cons)) %>%
  mutate(`Risk Type` = map2_chr(Lh, Cons, classify_risk)) %>%
  na.omit() %>%
  summarise(`Number of Activity` = sum(count), .by = `Risk Type`) 

identical(result, test)
# [1] TRUE

