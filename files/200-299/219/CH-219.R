library(tidyverse); library(readxl)
path <- "files/CH-219 Project scheduling.xlsx"
input <- read_excel(path, range = "B2:D11")
test <- read_excel(path, range = "F2:H11")

schedule_tasks <- function(tasks, start_date = Sys.Date()) {
    tasks_df <- tasks |> transmute(
        id = as.character(`Task Name`),
        duration = `Duration (day)`,
        predecessors = str_split(Predecessors, ",") |> map(~ setdiff(.x, "-") |> str_trim())
    )

    task_durations <- setNames(tasks_df$duration, tasks_df$id)
    task_preds <- setNames(tasks_df$predecessors, tasks_df$id)

    topo_order <- {
        visited <- setNames(rep(FALSE, nrow(tasks_df)), tasks_df$id)
        result <- character()
        dfs <- function(node) {
            if (visited[node]) return()
            visited[node] <<- TRUE
            walk(task_preds[[node]], dfs)
            result <<- c(node, result)
        }
        walk(tasks_df$id, dfs)
        rev(result)
    }

    dates <- list()
    for (id in topo_order) {
        preds <- task_preds[[id]]
        start <- if (length(preds) == 0) start_date else max(sapply(preds, \(p) dates[[p]]$end))
        end <- start + task_durations[[id]]
        dates[[id]] <- list(start = start, end = end)
    }

    tibble(
        id = names(dates),
        start_date = map_dbl(dates, "start") |> as.Date(origin = "1970-01-01"),
        end_date = map_dbl(dates, "end") |> as.Date(origin = "1970-01-01") - 1
    ) |> arrange(id)
}

schedule_tasks(input, as.Date("2025-04-01"))

