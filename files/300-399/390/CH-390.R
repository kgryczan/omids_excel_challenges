library(tidyverse)
library(readxl)
library(anytime)
library(lubridate)

path <- "300-399/390/CH-390 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:E6")
test <- read_excel(path, range = "G3:I9")

result <- input %>%
  pivot_longer(-col1, names_to = "col", values_to = "val") %>%
  pivot_wider(names_from = col1, values_from = val) %>%
  separate_longer_delim(Dates, delim = ", ") %>%
  select(Date = Dates, Customer, Product) %>%
  mutate(
    Date = as.character(Date),
    Date = case_when(
      str_detect(Date, "^\\d+$") ~ as.Date(
        as.numeric(Date),
        origin = "1899-12-30"
      ),
      TRUE ~ coalesce(dmy(Date), mdy(Date))
    )
  )

# transformation technically correct. one extra row in the result and incosistence in the date format.
