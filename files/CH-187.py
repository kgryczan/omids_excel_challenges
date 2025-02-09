import pandas as pd

path = "CH-187 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=5).astype('int32')

input['Group'] = (input['Date'].diff().dt.days.fillna(0).astype(int) > 1).cumsum() + 1
result = input.groupby('Group', as_index=False)['Sales'].sum().rename(columns={'Sales': 'Total Sales'}).astype({'Total Sales': 'int32'})

print(result.equals(test)) # True