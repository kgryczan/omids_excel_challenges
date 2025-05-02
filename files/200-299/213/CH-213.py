import pandas as pd

path = "CH-213 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=3)

input['Group'] = pd.cut(input['Temperature'], bins=[-float('inf'), 10, 24, float('inf')], labels=['Cold', 'Mild', 'Hot'])
input['Group'] = input['Group'].astype(str)
result = input['Group'].value_counts().sort_values(ascending=True).reset_index().rename(columns={'count': 'No days'})

print(result.equals(test)) # True