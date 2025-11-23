library(tidyverse)
library(readxl)

path <- "300-399/330/CH-330 Custom Grouping.xlsx"
input <- read_excel(path, range = "B2:D13")
test  <- read_excel(path, range = "H2:I8")

result <- input %>%
  mutate(
    p = as.numeric(`Start Date Time`) / 86400,
    q = as.numeric(`End Date Time`) / 86400,
    d = floor(q) - floor(p),
    rep_num = case_when(
      d > 2 ~ NA_real_,
      d == 2 ~ floor(p) + 1,
      (floor(p) + 1 - p) > (q %% 1) ~ floor(p),
      TRUE ~ floor(q)
    ),
    group = if_else(
      is.na(rep_num),
      "Uncategorzied",
      as.character(as.Date(rep_num, origin = "1970-01-01"))
    )
  ) %>%
  summarise(
    `AVG Polution Rate` = round(mean(Polution)),
    .by = group
  ) %>%
  arrange(group)

all.equal(result$`AVG Polution Rate`, test$`AVG Polution Rate`)
# [1] TRUE