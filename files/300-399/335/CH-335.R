library(tidyverse)
library(readxl)

path <- "300-399/335/CH-335 Table Transformation.xlsx"
input <- read_excel(path, range = "B2:C7")
test <- read_excel(path, range = "G2:H11")

result = input %>%
  mutate(
    prefix = str_extract(Level, "^[^0-9]+"),
    nums = str_extract(Level, "[0-9,]+")
  ) %>%
  separate_rows(nums, sep = ",") %>%
  mutate(Level = str_c(prefix, nums)) %>%
  select(`Issue ID`, Level)

all.equal(result, test)
# [1] TRUE
