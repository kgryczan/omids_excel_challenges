library(tidyverse)
library(readxl)

path <- "300-399/383/CH-383 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F5")

is_valid <- function(s) {
  digits <- str_extract_all(s, "\\d")[[1]] %>% as.integer()
  digits[1] %% 2 == 0 && digits[length(digits)] %% 2 == 1
}

result <- input %>%
  filter(map_lgl(ID, is_valid))

all.equal(result$ID, test$ID)
# [1] TRUE
