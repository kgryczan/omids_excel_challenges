import pandas as pd
import numpy as np
import re

path = "CH-177 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C", skiprows=1, nrows=22,  names=["Column 1"])
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=10)

input['col'] = input['Column 1'].apply(lambda x: 3 if re.match(r'^\d+$', str(x)) else (2 if re.match(r'^[A-Za-z]', str(x)) else 1))
input['Date'] = np.where(input['col'] == 1, input['Column 1'], np.nan)
input['Date'] = input['Date'].ffill()
input['Quantity'] = np.where(input['col'] == 3, input['Column 1'], np.nan)
input['Quantity'] = input['Quantity'].bfill()

result = input[input['col'] == 2][['Date', 'Column 1', 'Quantity']].reset_index(drop=True)
result.columns = ['Date', 'Product', 'Quantity']

print(result.equals(test)) #True