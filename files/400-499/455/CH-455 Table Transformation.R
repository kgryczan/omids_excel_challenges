library(tidyverse)
library(readxl)

path <- "400-499/455/CH-455 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:G8")
test <- read_excel(path, range = "I3:L11")

result <- input %>%
  mutate(.row = row_number()) %>%
  pivot_longer(A:D, names_to = "PRODUCT", values_to = "SALES") %>%
  filter(SALES != 0) %>%
  rename(DATE = Date, CUSTOMER = Custoemr) %>%
  arrange(DATE, CUSTOMER, desc(SALES)) %>%
  select(DATE, CUSTOMER, PRODUCT, SALES)
all.equal(result, test)
