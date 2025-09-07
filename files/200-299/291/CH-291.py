import pandas as pd

path = "200-299/291/CH-291 Randomly Reorder Columns.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=8)
result = input.sample(frac=1, axis=1)
print(result)