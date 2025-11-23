import pandas as pd
import numpy as np

path = "300-399/330/CH-330 Custom Grouping.xlsx"
df = pd.read_excel(path,  usecols="B:D", skiprows=1, nrows=12)
test = pd.read_excel(path, usecols="H:I", skiprows=1, nrows=6)

p = df["Start Date Time"].astype("int64") / (24*60*60*1_000_000_000)
q = df["End Date Time"].astype("int64")   / (24*60*60*1_000_000_000)
b, c = np.floor(p), np.floor(q)
rep = np.where(
    (c - b) > 2, np.nan,
    np.where(
        (c - b) == 2, b + 1,
        np.where((b + 1 - p) > (q % 1), b, c)
    )
)

df["group"] = np.where(
    np.isnan(rep),
    "Uncategorzied",
    pd.to_datetime(rep, unit="D", origin="1970-01-01").strftime("%-m/%-d/%Y")
)

result = (
    df.groupby("group")["Polution"]
      .mean().round()
      .reset_index(name="AVG Polution Rate")
      .sort_values("group")
)

print((result['AVG Polution Rate'] == test['AVG Polution Rate']).all())
# True