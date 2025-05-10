import pandas as pd

path = "200-299/232/CH-232 Table Transformation.xlsx"
input_df = pd.read_excel(path, usecols="B", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=4).sort_values("Price").reset_index(drop=True)

df = input_df.copy()
df['col'] = df.index % 2
df['row'] = df.index // 2 + 1
wide = df.pivot(index='row', columns='col', values='Column 1').reset_index(drop=True)
wide.columns = wide.columns.astype(str)

wide[['Product', 'Measure']] = wide['0'].str.split(n=1, expand=True)
result = wide.drop(columns=['0']).pivot(index='Product', columns='Measure', values='1').reset_index()
result = result.rename_axis(None, axis=1)
result = result[['Code', 'Product', 'Price']]
result['Price'] = pd.to_numeric(result['Price'])
result['Code'] = pd.to_numeric(result['Code'])
result = result.sort_values('Price').reset_index(drop=True)

print(result.equals(test)) # True