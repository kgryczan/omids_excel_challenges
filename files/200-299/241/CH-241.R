library(tidyverse)
library(readxl)
library(slider)

path = "files/200-299/241/CH-241 Moving Average.xlsx"
input = read_excel(path, range = "B2:C20")
test = read_excel(path, range = "G2:G20") %>%
  mutate(`Moving Average` = as.numeric(`Moving Average`))

result = input %>%
  mutate(
    `Moving Average` = slide_dbl(
      .x = Sales,
      .f = function(window_values) {
        non_zero_values <- window_values[window_values != 0]
        if (length(non_zero_values) >= 2) {
          mean(tail(non_zero_values, 2))
        } else {
          NA_real_
        }
      },
      .before = Inf,
      .after = -1,
      .complete = TRUE
    )
  )

all.equal(result$`Moving Average`, test$`Moving Average`, check.attributes = FALSE) # TRUE
