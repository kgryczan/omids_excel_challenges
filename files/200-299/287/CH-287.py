import pandas as pd

path = "200-299/287/CH-287 Transformation.xlsx"

input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=4)
test = pd.read_excel(path, usecols="I:K", skiprows=1, nrows=13)

result = (
    input.melt(var_name="Date", value_name="Value")
    .dropna(subset=["Value"])
    .assign(
        Date=lambda df: pd.to_datetime(df["Date"].astype(str).str[:11], format="%d/%b/%Y"),
        Product=lambda df: df["Value"].str.split("-", n=1).str[0],
        Value=lambda df: pd.to_numeric(df["Value"].str.split("-", n=1).str[1], errors="coerce"),
    )
    .sort_values(["Product", "Date"])
    .reset_index(drop=True)[["Date", "Product", "Value"]]
)

print(result.equals(test)) # True