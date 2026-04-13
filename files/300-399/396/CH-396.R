library(tidyverse)
library(readxl)

path <- "300-399/396/CH-396 Table Transformation.xlsx"
input <- read_excel(path, range = "B2:B3")
test <- read_excel(path, range = "C6:F12")

result = input %>%
  separate_longer_delim(Question, delim = "\r\n") %>%
  separate_wider_delim(Question, delim = "\t", names_sep = "_") %>%
  janitor::row_to_names(1) %>%
  mutate(Sale = as.numeric(Sale))

all.equal(test, result)
# > [1] TRUE
