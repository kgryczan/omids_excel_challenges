import pandas as pd

path = "CH-139 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=25).rename(columns={'Date': 'date', 'Stock price': 'stock_price'})
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=2)
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

input['percentage_change'] = input['stock_price'].pct_change()
input['first_value'] = input.groupby('check')['stock_price'].transform('first')
input['cumsum_per_check'] = input.groupby('check')['diff'].transform(lambda x: x.shift(-1).cumsum())
input['ratio'] = input['cumsum_per_check'] / input['first_value']
input['percentage_change'] = input['percentage_change'].fillna(0)
input['ratio'] = input['ratio'].fillna(0)

summary = input.groupby('Group').agg({'percentage_change': ['min', 'max'], 'ratio': ['min', 'max']})
result = pd.DataFrame({'Group': ['Increase','Decrease'], 'Percent': [summary.values.max(),summary.values.min()]})

print(result.equals(test))  # True