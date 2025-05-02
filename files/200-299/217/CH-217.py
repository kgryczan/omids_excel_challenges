import pandas as pd

path = "CH-217 Table Transformation.xlsx"

input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=9).sort_values(by=["Date", "Product", "Quantity"]).reset_index(drop=True)

input['Product'] = input.apply(
    lambda row: row['Column 1'][-1] if pd.isna(row['Column 2']) and isinstance(row['Column 1'], str) else None,
    axis=1
)
input['Product'] = input['Product'].ffill()
input = input[input['Column 2'].apply(lambda x: str(x).isdigit() and len(str(x)) == 1)]
input.rename(columns={"Column 1": "Date", "Column 2": "Quantity"}, inplace=True)
input['Quantity'] = input['Quantity'].astype('int64')

input = input[["Date", "Product", "Quantity"]].sort_values(by=["Date", "Product", "Quantity"])
input.reset_index(drop=True, inplace=True)
input['Date'] = pd.to_datetime(input['Date'])

print(input.equals(test)) # True