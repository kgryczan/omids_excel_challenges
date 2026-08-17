import pandas as pd

path = "400-499/459/CH-459 Filter.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=10)
test = pd.read_excel(path, usecols="H:I", skiprows=2, nrows=4)
test.columns = ["Date", "Product"]

daily = input.groupby(["Product", "Date"], as_index=False).Sales.sum()
qualified = daily.groupby("Product").Date.apply(
    lambda d: any(
        pd.Series(sorted(d.unique()))
        .diff()
        .dt.days.eq(1)
        .rolling(2)
        .sum()
        .eq(2)
        .fillna(False)
    )
)
qualified = qualified[qualified].index
result = (
    daily.loc[daily.Product.isin(qualified), ["Date", "Product"]]
    .sort_values("Date")
    .reset_index(drop=True)
)
print(result.equals(test))
