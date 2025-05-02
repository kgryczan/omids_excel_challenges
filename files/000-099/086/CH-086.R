library(tidyverse)
library(readxl)

path = "files/CH-86 KNN Missing values.xlsx"
input = read_excel(path, range = "C2:F12")
test  = read_excel(path, range = "I2:L12") %>%
  mutate(Y = ifelse(Y == 44, 43, Y)) # confirmed by Julian Poeltl in comment

fill_missing_values <- function(data) {
  comp_points <- data %>% filter(complete.cases(.))
  data_filled <- data
  
  for (i in which(!complete.cases(data))) {
    row_to_complete <- data_filled[i, ]
    missing_vars <- names(row_to_complete)[which(is.na(row_to_complete))]
    
    for (var in missing_vars) {
      distances <- comp_points %>%
        mutate(distance = 0)
      
      for (coord in names(row_to_complete)[!is.na(row_to_complete)]) {
        distances <- distances %>%
          mutate(distance = distance + (get(coord) - row_to_complete[[coord]]) ^
                   2)
      }
      
      distances <- distances %>%
        mutate(distance = sqrt(distance))
      closest_points <- distances %>%
        arrange(distance) %>%
        slice(1:2)
      average_value <- closest_points %>%
        summarize(mean_val = mean(.data[[var]], na.rm = TRUE)) %>%
        pull(mean_val)
      data_filled[i, var] <- average_value
      row_to_complete <- data_filled[i, ]
    }
  }
  return(data_filled)
}

result = fill_missing_values(input)

identical(result, test)
# [1] TRUE