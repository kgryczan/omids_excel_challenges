library(tidyverse)
library(readxl)

path <- "300-399/327/CH-327 Column Splitting.xlsx"
input <- read_excel(path, range = "B2:B9")
test  <- read_excel(path, range = "D2:E9")

levels = c("Upper Ground", "Ground", "Under Ground")
Zones = c("West", "East", "North", "South", "South East", "North West")

result = input %>%
  rowwise() %>%
  mutate(
    Level = str_extract_all(Info, paste0(levels, collapse = "|")),
    Zone = str_extract_all(Info, paste0(Zones, collapse = "|")),
    Zone = if (length(Zone) > 1) paste(Zone, collapse = " ") else as.character(Zone)
  ) %>%
  ungroup() %>%
  unnest(Level) %>%
  select(-Info)

all.equal(result, test)
# [1] TRUE
