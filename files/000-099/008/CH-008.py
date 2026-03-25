import pandas as pd

path = "CH-008.xlsx"
input_data = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=18)
test = pd.read_excel(path, usecols="I:L", skiprows=1, nrows=3)

input_data["Date"] = pd.to_datetime(input_data["Date"])
input_data = input_data.sort_values(["Product", "Date"]).reset_index(drop=True)
input_data["rn"] = input_data.groupby("Product").cumcount() + 1

full_index = pd.MultiIndex.from_product(
    [pd.date_range(input_data["Date"].min(), input_data["Date"].max(), freq="D"), ["A", "B", "C"]],
    names=["Date", "Product"],
)
result = full_index.to_frame(index=False).merge(input_data, on=["Date", "Product"], how="left")
result["sign"] = result["Type"].map({"Reduce": -1}).fillna(1)
result["Month"] = result["Date"].dt.month
result["Quantity"] = result["Quantity"] * result["sign"]
result["Quantity"] = result["Quantity"].fillna(0)
result = result.sort_values(["Product", "Date"])
result["rn"] = result.groupby("Product")["rn"].ffill()
result["cumsum"] = result.groupby("Product")["Quantity"].cumsum()
days = (
    result.groupby(["Product", "rn", "Month", "cumsum"], dropna=False)["Date"]
    .nunique()
    .reset_index(name="days")
)
result2 = (
    days.groupby(["Product", "Month"], as_index=False)
    .apply(lambda g: pd.Series({"weighted_value": (g["cumsum"] * g["days"]).sum() / g["days"].sum()}))
    .reset_index(drop=True)
    .pivot(index="Month", columns="Product", values="weighted_value")
    .reset_index(drop=True)
)

print(result2.equals(test))
