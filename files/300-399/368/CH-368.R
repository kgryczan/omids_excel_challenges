library(tidyverse)
library(readxl)
library(stringi)

path <- "300-399/368/CH-368 Text Cleaning.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "E3:E8")

mirror_half <- function(x) {
  n <- nchar(x)
  best <- ""
  for (i in seq_len(n)) {
    for (len in seq_len((n - i + 1) %/% 2)) {
      left <- substr(x, i, i + len - 1)
      right <- substr(x, i + len, i + 2 * len - 1)
      if (left == stri_reverse(right) && len > nchar(best)) {
        best <- left
      }
    }
  }
  best
}

result = input %>%
  mutate(ID = map_chr(ID, mirror_half))

all.equal(result$ID, test$ID)
# Last one correct but not accordign to given answers.
