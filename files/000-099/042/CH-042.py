import pandas as pd
import re

input = pd.read_excel('CH-042 Revisit after surgury.xlsx', usecols="B:E", skiprows=1, nrows = 27)
test = pd.read_excel('CH-042 Revisit after surgury.xlsx', usecols="I:K", skiprows=1, nrows = 2)

result = input.groupby(['Patient-ID', 'Gander\t']).apply(lambda x: ' -> '.join(x['Referral'])).reset_index(name='seq')
result = result[result['seq'].str.contains('Surgery ->')]
result = result.groupby('Gander\t').agg({'seq': 'count', 'Patient-ID': lambda x: ', '.join(sorted(x))})\
    .rename(columns={'seq': 'No of re-visit after surgery', 'Patient-ID': 'Patient ID'}).reset_index()
result = result.rename(columns={'Gander\t': 'Gender'}).sort_values(by= 'Gender', ascending=False).reset_index(drop=True)

print(result.equals(test)) # True