import pandas as pd

path = "CH-96 Top Products.xlsx"
input = pd.read_excel(path, skiprows=1, usecols="B:D", nrows=19)
test = pd.read_excel(path, skiprows=1, usecols="I:K", nrows=9)\
    .rename(columns={"Product.1":"Product", "% of Month sales":"Percent"})\
    .sort_values(["Month","Product"])\
    .reset_index(drop=True)

result = input.assign(Month=input['Date'].dt.month) \
    .groupby(['Product', 'Month']) \
    .agg(Quantity=('Quantity', 'sum')) \
    .reset_index() \
    .assign(Rank=lambda x: x.groupby('Month')['Quantity'].rank(method='dense', ascending=False)) \
    .assign(Product=lambda x: x.apply(lambda row: row['Product'] if row['Rank'] < 3 else 'Other', axis=1)) \
    .sort_values(['Month', 'Rank']) \
    .groupby(['Product', 'Month']) \
    .agg(Quantity=('Quantity', 'sum')) \
    .sort_values(["Month","Product"])\
    .reset_index() \
    .assign(Percent=lambda x: x['Quantity'] / x.groupby('Month')['Quantity'].transform('sum')) \
    .loc[:, ['Month', 'Product', 'Percent']]

print(all(result == test)) # True