library(tidyverse)
library(readxl)

path = "files/200-299/234/CH-234 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:G7")

result = input %>%
  separate(
    ID,
    into = c("ID.1", "ID.1.5", "ID.2", "ID.2.5", "ID.3", "ID.4"),
    sep = "-",
    extra = "merge"
  ) %>%
  unite("ID.1", ID.1, ID.1.5, sep = "-", remove = TRUE) %>%
  unite("ID.2", ID.2, ID.2.5, sep = "-", remove = TRUE)
