import pandas as pd

path = "CH-166 Time Zone.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="I:I", skiprows=1, nrows=10)

input[['Day', 'Month', 'Year', 'Hour', 'Minute']] = input['Date Time'].str.extract(r'(\d+)/(\d+)/(\d+) (\d+):(\d+)').astype(int)
input['Day'] += (input['Hour'] >= 24).astype(int)
input['Hour'] %= 24
input['Date Time'] = pd.to_datetime(input[['Year', 'Month', 'Day', 'Hour', 'Minute']])
input['GMT From'] = input['GMT From'].str.replace('GMT', '').astype(int)
input['GMT To'] = input['GMT To'].str.replace('GMT', '').astype(int)
input['New Date Time'] = input['Date Time'] + pd.to_timedelta(input['GMT To'] - input['GMT From'], unit='h')
input['New Date Time'] = input['New Date Time'].dt.strftime('%d/%m/%Y %H:%M')
result = input[['New Date Time']]

print(result == test) # False, Discrepancy on one row. Index 4.