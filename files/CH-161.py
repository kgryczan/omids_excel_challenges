import pandas as pd

path = "CH-161 Custom Index Column.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="E:H", skiprows=1, nrows=4)

result = input.assign(rn=input.groupby('Product').cumcount() + 1) \
               .pivot(index='rn', columns='Product', values='Date') \
               .reset_index(drop=True).rename_axis(None, axis=1)

print(result.equals(test)) # True