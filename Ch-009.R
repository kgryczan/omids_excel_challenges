library(tidyverse)
library(readxl)

input = read_excel("files/CH-009.xlsx", range = "B2:D32")
test1 = read_excel("files/CH-009.xlsx", range = "F2:G5") %>% janitor::clean_names()
test2 = read_excel("files/CH-009.xlsx", range = "I2:J5") %>% janitor::clean_names()


result = input %>%
  group_by(Product) %>% 
  summarise(seq = str_c(Result, collapse = "")) %>%
  ungroup()

# pattern +--

process_pattern1 = function(string) {
  string = string %>%
    str_replace_all("\\+\\-\\-", "3") %>%
    str_replace_all("\\-\\-3", "/5") %>%
    str_replace_all("3\\+\\-", "5/") %>%
    str_replace_all("\\-3", "/4") %>%
    str_replace_all("3\\+", "4/") %>%
    str_replace_all("/4\\+", "/5/") %>%
    str_replace_all("44", "8") %>%
    str_replace_all("35", "8") 
  
  numbers = as.numeric(str_extract_all(string, "")[[1]]) %>% max(., na.rm = TRUE) 
  return(numbers)
}

result1 = result %>%
  rowwise() %>%
  mutate(max_seq = map_dbl(seq, process_pattern1))
  
identical(result1$max_seq, test1$x)
#> [1] TRUE

# pattern +-

process_pattern2 = function(string) {
  string = string %>%
    str_replace_all("\\+\\-", "2") %>%
    str_replace_all("^\\-2", "3") %>%
    str_replace_all("2\\+$", "3") %>%
    str_replace_all("\\-3", "4") %>%
    str_replace_all("22", "4") %>%
    str_replace_all("32|23", "5") %>%
    str_replace_all("44", "8")

    numbers = as.numeric(str_extract_all(string, "")[[1]]) %>% max(., na.rm = TRUE)

  
  return(numbers)
}

result2 = result %>%
  rowwise() %>%
  mutate(max_seq = map_dbl(seq, process_pattern2))

identical(result2$max_seq, test2$x)
#> [1] TRUE


