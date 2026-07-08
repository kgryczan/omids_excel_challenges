import pandas as pd

path = "400-499/439/CH-439 Filter.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=6, skiprows=2)
test = pd.read_excel(path, usecols="H:J", nrows=2, skiprows=2)

result = input.copy()
result = result.loc[lambda x: x["Sales"] > x["Sales"].shift()].reset_index(drop=True)
test.columns = result.columns

print(result.equals(test))
# True
