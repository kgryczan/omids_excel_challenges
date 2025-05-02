import pandas as pd

path = "CH-123 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=24)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=3)

result = input.assign(Group=input.index // 10 + 1).drop(columns=["Date"]).groupby("Group").sum().rename(columns={"Sales": "Total Sales"}).reset_index()

print(result.equals(test))  # True