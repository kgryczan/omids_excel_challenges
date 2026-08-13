library(tidyverse)
library(readxl)

path <- "400-499/457/CH-457 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:F15")
test <- read_excel(path, range = "H3:J10")
fmt <- \(x) sub("^0", "", sub("/0", "/", format(x, "%d/%m/%Y")))

result <- input %>%
  mutate(
    PRODUCTS = pmap_chr(
      across(starts_with("Product")),
      ~ paste(sort(na.omit(c(...))), collapse = ",")
    ),
    Date = as.Date(Date)
  ) %>%
  arrange(Date) %>%
  mutate(
    group = cumsum(
      row_number() == 1 | PRODUCTS != lag(PRODUCTS) | Date - lag(Date) != 1
    )
  ) %>%
  group_by(group) %>%
  summarise(
    PRODUCTS = first(PRODUCTS),
    QUANTITY = sum(Quantity),
    start = min(Date),
    end = max(Date),
    .groups = "drop"
  ) %>%
  mutate(
    dates = if_else(
      start == end,
      fmt(start),
      paste(fmt(start), fmt(end), sep = "-")
    )
  ) %>%
  select(PRODUCTS, QUANTITY, dates)
all.equal(result, test)
# There are sorting discrepancies
