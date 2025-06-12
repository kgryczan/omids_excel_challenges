import pandas as pd

path = "200-299/248/CH-248 Time Difference.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=13)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=3).rename(columns=lambda col: col.replace('.1', ''))
input = input.sort_values(['User ID', 'Time'])
input = input.loc[(input['User ID'].shift() != input['User ID']) | (input['Action'].shift() != input['Action'])]

input['run'] = (input['Action'] == 'Login').cumsum()
pivot = input.pivot_table(index=['User ID', 'run'], columns='Action', values='Time', aggfunc='first').reset_index()

pivot['Duration'] = (pd.to_datetime(pivot['Logout']) - pd.to_datetime(pivot['Login'])).dt.total_seconds() / 3600
result = pivot.groupby('User ID', as_index=False)['Duration'].sum()
result['Time (Hour)'] = result['Duration'].fillna(0).astype(int)
result = result[['User ID', 'Time (Hour)']]

# To achieve expected result, rows 13 and 14 need to be switched.
print(result)
print(test)