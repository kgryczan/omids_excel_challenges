library(tidyverse)
library(readxl)

path <- "400-499/424/CH-424 Replacement.xlsx"
input <- read_excel(path, range = "B3:D9")
test <- read_excel(path, range = "F3:H9")

result <- input %>%
  mutate(`Product ID` = chartr("ABC", "BCA", `Product ID`))

all.equal(result, test)
# True
