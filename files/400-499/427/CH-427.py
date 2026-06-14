import pandas as pd

path = "400-499/427/CH-427 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:F", nrows=12, skiprows=2)
test = pd.read_excel(path, usecols="H:I", nrows=5, skiprows=2)

result = input.copy()
result["PRODUCTS"] = result[["PRODUCT 1", "PRODUCT 2", "PRODUCT 3"]].apply(
    lambda row: "-".join(sorted(row.dropna().astype(str))), axis=1
)
result = result.groupby("PRODUCTS").agg({"QUANTITY": "sum"}).reset_index()
result.columns = ["PRODUCTS", "TOTA; QUANTITY"]

# Result almost ideal. One set is not sorted in provided answer data.
