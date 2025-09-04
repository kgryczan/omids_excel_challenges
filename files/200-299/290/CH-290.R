library(tidyverse)
library(readxl)
library(hms)

path = "files/200-299/290/CH-290 Flight Planning.xlsx"
input1 = read_excel(path, range = "B2:F11")
input2 = read_excel(path, range = "H2:I6")
test  = read_excel(path, range = "K2:M5")

input2 = input2 %>% 
  mutate(`Time Zone` = parse_number(`Time Zone`))

input = input1 %>%
  left_join(input2, by = c("From" = "City"), suffix = c("_a","_orig")) %>%
  left_join(input2, by = c("To" = "City"), suffix = c("_orig","_dest")) %>%
  mutate(dep_time_utc = `Departure Time` - hours(`Time Zone_orig`),
         Duration = as_hms(Duration) %>% as.duration(),
         arr_time_utc = dep_time_utc + Duration,
         arr_time_local = arr_time_utc + hours(`Time Zone_dest`)) %>%
  select(ID, From, To, dep_time_utc, arr_time_utc, arr_time_local)
         
routes = function(city = "A", time = min(input$dep_time_utc) - hours(1), path = c(), target = "B") {
  if(city == target) return(list(path))
  if(city %in% names(path) || length(path) > 3) return(NULL)
  
  input %>% 
    filter(From == city, dep_time_utc >= time) %>%
    {do.call(c, pmap(list(.$ID, .$To, .$arr_time_utc), 
           ~routes(..2, ..3, c(path, setNames(..1, city)), target)))}
}

r = routes() %>% compact()

result = bind_rows(r) %>%
  mutate(rn = row_number()) %>%
  pivot_longer(-rn, names_to = "From", values_to = "ID") %>%
  left_join(input, by = c("From", "ID")) %>%
  na.omit(ID) %>%
  summarise(
    ID = paste(ID, collapse = ", ") %>% str_remove_all(", NA"),
    start = first(dep_time_utc),
    end = last(arr_time_utc),
    end_local = last(arr_time_local),
    .by = rn
  ) %>%
  mutate(Duration = as_hms(end - start),
         `Arrival Time` = format(end_local, "%H:%M")) %>%
  select(ID, Duration, `Arrival Time`)

print(result)
# A tibble: 3 × 3
# ID      Duration `Arrival Time`
# <chr>   <time>   <chr>         
# 1, 6    05:20    18:35         
# 3, 9    04:40    20:40         
# 7       04:45    23:45         