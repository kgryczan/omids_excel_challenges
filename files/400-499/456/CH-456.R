library(tidyverse)
library(readxl)

path <- "400-499/456/CH-456 Number Series.xlsx"
input <- read_excel(path, range = "B3:C6")
test <- read_excel(path, range = "E3:F10")

result <- input %>%
  complete(Date = seq(min(Date), max(Date), "day")) %>%
  mutate(Sale = approx(Date, Sale, Date)$y)

all.equal(result, test)
