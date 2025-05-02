import pandas as pd
import numpy as np

path = "CH-129 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=25).rename(columns={'Date': 'date', 'Stock price': 'stock_price'})
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=2)
test['Group'] = test['Group'].str.strip()

input['a'] = (input['stock_price'].shift() > input['stock_price']).cumsum()
input['d'] = (input['stock_price'].shift() < input['stock_price']).cumsum()
input['a_n'] = input.groupby('a')['a'].transform(lambda x: x if len(x) > 2 else pd.NA)
input['d_n'] = input.groupby('d')['d'].transform(lambda x: x if len(x) > 2 else pd.NA)

input['check'] = input.apply(lambda row: row['a_n'] if pd.notna(row['a_n']) and pd.isna(row['d_n']) else (
    row['d_n'] if pd.notna(row['d_n']) and pd.isna(row['a_n']) else (
        min(row['a_n'], row['d_n']) if pd.notna(row['a_n']) and pd.notna(row['d_n']) else pd.NA
    )
), axis=1)

input['diff'] = input['stock_price'] - input['stock_price'].shift(1, fill_value=0)
input['sign'] = input.groupby('check')['diff'].transform(lambda x: 1 if x.gt(0).sum() > x.lt(0).sum() else -1)
input['Group'] = input['sign'].apply(lambda x: "Upward" if x == 1 else "Downward")

result = input.groupby(['Group', 'check']).size().reset_index(name='n_of_days')
result = result.groupby('Group')['n_of_days'].agg(['mean', 'max']).sort_values(by='Group', ascending=False).reset_index()

result.columns = test.columns

print(result.equals(test))  # True