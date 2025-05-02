library(tidyverse)
library(readxl)

path = "files/CH-128 Cartesian Product.xlsx"
test  = read_excel(path, range = "C1:C65")

lets = c("A","B","C","D")

result = expand.grid(lets,lets, lets) %>%
  unite("result", Var1:Var3, sep = "") %>%
  arrange(result)

all.equal(result$result, test$Result)
#> [1] TRUE