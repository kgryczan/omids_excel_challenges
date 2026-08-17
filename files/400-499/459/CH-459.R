library(tidyverse)
library(readxl)

path <- "400-499/459/CH-459 Filter.xlsx"
input <- read_excel(path, range = "B3:D13")
test <- read_excel(path, range = "H3:I7")

daily <- input %>%
  summarise(Sales = sum(Sales), .by = c(Product, Date))

qualified <- daily %>%
  group_by(Product) %>%
  summarise(
    qualified = any(map_lgl(seq_len(n()), \(i) {
      i + 2 <= n() && all(diff(Date[i:(i + 2)]) == 1)
    })),
    .groups = "drop"
  ) %>%
  filter(qualified)

result <- daily %>%
  semi_join(qualified, by = "Product") %>%
  arrange(Date) %>%
  select(Date, Product)
all.equal(result, test)
