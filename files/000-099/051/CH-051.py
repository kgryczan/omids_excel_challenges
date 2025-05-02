import pandas as pd

input = pd.read_excel("CH-051 Purchasing together.xlsx", sheet_name="Sheet1", usecols="B:F", skiprows=1)
test = pd.read_excel("CH-051 Purchasing together.xlsx", sheet_name="Sheet1", usecols="J:K", skiprows=1, nrows = 5)
test = test.sort_values(by = "Products").reset_index(drop = True)

result = input[['Invoice ID', 'Product', 'Quantity']].pivot_table(index='Invoice ID', columns='Product', values='Quantity', fill_value=0)
result['A,B'] = (result['A'] > 0) & (result['B'] > 0)
result['A,C'] = (result['A'] > 0) & (result['C'] > 0)
result['C,D'] = (result['C'] > 0) & (result['D'] > 0)
result['A,B,C'] = (result['A'] > 0) & (result['B'] > 0) & (result['C'] > 0)
result['A,B,C,D'] = (result['A'] > 0) & (result['B'] > 0) & (result['C'] > 0) & (result['D'] > 0)
result = result[['A,B', 'A,C', 'C,D', 'A,B,C', 'A,B,C,D']].reset_index() 
result.columns.name = None
result = result.melt(id_vars='Invoice ID', var_name='Products', value_name='Purchased Together')
result = result[result['Purchased Together'] == True]
result = result.groupby('Products').size().reset_index(name='Count')

print(test.equals(result)) # True