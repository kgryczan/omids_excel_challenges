import pandas as pd

path = "CH-113 Manage Duplicate Values.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, names=["Product ID"])
test = pd.read_excel(path, usecols="D", skiprows=1, names=["result"])

input['rn'] = input.index + 1
input = input.sort_values('Product ID').reset_index()
input['dup'] = input.groupby('Product ID')['Product ID'].transform('size') > 1
input['a'] = input.groupby('Product ID')['rn'].diff().gt(1).cumsum()
input['a'] = input.groupby('Product ID')['a'].transform(lambda x: x - x.min() + 1)
input['b'] = input.groupby(['Product ID', 'a']).cumcount() + 1
input = input.sort_values('rn').reset_index()
input['result'] = input.apply(lambda row: f"{row['Product ID']}-{row['a']}-{row['b']}" if row['dup'] else row['Product ID'], axis=1)
print(input['result'].equals(test["result"])) # True
