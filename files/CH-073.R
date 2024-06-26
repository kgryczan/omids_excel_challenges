library(tidyverse)
library(readxl)

path = "files/CH-073 Custom splitter 2.xlsx"
input = read_xlsx(path, range = "B2:B15")
test  = read_xlsx(path, range = "D2:F24")

date_pattern = "[0-9]{4}\\/[0-9]{1,2}\\/[0-9]{1,2}"
product_quant_pattern = "([A-Z]+[0-9]+)"

result = input %>%
  mutate(
    Date = str_extract(Info, date_pattern),
    Info2 = str_remove(Info, date_pattern),
    prod_quant = map(Info2, ~ unlist(str_extract_all(.x, product_quant_pattern)))
  ) %>%
  unnest(prod_quant) %>%
  select(Date, prod_quant) %>%
  extract(prod_quant, into = c("Product", "Quantity"), regex = "([A-Z]+)([0-9]+)") %>%
  mutate(Quantity = as.numeric(Quantity))

identical(result, test)
# [1] TRUE
