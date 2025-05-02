library(tidyverse)
library(readxl)

path = "files/CH-225 Date Range.xlsx"
start = read_excel(path, range = "C3", col_names = F) %>% pull()
end = read_excel(path, range = "C4", col_names = F) %>% pull()
step = read_excel(path, range = "C5", col_names = F) %>% pull()
test = read_excel(path, range = "E2:E12") %>% mutate(Dates = as.Date(Dates))

result = data.frame(Dates = seq.Date(as.Date(start), as.Date(end), by = step))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
