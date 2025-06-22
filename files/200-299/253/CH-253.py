import pandas as pd

path = "200-299/253/CH-253 Custom Grouping.xlsx"

input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=25)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=4)

result = input.sort_values(by="Date").reset_index(drop=True)
result['Group'] = (result['Date'].diff().dt.days > 1).cumsum() + 1
result = result.groupby('Group', as_index=False).agg({'Sales': 'sum'})
result = result.rename(columns={'Sales': 'Total Sales'})

print(result.equals(test))