import pandas as pd

path = "300-399/329/CH-329 Date Calculation.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=6, skiprows=1)
test = pd.read_excel(path, usecols="D", nrows=6, skiprows=1)
test["End Time"] = pd.to_datetime(test["End Time"], dayfirst=True)

input["Start Date"] = pd.to_datetime(input["Start Date"], dayfirst=True)

dhms = input["Duration [d.h:m:s]"].str.split(":", expand=True)
dh = dhms[0].str.split(".", expand=True)
d = dh[0].astype(int)
h = dh[1].astype(int)
m = dhms[1].astype(int)
s = dhms[2].astype(int)
input[["d", "h", "m", "s"]] = pd.DataFrame({"d": d, "h": h, "m": m, "s": s})

input["calculated_end_date"] = (
    input["Start Date"]
    + pd.to_timedelta(input["d"], unit="D")
    + pd.to_timedelta(input["h"], unit="h") 
    + pd.to_timedelta(input["m"], unit="m")
    + pd.to_timedelta(input["s"], unit="s")
)

print(input["calculated_end_date"] == test["End Time"])