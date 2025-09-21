import pandas as pd

path = "200-299/299/CH-299 Advanced Filtering.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=6).rename(columns=lambda col: col.replace('.1', ''))

result = input[input['Sales'] > input['Sales'].shift(1)].reset_index(drop=True)

print(test.equals(result)) # True