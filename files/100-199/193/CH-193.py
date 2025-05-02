import pandas as pd

path = "CH-193 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=36)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=2)

result = input.assign(Group=input['Date'].dt.weekday >= 5).groupby('Group')['Sales'].sum().reset_index().rename(columns={'Group': 'Weekend', 'Sales': 'Total Sales'})

print(result.equals(test))