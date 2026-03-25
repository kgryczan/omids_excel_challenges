import pandas as pd

path = "CH-001.xlsx"
input_data = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="K:N", skiprows=1, nrows=12)

result = (
    input_data.melt(id_vars="Date", var_name="Product", value_name="Value")
    .dropna(subset=["Value"])
    .sort_values(["Product", "Date"])
)
result["From"] = result.groupby("Product")["Date"].shift(fill_value=pd.Timestamp("2024-01-01"))
result["diff"] = result.groupby("Product")["Value"].diff().fillna(result["Value"])
result[["Product Name", "Product"]] = result["Product"].str.rsplit(" ", n=1, expand=True)
result = (
    result[["From", "Date", "Product", "diff"]]
    .rename(columns={"Date": "To"})
    .sort_values(["From", "Product"])
    .reset_index(drop=True)
)

print(result.equals(test))
