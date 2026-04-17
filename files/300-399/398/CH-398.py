import pandas as pd

path = "300-399/398/CH-398  Replacement.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="G:J", nrows=8, skiprows=2)

result = input.copy()
result["Product ID"] = result["Product ID"].shift(-1, fill_value=result["Product ID"].iloc[0])

print(result["Product ID"].equals(test["Product ID.1"]))
# Output: True