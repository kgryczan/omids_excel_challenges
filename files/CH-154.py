import pandas as pd

path = "CH-154 Custom Index Column.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=11)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=11)

input['Date'] = pd.to_datetime(input['Date'])
input['index'] = (input['Date'].diff() != pd.Timedelta(days=1)).cumsum().astype('int64')

print(all(input['index'] == test['index'])) # True