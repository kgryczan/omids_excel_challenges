import pandas as pd

path = "CH-147 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C", skiprows=1, nrows=25, dtype=str)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=10, parse_dates=['Date'])

input['Date'] = pd.to_datetime(input['Column 1'], errors='coerce').ffill()

input['Group_Index'] = input.groupby('Date').cumcount()
input = input[input['Group_Index'] != 0].reset_index()

input['clmn'] = ['Product', 'Quantity'] * (len(input) // 2) + ['Product'] * (len(input) % 2)
input['group'] = (input['clmn'] == 'Product').cumsum()

result = input.pivot_table(index=['Date', 'group'], columns='clmn', values='Column 1', aggfunc='first').reset_index()
result = result.drop(columns=['group'])
result.columns.name = None
result['Quantity'] = result['Quantity'].astype('int64')

print(result.equals(test)) # True