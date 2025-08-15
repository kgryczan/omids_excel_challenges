library(tidyverse)
library(readxl)
library(hms)

path = "files/200-299/280/CH-280 Flight Planning.xlsx"
input = read_excel(path, range = "B2:F11")
test  = read_excel(path, range = "H2:J8") %>%
  mutate(Duration = as.character(Duration) %>% str_extract("([0-9]+:[0-9]+:[0-9]+)"),
         `Arrival time` = as.character(`Arrival time`) %>% str_extract("([0-9]+:[0-9]+:[0-9]+)")) 

start = "A" 
final_dest = "B"

result = input %>%
  transmute(
    flight_id = as.character(ID),
    origin = From, destination = To,
    start_time = ymd("2024-01-01") + seconds(as.numeric(as_hms(`Departure Time`))),
    end_time = start_time + seconds(as.numeric(as_hms(Duration)))
  ) %>%
  {
    flights_tbl = .
    initial_paths = filter(flights_tbl, origin == start) %>%
      transmute(path = map(flight_id, ~ .x), start_time, end_time, current_location = destination)
    step = function(paths) inner_join(paths, flights_tbl, by = c("current_location" = "origin")) %>%
      filter(start_time.y >= end_time.x) %>%
      transmute(
        path = map2(path, flight_id, c),
        start_time = start_time.x,
        end_time = end_time.y,
        current_location = destination
      )
    accumulate(seq_len(nrow(flights_tbl)), ~ step(.x), .init = initial_paths) %>%
      list_rbind() %>%
      distinct()
  } %>%
  filter(current_location == final_dest) %>%
  transmute(
    ID = map_chr(path, ~ paste(.x, collapse = ",")),
    Duration = as.character(hms::as_hms(as.numeric(end_time - start_time, "secs"))),
    `Arrival time` = format(end_time, "%H:%M:%S")
  ) %>%
  arrange(ID)

all.equal(result, test, check.attributes = FALSE)
# > [1] TRUE