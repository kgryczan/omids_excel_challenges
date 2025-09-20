library(tidyverse)
library(readxl)

path = "files/200-299/298/CH-298 Table Transformation.xlsx"
input = read_excel(path, range = "B2:C5")
test  = read_excel(path, range = "E2:F26")

result = input %>%
  mutate(
    Date = str_extract_all(Date, "\\d{1,2}/\\d{1,2}/\\d{4}") %>%
      map(~ {
        seqs <- mdy(.x)
        seq(seqs[1], seqs[2], by = "day")
      })) %>%
  mutate(n = map_int(Date, length),
         `Daily Sale` = `Total Sales` / n) %>%
  unnest() %>%
  select(Date, `Daily Sale`)

# Result not equal because of mistake in provided data.