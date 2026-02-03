import pandas as pd

path = "300-399/362/CH-362 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="H:I", skiprows=2, nrows=3)

input['Customer ID'] = input['Customer ID'].where(input['Customer ID'].duplicated(keep=False), 'Other')
total_sales = input.groupby('Customer ID', as_index=False)['Total Sales'].sum()
total_sales.columns = ['IDs', 'Sales']

print(total_sales.equals(test))
# True