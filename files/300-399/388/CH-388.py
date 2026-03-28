import pandas as pd
from datetime import datetime
path = "300-399/388/CH-388 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=22, skiprows=2)
test = pd.read_excel(path, usecols="E:H", nrows=6, skiprows=2)

df = input.copy()

df['Date'] = df['Col 2'].where(df['Col1'].eq('Date')).ffill()
df['Customer'] = df['Col 2'].where(df['Col1'].eq('Customer')).ffill()

result = (
    df[df['Col1'].isin(['Product', 'Sale'])]
    .assign(grp=lambda x: x['Col1'].eq('Product').cumsum())
    .pivot(index='grp', columns='Col1', values='Col 2')
    .reset_index(drop=True)
    .assign(
        Date=df['Date'],
        Customer=df['Customer']
    )
    [['Date', 'Customer', 'Product', 'Sale']]
)

result['Sale'] = result['Sale'].astype('Int64')

print(result.equals(test))
# Output: True but cannot align dates format. :)