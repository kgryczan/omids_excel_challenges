import pandas as pd

path = "200-299/242/CH-242 Table Transformation.xlsx"
input_df = pd.read_excel(path, usecols="B", skiprows=1, nrows=13)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=5).sort_values("Product").reset_index(drop=True)

df = pd.DataFrame({
    'Product': input_df.iloc[::2, 0].reset_index(drop=True),
    'Price': input_df.iloc[1::2, 0].reset_index(drop=True)
})
df[['Product', 'unit']] = df['Product'].str.rsplit(' ', n=1, expand=True)
df = df.assign(Product=df['Product'].str.split(', ')).explode('Product')
df[['Product', 'unit']] = df[['Product', 'unit']].apply(lambda x: x.str.strip())
df['Price'] = df['Price'].astype(int)
result = df.sort_values('Product').pivot(index='Product', columns='unit', values='Price').reset_index()
result.columns.name = None
result = result[['Code', 'Product', 'Price']]

print(result.equals(test))
# True