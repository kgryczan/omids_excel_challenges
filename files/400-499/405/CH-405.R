library(tidyverse)
library(readxl)

path <- "400-499/405/CH-405 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:C7")
test <- read_excel(path, range = "E3:H11")

result = input %>%
  deframe() %>%
  as.list() %>%
  as_tibble() %>%
  separate_rows(everything(), sep = " , ") %>%
  mutate(
    DATE = as.Date(DATE, format = "%d/%m/%Y") %>% as.POSIXct(),
    SALES = as.numeric(SALES)
  )

all.equal(result, test)
# [1] TRUE
