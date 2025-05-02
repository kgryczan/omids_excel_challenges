import pandas as pd

path = "CH-158 Filter the last transaction in mounth.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=12)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=4).rename(columns=lambda x: x.split('.')[0])

input['Date'] = pd.to_datetime(input['Date'])
input['month'] = input['Date'].dt.month

result = input.loc[input.groupby(['Product ID', 'month'])['Date'].idxmax()].sort_values(by='Date').reset_index(drop=True).drop(columns=['month'])

print(result.equals(test)) # True