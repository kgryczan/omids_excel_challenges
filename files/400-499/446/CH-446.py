import pandas as pd

path = "400-499/446/CH-446 Number Series.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="E:F", nrows=7, skiprows=2)
test.columns = input.columns

input["Sale"] = (
    pd.to_numeric(input["Sale"], errors="coerce").interpolate().astype("int64")
)
print(input.equals(test))
# True
