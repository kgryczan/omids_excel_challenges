library(tidyverse)
library(readxl)

path <- "400-499/437/CH-437 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:D14")
test <- read_excel(path, range = "F3:G8")

result <- input %>%
  mutate(
    sorted_products = str_split(Products, ",") %>%
      map(~ str_c(sort(.), collapse = ","))
  ) %>%
  unnest() %>%
  summarise(total = sum(Quantity, na.rm = TRUE), .by = sorted_products)
names(result) <- names(test)

all.equal(result, test)
# BMD should be BDM
