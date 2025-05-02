import pandas as pd
import numpy as np

path = "CH-181 Table Transformation.xlsx"

input = pd.read_excel(path, usecols="C", skiprows=1, nrows=40, dtype=str)

test = pd.read_excel(path, usecols="E:H", skiprows=1, nrows=7).rename(columns=lambda x: x.split('.')[0])
test['From'] = pd.to_datetime(test['From'], errors='coerce').dt.date
test['To'] = pd.to_datetime(test['To'], errors='coerce').dt.date

input['row'] = input['Name'].str.match(r'^[A-Z]{3}$').cumsum()
input['row'] = input['row'].ffill()

grouped = input.groupby('row')
input['Name1'] = grouped['Name'].transform(lambda x: x[x.str.match(r'^[A-Z]{3}$')].iloc[0])
input['prop'] = np.where(input['Name'].isin(['From', 'To', 'Status']), input['Name'], np.nan)
input['prop'] = input['prop'].ffill()

filtered = input.groupby('row').apply(lambda x: x[~((x['Name'] == x['prop']) & x['prop'].notna())]).reset_index(drop=True)
filtered['prop'] = np.where(filtered['Name'] == filtered['Name1'], 'Name', filtered['prop'])

result = filtered.pivot(index='row', columns='prop', values='Name').reset_index(drop=True)
result['From'] = pd.to_datetime(result['From'], errors='coerce').dt.date
result['To'] = pd.to_datetime(result['To'], errors='coerce').dt.date

result = result[['Name', 'From', 'To', 'Status']]
result = result.rename_axis(None, axis=1)

print(result.equals(test)) # True