library(tidyverse)
library(readxl)

path = "files/200-299/295/CH-295 Text Matching.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:E9")

get_substrings <- function(id, min_length = 3, max_length = NULL) {
  id1 = unlist(strsplit(id, ""))
  n = length(id1)
  if (is.null(max_length)) max_length = n
  purrr::flatten_chr(
    purrr::map(min_length:min(max_length, n), function(len) {
      purrr::map_chr(1:(n - len + 1), function(start) {
        paste(id1[start:(start + len - 1)], collapse = "")
      })
    })
  )
}

result = expand.grid(`ID 1` = input$ID, `ID 2` = input$ID) %>%
  mutate_all(as.character) %>%
  filter(`ID 1` != `ID 2`,`ID 1` < `ID 2`) %>%
  rowwise() %>%
  mutate(substrings = list(get_substrings(`ID 1`))) %>%
  unnest(substrings) %>%
  ungroup() %>%
  filter(str_detect(`ID 2`, substrings))

# # A tibble: 10 × 3
# `ID 1`      `ID 2`   substrings
# <chr>       <chr>    <chr>     
# 1 MA-210      MX-21551 -21       
# 2 MX-21551    MX-21F   MX-       
# 3 MX-21551    MX-21F   X-2       
# 4 MX-21551    MX-21F   -21       
# 5 MA-210      MX-21F   -21       
# 6 MX-21551    MX-M5512 MX-       
# 7 MX-21551    MX-M5512 551       
# 8 MX-21F      MX-M5512 MX-       
# 9 FF-512      MX-M5512 512       
# 10 BN-8213F2  RF_821   821       


r2 = result %>%
  select(-substrings) %>%
  distinct()
