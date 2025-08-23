import pandas as pd
import numpy as np

path = "200-299/284/CH-284 Transformation.xlsx"

input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="I:J", skiprows=1, nrows=17)

input['row'] = (np.arange(len(input)) + 1) % 2
input['nr'] = ((np.arange(len(input)) + 2) // 2)

result = (
    input.melt(id_vars=['row', 'nr'], var_name='col', value_name='value')
    .pivot_table(index=['nr', 'col'], columns='row', values='value', aggfunc='first')
    .rename(columns={1: 'Date', 0: 'Value'})
    .reset_index()[['Date', 'Value']]
    .assign(
        Date=lambda df: pd.to_datetime(df['Date']),
        Value=lambda df: df['Value'].astype('int64')
    )
)

print(result.equals(test)) # True
