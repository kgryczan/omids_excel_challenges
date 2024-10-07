import pandas as pd

path = "CH-124 Merge.xlsx"

input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=5).sort_values('Date').reset_index(drop=True)
input2 = pd.read_excel(path, usecols="H:H", skiprows=1, nrows=7) \
    .rename(columns=lambda x: x.replace('.1', '')) \
    .sort_values('Date') \
    .reset_index(drop=True)
test = pd.read_excel(path, usecols="H:I", skiprows=1, nrows=7).rename(columns=lambda x: x.replace('.1', ''))

result = pd.merge_asof(input2, input, on='Date', direction='nearest')
result = pd.merge(result, test, on='Date', how='inner')

print(result["Price"].eq(result["price"]).all()) # True
