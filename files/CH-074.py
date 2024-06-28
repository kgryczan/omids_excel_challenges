import pandas as pd

# Read the Excel file
path = 'CH-074 Determining missing fields.xlsx'
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=14)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=4)

input['cumsum'] = (input['Info'] == "Name").cumsum()
result = (input.groupby(['cumsum', 'Info'])
          .size()
          .unstack(fill_value=0)
          .reset_index()
          .melt(id_vars=['cumsum'], var_name='Info', value_name='n')
          .groupby(['cumsum', 'n'])['Info']
          .apply(list)
          .unstack(fill_value=[])
          .reset_index())
result['Missing fields'] = result[0].apply(lambda x: "-" if not x else ", ".join(x))
result['Duplicate Fields'] = result[2].apply(lambda x: "-" if not x else ", ".join(x))
result = result[['cumsum', 'Missing fields', 'Duplicate Fields']]
result.columns = ['Record No', 'Missing fields', 'Duplicate Fields']

print(result)
print(test)

# One field differs, because there is empty cell where hyphen should be in H3