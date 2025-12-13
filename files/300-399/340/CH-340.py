import pandas as pd
import numpy as np

path = "300-399/340/CH-340 Table Transformation.xlsx"
input = pd.read_excel(path, sheet_name=0, usecols="B:G", skiprows=2, nrows=8)
test = pd.read_excel(path, sheet_name=0, usecols="K:N", skiprows=2, nrows=5)
test.columns = [col.replace('.1', '') for col in test.columns]

arr = input.values

def remove_l(arr):
    result = []
    for row in arr:
        filtered = [cell for cell in row if cell != 'L']
        result.append(filtered + [''] * (arr.shape[1] - len(filtered)))
    return np.array(result)

def remove_u(arr):
    result = []
    for col in arr.T:
        filtered = [cell for cell in col if cell != 'U']
        result.append(list(filtered) + [''] * (arr.shape[0] - len(filtered)))
    return np.array(result).T

arr = remove_l(arr)
arr = remove_u(arr)

result = pd.DataFrame(arr)
result = result.replace('', np.nan).dropna(axis=1, how='all').dropna()
result.columns = ['Date', 'Product', 'Customer', 'Quantity']
result['Quantity'] = result['Quantity'].astype('int64')

print(result.equals(test)) # True