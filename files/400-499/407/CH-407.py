import pandas as pd

path = "400-499/407/CH-407 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=10, skiprows=2)
test = pd.read_excel(path, usecols="G:H", nrows=3, skiprows=2)

result = input.assign(ROW=input.apply(lambda x: f"{min(x['FROM'], x['TO'])}-{max(x['FROM'], x['TO'])}", axis=1)) \
    .groupby('ROW', as_index=False)['QUANTITY'].sum().rename(columns={'QUANTITY': 'TOTA; QUANTITY'})

print(result.equals(test))
# True