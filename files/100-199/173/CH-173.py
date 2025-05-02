import pandas as pd

path = "CH-173 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=25)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=25).rename(columns=lambda x: x.split('.')[0])

input['Month'] = input['Date'].dt.month
input['Group'] = input.groupby('Month').cumcount() + 1
input['Group'] = input.apply(lambda x: f"{x['Month']}-{min(x['Group'], len(input[input['Month'] == x['Month']]) - x['Group'] + 1)}", axis=1)

result = input[['Date','Quantity', 'Group']]
print(result.equals(test)) # Test