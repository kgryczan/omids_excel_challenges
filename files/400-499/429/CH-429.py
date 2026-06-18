import pandas as pd

path = "400-499/429/CH-429 Filter.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=6, skiprows=2)
test = pd.read_excel(path, usecols="H:J", nrows=4, skiprows=2).rename(
    columns=lambda c: c[:-2] if isinstance(c, str) and c.endswith(".1") else c
)

result = (
    input.groupby("Customer")
    .apply(lambda x: x.nlargest(2, "Sales"))
    .reset_index(drop=True)
)

print(result.equals(test))
# True
