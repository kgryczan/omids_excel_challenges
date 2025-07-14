import pandas as pd

path = "200-299/263/CH-263 UnGrouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=3)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=16)

input[['From', 'To']] = input['Group'].str.split('-', expand=True)
result = (
    input
    .explode('Date', ignore_index=True)
    if 'Date' in input.columns else
    input.assign(Date=input.apply(lambda r: pd.date_range(r['From'], r['To']), axis=1)).explode('Date')
)
result['Sales'] = input.loc[result.index, 'Total Sales'].values / result.groupby('From')['Date'].transform('nunique')
result = result[['Date', 'Sales']].reset_index(drop=True)
print(result.equals(test))