library(tidyverse)
library(readxl)

path <- "300-399/374/CH-374 Text Cleaning.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "E3:E8") %>%
  replace_na(list(ID = ""))

bounded_substrings <- function(s) {
  chars <- strsplit(s, "")[[1]]
  n <- length(chars)

  expand.grid(i = 1:(n - 1), j = 2:n) |>
    filter(i < j, chars[i] == chars[j]) |>
    mutate(
      val = purrr::map2_chr(
        i,
        j,
        ~ paste(chars[(.x + 1):(.y - 1)], collapse = "")
      )
    ) |>
    pull(val)
}

result = input %>%
  mutate(
    substrings = map(ID, bounded_substrings) %>% map_chr(paste, collapse = ", ")
  )

all.equal(result$substrings, test$ID)
## [1] TRUE
