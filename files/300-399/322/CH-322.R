library(tidyverse)
library(readxl)

path = "300-399/322/CH-322 Text Cleaning.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:E9")

result = input %>%
  mutate(
    Level = str_extract(Info, "(?i)level\\s*(\\d+)") %>%
      str_extract("\\d+") %>%
      parse_number() %>%
      as.character() %>%
      coalesce(str_extract(Info, "(?i)ground")),
    Zone  = str_extract(Info, "(?i)zone\\s*(\\d+)") %>%
      str_extract("\\d+") %>%
      coalesce(str_extract(Info, "(?i)\\b(North|South|East|West)\\b")) %>%
      replace_na("-")
  )

all.equal(result %>% select(-Info), test)
