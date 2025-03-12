import pandas as pd
import numpy as np

path = "CH-202 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=9)

input['Date'] = input['Column 1'].where(pd.to_datetime(input['Column 1'], errors='coerce').notna())
input['Date'] = input['Date'].apply(lambda x: np.nan if pd.to_datetime(x, errors='coerce') and len(str(x)) == 1 else x)
input['Date'] = input['Date'].ffill()
input = input[input['Date'] != input['Column 1']]
input['Type'] = input['Column 1'].apply(lambda x: 'Quantity' if str(x).isdigit() else 'Product')
input['change'] = np.where((input['Type'].shift() == "Product") & (input['Type'] == "Quantity"), 0, 1)
input['row'] = input.groupby('Date')['change'].cumsum()
result = input.pivot(index=['Date', 'row'], columns='Type', values='Column 1').reset_index()
result['Quantity'] = result['Quantity'].astype('float64')
result.columns.name = None
result = result.drop(columns=['row'])
print(result.equals(test)) # True