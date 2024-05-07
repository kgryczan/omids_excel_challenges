library(tidyverse)
library(readxl)

input = read_excel("files/CH-048 Transformation.xlsx", range = "B1:B20")
test  = read_excel("files/CH-048 Transformation.xlsx", range = "E2:O12") %>%
  column_to_rownames('...1')


r1 = input %>%
  separate(`Questions - Combination models`, into = c("first", "second"), sep = "\\+")

r2 = data.frame(first = r1$second, second = r1$first)

r3 = rbind(r1, r2) %>%
  mutate(value = 1) %>%
  pivot_wider(names_from = second, values_from = value, values_fn = sum) %>%
  select(first, GA, PSO, DE, FA, HS, RO, SO, CS, TS, MPSO) %>%
  column_to_rownames('first')

all.equal(test, r3, check.attributes = FALSE)
# [1] TRUE
         