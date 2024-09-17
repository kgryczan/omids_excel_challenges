import pandas as pd

path = "CH-114 Merge.xlsx"

input1 = pd.read_excel(path, usecols = "B:C", nrows = 7, skiprows = 1)
input2 = pd.read_excel(path, usecols = "B:C", nrows = 5, skiprows = 12)
test = pd.read_excel(path, usecols="H:J", nrows=7, skiprows=1).rename(columns=lambda x: x.replace('.1', ''))
test["price"] = test["price"].astype(str)

input1['Product ID'] = input1['Product ID'].str.split(',')
input1 = input1.explode('Product ID')
r1 = input1.merge(input2, left_on='Product ID', right_on='product id') \
           .groupby('Date').agg({'price': lambda x: x.iloc[0].astype(str)}).reset_index()
r2 = input1.merge(r1, on='Date', how='left').fillna({'price': '-'}).groupby('Date').agg({'Product ID': ','.join, 'price': 'first'}).reset_index()

print(r2.equals(test)) # True
