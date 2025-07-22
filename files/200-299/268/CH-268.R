library(tidyverse)
library(readxl)

excel = "files/200-299/268/CH-268 Custom Grouping.xlsx"
dat = read_excel(excel, range = "B2:C16")
test = read_excel(excel, range = "F2:H16")

conf = list(c("A101", "A105"), c("B01", "B03"))

grp = function(ids, pairs) {
  g = 1
  seen = character()
  out = integer(length(ids))
  for (i in seq_along(ids)) {
    id = ids[i]
    hit = any(map_lgl(pairs, ~all(.x %in% c(seen, id))))
    if (hit) {
      g = g + 1
      seen = id
    } else {
      seen = union(seen, id)
    }
    out[i] = g
  }
  out
}

res = dat %>% mutate(Group = grp(ID, conf))

all.equal(res$Group, test$Group) # TRUE