library(tidyverse)
library(readxl)

path <- "300-399/384/CH-384 Table Transformation.xlsx"
df <- read_excel(path, range = "B3:E11", col_names = TRUE)
test <- read_excel(path, range = "G3:J9", col_names = TRUE)

name <- df[seq(1, nrow(df), 2), ]
sale <- df[seq(2, nrow(df), 2), ]
name <- name |>
  mutate(Date = zoo::na.locf(Date))
result <- bind_rows(
  name |>
    transmute(
      Date,
      Customer,
      Product = `product 1`,
      Sale = sale$`product 1`
    ),
  name |>
    transmute(Date, Customer, Product = `product 2`, Sale = sale$`product 2`)
) |>
  mutate(.row = rep(seq_len(nrow(name)), 2)) |>
  drop_na() |>
  arrange(.row) |>
  select(-.row) |>
  mutate(Sale = as.integer(Sale))

colnames(test) <- colnames(result)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
