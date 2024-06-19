library(tidyverse)
library(readxl)

path = "files/CH-070 coin change problem.xlsx"
test = read_excel(path, range = "H2:K14") %>% arrange(`1$`,`2$`,`5$`,`10$`)

target <- 11
coins <- c(1, 2, 5, 10)

counts <- expand.grid(
  n1 = 0:(target / coins[1]),
  n2 = 0:(target / coins[2]),
  n3 = 0:(target / coins[3]),
  n4 = 0:(target / coins[4])
)

combinations <- counts %>%
  mutate(
    total = n1 * coins[1] + n2 * coins[2] + n3 * coins[3] + n4 * coins[4]
  ) %>%
  filter(total == target) %>%
  select(-total) %>%
  arrange(n1,n2,n3,n4)

all.equal(combinations, test, check.attributes = FALSE)
# [1] TRUE