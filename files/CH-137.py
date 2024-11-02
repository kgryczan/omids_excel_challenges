import pandas as pd

path = "CH-137 Table Transformation.xlsx"

input = pd.read_excel(path, usecols="C:D", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=10, parse_dates=['Date'], dtype={'Quantity': 'float64'})

input['Date'] = input.apply(lambda row: row['Column 1'] if pd.isna(row['Column 2']) else None, axis=1)
input['Date'] = input['Date'].ffill()
input = input.dropna()

result = input[['Date', 'Column 1', 'Column 2']].rename(columns={'Column 1': 'Product', 'Column 2': 'Quantity'}).reset_index(drop=True)

print(test.equals(result)) # True
