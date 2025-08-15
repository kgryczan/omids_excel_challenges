import pandas as pd
import re
from collections import deque

path = "200-299/280/CH-280 Flight Planning.xlsx"
input = pd.read_excel(path, usecols="B:F", skiprows=1, nrows=9, dtype=str)
test = pd.read_excel(path, usecols="H:J", skiprows=1, nrows=6, dtype=str).rename(columns=lambda c: re.sub(r'\.1$', '', c))

start = "A"
final_dest = "B"

to_seconds = lambda hms: int(pd.to_timedelta(str(hms)).total_seconds()) if pd.notnull(hms) else 0
flights = pd.DataFrame({
    "flight_id": input["ID"].astype(str),
    "origin": input["From"],
    "destination": input["To"],
    "start_time": pd.to_datetime("2024-01-01") + pd.to_timedelta(input["Departure Time"].astype(str)),
    "end_time": pd.to_datetime("2024-01-01") + pd.to_timedelta(input["Departure Time"].astype(str)) + pd.to_timedelta(input["Duration"].apply(to_seconds), unit="s")
})

results = []
queue = deque(([r["flight_id"]], r["start_time"], r["end_time"], r["destination"]) 
              for _, r in flights[flights["origin"] == start].iterrows())
while queue:
    path, st, et, loc = queue.popleft()
    if loc == final_dest:
        results.append((path, st, et))
        continue
    for _, nrow in flights[(flights["origin"] == loc) & (flights["start_time"] >= et)].iterrows():
        if nrow["flight_id"] not in path:
            queue.append((path + [nrow["flight_id"]], st, nrow["end_time"], nrow["destination"]))

def format_duration(td):
    return f"{int(td.total_seconds())//3600:02}:{int(td.total_seconds())%3600//60:02}:{int(td.total_seconds())%60:02}"

result = pd.DataFrame([(",".join(p), format_duration(et - st), et.strftime("%H:%M:%S")) for p, st, et in results], 
                     columns=["ID", "Duration", "Arrival time"]).sort_values("ID").reset_index(drop=True)

print(result.equals(test))
