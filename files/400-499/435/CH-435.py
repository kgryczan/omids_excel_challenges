import pandas as pd

path = "400-499/435/CH-435 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=3, skiprows=2)
test = pd.read_excel(path, usecols="G:J", nrows=10, skiprows=2)

result = input.melt(
    id_vars=["Column1"], var_name="Variable", value_name="Value"
).dropna(subset=["Value"])
result[["Value1", "Value2"]] = result["Value"].str.split("},{", n=1, expand=True)
result[["Value1", "Value2"]] = result[["Value1", "Value2"]].replace(
    {r"[{}]": ""}, regex=True
)
result[["Value1", "Value2"]] = result[["Value1", "Value2"]].apply(
    lambda col: col.str.split(",")
)
result = (
    result.explode(["Value1", "Value2"])
    .rename(
        columns={
            "Column1": "DATE",
            "Variable": "CUSTOMER",
            "Value1": "PRODUCT",
            "Value2": "SALES",
        }
    )
    .sort_values(["DATE", "CUSTOMER"])[["DATE", "CUSTOMER", "PRODUCT", "SALES"]]
).reset_index(drop=True)

result["SALES"] = pd.to_numeric(result["SALES"], errors="coerce")
print(result.equals(test))
# True
