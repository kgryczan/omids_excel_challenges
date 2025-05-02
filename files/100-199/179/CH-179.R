library(tidyverse)
library(readxl)

path = "files/CH-179 Reshape a table.xlsx"
input = read_excel(path, range = "B2:F10") %>% as.matrix()
test  = read_excel(path, range = "H2:J14")

result = input %>%
  t() %>%
  as.vector() %>%
  na.omit() %>%
  matrix(ncol = 3, byrow = TRUE) %>%
  as.data.frame() %>%
  setNames(c("Date", "Product ID", "Quantity")) %>%
  mutate(Date = as.POSIXct(janitor::excel_numeric_to_date(as.numeric(Date))),
         Quantity = as.numeric(Quantity))

all.equal(result, test, check.attributes = F)
#> [1] TRUE

