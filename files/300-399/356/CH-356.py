import pandas as pd
path = "300-399/356/CH-356 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=15)
test = pd.read_excel(path, usecols="D:F", skiprows=2, nrows=5)

input['Type'] = input['Name'].apply(lambda x: type(x).__name__)
input = input.sort_values('Type').reset_index(drop=True)
input['GroupIndex'] = input.groupby('Type').cumcount() + 1
input['Name'] = input.apply(lambda row: pd.Timestamp(row['Name']) if type(row['Name']).__name__ == 'datetime' else row['Name'], axis=1)
pivoted = input.pivot(index='GroupIndex', columns='Type', values='Name')
pivoted['int'] = pivoted['int'].astype('int64')
column_map = {'datetime': 'Date', 'str': 'Product', 'int': 'Sale'}
pivoted = pivoted.rename(columns=column_map)
desired_order = ['Date', 'Product', 'Sale']
pivoted = pivoted[[col for col in desired_order if col in pivoted.columns]].reset_index(drop=True)
pivoted.columns.name = None

print(all(pivoted == test))
# True