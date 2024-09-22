import pandas as pd

path = "CH-117 Add Index Column.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1)
test = pd.read_excel(path, usecols="E:G", skiprows=1).rename(columns=lambda x: x.replace(".1", ""))

result = input.assign(index = input.groupby("Stock").cumcount() + 1)
print(result.equals(test))  # True