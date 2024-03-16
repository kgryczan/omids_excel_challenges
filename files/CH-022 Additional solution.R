library(tidyverse)
library(readxl)

input = read_excel("files/CH-022 Convert Number To Text.xlsx" , range = "B2:B10")
test  = read_excel("files/CH-022 Convert Number To Text.xlsx" , range = "G2:H10")

textify_number = function(number) {
  lookup = tibble(num = c(0:19), 
         text = c("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                  "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                  "seventeen","eighteen", "nineteen"))
  lookup_tens = tibble(num = c(2:9), 
                       text = c("twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"))
  
  split_decimal = function(number) {
    number = as.character(number)
    if (str_detect(number, "\\.")) {
      whole_part = substr(number, 1, str_locate(number, "\\.")[[1]] - 1)
      decimal_part = substr(number, str_locate(number, "\\.")[[1]] + 1, nchar(number))
    }
    else {
      whole_part = number
      decimal_part = ""
    }

    return(list(whole_part, decimal_part))
  }
  
  split_and_textify_number = function(number) {
    lenght = nchar(number)
    if (lenght == 1) {
      return(lookup$text[lookup$num == as.numeric(number)])
    } else if (lenght == 0) {
      return("")
    } else if (lenght == 2) {
      if (as.numeric(number) < 20) {
        return(lookup$text[lookup$num == as.numeric(number)])
      } else {
        first_digit = substr(number, 1, 1) 
        second_digit = substr(number, 2, 2)
        return(paste(lookup_tens$text[lookup_tens$num == as.numeric(first_digit)], 
                     lookup$text[lookup$num == as.numeric(second_digit)], sep = "-"))
      }
    } else if (lenght == 3) {
      first_digit = substr(number, 1, 1) 
      second_digit = substr(number, 2, 2)
      third_digit = substr(number, 3, 3)
      return(paste(lookup$text[lookup$num == as.numeric(first_digit)], "hundred", 
                   split_and_textify_number(paste(second_digit, third_digit, sep = "")), sep = " "))
    } else if (lenght == 4) {
      first_digit = substr(number, 1, 1) 
      second_digit = substr(number, 2, 2)
      third_digit = substr(number, 3, 3)
      fourth_digit = substr(number, 4, 4)
      return(paste(lookup$text[lookup$num == as.numeric(first_digit)], "thousand", 
                   split_and_textify_number(paste(second_digit, third_digit, fourth_digit, sep = "")), sep = " "))
    }
  }
  
  inp_part_text = split_and_textify_number(split_decimal(number)[[1]])
  dec_part_text = split_and_textify_number(split_decimal(number)[[2]])
  result = ifelse(dec_part_text == "", inp_part_text, paste(inp_part_text, "point", dec_part_text)) %>%
    str_to_sentence()

  return(result)
  
}

result = input %>%
  mutate(Text = map_chr(Number, textify_number)) 

identical(result, test)
# [1] TRUE


