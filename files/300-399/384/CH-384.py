import pandas as pd

path = "300-399/384/CH-384 Table Transformation.xlsx"
df = pd.read_excel(path, usecols="B:E", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="G:J", skiprows=2, nrows=6)

name = df.iloc[::2].reset_index(drop=True)
sale = df.iloc[1::2].reset_index(drop=True)

name["Date"] = name["Date"].ffill()

result = (
    pd.concat([
        name[["Date", "Customer"]].assign(Product=name["product 1"], Sale=sale["product 1"]),
        name[["Date", "Customer"]].assign(Product=name["product 2"], Sale=sale["product 2"]),
    ])
    .dropna()
    .sort_index(kind="stable")
    .reset_index(drop=True)
)

result["Sale"] = result["Sale"].astype(int)

test.columns = result.columns
print(result.equals(test))
