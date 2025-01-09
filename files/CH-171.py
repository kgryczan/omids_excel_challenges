import pandas as pd

path = "CH-171 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C", skiprows=1, nrows=148, names=["Name"])
test = pd.read_excel(path, usecols="E:H", skiprows=1, nrows=6).rename(columns=lambda x: x.split('.')[0])
test[['From', 'To']] = test[['From', 'To']].replace("availabe", "available", regex=True)
test = test.sort_values(by='Name').reset_index(drop=True)

even_rows, odd_rows = input.iloc[::2].reset_index(drop=True), input.iloc[1::2].reset_index(drop=True)
result = pd.DataFrame({'Name': even_rows['Name'], 'Value': odd_rows['Name']})
result = result[(result['Name'].isin(['From', 'To', 'Status'])) | (result['Value'] == "Process")]
result['group'] = result.apply(lambda row: row['Name'] if row['Value'] == "Process" else None, axis=1).ffill()
result = result[result['Name'] != result['group']]

pivot_result = result.pivot(index='group', columns='Name', values='Value').reset_index().rename(columns={'group': 'Name'})
pivot_result = pivot_result[['Name', 'From', 'To', 'Status']]

print(pivot_result.equals(test)) # True