import pandas as pd

path = "CH-144 First transaction in each month.xlsx"
input = pd.read_excel(path, usecols="C:E", skiprows=1, nrows=26)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=4).rename(columns=lambda x: x.split('.')[0])

result = input.assign(month=input['Date'].dt.month).groupby('month').head(1).drop(columns='month').reset_index(drop=True)

print(result.equals(test))  # True
