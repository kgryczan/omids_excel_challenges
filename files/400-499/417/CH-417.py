import pandas as pd

path = "400-499/417/CH-417 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=10, skiprows=2)
test = pd.read_excel(path, usecols="G:H", nrows=6, skiprows=2)

result = input.copy()
result["srow"] = result[["FROM", "TO"]].apply(lambda r: f"{min(r['FROM'], r['TO'])}-{max(r['FROM'], r['TO'])}", axis=1)
result["group"] = (result["srow"] != result["srow"].shift()).cumsum()
result["row"] = result.groupby("group")["FROM"].transform("first").astype(str) + "-" + result.groupby("group")["TO"].transform("first").astype(str)
result = result.groupby(["row", "group"], sort=False).agg(**{"TOTAL QUANTITY": ("QUANTITY", "sum")}).reset_index()
result = result.drop(columns=["group"])

print(result.equals(test))
# incorrect results in test

