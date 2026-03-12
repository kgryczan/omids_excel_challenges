library(tidyverse)
library(readxl)

path <- "300-399/380/CH-380 Matrix Calculation.xlsx"
input <- read_excel(path, range = "B3:G8")
test <- read_excel(path, range = "J3:K8")

result = input %>%
  mutate(weight = 2^(rev(row_number()) - 1)) %>%
  pivot_longer(A:E, names_to = "Factor", values_to = "bit") %>%
  summarise(score = sum(bit * weight), .by = Factor) %>%
  arrange(score) %>%
  mutate(Rank = row_number()) %>%
  select(Rank, Factor)

all.equal(result, test)
#> [1] TRUE
