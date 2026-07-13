library(tidyverse)
library(readxl)

path <- "400-499/441/CH-441 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:I10")

chars <- str_split(input$ID, "")
seen <- accumulate(chars, union, .init = character())

result <- tibble(
  ID = input$ID,
  chars = map2(chars, head(seen, -1), \(x, previous) {
    unique(x[!x %in% previous])
  })
) %>%
  unnest_wider(chars, names_sep = "") %>%
  rename_with(\(x) str_replace(x, "^chars", "ID")) %>%
  select(-ID)

all.equal(result, test)
# TRUE
