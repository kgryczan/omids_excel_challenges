library(tidyverse)
library(readxl)

path <- "400-499/445/CH-445 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:F12")
test <- read_excel(path, range = "H3:K12")

result <- input %>%
  pivot_longer(
    cols = c(C1, C2, C3),
    names_to = "CUSTOMER",
    values_to = "SALES",
    values_drop_na = TRUE
  ) %>%
  arrange(DATE, CUSTOMER) %>%
  select(DATE, CUSTOMER, PRODUCT, SALES)

all.equal(result, test)
# TRUE
