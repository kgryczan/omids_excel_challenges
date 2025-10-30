library(tidyverse)
library(readxl)
library(janitor)

path = "files/300-399/318/CH-318 Table Transformation.xlsx"
input = read_excel(path, range = "B2:E10", col_names = FALSE)
test  = read_excel(path, range = "G2:J7")

m = as.matrix(input)
m[str_starts(m, "Column")] = NA

df = m %>%
    as_tibble() %>%
    map_df(~ {
        x = na.omit(.x)
        c(x, rep(NA, nrow(m) - length(x)))
    }) %>%
    row_to_names(1) %>%
    drop_na() %>%
    mutate(Date = excel_numeric_to_date(as.numeric(Date)) %>% as.POSIXct(),
        Quantity = as.numeric(Quantity))

all.equal(result, test)
