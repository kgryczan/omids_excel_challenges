library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-061 Sales per customer.xlsx", range = "B2:D36")
input2 = read_excel("files/CH-061 Sales per customer.xlsx", range = "F2:G8")
test   = read_excel("files/CH-061 Sales per customer.xlsx", range = "I2:J10") %>%
  arrange(desc(Sales))

find_latest_id <- function(id, changes) {
  new_id <- changes %>% filter(`OLD ID` == id) %>% pull(`New ID`)
  if (length(new_id) == 0) {
    return(id)
  } else {
    return(find_latest_id(new_id, changes))
  }
}

transactions <- input1 %>%
  mutate(Customer = map_chr(`Customer ID`, find_latest_id, input2)) %>%
  summarise(Sales = sum(Quantity), .by = Customer) %>%
  arrange(desc(Sales))

identical(test, transactions)
# [1] TRUE