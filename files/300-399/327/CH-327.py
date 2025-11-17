import pandas as pd
import re

path = "300-399/327/CH-327 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows = 8, skiprows = 1)
test = pd.read_excel(path, usecols= "D:E", nrows = 8, skiprows = 1)

level_pattern = "|".join(map(re.escape, (levels := ["Upper Ground", "Ground", "Under Ground"])))
zone_pattern = "|".join(map(re.escape, (levels :=  ["West", "East", "North", "South", "South East", "North West"])))

df = input.copy()
df["Level"] = df["Info"].apply(lambda info: re.findall(level_pattern, str(info)))
df["Zone"] = df["Info"].apply(
    lambda info: (
        " ".join(zones) if len((zones := re.findall(zone_pattern, str(info)))) > 1
        else zones[0] if zones
        else None
    )
)
df = df.explode("Level")
df = df.drop(columns=["Info"])

print(df.equals(test)) # True