import pandas as pd

input = pd.read_excel("CH-034 Customer Return Cycle.xlsx", sheet_name="Sheet1", usecols="B:F", skiprows=1)
test = pd.read_excel("CH-034 Customer Return Cycle.xlsx", sheet_name="Sheet1", usecols="J:K", skiprows=1, nrows = 4)

result = input[['Date', 'Customer ID']].sort_values(by=['Customer ID', 'Date']).drop_duplicates().reset_index(drop=True)
result['lag'] = result.groupby('Customer ID')['Date'].shift(1)
result['diff'] = (result['Date'] - result['lag']).dt.days
result = result.groupby('Customer ID')['diff'].mean().astype(int).reset_index()
result.columns = ['Customer', 'Avg Return Cycle']

print(result == test)   # True