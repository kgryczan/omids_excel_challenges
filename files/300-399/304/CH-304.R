library(tidyverse)
library(readxl)

path = "files/300-399/304/CH-304 Reverse Substrings Between Dashes.xlsx"
input = read_excel(path, range = "B1:B6")
test  = read_excel(path, range = "C1:C6")

reverse_segments <- function(s) {
  str_replace_all(s, "(?<=-)\\w+(?=-)", 
                  ~str_c(rev(str_split(.x, "", simplify = TRUE)), collapse = ""))
}
result = input %>%
  mutate(Result = map_chr(Question, ~ reverse_segments(.)))
all.equal(result$Result, test$Result)
## [1] TRUE        