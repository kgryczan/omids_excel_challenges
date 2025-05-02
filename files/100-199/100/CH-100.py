import pandas as pd
import numpy as np

path = "CH-100 Manage Duplicate Values.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, dtype=str)
test  = pd.read_excel(path, usecols="D", skiprows=1, dtype=str)
test.columns = test.columns.str.replace('.1', '')

result = input.copy()
result['row'] = result.groupby('Product ID').cumcount()
result['nrows'] = result.groupby('Product ID')['Product ID'].transform('size')
result['letter'] = np.where(result['nrows'] > 1, result['row'].apply(lambda x: chr(x + 65)), '')
result['Product ID'] = result['Product ID'] + result['letter']
result = result[['Product ID']]

print(result.equals(test))  # True