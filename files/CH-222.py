import pandas as pd

path = "CH-222 Table Transformation.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=16)
test_data = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=5)

input_data['Type'] = input_data.iloc[:, 0].apply(lambda v: "Product" if isinstance(v, str) and v.isalpha() else "Quantity" if isinstance(v, (int, float)) else "Date")
input_data['RowNumber'] = input_data.groupby('Type').cumcount() + 1

pivoted_data = input_data.pivot(index='RowNumber', columns='Type', values=input_data.columns[0]).reset_index(drop=True)
pivoted_data['Date'] = pd.to_datetime(pivoted_data['Date'], errors='coerce')
pivoted_data['Quantity'] = pivoted_data['Quantity'].astype('int64', errors='ignore')
pivoted_data.columns.name = None

print(pivoted_data.equals(test_data))