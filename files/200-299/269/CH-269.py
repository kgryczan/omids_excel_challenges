import pandas as pd

path = "200-299/269/CH-269 Text Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=8)

input["ID 1"] = ["-".join(c for c in name if c != "-") for name in input["ID"]]

print(input["ID 1"].equals(test["ID 1"])) # True