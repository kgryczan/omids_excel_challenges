library(tidyverse)
library(readxl)

path = "files/CH-211Column Splitting.xlsx"
input = read_excel(path, range = "B2:B8")
test  = read_excel(path, range = "D2:F8")

split_string <- function(x) {
  x <- as.character(x)
  n <- nchar(x)
  
  get_parts <- function(s, len) {
    if (len <= 3) {
      c(s, NA, NA)
    } else if (len <= 6) {
      mid <- ceiling(len / 2)
      c(substr(s, 1, mid),
        substr(s, mid + 1, len),
        NA)
    } else {
      first <- substr(s, 1, 3)
      second <- substr(s, 4, 6)
      third <- substr(s, 7, len)
      c(first, second, third)
    }
  }
  result <- t(sapply(seq_along(x), function(i) {
    get_parts(x[i], n[i])
  }))
  colnames(result) <- c("Part 1", "Part 2", "Part 3")
  as.data.frame(result, stringsAsFactors = FALSE)
}

result = split_string(input$ID)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE