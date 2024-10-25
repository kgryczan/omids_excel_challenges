library(tidyverse)
library(readxl)

path = "files/CH-133 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C40")
test  = read_excel(path, range = "K2:L8")


dates = seq(as.Date("2024-01-01"), as.Date("2024-02-29"), by = "day")
dates = data.frame(Date = dates)

result = dates %>%
  left_join(input, by = c("Date" = "Date")) %>%
  mutate(year = year(Date), 
         month = month(Date),
         day = day(Date), 
         decade_days = ifelse(ceiling(day / 10) == 4, 3, ceiling(day/10))) %>%
  summarise(`Total Sales` = sum(Sales, na.rm = TRUE),
            group = paste(min(Date), max(Date), sep = " - "),
            .by = c("year", "month", "decade_days")) %>%
  select(Group = group, `Total Sales`)

# results in test are not correct
#    
