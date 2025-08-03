import pandas as pd

path = "200-299/274/CH-274 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=16).rename(columns=lambda col: col.replace('.1', ''))

input['Group'] = input['Date'].diff().dt.days.gt(2).cumsum() + 1

print(input.equals(test)) # True