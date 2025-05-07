library(tidyverse)
library(readxl)

path = "files/200-299/230/CH-230 Project scheduling.xlsx"
test = read_excel(path, range = "F2:H11") %>%
  mutate(across(c(Start, Finish), ~ as.Date(.x, origin = "1899-12-30")))
input = read_excel(path, range = "B3:D11", col_names = c('id', 'dur', 'pred'))

parse_rel <- function(x) {
  str_remove_all(x, " days?") %>%
    str_split(",", simplify = FALSE) %>%
    unlist() %>%
    map_dfr(
      ~ {
        m <- str_match(.x, "(\\d+)(FS|FF)?(?:\\+([0-9]+))?")
        pred <- as.integer(m[2])
        type <- ifelse(is.na(m[3]), "FS", m[3])
        lag <- as.integer(m[4])
        lag <- replace_na(lag, 0L)
        tibble(pred, type, lag)
      }
    )
}

input <- input %>%
  mutate(
    start = as.Date(NA),
    finish = as.Date(NA)
  ) %>%
  arrange(id)

input$start[input$id == 1] <- ymd("2025-04-01")
input$finish[input$id == 1] <- input$start[input$id == 1] +
  days(input$dur[input$id == 1] - 1)

while (any(is.na(input$start))) {
  walk(input$id[is.na(input$start)], function(i) {
    if (is.na(input$pred[i])) return()
    rels <- parse_rel(input$pred[i])
    if (!all(rels$pred %in% input$id[!is.na(input$finish)])) return()

    cand_st <- rels %>%
      mutate(
        st = case_when(
          type == "FS" ~ input$finish[pred] + days(lag + 1),
          type == "FF" ~
            (input$finish[pred] + days(lag)) - days(input$dur[i] - 1)
        )
      ) %>%
      pull(st)

    st_i <- max(cand_st)
    input$start[i] <<- st_i
    input$finish[i] <<- st_i + days(input$dur[i] - 1)
  })
}

result = input %>%
  select(`Task Name` = id, Start = start, Finish = finish)

all.equal(test, result, check.attributes = FALSE)
