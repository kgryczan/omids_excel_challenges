import pandas as pd

path = "CH-143 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=25)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=4)

input['Group'] = (input['Date'] - pd.to_timedelta((input['Date'].dt.weekday - 4) % 7, unit='d')).diff().dt.days.ne(0).cumsum().astype("int64")
result = input.groupby('Group')['Sales'].sum().reset_index(name='Total Sales')

print(result.equals(test)) # True