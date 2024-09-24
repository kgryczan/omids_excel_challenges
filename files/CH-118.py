import pandas as pd

path = "CH-118 DSO.xlsx"
input1 = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=23)
input2 = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=3)
input2.columns = input2.columns.str.replace('.1', '')
test = pd.read_excel(path, usecols="H:H", skiprows=1, nrows=3)

input1 = input1.sort_values(by=['Customer', 'Date'], ascending=[True, False])

r2 = input2.merge(input1, on='Customer', how='left')
r2['days'] = pd.to_datetime('2024-08-31') - pd.to_datetime(r2['Date'])
r2['cumsum'] = r2.groupby('Customer')['Sales'].cumsum()
r2['balance_cover'] = r2.apply(lambda row: row['Sales'] if row['cumsum'] <= row['Balance'] else row['Balance'] - (row['cumsum'] - row['Sales']), axis=1)
r2 = r2[r2['balance_cover'] > 0]
r2['weighted_days'] = r2['days'].dt.days * r2['balance_cover']
result = r2.groupby('Customer').apply(lambda x: x['weighted_days'].sum() / x['balance_cover'].sum()).reset_index(name='weighted_days')

print(result["weighted_days"].equals(test["DSO (day)"])) # True