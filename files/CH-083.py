import pandas as pd

path = "CH-083 Custom splitter 3.xlsx"
input = pd.read_excel(path, usecols="B", nrows = 1, skiprows = 1)
test = pd.read_excel(path, usecols="D:F", skiprows = 4)

result = input['Info'].str.split(';', expand=True).stack().str.split(", ", expand=True)\
    .rename(columns={0: 'Date', 1: 'Product', 2: "Quantity"}).reset_index(drop=True)
result['Quantity'] = result['Quantity'].astype('int64')

print(result.equals(test)) # True