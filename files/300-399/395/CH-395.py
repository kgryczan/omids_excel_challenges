import pandas as pd

path = "300-399/395/CH-395  Replacement.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="G:J", nrows=8, skiprows=2)

input["Total Sales"] *= (1 - 0.1 * (input["Customer ID"] == "C-12"))

print((input["Total Sales"] == test["Total Sales.1"].astype('int64')).all())
# True