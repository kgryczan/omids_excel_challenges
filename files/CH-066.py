import pandas as pd

input = pd.read_excel("CH-066 Merged cells.xlsx", skiprows=1, usecols="B:G", header=None, nrows=7)
test = pd.read_excel("CH-066 Merged cells.xlsx", skiprows=1, usecols="I:L", nrows=16)
test.columns = test.columns.str.replace('.1', '')

input = input.transpose()
input[0] = input[0].fillna(method='ffill')
input.columns = input.iloc[0]
input = input[1:]
input = input.rename(columns={'Department': 'Scenario'})
input = input.rename(columns={input.columns[1]: 'Year'})

for i in range(1, len(input.columns)):
    input[input.columns[i]] = pd.to_numeric(input[input.columns[i]], errors='coerce')

input = pd.melt(input, id_vars=['Scenario', 'Year'], var_name='Department', value_name='Value')
input = input.pivot_table(index=['Department', 'Year'], columns='Scenario', values='Value').reset_index()
input = input.sort_values(['Year', 'Department']).reset_index(drop=True)
input["Budget"] = input["Budget"].astype('int64')
input.columns.name = None

test = test.sort_values(['Year', 'Department']).reset_index(drop=True)

print(input.equals(test)) # True