import pandas as pd

path = "CH-126 Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=19).rename(columns=lambda x: x.replace('.1', ''))
test['Dates'] = pd.to_datetime(test['Dates'])

result = input\
          .assign(Dates=input['Dates'].str.split(', '))\
          .explode('Dates')\
          .assign(Dates=lambda df: pd.to_datetime(df['Dates']))\
          .assign(rownumber=lambda df: df.groupby('Order IDS').cumcount() + 1)\
          .assign(Group=lambda df: df['rownumber'].map({1: 'Registeration', 2: 'Evaluation', 3: 'Approved'}))\
          .drop(columns='rownumber')\
          .sort_values(by = ['Order IDS', 'Dates'])\
          .reset_index(drop=True)
result = result[['Order IDS', 'Group', 'Dates']]

print(result.equals(test)) # True