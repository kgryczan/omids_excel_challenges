import pandas as pd
import re

input = pd.read_excel("CH-064 Text Cleaning.xlsx", usecols="B", skiprows=1, nrows = 7)
test = pd.read_excel("CH-064 Text Cleaning.xlsx", usecols="D:F", skiprows = 1, nrows = 12)
test['Date'] = test['Date'].astype(str)

result = input.copy()
result[['Date', 'Product']] = result['Description'].str.split(", ", n=1, expand=True)
result['Product'] = result['Product'].str.split(", ")
result = result.explode('Product')
result[['Product', 'Quantity']] = result['Product'].str.split(" ", n=1, expand=True)
result['Quantity'] = pd.to_numeric(result['Quantity'])
result['Date'] = result['Date'].str.replace("/", "-")
result['Quantity'].fillna(1, inplace=True)
result['Quantity'] = result['Quantity'].astype('int64')
result.drop('Description', axis=1, inplace=True)a
result = result.reset_index(drop=True)

print(test.equals(result)) # True
