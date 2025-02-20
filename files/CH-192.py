import pandas as pd
import numpy as np

path = "CH-192 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=11)
test = pd.read_excel(path, usecols="B:D", skiprows=14, nrows=4)

input['sign'] = np.sign(input['Quantity'])
input['group'] = input.groupby('Product')['sign'].apply(lambda x: (x != x.shift()).cumsum()).reset_index(level=0, drop=True)
input['group'] = np.ceil(input['group']/2)
result = input.groupby(['Product', 'group']).agg({'Quantity': 'sum', 'Date': 'min'}).reset_index()
result = result[result['Quantity'] != 0][['Date', 'Product', 'Quantity']].sort_values(by = "Date").reset_index(drop= True)

print(result.equals(test)) # True