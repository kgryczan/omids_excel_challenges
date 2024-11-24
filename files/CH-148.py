import pandas as pd

path = "CH-148 Filter Dates.xlsx"
input = pd.read_excel(path, usecols="C:E", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=9).rename(columns=lambda x: x.split('.')[0])

result = input.groupby('Customer').apply(
    lambda x: x.loc[x['Date'].isin([x['Date'].min(), x['Date'].max(), x['Date'].iloc[len(x) // 2]])]
).reset_index(drop=True)

print(test.equals(test)) # True