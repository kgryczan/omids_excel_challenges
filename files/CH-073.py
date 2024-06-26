import pandas as pd
import re

path = "CH-073 Custom Splitter 2.xlsx"
input = pd.read_excel(path, usecols= "B", skiprows=1, nrows = 13)
test  = pd.read_excel(path, usecols= "D:F", skiprows=1)

date_pattern = r"\d{4}/\d{1,2}/\d{1,2}"
product_quant_pattern = r"([A-Z]+\d+)"

input['Date'] = input['Info'].apply(lambda x: re.search(date_pattern, x).group())
input['Info2'] = input['Info'].apply(lambda x: re.sub(date_pattern, '', x))
input['prod_quant'] = input['Info2'].apply(lambda x: re.findall(product_quant_pattern, x))
input = input.explode('prod_quant')
input[['Product', 'Quantity']] = input['prod_quant'].str.extract(r"([A-Z]+)(\d+)")
input['Quantity'] = input['Quantity'].astype("int64")
result = input[['Date', 'Product', 'Quantity']].reset_index(drop=True)

print(result.equals(test)) # True