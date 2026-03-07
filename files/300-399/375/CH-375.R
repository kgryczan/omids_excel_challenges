library(tidyverse)
library(readxl)

path <- "300-399/375/CH-375 Table Transformation.xlsx"
input <- read_excel(
  path,
  range = "B4:C11",
  col_types = c("text", "text"),
  col_names = F
) %>%
  as.matrix()
test <- read_excel(path, range = "E3:G8")

result = input %>%
  matrix(., ncol = 1, byrow = TRUE) %>%
  na.omit() %>%
  as.data.frame() %>%
  mutate(group = cumsum(str_detect(V1, "^[0-9]{5}"))) %>%
  mutate(nr = row_number(), .by = group) %>%
  pivot_wider(names_from = nr, values_from = V1) %>%
  select(Date = `1`, Product = `3`, Sale = `2`) %>%
  mutate(
    Date = janitor::excel_numeric_to_date(as.numeric(Date)) %>% as.POSIXct(),
    Sale = as.numeric(Sale)
  ) %>%
  arrange(Date, desc(Product), desc(Sale))

all.equal(result, test, check.attributes = FALSE)
# different Product mapping.
