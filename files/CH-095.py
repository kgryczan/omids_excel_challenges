import pandas as pd

path = "CH-095 Last Inventory.xlsx"
input = pd.read_excel(path, usecols = "B:G", skiprows = 1)
test  = pd.read_excel(path, usecols = "i:j", skiprows = 1)
test.columns = test.columns.str.replace(".1", "")

result = input.copy()
result['Last Inventory'] = input.iloc[:, 1:]\
    .apply(lambda x: x[x.last_valid_index()], axis = 1)\
    .astype("int64")
result = result[['Product', 'Last Inventory']]

print(result.equals(test)) # True