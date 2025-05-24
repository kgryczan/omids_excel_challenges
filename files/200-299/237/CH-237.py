import pandas as pd
import re

path = "200-299/237/CH-237 Table Transformation.xlsx"
input = pd.read_excel(path, sheet_name=0, usecols="B:E", skiprows=1, nrows=8)
test = pd.read_excel(path, sheet_name=0, usecols="H:O", skiprows=1, nrows=4).rename(columns=lambda col: col.replace('.1', ''))

input['rn'] = input.groupby(['Doc', 'Status']).cumcount() + 1
result = input.pivot_table(
    index=['Doc', 'Status'],
    columns='rn',
    values=['Code', 'Num'],
    aggfunc='first'
)
result.columns = [f"{col[0]}{col[1]}" for col in result.columns]

def sort_key(col):
    m = re.match(r'(Code|Num)(\d+)', col)
    if m:
        return int(m.group(2)), 0 if m.group(1) == 'Code' else 1
    return (float('inf'), col)

result = result.reindex(sorted(result.columns, key=sort_key), axis=1)
result['Num1'] = result['Num1'].astype(int)
result = result.reset_index()

print(result.equals(test)) # True
