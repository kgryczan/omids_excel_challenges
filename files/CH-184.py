import pandas as pd

path = "CH-184 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C", skiprows=1, nrows=15, dtype=str)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=10, dtype=str)

input['Date'] = input['Column 1'].where(~input['Column 1'].str.contains(','), None).ffill()
input = input[input['Date'] != input['Column 1']]
input[['Product', 'Quantity']] = input['Column 1'].str.split(', ', expand=True)
input = input[['Date', 'Product', 'Quantity']].reset_index(drop=True)

print(input.equals(test)) # True