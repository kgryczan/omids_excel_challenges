library(tidyverse)
library(readxl)

path <- "300-399/381/CH-381 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F7")

is_valid = function(num) {
  digits <- str_extract_all(num, "\\d") %>% unlist() %>% as.integer()
  val = sum(abs(diff(digits %% 2))) >= 2
  return(val)
}

result <- input %>%
  mutate(is_valid = map_lgl(ID, is_valid)) %>%
  filter(is_valid)

all.equal(result$ID, test$ID)
# [1] TRUE
