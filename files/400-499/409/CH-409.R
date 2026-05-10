library(tidyverse)
library(readxl)

path <- "400-499/409/CH-409 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F5")

result <- input %>%
  mutate(num = str_extract_all(ID, "\\d+")) %>%
  unnest(num) %>%
  filter(
    as.numeric(str_sub(num, 1, 1)) %% 2 == 0,
    as.numeric(str_sub(num, -1, -1)) %% 2 == 1
  )

all.equal(result$ID, test$ID)
# [1] TRUE
