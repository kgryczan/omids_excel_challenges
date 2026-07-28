import pandas as pd

path = "400-499/449/CH-449 Filter.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=7).sort_values(
    ["Product", "Date"]
)
test = pd.read_excel(path, usecols="H:J", skiprows=2, nrows=2)
test.columns = input.columns

input["m"] = input.groupby("Product").Sales.transform(lambda s: s.rolling(3).mean())
print(input.query("Sales > m")[test.columns].reset_index(drop=True).equals(test))
# True
