import pandas as pd

path = "CH-163 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=38)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=15)

input['Season'] = pd.to_datetime(input['Year'].astype(str) + " " + input['Month'], format='%Y %b').dt.quarter

result = input.groupby(['Year', 'Season'])['Sale'].sum().reset_index()
result.columns = test.columns = ['Year', 'Season', 'Total Sale']

print(all(result ==test)) # True