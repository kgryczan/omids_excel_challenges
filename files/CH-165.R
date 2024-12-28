library(tidyverse)
library(readxl)

path <- "files/CH-165 Customer Grouping.xlsx"
input <- read_excel(path, range = "B2:D11")
test <- read_excel(path, range = "F2:J6")

grid <- expand.grid(unique(input$Month), unique(input$Customer)) %>%
  left_join(input, by = c("Var1" = "Month", "Var2" = "Customer")) %>%
  rename(Month = Var1, Customer = Var2) %>%
  replace_na(list(Quantity = 0)) %>%
  arrange(Customer, Month) %>%
  mutate(FirstDate = min(Month[Quantity > 0]),
         status = case_when(
           Month == FirstDate ~ "New",
           Month < FirstDate & Quantity == 0 ~ "",
           Month != FirstDate & Quantity == 0 ~ "Inactive",
           Month != FirstDate & Quantity > 0 & lag(Quantity) == 0 ~ "Returning",
           Month != FirstDate & Quantity > 0 & lag(Quantity) > 0 ~ "ACTIVE",
           TRUE ~ ""
         ), .by = Customer) %>%
  filter(Month > 1, status != "") %>%
  select(Month, Customer, status) %>%
  summarise(Customer = str_c(Customer, collapse = ", "), .by = c(Month, status)) %>%
  pivot_wider(names_from = status, values_from = Customer) %>%
  relocate(New, .after = Month)

all.equal(grid, test, check.attributes = FALSE) 
#> [1] TRUE
