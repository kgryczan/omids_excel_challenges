library(tidyverse)
library(readxl)

path = "files/300-399/CH-300 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "G2:H7")

custom_grouping = function(sales) {
  if (!length(sales)) return(data.frame(Group = integer(), `Total Sales` = numeric()))
  res = list(data.frame(Group = 1, `Total Sales` = sales[1]))
  grp = 2
  sum = 0
  prev = sales[1]
  for (i in sales[-1]) {
    sum = sum + i
    if (sum >= 2 * prev) {
      res[[grp]] = data.frame(Group = grp, `Total Sales` = sum)
      grp = grp + 1
      prev = sum 
      sum = 0
    }
  }
  if (sum) res[[grp]] = data.frame(Group = grp, `Total Sales` = sum)
  bind_rows(res)
}


result = custom_grouping(input$Sales)
  