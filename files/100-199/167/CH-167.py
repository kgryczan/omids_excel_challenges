import pandas as pd
import numpy as np
import re

path = "CH-167 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C", skiprows=1, nrows=25)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=10)

def classify_type(value):
    str_val = str(value)
    if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', str_val):
        return 'date'
    if re.match(r'^[A-Za-z]+$', str_val):
        return 'letter'
    if re.match(r'^\d+$', str_val):
        return 'digit'
    return 'unknown'

input['type'] = input.iloc[:, 0].apply(classify_type)
input['group'] = (input['type'] == 'date').cumsum()

result = input.groupby(['group', 'type'])[input.columns[0]].apply(list).unstack().reset_index()
result = result.explode(['letter', 'digit']).reset_index(drop=True)
result.columns.name = None

result = result[['date', 'letter', 'digit']]
result.columns = ['Date', 'Product', 'Quantity']

result['Date'] = pd.to_datetime(result['Date'].apply(lambda x: x[0] if isinstance(x, list) else x), errors='coerce')
result['Quantity'] = pd.to_numeric(result['Quantity'], errors='coerce').astype('int64')

print(result.equals(test)) # True
