library(tidyverse)
library(readxl)

path = "files/200-299/294/CH-294 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C18")
test  = read_excel(path, range = "G2:H5")

g <- c <- 1
for(i in 1:nrow(input)) {
  input$Group[i] <- g
  c <- ifelse(input$Result[i] == "+", c + 1, 1)
  if(c > 4) { g <- g + 1; c <- 1 }
}

result = input %>%
  group_by(Group) %>%
  summarise(
    Start_Date = format(as.Date(first(Date)), "%d/%b/%Y"),
    End_Date = format(as.Date(last(Date)), "%d/%b/%Y"),
    `number of dates` = n(),
    .groups = 'drop'
  ) %>%
  mutate(
    End_Date = ifelse(`number of dates` < 4, NA, End_Date),
    `number of dates` = ifelse(`number of dates` < 4, "-", `number of dates`)) %>%
  select(-Group) %>%
  unite("Group", Start_Date, End_Date, sep = " - ", remove = TRUE)

all.equal(result, test)
# TRUE
