import pandas as pd

path = "200-299/246/CH-246 Table Transformation.xlsx"

input = pd.read_excel(path,  usecols="B:H", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="B:E", skiprows=9, nrows=5)

result = input.loc[:, input.astype(str).apply(lambda col: col.str.contains(r"\*").any())]

print(result.equals(test))
# True