import pandas as pd

path = "300-399/373/CH-373 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=2, nrows=9)
test = pd.read_excel(path, usecols="H:I", skiprows=2, nrows=5).rename(columns=lambda col: col.replace(".1", ""))

lower = 600
upper = 1200

input['s'] = input['Total Sales']
input['small'] = input['s'] < lower
input['start'] = ~input['small'].shift(fill_value=False)
input['grp'] = (~(input['Total Sales'] < lower).shift(fill_value=False)).cumsum()
result = input.groupby('grp', as_index=False)['Total Sales'].sum()
result['IDs'] = [f"Group {i}" for i in range(1, len(result) + 1)]
result = result[['IDs', 'Total Sales']]

print(result.equals(test))