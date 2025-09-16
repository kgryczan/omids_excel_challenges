import pandas as pd
import numpy as np

path = "200-299/296/CH-296 Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="I:K", skiprows=1, nrows=25).sort_values(['Date', 'Product']).reset_index(drop=True)

df = input.melt(value_name='Value')['Value']
df = pd.DataFrame(df)
df['Date'] = df['Value'].where(df['Value'].astype(str).str.startswith('2024')).ffill()
df['Product'] = df['Value'].where(df['Value'].isin(['A', 'B', 'C'])).ffill()
df = df[~df['Value'].isin(df['Date'].dropna().unique()) & ~df['Value'].isin(['A', 'B', 'C'])]
df = df.sort_values(['Date', 'Product']).reset_index(drop=True)
df['Result'] = df['Value'].astype(np.int64)
result = df[['Date', 'Product', 'Result']]

print(result.equals(test)) # True