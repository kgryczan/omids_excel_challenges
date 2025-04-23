import pandas as pd
from datetime import timedelta, time

path = "CH-223 Custom Grouping.xlsx"

input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="H:I", skiprows=1, nrows=7).rename(columns=lambda col: col.replace('.1', ''))
input['Date'] = input['Date'].dt.day + (input['Time'] > time(12, 0)).astype(int)
result = input.groupby(input['Date']).Sales.sum().reset_index(name='Sales').assign(Day=lambda df: range(1, len(df) + 1))
result = result[['Day', 'Sales']]
print(result.equals(test)) # True

