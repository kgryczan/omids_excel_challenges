library(tidyverse)
library(readxl)

path <- "400-499/446/CH-446 Number Series.xlsx"
input <- read_excel(path, range = "B3:C10")
test <- read_excel(path, range = "E3:F10")

result <- input %>%
  mutate(
    Sale = case_when(
      str_detect(Sale, "\\d") ~ as.numeric(Sale),
      TRUE ~ NA_integer_
    )
  ) %>%
  mutate(Sale = zoo::na.approx(Sale))

all.equal(result, test)
# True
