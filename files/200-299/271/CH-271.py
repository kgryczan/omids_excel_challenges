import pandas as pd

path = "200-299/271/CH-271 Randomly Reorder rows.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=7)

result = input.sample(frac=1)
print(result)