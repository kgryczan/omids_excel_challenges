import pandas as pd

path = "200-299/265/CH-265 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="F:I", skiprows=1, nrows=6)

input['Region'] = input['Column1'].where(input['Column1'].str.contains('Region'), pd.NA)
input['Region'] = input['Region'].ffill()
input = input[~input['Column1'].duplicated()]
input = input[input['Column1'] != input['Region']]
input.columns = ["Product", "Jan", "Feb", "Region"]
input = input.iloc[1:]
result = input.melt(id_vars=['Region', 'Product'], value_vars=['Jan', 'Feb'],
                       var_name='Month', value_name='Value')
result = result[['Region', 'Product', 'Month', 'Value']]\
    .sort_values(by=['Region', 'Product', 'Month'],ascending=[True, True, False]).reset_index(drop=True)
result['Value'] = pd.to_numeric(result['Value'])

print(result.equals(test))  # True