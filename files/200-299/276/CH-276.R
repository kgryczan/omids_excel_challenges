library(tidyverse)
library(readxl)
library(gmp)

path = "files/200-299/276/CH-276 Value COnversion.xlsx"
input = read_excel(path, range = "B2:E8")
test  = read_excel(path, range = "F2:F8")

convert_base = function(x, from, to) {
  pmap_chr(list(x, from, to), \(x, from, to) {
    n = strtoi(x, base = from)
    switch(as.character(to),
      "2"  = as.character(as.bigz(n), b=2),
      "8"  = as.character(as.octmode(n)),
      "10" = as.character(n),
      "16" = str_to_upper(as.character(as.hexmode(n)))
    )
  })
}

result = input %>%
  mutate(Answer = convert_base(Number, `From Base`, `To Base`)) 

all.equal(result$Answer, test$`Converted Value`)
# > [1] TRUE