library(tidyverse)
library(readxl)

path <- "300-399/376/CH-376 Table Transformation.xlsx"
input <- read_excel(path, range = "B4:C11", col_names = F) %>% as.matrix()
test <- read_excel(path, range = "E3:G9")

arr = as.vector(t(input))
arr = arr[!is.na(arr)] %>%
  as.data.frame() %>%
  set_names("value") %>%
  mutate(id = row_number())

result = arr %>%
  mutate(
    type = case_when(
      str_length(value) > 3 ~ "Date",
      str_detect(value, "^[A-Za-z]+$") ~ "Name",
      TRUE ~ "Number"
    )
  ) %>%
  pivot_wider(names_from = type, values_from = value) %>%
  fill(Date, Name, .direction = "down") %>%
  filter(!if_any(everything(), is.na))

print(result)
# Different dates
